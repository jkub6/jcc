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

    def visit_ArrayDecl(self, node):  # ArrayDecl: [type*, dim*, dim_quals]
        """Call on each ArrayDecl visit."""

    def visit_ArrayRef(self, node):  # ArrayRef: [name*, subscript*]
        """Call on each ArrayRef visit."""

    def visit_Assignment(self, node):  # Assignment: [op, lvalue*, rvalue*]
        """Call on each Assignment visit."""

    def visit_BinaryOp(self, node):  # BinaryOp: [op, left*, right*]
        """Call on each BinaryOp visit."""

    def visit_Break(self, node):  # Break: []
        """Call on each Break visit."""

    def visit_Case(self, node):  # Case: [expr*, stmts**]
        """Call on each Case visit."""

    def visit_Cast(self, node):  # Cast: [to_type*, expr*]
        """Call on each Cast visit."""

    def visit_Compound(self, node):  # Compound: [block_items**]
        """Call on each Compound visit."""

    def visit_CompoundLiteral(self, node):  # CompoundLiteral: [type*, init*]
        """Call on each CompoundLiteral visit."""

    def visit_Constant(self, node):  # Constant: [type, value]
        """Call on each Constant visit."""

    def visit_Continue(self, node):  # Continue: []
        """Call on each Continue visit."""

    def visit_Decl(self, node):
        # Decl: [name, quals, storage, funcspec, type*, init*, bitsize*]
        """Call on each Decl visit."""

    def visit_DeclList(self, node):  # DeclList: [decls**]
        """Call on each DeclList visit."""

    def visit_Default(self, node):  # Default: [stmts**]
        """Call on each Default visit."""

    def visit_DoWhile(self, node):  # DoWhile: [cond*, stmt*]
        """Call on each DoWhile visit."""

    def visit_EllipsisParam(self, node):  # EllipsisParam: []
        """Call on each EllipsisParam visit."""

    def visit_EmptyStatement(self, node):  # EmptyStatement: []
        """Call on each EmptyStatement visit."""

    def visit_Enum(self, node):  # Enum: [name, values*]
        """Call on each Enum visit."""

    def visit_Enumerator(self, node):  # Enumerator: [name, value*]
        """Call on each Enumerator visit."""

    def visit_EnumeratorList(self, node):  # EnumeratorList: [enumerators**]
        """Call on each EnumeratorList visit."""

    def visit_ExprList(self, node):  # ExprList: [exprs**]
        """Call on each ExprList visit."""

    def visit_FileAST(self, node):  # FileAST: [ext**]
        """Call on each FileAST visit."""

    def visit_For(self, node):  # For: [init*, cond*, next*, stmt*]
        """Call on each For visit."""

    def visit_FuncCall(self, node):  # FuncCall: [name*, args*]
        """Call on each FuncCall visit."""

    def visit_FuncDecl(self, node):  # FuncDecl: [args*, type*]
        """Call on each FuncDecl visit."""

    def visit_FuncDef(self, node):  # FuncDef: [decl*, param_decls**, body*]
        """Call on each FuncDef visit."""
        self.label(node.decl.name)
        if node.decl.name != "main":
            self.comment("function prep here")

        for c in node.body:
            self.visit(c)

        if node.decl.name != "main":
            self.comment("function clean-up here")
        else:
            self.instr("JUC .end")

    def visit_Goto(self, node):  # Goto: [name]
        """Call on each Goto visit."""

    def visit_ID(self, node):  # ID: [name]
        """Call on each ID visit."""

    def visit_IdentifierType(self, node):  # IdentifierType: [names]
        """Call on each IdentifierType visit."""

    def visit_If(self, node):  # If: [cond*, iftrue*, iffalse*]
        """Call on each If visit."""

    def visit_InitList(self, node):  # InitList: [exprs**]
        """Call on each InitList visit."""

    def visit_Label(self, node):  # Label: [name, stmt*]
        """Call on each Label visit."""

    def visit_NamedInitializer(self, node):  # NamedInitializer: [name**,expr*]
        """Call on each NamedInitializer visit."""

    def visit_ParamList(self, node):  # ParamList: [params**]
        """Call on each ParamList visit."""

    def visit_PtrDecl(self, node):  # PtrDecl: [quals, type*]
        """Call on each PtrDecl visit."""

    def visit_Return(self, node):  # Return: [expr*]
        """Call on each Return visit."""
        if isinstance(node.expr, pycparser.c_ast.Constant):
            # self.instr("XOR %RA, %RA")
            # self.instr("ADDI $" + str(node.expr.value) + ", %RA")
            self.instr("MOVI $" + str(node.expr.value) + ", %RA")

    def visit_Struct(self, node):  # Struct: [name, decls**]
        """Call on each Struct visit."""

    def visit_StructRef(self, node):  # StructRef: [name*, type, field*]
        """Call on each StructRef visit."""

    def visit_Switch(self, node):  # Switch: [cond*, stmt*]
        """Call on each Switch visit."""

    def visit_TernaryOp(self, node):  # TernaryOp: [cond*, iftrue*, iffalse*]
        """Call on each TernaryOp visit."""

    def visit_TypeDecl(self, node):  # TypeDecl: [declname, quals, type*]
        """Call on each TypeDecl visit."""

    def visit_Typedef(self, node):  # Typedef: [name, quals, storage, type*]
        """Call on each Typedef visit."""

    def visit_Typename(self, node):  # Typename: [name, quals, type*]
        """Call on each Typename visit."""

    def visit_UnaryOp(self, node):  # UnaryOp: [op, expr*]
        """Call on each UnaryOp visit."""

    def visit_Union(self, node):  # Union: [name, decls**]
        """Call on each Union visit."""

    def visit_While(self, node):  # While: [cond*, stmt*]
        """Call on each While visit."""

    def visit_Pragma(self, node):  # Pragma: [string]
        """Call on each Pragma visit."""

    def generate(self, ast):
        """Wrap visit and return result."""
        self.instr("JUC main")
        self.visit(ast)
        self.label(".end")
        return self.assembly_data

    def label(self, l):
        """Add label."""
        self.assembly_data += l + ":\n"

    def instr(self, i):
        """Add instruction."""
        self.assembly_data += "    " + i + "\n"

    def comment(self, c):
        """Add instruction."""
        self.assembly_data += "    ; " + c + "\n"


def generate(ast):
    """Generate assembly code from abstract syntax tree."""
    av = AssemblyGenerator()
    assembly_data = av.generate(ast)

    return assembly_data
