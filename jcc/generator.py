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
        self.source_line_num = 0
        self.to_be_commented = None

    def visit_ArrayDecl(self, node):  # ArrayDecl: [type*, dim*, dim_quals]
        """Call on each ArrayDecl visit."""
        raise NotImplementedError()

    def visit_ArrayRef(self, node):  # ArrayRef: [name*, subscript*]
        """Call on each ArrayRef visit."""
        raise NotImplementedError()

    def visit_Assignment(self, node):  # Assignment: [op, lvalue*, rvalue*]
        """Call on each Assignment visit."""
        raise NotImplementedError()

    def visit_BinaryOp(self, node):  # BinaryOp: [op, left*, right*]
        """Call on each BinaryOp visit."""
        print(node.left.coord.line, node.coord,node.right.coord)
        if node.op == "+":
            self.visit(node.left)
            self.instr("PUSH %RA")
            self.visit(node.right)
            self.instr("POP %R0")
            self.instr("ADD %R0, %RA")
        elif node.op == "-":
            self.visit(node.left)
            self.instr("PUSH %RA")
            self.visit(node.right)
            self.instr("POP %R0")
            self.instr("SUB %R0, %RA")
        elif node.op == "*":
            pass
        elif node.op == "/":
            pass
        elif node.op == "%":
            pass
        elif node.op == "|":
            pass
        elif node.op == "&":
            pass
        elif node.op == "^":
            pass
        elif node.op == "<<":
            pass
        elif node.op == ">>":
            pass
        elif node.op == "||":
            pass
        elif node.op == "&&":
            pass
        elif node.op == "<":
            pass
        elif node.op == "<=":
            pass
        elif node.op == ">":
            pass
        elif node.op == ">=":
            pass
        elif node.op == "==":
            pass
        elif node.op == "!=":
            pass

    def visit_Break(self, node):  # Break: []
        """Call on each Break visit."""
        raise NotImplementedError()

    def visit_Case(self, node):  # Case: [expr*, stmts**]
        """Call on each Case visit."""
        raise NotImplementedError()

    def visit_Cast(self, node):  # Cast: [to_type*, expr*]
        """Call on each Cast visit."""
        raise NotImplementedError()

    def visit_Compound(self, node):  # Compound: [block_items**]
        """Call on each Compound visit."""
        raise NotImplementedError()

    def visit_CompoundLiteral(self, node):  # CompoundLiteral: [type*, init*]
        """Call on each CompoundLiteral visit."""
        raise NotImplementedError()

    def visit_Constant(self, node):  # Constant: [type, value]
        """Call on each Constant visit."""
        if node.type == "int":
            self.instr("MOVI ${0}, %RA".format(node.value))
        elif node.type == "char":
            raise NotImplementedError()
        elif node.type == "float":
            raise NotImplementedError()

    def visit_Continue(self, node):  # Continue: []
        """Call on each Continue visit."""
        raise NotImplementedError()

    def visit_Decl(self, node):
        # Decl: [name, quals, storage, funcspec, type*, init*, bitsize*]
        """Call on each Decl visit."""
        raise NotImplementedError()

    def visit_DeclList(self, node):  # DeclList: [decls**]
        """Call on each DeclList visit."""
        raise NotImplementedError()

    def visit_Default(self, node):  # Default: [stmts**]
        """Call on each Default visit."""
        raise NotImplementedError()

    def visit_DoWhile(self, node):  # DoWhile: [cond*, stmt*]
        """Call on each DoWhile visit."""
        raise NotImplementedError()

    def visit_EllipsisParam(self, node):  # EllipsisParam: []
        """Call on each EllipsisParam visit."""
        raise NotImplementedError()

    def visit_EmptyStatement(self, node):  # EmptyStatement: []
        """Call on each EmptyStatement visit."""
        raise NotImplementedError()

    def visit_Enum(self, node):  # Enum: [name, values*]
        """Call on each Enum visit."""
        raise NotImplementedError()

    def visit_Enumerator(self, node):  # Enumerator: [name, value*]
        """Call on each Enumerator visit."""
        raise NotImplementedError()

    def visit_EnumeratorList(self, node):  # EnumeratorList: [enumerators**]
        """Call on each EnumeratorList visit."""
        raise NotImplementedError()

    def visit_ExprList(self, node):  # ExprList: [exprs**]
        """Call on each ExprList visit."""
        raise NotImplementedError()

    # def visit_FileAST(self, node):  # FileAST: [ext**]
    #    """Call on each FileAST visit."""

    def visit_For(self, node):  # For: [init*, cond*, next*, stmt*]
        """Call on each For visit."""
        raise NotImplementedError()

    def visit_FuncCall(self, node):  # FuncCall: [name*, args*]
        """Call on each FuncCall visit."""
        raise NotImplementedError()

    def visit_FuncDecl(self, node):  # FuncDecl: [args*, type*]
        """Call on each FuncDecl visit."""
        raise NotImplementedError()

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
        raise NotImplementedError()

    def visit_ID(self, node):  # ID: [name]
        """Call on each ID visit."""
        raise NotImplementedError()

    def visit_IdentifierType(self, node):  # IdentifierType: [names]
        """Call on each IdentifierType visit."""
        raise NotImplementedError()

    def visit_If(self, node):  # If: [cond*, iftrue*, iffalse*]
        """Call on each If visit."""
        raise NotImplementedError()

    def visit_InitList(self, node):  # InitList: [exprs**]
        """Call on each InitList visit."""
        raise NotImplementedError()

    def visit_Label(self, node):  # Label: [name, stmt*]
        """Call on each Label visit."""
        raise NotImplementedError()

    def visit_NamedInitializer(self, node):  # NamedInitializer: [name**,expr*]
        """Call on each NamedInitializer visit."""
        raise NotImplementedError()

    def visit_ParamList(self, node):  # ParamList: [params**]
        """Call on each ParamList visit."""
        raise NotImplementedError()

    def visit_PtrDecl(self, node):  # PtrDecl: [quals, type*]
        """Call on each PtrDecl visit."""
        raise NotImplementedError()

    def visit_Return(self, node):  # Return: [expr*]
        """Call on each Return visit."""
        self.visit(node.expr)

    def visit_Struct(self, node):  # Struct: [name, decls**]
        """Call on each Struct visit."""
        raise NotImplementedError()

    def visit_StructRef(self, node):  # StructRef: [name*, type, field*]
        """Call on each StructRef visit."""
        raise NotImplementedError()

    def visit_Switch(self, node):  # Switch: [cond*, stmt*]
        """Call on each Switch visit."""
        raise NotImplementedError()

    def visit_TernaryOp(self, node):  # TernaryOp: [cond*, iftrue*, iffalse*]
        """Call on each TernaryOp visit."""
        raise NotImplementedError()

    def visit_TypeDecl(self, node):  # TypeDecl: [declname, quals, type*]
        """Call on each TypeDecl visit."""
        raise NotImplementedError()

    def visit_Typedef(self, node):  # Typedef: [name, quals, storage, type*]
        """Call on each Typedef visit."""
        raise NotImplementedError()

    def visit_Typename(self, node):  # Typename: [name, quals, type*]
        """Call on each Typename visit."""
        raise NotImplementedError()

    def visit_UnaryOp(self, node):  # UnaryOp: [op, expr*]
        """Call on each UnaryOp visit. Most falsely assume RA is a short."""
        # self.comment('unary operator "{0}"'.format(node.op))
        self.visit(node.expr)
        if node.op == "+":
            pass  # do nothing on (+ expr)
        elif node.op == "-":
            self.instr("MOVI $0, %R0")
            self.instr("SUBI $RA, %R0")
            self.instr("MOV $R0, %RA")
        elif node.op == "~":
            self.instr("XORI $65535, %RA")
        elif node.op == "!":
            self.instr("CMPI $0, %RA")
            self.instr("BEQ $2")
            self.instr("MOVI $0, %RA")
            self.instr("BUC $1")
            self.instr("MOVI $1, %RA")
        elif node.op == "&":
            raise NotImplementedError()
        elif node.op == "*":
            raise NotImplementedError()
        elif node.op == "++":
            raise NotImplementedError()
        elif node.op == "--":
            raise NotImplementedError()
        else:
            raise Exception("Unknown Unary Operator:", node.op)

    def visit_Union(self, node):  # Union: [name, decls**]
        """Call on each Union visit."""
        raise NotImplementedError()

    def visit_While(self, node):  # While: [cond*, stmt*]
        """Call on each While visit."""
        raise NotImplementedError()

    def visit_Pragma(self, node):  # Pragma: [string]
        """Call on each Pragma visit."""
        raise NotImplementedError()

    def generate(self, ast):
        """Wrap visit and return result."""
        self.instr("JUC main")
        self.visit(ast)
        self.label(".end")
        return self.assembly_data

    def label(self, l):
        """Add label."""
        self.assembly_data += l + ":\n"

    def instr(self, i, comment=None):
        """Add instruction."""
        if self.to_be_commented is not None:
            comment = self.to_be_commented
            self.to_be_commented = None
        if comment is not None:
            self.assembly_data += "    {0}".format(i)
            self.comment(comment)
        else:
            self.assembly_data += "    {0}\n".format(i)

    def comment(self, c, to_be_commented=False):
        """Add comment."""
        if not to_be_commented:
            self.assembly_data += "    ; {0}\n".format(c)
        else:
            self.to_be_commented = to_be_commented


def generate(ast):
    """Generate assembly code from abstract syntax tree."""
    av = AssemblyGenerator()
    assembly_data = av.generate(ast)

    return assembly_data
