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


skips = ["3div", "3mod", "3associativity_2",
         "4skip_on_failure_multi_short_circuit",
         "4skip_on_failure_short_circuit_and",
         "4skip_on_failure_short_circuit_or"]
skips += ["8break", "8continue_empty_post", "8continue", "8do_while",
          "8empty_expression", "8for_decl", "8for_empty", "8for_nested_scope",
          "8for_variable_shadow", "8for", "8nested_break"]
skips += ["8nested_while"]
skips += ["9fib", "9forward_decl_args",
          "9forward_decl_multi_arg", "9forward_decl",
          "9fun_in_expr", "9hello_world", "9later_decl",
          "9mutual_recursion",
          "9rename_function_param"]
skips += ["10forward_declaration", "10fun_shadowed_by_variable",
          "10global_not_initialized", "10global_shadowed", "10global",
          "10multiple_global"]
skips += ["1bin_num", "1hex_num"]
stages = [i+1 for i in range(11)]
parameters = []
ids = []
for stage in stages:
    for fileGroup in load_files(stage, True):
        parameters.append((stage, fileGroup, 0))
        ids.append(str(stage) + ":" + fileGroup.name + ".s")
        # parameters.append((stage, fileGroup, 1))
        # ids.append(str(stage) + ":" + fileGroup.name + ".scl")
        # parameters.append((stage, fileGroup, 2))
        # ids.append(str(stage) + ":" + fileGroup.name + ".dat")


@pytest.mark.parametrize("stage, fileGroup, phase", parameters, ids=ids)
def test(stage, fileGroup, phase):
    """Test parsing a whole bunch of premade file groups."""
    if str(stage)+fileGroup.name in skips:
        pytest.skip("Unimplemented")

    tmp_args = [fileGroup.c_filepath, "-cla", "-A", "tests/tmp/tmp.s",
                "-L", "tests/tmp/tmp.scl", "-B", "tests/tmp/tmp.dat",
                "-r", "0"]

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


stages_inv = [i+1 for i in range(10)]
parameters_inv = []
ids_inv = []
skips_inv = ["3malformed_paren", "8out_of_scope_do_while",
             "10non_constant_init", "9declaration_mismatch",
             "9declaration_mismatch_2"]
# skips_inv += ["9bad_arg", "9declaration_mismatch", "9declaration_mismatch_2",
#               "9redefine_function", "9too_many_args"]
for stage in stages_inv:
    for fileGroup in load_files(stage, False):
        parameters_inv.append((stage, fileGroup))
        ids_inv.append(str(stage) + ":" + fileGroup.name)


@pytest.mark.parametrize("stage, fileGroup", parameters_inv, ids=ids_inv)
def test_inv(stage, fileGroup):
    """Test parsing a whole bunch of premade file groups."""
    if str(stage)+fileGroup.name in skips_inv:
        pytest.skip("Unimplemented")

    tmp_args = [fileGroup.c_filepath, "-cla", "-A", "tests/tmp/tmp.s",
                "-L", "tests/tmp/tmp.scl", "-B", "tests/tmp/tmp.dat"]

    with pytest.raises(SystemExit) as pytest_wrapped_e:
        jcc.run(tmp_args)
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 3


def teardown_module(module):
    """Teardown the module."""
    shutil.rmtree("tests/tmp")
