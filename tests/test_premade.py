"""
Contains tests for premade test files.

This file is a part of Jake's C Compiler (JCC)
(c) Copyright 2019 Jacob Larkin
"""

import os
import shutil

import pytest

import jcc


class FileGroup:
    """Represent a set of matching C code, assembly, and binary data."""

    def __init__(self):
        """Override default constructor."""
        self.name = ""
        self.c_filepath = ""
        self.assembly_filepath = ""
        self.clean_filepath = ""
        self.binary_filepath = ""
        self.c_data = ""
        self.assembly_data = ""
        self.clean_data = ""
        self.binary_data = ""

    def __repr__(self):
        """Override default repr."""
        return '<FileGroup: "{0}">'.format(self.name)


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
                fg.name = filename[:-2]
                fg.c_filepath = os.path.join(path, filename)
                fg.assembly_filepath = os.path.join(path, fg.name+".s")
                fg.clean_filepath = os.path.join(path, fg.name+".scl")
                fg.binary_filepath = os.path.join(path, fg.name+".dat")
                fg.c_data = open(fg.c_filepath, "r").read()

                try:
                    fg.assembly_data = open(fg.assembly_filepath, "r").read()
                except Exception:
                    fg.assembly_data = "Error loading file"
                try:
                    fg.clean_data = open(fg.clean_filepath, "r").read()
                except Exception:
                    fg.clean_data = "Error loading file"
                try:
                    fg.binary_data = open(fg.binary_filepath, "r").read()
                except Exception:
                    fg.binary_data = "Error loading file"

                file_groups.append(fg)
    return file_groups


stages = [i+1 for i in range(3)]
parameters = []
ids = []
for stage in stages:
    for fileGroup in load_files(stage, True):
        parameters.append((stage, fileGroup, 0))
        ids.append(str(stage) + ":" + fileGroup.name + ".s")
        parameters.append((stage, fileGroup, 1))
        ids.append(str(stage) + ":" + fileGroup.name + ".scl")
        # parameters.append((stage, fileGroup, 2))
        # ids.append(str(stage) + ":" + fileGroup.name + ".dat")


@pytest.mark.parametrize("stage, fileGroup, phase", parameters, ids=ids)
def test(stage, fileGroup, phase):
    """Test parsing a whole bunch of premade file groups."""
    tmp_args = [fileGroup.c_filepath, "-cla", "-A", "tests/tmp/tmp.s",
                "-L", "tests/tmp/tmp.scl", "-B", "tests/tmp/tmp.dat"]

    jcc.run(tmp_args)

    if phase == 0:
        with open(tmp_args[3], "r") as assembly_file:
            assert assembly_file.read() == fileGroup.assembly_data
    elif phase == 1:
        with open(tmp_args[5], "r") as cleaned_file:
            assert cleaned_file.read() == fileGroup.clean_data
    elif phase == 2:
        with open(tmp_args[7], "r") as binary_file:
            assert binary_file.read() == fileGroup.binary_data


def teardown_module(module):
    """Teardown the module."""
    shutil.rmtree("tests/tmp")
