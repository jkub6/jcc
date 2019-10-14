"""
Generate assembly code from an abstract syntax tree.

This file is a part of Jake's C Compiler (JCC)
(c) Copyright 2019 Jacob Larkin
"""

import pycparser
import sys


class Scope:
    """Deffine a scope of variables within a given block."""

    def __init__(self):
        """Override default constructor."""
        self.variables = {}
        self.stack_index = 2


class NodeData:
    """Represent the data stored at each node."""

    def __init__(self, _parent, _scope=None):
        """Override default constructor."""
        self.scope = _scope
        self.parent = _parent


class AssemblyGenerator(pycparser.c_ast.NodeVisitor):
    """Generator class for creating assembly form asts."""

    def __init__(self):
        """Override default constructor."""
        self.assembly_data = ""
        self.source_line_num = 0
        self.to_be_commented = None
        self.node_data_lookup = {}

    def get_parent(self, node):
        """Return the parent of the given node."""
        if node not in self.node_data_lookup.keys():
            return None
        return self.node_data_lookup[node].parent

    def get_scope(self, node):
        """Return the parent of the given node."""
        if node not in self.node_data_lookup.keys():
            return None
        return self.node_data_lookup[node].scope

    def set_scope(self, node, _scope):
        """Return the scope for the given node."""
        if node not in self.node_data_lookup.keys():
            raise Exception("not in nodes, tried to set scope")
        self.node_data_lookup[node].scope = _scope

    def get_closest_scope(self, node):
        """Return the scope that belongs to."""
        while node is not None:
            scope = self.get_scope(node)
            if scope is not None:
                return self.get_scope(node)
            node = self.get_parent(node)
        return None

    def get_variable_location(self, name, node):
        """Return stack depth of a variable in the nearest scope, else None."""
        while node is not None:
            scope = self.get_scope(node)
            if scope is not None:
                if name in scope.variables.keys():
                    return scope.variables[name]  # might have to add per depth
            node = self.get_parent(node)
        return None

    def pvisit(self, node, parent):
        """Wrap visit function, but set parent."""
        self.node_data_lookup[node] = NodeData(parent)
        self.visit(node)

    def visit_ArrayDecl(self, node):  # ArrayDecl: [type*, dim*, dim_quals]
        """Call on each ArrayDecl visit."""
        raise NotImplementedError()

    def visit_ArrayRef(self, node):  # ArrayRef: [name*, subscript*]
        """Call on each ArrayRef visit."""
        raise NotImplementedError()

    def visit_Assignment(self, node):  # Assignment: [op, lvalue*, rvalue*]
        """Call on each Assignment visit."""
        if node.op == "=":
            # TODO visit left node instead of just taking name
            # if isinstance(node.lvalue, type): # check if lvalue is a variable
            self.pvisit(node.rvalue, node)
            self._assignment(node.lvalue.name, node)
        else:
            raise NotImplementedError()

    def visit_BinaryOp(self, node):  # BinaryOp: [op, left*, right*]
        """Call on each BinaryOp visit."""
        self.pvisit(node.left, node)
        self.instr("PUSH %RA")
        self.pvisit(node.right, node)
        self.instr("POP %R0")
        if node.op == "+":
            self.instr("ADD %R0, %RA")
        elif node.op == "-":
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
            self.instr("CMPI $0, %R0")
            self.instr("BEQ $0x4")
            self.instr("MOVI $1, %RA")
            self.instr("BUC $0x2")
            self.instr("MOVI $0, %RA")

            self.instr("CMPI $0, %RA")
            self.instr("BEQ $0x2")
            self.instr("MOVI $1, %RA")
        elif node.op == "&&":
            self.instr("CMPI $0, %R0")
            self.instr("BEQ $0x4")
            self.instr("MOVI $1, %RA")
            self.instr("BUC $0x2")
            self.instr("MOVI $0, %RA")

            self.instr("CMPI $0, %RA")
            self.instr("BNE $0x2")
            self.instr("MOVI $0, %RA")
        elif node.op == "<":
            self.instr("CMP $RA, %R0")
            self.instr("BLT $0x4")
            self.instr("MOVI $0, %RA")
            self.instr("BUC $0x2")
            self.instr("MOVI $1, %RA")
        elif node.op == "<=":
            self.instr("CMP $RA, %R0")
            self.instr("BLE $0x4")
            self.instr("MOVI $0, %RA")
            self.instr("BUC $0x2")
            self.instr("MOVI $1, %RA")
        elif node.op == ">":
            self.instr("CMP $RA, %R0")
            self.instr("BGT $0x4")
            self.instr("MOVI $0, %RA")
            self.instr("BUC $0x2")
            self.instr("MOVI $1, %RA")
        elif node.op == ">=":
            self.instr("CMP $RA, %R0")
            self.instr("BGE $0x4")
            self.instr("MOVI $0, %RA")
            self.instr("BUC $0x2")
            self.instr("MOVI $1, %RA")
        elif node.op == "==":
            self.instr("CMP $RA, %R0")
            self.instr("BEQ $0x4")
            self.instr("MOVI $0, %RA")
            self.instr("BUC $0x2")
            self.instr("MOVI $1, %RA")
        elif node.op == "!=":
            self.instr("CMP $RA, %R0")
            self.instr("BNE $0x4")
            self.instr("MOVI $0, %RA")
            self.instr("BUC $0x2")
            self.instr("MOVI $1, %RA")

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

    def visit_Decl(self, node):  # TODO make work with bitsizes
        # Decl: [name, quals, storage, funcspec, type*, init*, bitsize*]
        """Call on each Decl visit."""
        # check if short, then:
        size_in_bytes = 2

        scope = self.get_closest_scope(node)
        if node.type.declname in scope.variables:
            raise Exception(node.type.declname + " is already in scope!")
        scope.variables[node.type.declname] = scope.stack_index
        scope.stack_index += size_in_bytes

        if node.init is not None:
            self.pvisit(node.init, node)
            self._assignment(node.name, node)

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

    def visit_FileAST(self, node):  # FileAST: [ext**]
        """Call on each FileAST visit."""
        scope = Scope()
        self.set_scope(node, scope)
        for c in node:
            self.pvisit(c, node)

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
        found_return = False

        scope = Scope()  # add arguments to scope
        self.set_scope(node, scope)

        self.label(node.decl.name)
        if node.decl.name != "main":
            self.comment("function prep here")
            self.instr("PUSH %R12")
            self.instr("MOV %SP, %R12")

        for c in node.body:
            if isinstance(c, pycparser.c_ast.Return):
                found_return = True
            self.pvisit(c, node)

        if node.decl.name != "main":
            self.comment("function clean-up here")
            self.instr("MOV %R12, %SP")
            self.instr("POP %R12")
        else:
            if not found_return:
                self.instr("MOVI $0, %RA")
            self.instr("JUC .end")

    def visit_Goto(self, node):  # Goto: [name]
        """Call on each Goto visit."""
        raise NotImplementedError()

    def visit_ID(self, node):  # ID: [name]
        """Call on each ID visit."""
        dist = self.get_variable_location(node.name, node)
        if dist is None:
            raise Exception(node.name + " not found in scope")
        self.instr("MOV %R12, %R0")
        self.instr("SUBI ${0}, %R0".format(dist))
        self.instr("LOAD %RA, %R0")

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
        self.pvisit(node.expr, node)

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
        self.pvisit(node.expr, node)
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
            self.instr("BEQ $0x4")
            self.instr("MOVI $0, %RA")
            self.instr("BUC $0x2")
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

    def _assignment(self, name, node):
        """Assign value to variable."""
        dist = self.get_variable_location(name, node)
        if dist is None:
            raise Exception(name + " not found in scope")
        self.instr("MOV %R12, %R0")
        self.instr("SUBI ${0}, %R0".format(dist))
        self.instr("STOR %RA, %R0")

    def generate(self, ast):
        """Wrap visit and return result."""
        self.instr("JUC main")
        self.pvisit(ast, None)
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
