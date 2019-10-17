"""
Clean assembly file. Replace labels, pseudo instructions, etc...

This file is a part of Jake's C Compiler (JCC)
(c) Copyright 2019 Jacob Larkin
"""

import re


def clean(assembly_data):
    """Take assembly, Swap labels for addresses, remove whitespace, etc."""
    labels = {}

    # initial pass for label locations
    count = 0
    clean_data = ""
    for line in assembly_data.split("\n"):
        line = line.strip()
        line = line.split(";")[0]
        line = line.strip()
        if line == "":  # if blank line or was a comment
            continue
        if line.endswith(":"):
            label = line[:-1]
            if label in labels:
                raise Exception("duplicate label")
            labels[label] = str(count)
        else:
            count += 1  # only increase count if none of above
            clean_data += line + "\n"

    # second pass for replacing
    for label in labels:
        clean_data = re.sub("(?<=(\\s|,))" + label + "(?=(,|\\n))",
                            "$" + labels[label], clean_data)
    return clean_data
