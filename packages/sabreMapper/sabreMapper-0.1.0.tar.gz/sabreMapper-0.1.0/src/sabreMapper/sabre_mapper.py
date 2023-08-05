# (C) Copyright Tingyu Luo 2023.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.
#
# notice: the original code of SabreSwap and SabreLayout are from Qiskit(at https://github.com/Qiskit/qiskit-terra/tree/stable/0.22) and has been modified by Tingyu Luo.

import logging
import retworkx
import numpy as np
from collections import defaultdict
from copy import copy, deepcopy

from mapperFrontend.mapper_frontend import chip_parser, gen_mapping_info, generator

from qiskit import QuantumCircuit
from qiskit.transpiler import CouplingMap
from qiskit.circuit import QuantumCircuit
from qiskit.circuit import QuantumRegister, Qubit
from qiskit.dagcircuit import DAGOpNode
from qiskit.transpiler.layout import Layout
from qiskit.transpiler.passmanager import PassManager
from qiskit.transpiler.basepasses import AnalysisPass
from qiskit.transpiler.exceptions import TranspilerError
from qiskit.converters import circuit_to_dag, dag_to_circuit
from qiskit.circuit.library.standard_gates import SwapGate
from qiskit.transpiler.basepasses import TransformationPass
from qiskit.transpiler.passes.layout.set_layout import SetLayout
from qiskit.transpiler.passes.layout.enlarge_with_ancilla import EnlargeWithAncilla
from qiskit.transpiler.passes.layout.apply_layout import ApplyLayout
from qiskit.transpiler.passes.layout.full_ancilla_allocation import (
    FullAncillaAllocation,
)


logger = logging.getLogger(__name__)

# Size of lookahead window. TODO: set dynamically to len(current_layout)
EXTENDED_SET_SIZE = 20
# Weight of lookahead window compared to front_layer.
EXTENDED_SET_WEIGHT = 0.5

DECAY_RATE = 0.001  # Decay coefficient for penalizing serial swaps.
DECAY_RESET_INTERVAL = 5  # How often to reset all decay rates to 1.


def _generate_circuit_after_sabre_layout(dag, initial_layout, size):
    """Generate a circuit after sabre layout.

    Args:
        dag (DAGCircuit): DAG to map.
        initial_layout (Layout): initial layout of qubits in `dag`.

    Returns:
        DAGCircuit: A circuit with the same operations as `dag`, but
            with the layout specified by `initial_layout`.
    """
    old_circ = dag_to_circuit(dag)
    circ = QuantumCircuit(name=old_circ.name, global_phase=old_circ.global_phase)
    # get the map from initial layout
    initial_mapping = initial_layout._v2p
    mapping_qubits = dict()
    p_qreg = QuantumRegister(name="q", size=size)
    for qreg, id in initial_mapping.items():
        mapping_qubits[qreg.register.name + str(qreg.index)] = Qubit(p_qreg, id)

    circ.add_register(p_qreg)
    for reg in old_circ.cregs:
        circ.add_register(reg)

    for instr in old_circ.data:
        qubits = [
            mapping_qubits[qubit.register.name + str(old_circ.find_bit(qubit).index)]
            for qubit in instr.qubits
        ]
        clbits = [clbit for clbit in instr.clbits]
        circ._append(instr.replace(qubits=qubits, clbits=clbits))
    return circ


def _package_mapping_info(initial_mapping_list, final_mapping_list, qubitMap):
    mapping_info = {
        "has multiple chips": False,
        "final mapping": {},
        "initial mapping": {},
        "physical qubits idx": {},
    }
    initial_mapping = dict()
    final_mapping = dict()
    physical_qubits_idx = dict()

    # Expecially, in Sabre Mapper the logic qubits also singed from 0 to n, and using a unique quantum register.
    for v_qubit, p_qubit in initial_mapping_list.items():
        #! TODO: support any string qreg name.
        virtual_qubit = "%d" % v_qubit.index
        physical_qubit = "%d" % p_qubit
        initial_mapping.update({virtual_qubit: physical_qubit})

    for v_qubit, p_qubit in final_mapping_list.items():
        #! TODO: support any string qreg name.
        virtual_qubit = "%d" % v_qubit.index
        physical_qubit = "%d" % p_qubit
        final_mapping.update({virtual_qubit: physical_qubit})

    phy_qubit_dict = qubitMap.getQubitMap()
    for qubitName in phy_qubit_dict.keys():
        qubitIdx = "%d" % phy_qubit_dict[qubitName]
        physical_qubits_idx.update({qubitIdx: qubitName})

    mapping_info["final mapping"] = final_mapping
    mapping_info["initial mapping"] = initial_mapping
    mapping_info["physical qubits idx"] = physical_qubits_idx

    return mapping_info


def _sabre_chip_info_extract(physical_coupling_list, qubitMap):
    coupling_list = list()
    for coupling in physical_coupling_list:
        pair = [
            qubitMap.getQubitNum(coupling["qubit pair"][0]),
            qubitMap.getQubitNum(coupling["qubit pair"][1]),
        ]
        coupling_list.append(pair)
    return coupling_list


def _transform_gate_for_layout(op_node, layout, device_qreg):
    """Return node implementing a virtual op on given layout."""
    mapped_op_node = copy(op_node)
    mapped_op_node.qargs = tuple(device_qreg[layout._v2p[x]] for x in op_node.qargs)
    return mapped_op_node


def _shortest_swap_path(target_qubits, coupling_map, layout):
    """Return an iterator that yields the swaps between virtual qubits needed to bring the two
    virtual qubits in ``target_qubits`` together in the coupling map."""
    v_start, v_goal = target_qubits
    start, goal = layout._v2p[v_start], layout._v2p[v_goal]
    # TODO: remove the list call once using retworkx 0.12, as the return value can be sliced.
    path = list(
        retworkx.dijkstra_shortest_paths(coupling_map.graph, start, target=goal)[goal]
    )
    # Swap both qubits towards the "centre" (as opposed to applying the same swaps to one) to
    # parallelise and reduce depth.
    split = len(path) // 2
    forwards, backwards = path[1:split], reversed(path[split:-1])
    for swap in forwards:
        yield v_start, layout._p2v[swap]
    for swap in backwards:
        yield v_goal, layout._p2v[swap]


class SabreMapper:
    def __init__(self) -> None:
        self.max_iteration = 3

    def map_schedule(
        self, origin_qasm_fn, chip_info_fn, mapped_qasm_fn, qubit_mapping_fn
    ):
        """Routing via SWAP insertion using the SABRE method from Li et al.

        Args:
            In this interface function, there exits four input arguments, and they are all the path name of a file:
            - origin_qasm_fn:   the file will be mapped.
            - chip_info_fn:     the file carries the essential chip info for mapping and scheduling
            - mapped_qasm_fn:   the file records the mapped OpenQASM program.
            - qubit_mapping_fn: the file records the mapping result.

             'is_mapped_success' is the only output argument for this interface function,  meaning that whether the
            mapper runs successfully.
        """

        # Get the output flag argument first, the default value is False.
        is_mapped_success = False

        # Before activating the flow of mapping and scheduling,
        # we should get the chip information.
        (
            physical_qubits_list,
            singleGates_fidelity_list,
            physical_coupling_list,
        ) = chip_parser(chip_info_fn)

        # In the sabre algorithms, we only need the two qubits coupling information
        qubitMap = QubitMap(physical_qubits_list)
        coupling_info = _sabre_chip_info_extract(physical_coupling_list, qubitMap)

        # Parse the qasm file to the Qiskit QuantumCircuit object and generate the DAG.
        qasm = QuantumCircuit.from_qasm_file(origin_qasm_fn)
        qasm_dag = circuit_to_dag(qasm)

        # Run the Sabre algorithms.
        coupling_map = CouplingMap(coupling_info)
        sabre_layout = SabreLayout(coupling_map, max_iterations=self.max_iteration)
        initial_mapping_list, final_mapping_list, initial_layout = sabre_layout.run(
            qasm_dag
        )

        initial_circuit = _generate_circuit_after_sabre_layout(
            qasm_dag, initial_layout, len(physical_qubits_list)
        )

        mapper = SabreSwap(coupling_map, "basic")
        initial_dag = circuit_to_dag(initial_circuit)
        final_dag = mapper.run(initial_dag)
        final_circuit = dag_to_circuit(final_dag)

        # Output the mapping result.
        # Package the mapping information to the json file.
        mapping_info = _package_mapping_info(
            initial_mapping_list, final_mapping_list, qubitMap
        )
        gen_mapping_info(mapping_info, qubit_mapping_fn)

        # Output the mapped OpenQASM file.
        generator(final_circuit, mapped_qasm_fn)

        is_mapped_success = True

        return is_mapped_success


class QubitMap:
    def __init__(self, qubit_list: list) -> None:
        self._qubit_map = dict()
        for qubit in qubit_list:
            self.allocQubit(qubit)

    def allocQubit(self, qubit: str):
        qubitNum = len(self._qubit_map)
        self._qubit_map.update({qubit: qubitNum})

    def getQubitNum(self, qubit: str):
        if qubit not in self._qubit_map.keys():
            return False
        return self._qubit_map[qubit]

    def getQubitMap(self):
        return self._qubit_map

    def getQubitName(self, idx):
        for qubit, qubitNum in self._qubit_map.items():
            if idx == qubitNum:
                return qubit


class SabreLayout(AnalysisPass):
    """Choose a Layout via iterative bidirectional routing of the input circuit.

    Starting with a random initial `Layout`, the algorithm does a full routing
    of the circuit (via the `routing_pass` method) to end up with a
    `final_layout`. This final_layout is then used as the initial_layout for
    routing the reverse circuit. The algorithm iterates a number of times until
    it finds an initial_layout that reduces full routing cost.

    This method exploits the reversibility of quantum circuits, and tries to
    include global circuit information in the choice of initial_layout.

    **References:**

    [1] Li, Gushu, Yufei Ding, and Yuan Xie. "Tackling the qubit mapping problem
    for NISQ-era quantum devices." ASPLOS 2019.
    `arXiv:1809.02573 <https://arxiv.org/pdf/1809.02573.pdf>`_
    """

    def __init__(self, coupling_map, routing_pass=None, seed=None, max_iterations=3):
        """SabreLayout initializer.

        Args:
            coupling_map (Coupling): directed graph representing a coupling map.
            routing_pass (BasePass): the routing pass to use while iterating.
            seed (int): seed for setting a random first trial layout.
            max_iterations (int): number of forward-backward iterations.
        """
        super().__init__()
        self.coupling_map = coupling_map
        self.routing_pass = routing_pass
        self.seed = seed
        self.max_iterations = max_iterations

    def run(self, dag):
        """Run the SabreLayout pass on `dag`.

        Args:
            dag (DAGCircuit): DAG to find layout for.

        Raises:
            TranspilerError: if dag wider than self.coupling_map
        """
        if len(dag.qubits) > self.coupling_map.size():
            raise TranspilerError("More virtual qubits exist than physical.")

        # Choose a random initial_layout.
        if self.seed is None:
            self.seed = np.random.randint(0, np.iinfo(np.int32).max)
        rng = np.random.default_rng(self.seed)

        physical_qubits = rng.choice(
            self.coupling_map.size(), len(dag.qubits), replace=False
        )
        physical_qubits = rng.permutation(physical_qubits)
        initial_layout = Layout(
            {q: dag.qubits[i] for i, q in enumerate(physical_qubits)}
        )

        if self.routing_pass is None:
            self.routing_pass = SabreSwap(
                self.coupling_map, "decay", seed=self.seed, fake_run=True
            )
        else:
            self.routing_pass.fake_run = True

        # Save the initial mapping result
        initial_mapping_result = deepcopy(initial_layout._v2p)

        # Do forward-backward iterations.
        circ = dag_to_circuit(dag)
        rev_circ = circ.reverse_ops()
        for _ in range(self.max_iterations):
            for _ in ("forward", "backward"):
                pm = self._layout_and_route_passmanager(initial_layout)
                new_circ = pm.run(circ)

                # Update initial layout and reverse the unmapped circuit.
                pass_final_layout = pm.property_set["final_layout"]
                final_layout = self._compose_layouts(
                    initial_layout, pass_final_layout, new_circ.qregs
                )
                initial_layout = final_layout
                circ, rev_circ = rev_circ, circ

            # Diagnostics
            logger.info("new initial layout")
            logger.info(initial_layout)

        for qreg in dag.qregs.values():
            initial_layout.add_register(qreg)

        self.property_set["layout"] = initial_layout
        self.routing_pass.fake_run = False

        # get final mapping result and mapped circuit
        final_mapping_result = deepcopy(initial_layout._v2p)

        return initial_mapping_result, final_mapping_result, initial_layout

    def _layout_and_route_passmanager(self, initial_layout):
        """Return a passmanager for a full layout and routing.

        We use a factory to remove potential statefulness of passes.
        """
        layout_and_route = [
            SetLayout(initial_layout),
            FullAncillaAllocation(self.coupling_map),
            EnlargeWithAncilla(),
            ApplyLayout(),
            self.routing_pass,
        ]
        pm = PassManager(layout_and_route)
        return pm

    def _compose_layouts(self, initial_layout, pass_final_layout, qregs):
        """Return the real final_layout resulting from the composition
        of an initial_layout with the final_layout reported by a pass.

        The routing passes internally start with a trivial layout, as the
        layout gets applied to the circuit prior to running them. So the
        "final_layout" they report must be amended to account for the actual
        initial_layout that was selected.
        """
        trivial_layout = Layout.generate_trivial_layout(*qregs)
        qubit_map = Layout.combine_into_edge_map(initial_layout, trivial_layout)
        final_layout = {
            v: pass_final_layout._v2p[qubit_map[v]] for v in initial_layout._v2p
        }
        return Layout(final_layout)


class SabreSwap(TransformationPass):
    r"""Map input circuit onto a backend topology via insertion of SWAPs.

    Implementation of the SWAP-based heuristic search from the SABRE qubit
    mapping paper [1] (Algorithm 1). The heuristic aims to minimize the number
    of lossy SWAPs inserted and the depth of the circuit.

    This algorithm starts from an initial layout of virtual qubits onto physical
    qubits, and iterates over the circuit DAG until all gates are exhausted,
    inserting SWAPs along the way. It only considers 2-qubit gates as only those
    are germane for the mapping problem (it is assumed that 3+ qubit gates are
    already decomposed).

    In each iteration, it will first check if there are any gates in the
    ``front_layer`` that can be directly applied. If so, it will apply them and
    remove them from ``front_layer``, and replenish that layer with new gates
    if possible. Otherwise, it will try to search for SWAPs, insert the SWAPs,
    and update the mapping.

    The search for SWAPs is restricted, in the sense that we only consider
    physical qubits in the neighborhood of those qubits involved in
    ``front_layer``. These give rise to a ``swap_candidate_list`` which is
    scored according to some heuristic cost function. The best SWAP is
    implemented and ``current_layout`` updated.

    **References:**

    [1] Li, Gushu, Yufei Ding, and Yuan Xie. "Tackling the qubit mapping problem
    for NISQ-era quantum devices." ASPLOS 2019.
    `arXiv:1809.02573 <https://arxiv.org/pdf/1809.02573.pdf>`_
    """

    def __init__(
        self,
        coupling_map,
        heuristic="basic",
        seed=None,
        fake_run=False,
    ):
        r"""SabreSwap initializer.

        Args:
            coupling_map (CouplingMap): CouplingMap of the target backend.
            heuristic (str): The type of heuristic to use when deciding best
                swap strategy ('basic' or 'lookahead' or 'decay').
            seed (int): random seed used to tie-break among candidate swaps.
            fake_run (bool): if true, it only pretend to do routing, i.e., no
                swap is effectively added.

        Additional Information:

            The search space of possible SWAPs on physical qubits is explored
            by assigning a score to the layout that would result from each SWAP.
            The goodness of a layout is evaluated based on how viable it makes
            the remaining virtual gates that must be applied. A few heuristic
            cost functions are supported

            - 'basic':

            The sum of distances for corresponding physical qubits of
            interacting virtual qubits in the front_layer.

            .. math::

                H_{basic} = \sum_{gate \in F} D[\pi(gate.q_1)][\pi(gate.q2)]

            - 'lookahead':

            This is the sum of two costs: first is the same as the basic cost.
            Second is the basic cost but now evaluated for the
            extended set as well (i.e. :math:`|E|` number of upcoming successors to gates in
            front_layer F). This is weighted by some amount EXTENDED_SET_WEIGHT (W) to
            signify that upcoming gates are less important that the front_layer.

            .. math::

                H_{decay}=\frac{1}{\left|{F}\right|}\sum_{gate \in F} D[\pi(gate.q_1)][\pi(gate.q2)]
                    + W*\frac{1}{\left|{E}\right|} \sum_{gate \in E} D[\pi(gate.q_1)][\pi(gate.q2)]

            - 'decay':

            This is the same as 'lookahead', but the whole cost is multiplied by a
            decay factor. This increases the cost if the SWAP that generated the
            trial layout was recently used (i.e. it penalizes increase in depth).

            .. math::

                H_{decay} = max(decay(SWAP.q_1), decay(SWAP.q_2)) {
                    \frac{1}{\left|{F}\right|} \sum_{gate \in F} D[\pi(gate.q_1)][\pi(gate.q2)]\\
                    + W *\frac{1}{\left|{E}\right|} \sum_{gate \in E} D[\pi(gate.q_1)][\pi(gate.q2)]
                    }
        """

        super().__init__()

        # Assume bidirectional couplings, fixing gate direction is easy later.
        if coupling_map is None or coupling_map.is_symmetric:
            self.coupling_map = coupling_map
        else:
            self.coupling_map = deepcopy(coupling_map)
            self.coupling_map.make_symmetric()

        self.heuristic = heuristic
        self.seed = seed
        self.fake_run = fake_run
        self.required_predecessors = None
        self.qubits_decay = None
        self._bit_indices = None
        self.dist_matrix = None

    def run(self, dag):
        """Run the SabreSwap pass on `dag`.

        Args:
            dag (DAGCircuit): the directed acyclic graph to be mapped.
        Returns:
            DAGCircuit: A dag mapped to be compatible with the coupling_map.
        Raises:
            TranspilerError: if the coupling map or the layout are not
            compatible with the DAG
        """
        if len(dag.qregs) != 1 or dag.qregs.get("q", None) is None:
            raise TranspilerError("Sabre swap runs on physical circuits only.")

        if len(dag.qubits) > self.coupling_map.size():
            raise TranspilerError("More virtual qubits exist than physical.")

        max_iterations_without_progress = 10 * len(dag.qubits)  # Arbitrary.
        ops_since_progress = []
        extended_set = None

        # Normally this isn't necessary, but here we want to log some objects that have some
        # non-trivial cost to create.
        do_expensive_logging = logger.isEnabledFor(logging.DEBUG)

        self.dist_matrix = self.coupling_map.distance_matrix

        rng = np.random.default_rng(self.seed)

        # Preserve input DAG's name, regs, wire_map, etc. but replace the graph.
        mapped_dag = None
        if not self.fake_run:
            mapped_dag = dag.copy_empty_like()

        canonical_register = dag.qregs["q"]
        current_layout = Layout.generate_trivial_layout(canonical_register)

        self._bit_indices = {bit: idx for idx, bit in enumerate(canonical_register)}

        # A decay factor for each qubit used to heuristically penalize recently
        # used qubits (to encourage parallelism).
        self.qubits_decay = dict.fromkeys(dag.qubits, 1)

        # Start algorithm from the front layer and iterate until all gates done.
        self.required_predecessors = self._build_required_predecessors(dag)
        num_search_steps = 0
        front_layer = dag.front_layer()

        while front_layer:
            execute_gate_list = []

            # Remove as many immediately applicable gates as possible
            new_front_layer = []
            for node in front_layer:
                if len(node.qargs) == 2:
                    v0, v1 = node.qargs
                    # Accessing layout._v2p directly to avoid overhead from __getitem__ and a
                    # single access isn't feasible because the layout is updated on each iteration
                    if self.coupling_map.graph.has_edge(
                        current_layout._v2p[v0], current_layout._v2p[v1]
                    ):
                        execute_gate_list.append(node)
                    else:
                        new_front_layer.append(node)
                else:  # Single-qubit gates as well as barriers are free
                    execute_gate_list.append(node)
            front_layer = new_front_layer

            if (
                not execute_gate_list
                and len(ops_since_progress) > max_iterations_without_progress
            ):
                # Backtrack to the last time we made progress, then greedily insert swaps to route
                # the gate with the smallest distance between its arguments.  This is a release
                # valve for the algorithm to avoid infinite loops only, and should generally not
                # come into play for most circuits.
                self._undo_operations(ops_since_progress, mapped_dag, current_layout)
                self._add_greedy_swaps(
                    front_layer, mapped_dag, current_layout, canonical_register
                )
                continue

            if execute_gate_list:
                for node in execute_gate_list:
                    self._apply_gate(
                        mapped_dag, node, current_layout, canonical_register
                    )
                    for successor in self._successors(node, dag):
                        self.required_predecessors[successor] -= 1
                        if self._is_resolved(successor):
                            front_layer.append(successor)

                    if node.qargs:
                        self._reset_qubits_decay()

                # Diagnostics
                if do_expensive_logging:
                    logger.debug(
                        "free! %s",
                        [
                            (n.name if isinstance(n, DAGOpNode) else None, n.qargs)
                            for n in execute_gate_list
                        ],
                    )
                    logger.debug(
                        "front_layer: %s",
                        [
                            (n.name if isinstance(n, DAGOpNode) else None, n.qargs)
                            for n in front_layer
                        ],
                    )

                ops_since_progress = []
                extended_set = None
                continue

            # After all free gates are exhausted, heuristically find
            # the best swap and insert it. When two or more swaps tie
            # for best score, pick one randomly.
            if extended_set is None:
                extended_set = self._obtain_extended_set(dag, front_layer)
            swap_scores = {}
            for swap_qubits in self._obtain_swaps(front_layer, current_layout):
                trial_layout = current_layout.copy()
                trial_layout.swap(*swap_qubits)
                score = self._score_heuristic(
                    self.heuristic, front_layer, extended_set, trial_layout, swap_qubits
                )
                swap_scores[swap_qubits] = score
            min_score = min(swap_scores.values())
            best_swaps = [k for k, v in swap_scores.items() if v == min_score]
            best_swaps.sort(
                key=lambda x: (self._bit_indices[x[0]], self._bit_indices[x[1]])
            )
            best_swap = rng.choice(best_swaps)
            swap_node = self._apply_gate(
                mapped_dag,
                DAGOpNode(op=SwapGate(), qargs=best_swap),
                current_layout,
                canonical_register,
            )
            current_layout.swap(*best_swap)
            ops_since_progress.append(swap_node)

            num_search_steps += 1
            if num_search_steps % DECAY_RESET_INTERVAL == 0:
                self._reset_qubits_decay()
            else:
                self.qubits_decay[best_swap[0]] += DECAY_RATE
                self.qubits_decay[best_swap[1]] += DECAY_RATE

            # Diagnostics
            if do_expensive_logging:
                logger.debug("SWAP Selection...")
                logger.debug(
                    "extended_set: %s", [(n.name, n.qargs) for n in extended_set]
                )
                logger.debug("swap scores: %s", swap_scores)
                logger.debug("best swap: %s", best_swap)
                logger.debug("qubits decay: %s", self.qubits_decay)

        self.property_set["final_layout"] = current_layout
        if not self.fake_run:
            return mapped_dag
        return dag

    def _apply_gate(self, mapped_dag, node, current_layout, canonical_register):
        new_node = _transform_gate_for_layout(node, current_layout, canonical_register)
        if self.fake_run:
            return new_node
        return mapped_dag.apply_operation_back(
            new_node.op, new_node.qargs, new_node.cargs
        )

    def _reset_qubits_decay(self):
        """Reset all qubit decay factors to 1 upon request (to forget about
        past penalizations).
        """
        self.qubits_decay = {k: 1 for k in self.qubits_decay.keys()}

    def _build_required_predecessors(self, dag):
        out = defaultdict(int)
        # We don't need to count in- or out-wires: outs can never be predecessors, and all input
        # wires are automatically satisfied at the start.
        for node in dag.op_nodes():
            for successor in self._successors(node, dag):
                out[successor] += 1
        return out

    def _successors(self, node, dag):
        """Return an iterable of the successors along each wire from the given node.

        This yields the same successor multiple times if there are parallel wires (e.g. two adjacent
        operations that have one clbit and qubit in common), which is important in the swapping
        algorithm for detecting if each wire has been accounted for."""
        for _, successor, _ in dag.edges(node):
            if isinstance(successor, DAGOpNode):
                yield successor

    def _is_resolved(self, node):
        """Return True if all of a node's predecessors in dag are applied."""
        return self.required_predecessors[node] == 0

    def _obtain_extended_set(self, dag, front_layer):
        """Populate extended_set by looking ahead a fixed number of gates.
        For each existing element add a successor until reaching limit.
        """
        extended_set = []
        decremented = []
        tmp_front_layer = front_layer
        done = False
        while tmp_front_layer and not done:
            new_tmp_front_layer = []
            for node in tmp_front_layer:
                for successor in self._successors(node, dag):
                    decremented.append(successor)
                    self.required_predecessors[successor] -= 1
                    if self._is_resolved(successor):
                        new_tmp_front_layer.append(successor)
                        if len(successor.qargs) == 2:
                            extended_set.append(successor)
                if len(extended_set) >= EXTENDED_SET_SIZE:
                    done = True
                    break
            tmp_front_layer = new_tmp_front_layer
        for node in decremented:
            self.required_predecessors[node] += 1
        return extended_set

    def _obtain_swaps(self, front_layer, current_layout):
        """Return a set of candidate swaps that affect qubits in front_layer.

        For each virtual qubit in front_layer, find its current location
        on hardware and the physical qubits in that neighborhood. Every SWAP
        on virtual qubits that corresponds to one of those physical couplings
        is a candidate SWAP.

        Candidate swaps are sorted so SWAP(i,j) and SWAP(j,i) are not duplicated.
        """
        candidate_swaps = set()
        for node in front_layer:
            for virtual in node.qargs:
                physical = current_layout[virtual]
                for neighbor in self.coupling_map.neighbors(physical):
                    virtual_neighbor = current_layout[neighbor]
                    swap = sorted(
                        [virtual, virtual_neighbor], key=lambda q: self._bit_indices[q]
                    )
                    candidate_swaps.add(tuple(swap))
        return candidate_swaps

    def _add_greedy_swaps(self, front_layer, dag, layout, qubits):
        """Mutate ``dag`` and ``layout`` by applying greedy swaps to ensure that at least one gate
        can be routed."""
        layout_map = layout._v2p
        target_node = min(
            front_layer,
            key=lambda node: self.dist_matrix[
                layout_map[node.qargs[0]], layout_map[node.qargs[1]]
            ],
        )
        for pair in _shortest_swap_path(
            tuple(target_node.qargs), self.coupling_map, layout
        ):
            self._apply_gate(dag, DAGOpNode(op=SwapGate(), qargs=pair), layout, qubits)
            layout.swap(*pair)

    def _compute_cost(self, layer, layout):
        cost = 0
        layout_map = layout._v2p
        for node in layer:
            cost += self.dist_matrix[
                layout_map[node.qargs[0]], layout_map[node.qargs[1]]
            ]
        return cost

    def _score_heuristic(
        self, heuristic, front_layer, extended_set, layout, swap_qubits=None
    ):
        """Return a heuristic score for a trial layout.

        Assuming a trial layout has resulted from a SWAP, we now assign a cost
        to it. The goodness of a layout is evaluated based on how viable it makes
        the remaining virtual gates that must be applied.
        """
        first_cost = self._compute_cost(front_layer, layout)
        if heuristic == "basic":
            return first_cost

        first_cost /= len(front_layer)
        second_cost = 0
        if extended_set:
            second_cost = self._compute_cost(extended_set, layout) / len(extended_set)
        total_cost = first_cost + EXTENDED_SET_WEIGHT * second_cost
        if heuristic == "lookahead":
            return total_cost

        if heuristic == "decay":
            return (
                max(
                    self.qubits_decay[swap_qubits[0]], self.qubits_decay[swap_qubits[1]]
                )
                * total_cost
            )

        raise TranspilerError("Heuristic %s not recognized." % heuristic)

    def _undo_operations(self, operations, dag, layout):
        """Mutate ``dag`` and ``layout`` by undoing the swap gates listed in ``operations``."""
        if dag is None:
            for operation in reversed(operations):
                layout.swap(*operation.qargs)
        else:
            for operation in reversed(operations):
                dag.remove_op_node(operation)
                p0 = self._bit_indices[operation.qargs[0]]
                p1 = self._bit_indices[operation.qargs[1]]
                layout.swap(p0, p1)
