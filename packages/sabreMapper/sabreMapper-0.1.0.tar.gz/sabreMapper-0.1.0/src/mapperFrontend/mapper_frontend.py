# (C) Copyright Tingyu Luo 2023.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

import json
from pathlib import Path


def chip_parser(config_file_path: Path):
    """Read the quantum chip config file, and get some related information

    Args:
        config_file_path(Path): The path of quantum chip config file

    Returns:
        physical_qubits_list(list): The list of physical qubits.
        singleGates_fidelity_list(dict): The dict of each qubit fidelity.
        physical_coupling_list(list): The list of each two qubits connections and their fidelity


    """
    with open(config_file_path, "r") as fp:
        chip_info = json.load(fp)
        if chip_info["has multiple chips"]:
            pass

        physical_qubits_list = chip_info["qubits"]
        singleGates_fidelity_list = chip_info["fidelity"]
        physical_coupling_list = chip_info["couplings"]

        return physical_qubits_list, singleGates_fidelity_list, physical_coupling_list


def gen_mapping_info(mapping_info, qubit_mapping_fn: Path):
    with open(qubit_mapping_fn, "w") as map_fp:
        info = json.dumps(mapping_info)
        map_fp.write(info)


def generator(quantum_circuit, qasm_file_path: Path):
    """Generate the openqasm file by using QuantumCircuit

    Args:
        circuit(QuantumCircuit): The circuit of the program
        qasn_fn(Path): the path of the openqasm file

    Returns:
        None

    """
    with open(qasm_file_path, "w") as fp:
        fp.write(quantum_circuit.qasm())
