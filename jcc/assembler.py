"""
Create binary code from assembly.

This file is a part of Jake's C Compiler (JCC)
(c) Copyright 2019 Jacob Larkin
"""

command_binary_table_baseline = {
    "ADD": (0b0000, 0b0101),
    "ADDI": 0b0101,
    "SUB": (0b0000, 0b1001),
    "SUBI": 0b1001,
    "CMP": (0b0000, 0b1011),
    "CMPI": 0b1011,
    "AND": (0b0000, 0b0001),
    "ANDI": 0b0001,
    "OR": (0b0000, 0b0010),
    "ORI": 0b0010,
    "XOR": (0b0000, 0b0011),
    "XORI": 0b0011,
    "MOV": (0b0000, 0b1101),
    "MOVI": 0b1101,
    "LSH": (0b1000, 0b0100),
    "LSHI": (0b1000, 0b0000),
    "LSHI2": (0b1000, 0b0001),  # -----------?
    "LUI": 0b1111,
    "LOAD": (0b0100, 0b0000),
    "STOR": (0b0100, 0b0100),
    "Bcond": 0b1100,
    "Jcond": (0b0100, 0b1100),
    "JAL": (0b0100, 0b1000),
    "UU1": (0b0000, 0b0100),
    "UU2": (0b0000, 0b1000),
    "UU3": (0b0000, 0b1100),
    "UU4": (0b0000, 0b1111)
    }

pseudo_instructions = ["push", "pop", "mul?", "div?"]


def assemble(assembly_data):
    """Create binary code from cleaned assembly."""
    binary_data = ""

    return binary_data
