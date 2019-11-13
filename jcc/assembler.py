"""
Create binary code from assembly.

This file is a part of Jake's C Compiler (JCC)
(c) Copyright 2019 Jacob Larkin
"""

from bitstring import Bits


standard_commands = {
    "ADD": (0b0000, 0b0101),
    "SUB": (0b0000, 0b1001),
    "CMP": (0b0000, 0b1011),
    "AND": (0b0000, 0b0001),
    "OR": (0b0000, 0b0010),
    "XOR": (0b0000, 0b0011),
    "MOV": (0b0000, 0b1101),
    "LSH": (0b1000, 0b0100),
    "LOAD": (0b0100, 0b0000),
    "STOR": (0b0100, 0b0100),
    "JAL": (0b0100, 0b1000),
    "ADDU": (0b0000, 0b0110),
    "ADDC": (0b0000, 0b0111),
    "MUL": (0b0000, 0b1110),
    # "MUL": (0b0000, 0b1000),
    "SUBC": (0b0000, 0b1010),
    "NOT": (0b0000, 0b0100),
    "SAR": (0b1000, 0b1000)
    # "CLK": (0b0000, 0b0100)
    }

immediate_commands = {
    "ADDI": 0b0101,
    "SUBI": 0b1001,
    "CMPI": 0b1011,
    "ANDI": 0b0001,
    "ORI": 0b0010,
    "XORI": 0b0011,
    "MOVI": 0b1101,
    "LUI": 0b1111,
    "SUBCI": 0b1010,
    "MULI": 0b1110,
    "ADDUI": 0b0110
    }

special_commands = {
    "LSHI": (0b1000, 0b0000),
    "LSHI2": (0b1000, 0b0001),
    "B": 0b1100,
    "J": (0b0100, 0b1100),
    "S": (0b0100, 0b1101)
    }

condition_codes = {
    "EQ": 0b0000,
    "NE": 0b0001,
    "GE": 0b1101,
    "CS": 0b0010,
    "CC": 0b0011,
    "HI": 0b0100,
    "LS": 0b0101,
    "LO": 0b1010,
    "HS": 0b1011,
    "GT": 0b0110,
    "LE": 0b0111,
    "FS": 0b1000,
    "FC": 0b1001,
    "LT": 0b1100,
    "UC": 0b1110,
    "XX": 0b1111,
}

reg_map = {
    "SP": 0b1111,
    "BP": 0b1110,
    "RA": 0b0000,
    "T0": 0b0001,
    "T1": 0b0010,

    "R0": 0b0000,
    "R1": 0b0001,
    "R2": 0b0010,
    "R3": 0b0011,
    "R4": 0b0100,
    "R5": 0b0101,
    "R6": 0b0110,
    "R7": 0b0111,
    "R8": 0b1000,
    "R9": 0b1001,
    "R10": 0b1010,
    "R11": 0b1011,
    "R12": 0b1100,
    "R13": 0b1101,
    "R14": 0b1110,
    "R15": 0b1111
    }


def assemble(assembly_data, zeros=True):
    """Create binary code from cleaned assembly."""
    binary_data = ""

    assembly_data = assembly_data.strip()

    lines = 0

    for line in assembly_data.split("\n"):
        elements = []
        elements = line.split(" ")
        for i, element in enumerate(elements):
            elements[i] = element.strip(" \n$,%")

        cmd_str = elements[0]

        if cmd_str in standard_commands:
            cmd = Bits(uint=standard_commands[cmd_str][0], length=4)
            cmd2 = Bits(uint=standard_commands[cmd_str][1], length=4)
            rsrc = Bits(uint=reg_map[elements[1]], length=4)
            rdest = Bits(uint=reg_map[elements[2]], length=4)

            if cmd_str == "LOAD" or cmd_str == "STOR":
                binary_data += cmd.hex + rsrc.hex + cmd2.hex + rdest.hex + "\n"
            else:
                binary_data += cmd.hex + rdest.hex + cmd2.hex + rsrc.hex + "\n"

        elif cmd_str in immediate_commands:
            cmd = Bits(uint=immediate_commands[cmd_str], length=4)
            rdest = Bits(uint=reg_map[elements[2]], length=4)

            if elements[1] == "0":
                elements[1] = "0x00"

            try:
                imm = Bits(elements[1], length=8)
            except ValueError:
                imm = Bits(int=int(elements[1]), length=8)

            binary_data += cmd.hex + rdest.hex + imm.hex + "\n"

        elif cmd_str in special_commands:
            pass

        elif cmd_str[0] in special_commands:
            if cmd_str.startswith("J"):
                cmd = Bits(uint=special_commands[cmd_str[0]][0], length=4)
                cmd2 = Bits(uint=special_commands[cmd_str[0]][1], length=4)
                cond_str = cmd_str[1:]
                if cond_str not in condition_codes.keys():
                    raise Exception("Error, cond code not found: " + cond_str)
                cond = Bits(uint=condition_codes[cond_str], length=4)
                rdest = Bits(uint=reg_map[elements[1]], length=4)

                binary_data += cmd.hex + cond.hex + cmd2.hex + rdest.hex + "\n"

            elif cmd_str.startswith("B"):
                cmd = Bits(uint=special_commands[cmd_str[0]], length=4)
                cond_str = cmd_str[1:]
                if cond_str not in condition_codes.keys():
                    raise Exception("Error, cond code not found: " + cond_str)
                cond = Bits(uint=condition_codes[cond_str], length=4)

                if elements[1] == "0":
                    elements[1] = "0x00"

                try:
                    disp = Bits(elements[1], length=8)
                except ValueError:
                    disp = Bits(int=int(elements[1]), length=8)

                binary_data += cmd.hex + cond.hex + disp.hex + "\n"

        else:
            binary_data += "Error, command not found: " + cmd_str + "\n"
            # raise Exception("Error, command not found: " + cmd)

        lines += 1

    if zeros:  # pack end with zeros if desired
        while lines < 0xFFFF:
            binary_data += "0000\n"
            lines += 1

    return binary_data
