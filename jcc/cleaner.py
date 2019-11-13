"""
Clean assembly file. Replace labels, pseudo instructions, etc...

This file is a part of Jake's C Compiler (JCC)
(c) Copyright 2019 Jacob Larkin
"""

import re

from bitstring import Bits


def clean(assembly_data):
    """Take assembly, Swap labels for addresses, remove whitespace, etc."""
    start_values = {
        "SP": 0xE000,
        "BP": 0xE000,
        "RA": 0x0000,
        "T0": 0x0000,
        "T1": 0x0000
        }

    # add blank line
    temp_data = "BUC $1\n"

    # get rid of later
    bits = Bits(uint=start_values["SP"], length=16)
    temp_data += "LUI $0x{}, %{}\n".format(bits[:8].hex, "SP")
    temp_data += "ADDUI $0x{}, %{}\n".format(bits[8:].hex, "SP")

    # add reg stating values
    # temp_data = ""
    for reg in start_values.keys():
        bits = Bits(uint=start_values[reg], length=16)
        temp_data += "LUI $0x{}, %{}\n".format(bits[:8].hex, reg)
        temp_data += "ADDUI $0x{}, %{}\n".format(bits[8:].hex, reg)
    assembly_data = temp_data + assembly_data

    # pass for cleaning
    count = 0
    temp_data = ""
    for line in assembly_data.split("\n"):
        line = line.strip()
        line = line.split(";")[0]
        line = line.strip()
        if ":" in line:
            temp_data += line.split(":")[0] + ":\n"
            line = line.split(":")[1]
        if line == "":  # if blank line or was a comment or label
            continue

        cmd = line.split(" ")[0]
        cmd = cmd.strip().upper()

        args = "".join(line.split(" ")[1:]).split(",")
        for arg in args:
            arg = arg.strip()

        temp_data += cmd + " " + ", ".join(args) + "\n"
    assembly_data = temp_data

    # pass for pseudo commands
    temp_data = ""
    for line in assembly_data.split("\n"):
        if line.startswith("PUSH"):
            temp_data += "STOR" + line[4:] + ", %SP\n"
            temp_data += "SUBI $1, %SP\n"
            # temp_data += "STOR %RA, %SP\n"
            # temp_data += "SUBI 2, %SP"
        elif line.startswith("POP"):
            temp_data += "ADDI $1, %SP\n"
            temp_data += "LOAD" + line[3:] + ", %SP\n"
            # temp_data += "LOAD %RA, %SP\n"
            # temp_data += "ADDI 2, %SP"
        else:
            temp_data += line + "\n"
    assembly_data = temp_data

    # pass for makeing labels multi-line
    count = 0
    temp_data = ""
    temp_lines = []
    for line in assembly_data.split("\n"):
        cmd = line.split(" ")[0]
        cmd = cmd.strip()

        if line.endswith(":"):
            temp_data += line + "\n"
            temp_lines.append(line)
            continue

        args = "".join(line.split(" ")[1:]).split(",")
        temp_args = []
        for arg in args:
            arg = arg.strip()
            if arg.startswith("@"):
                temp_data += "LUI @{}._high, %T1\n".format(arg[1:])
                temp_data += "ADDUI @{}._low, %T1\n".format(arg[1:])
                if temp_lines[-1].startswith("CMP"):
                    temp_lines.insert(-1, "LUI @{}._high, %T1".format(arg[1:]))
                    temp_lines.insert(-1,
                                      "ADDUI @{}._low, %T1".format(arg[1:]))
                else:
                    temp_lines.append("LUI @{}._high, %T1".format(arg[1:]))
                    temp_lines.append("ADDUI @{}._low, %T1".format(arg[1:]))
                arg = "%T1"
            temp_args.append(arg)
        args = temp_args

        temp_data += cmd + " " + ", ".join(args) + "\n"
        temp_lines.append(cmd + " " + ", ".join(args))
    assembly_data = temp_data
    assembly_data = "\n".join(temp_lines)

    # pass for label locations
    labels = {}
    count = 0
    temp_data = ""
    for line in assembly_data.split("\n"):
        if line.endswith(":"):
            label = line[:-1]
            if label in labels:
                raise Exception("duplicate label")
            labels[label] = count
        else:
            count += 1  # only increase count if none of above
            temp_data += line + "\n"
    assembly_data = temp_data

    assembly_data = assembly_data.strip()

    # loop and replace labels
    for label in labels:
        loc = Bits(uint=labels[label], length=16)
        assembly_data = re.sub("(?<=(\\s|,))@" + label + "\\._high(?=(,|\\n))",
                               "$0x" + loc[:8].hex, assembly_data)
        assembly_data = re.sub("(?<=(\\s|,))@" + label + "\\._low(?=(,|\\n))",
                               "$0x" + loc[8:].hex, assembly_data)

    # add infinite loop at end
    assembly_data += "\nBUC $0\n"

    return assembly_data
