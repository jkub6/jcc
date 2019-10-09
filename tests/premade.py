"""
Contains utility function for loading premade test files.

This file is a part of Jake's C Compiler (JCC)
(c) Copyright 2019 Jacob Larkin
"""

import os


class FileGroup:
    """Represent a set of matching C code, assembly, and binary data."""

    def __init__(self):
        """Override default constructor."""
        self.c_filepath = ""
        self.assembly_filepath = ""
        self.clean_filepath = ""
        self.binary_filepath = ""
        self.c_data = ""
        self.assembly_data = ""
        self.clean_data = ""
        self.binary_data = ""


def load_files(stage_num, valid):
    """Load all files for a given stage number."""
    file_groups = []
    if valid:
        path = "./tests/premade/stage_{0}/valid".format(stage_num)
    else:
        path = "./tests/premade/stage_{0}/invalid".format(stage_num)
    filenames = os.listdir(path)
    for filename in filenames:
        if os.path.isfile(os.path.join(path, filename)):
            if filename.endswith(".c"):
                fg = FileGroup()
                fg.c_filepath = os.path.join(path, filename)
                fg.assembly_filepath = os.path.join(path, filename[:-2]+".s")
                fg.binary_filepath = os.path.join(path, filename[:-2]+".dat")
                fg.clean_filepath = os.path.join(path,
                                                 filename[:-2]+".scl")
                fg.c_data = open(fg.c_filepath, "r").read()

                try:
                    fg.assembly_data = open(fg.assembly_filepath, "r").read()
                except:
                    fg.assembly_data = "Error loading file"
                try:
                    fg.clean_data = open(fg.clean_filepath, "r").read()
                except:
                    fg.clean_data = "Error loading file"
                try:
                    fg.binary_data = open(fg.binary_filepath, "r").read()
                except:
                    fg.binary_data = "Error loading file"

                file_groups.append(fg)
    return file_groups
