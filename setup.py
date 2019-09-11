"""
Build options for JCC.

This file is a part of Jake's C Compiler (JCC)
(c) Copyright 2019 Jacob Larkin
"""

import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}


exe_options = Executable(
                        script="jcc/jcc.py",
                        targetName="jcc.exe",
                        base=None
                        )

setup(
    name="jcc",
    version="0.1",
    description="description",
    options={"build_exe": build_exe_options},
    executables=[exe_options])
