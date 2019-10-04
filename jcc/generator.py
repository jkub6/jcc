"""
Generate assembly code from an abstract syntax tree.

This file is a part of Jake's C Compiler (JCC)
(c) Copyright 2019 Jacob Larkin
"""

import pycparser


class AssemblyGenerator(pycparser.c_ast.NodeVisitor):
    """Generator class for creating assembly form asts."""

    def __init__(self):
        """Override default constructor."""
        self.assembly_data = ""

    def visit_FuncDef(self, node):
        """Call on each function deffinition visit."""
        self.label(node.decl.name)
        if node.decl.name != "main":
            self.comment("function prep here")

        for c in node.body:
            self.visit(c)

        if node.decl.name != "main":
            self.comment("function clean-up here")
        else:
            self.instr("JUMP .end")

    def visit_Return(self, node):
        """Call on return visit."""
        if isinstance(node.expr, pycparser.c_ast.Constant):
            self.instr("XOR %RA, %RA")
            self.instr("ADDI " + str(node.expr.value) + ", %RA")

    def generate(self, ast):
        """Wrap visit and return result."""
        self.instr("JUMP main")
        self.visit(ast)
        self.label(".end")
        return self.assembly_data

    def label(self, l):
        """Add label."""
        self.assembly_data += l + ":\n"

    def instr(self, i):
        """Add instruction."""
        self.assembly_data += "\t" + i + "\n"

    def comment(self, c):
        """Add instruction."""
        self.assembly_data += "\t; " + c + "\n"


def generate(ast):
    """Generate assembly code from abstract syntax tree."""
    av = AssemblyGenerator()
    assembly_data = av.generate(ast)

    return assembly_data
