"""
Generate assembly code from an abstract syntax tree.

This file is a part of Jake's C Compiler (JCC)
(c) Copyright 2019 Jacob Larkin
"""

import sys

import pycparser
from bitstring import Bits

from jcc.parser import ParseError


class Scope:
    """Deffine a scope of variables within a given block."""

    def __init__(self):
        """Override default constructor."""
        self.variables = {}
        self.stack_index = 1


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
        self.readability = 0
        self.assembly_data = ""
        self.source_line_num = 0
        self.to_be_commented = None
        self.node_data_lookup = {}

        self.function_decs = []
        self.function_defs = []
        self.num_ternaries = 0
        self.num_ifs = 0
        self.num_loops = 0
        self.found_return = False
        self.found_main = False
        self.jumped_to_main = False

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

    def create_scope(self, node):
        """Create a new scope for a node, and maintains previous index."""
        scope = Scope()
        prev_scope = self.get_closest_scope(node)
        if prev_scope is not None:
            scope.stack_index = prev_scope.stack_index
        self.set_scope(node, scope)

    def get_closest_function(self, node):
        """Get the function that a node is inside of."""
        while node is not None:
            if isinstance(node, pycparser.c_ast.FuncDef):
                return node.decl.name
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
        """Wrap visit function, but set."""
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
            print(node.lvalue)
            print(type(node.lvalue))
            if (isinstance(node.lvalue, pycparser.c_ast.UnaryOp) and
               node.lvalue.op == "*"):
                print("oi", node.rvalue, node.lvalue)
                self.pvisit(node.rvalue, node)
                self.instr("PUSHPP %RA")
                self.pvisit(node.lvalue.expr, node)
                # self.instr("MOV %T0, %RA")

                self.instr("POPP %T0")
                self.instr("STOR %T0, %RA")
            else:
                # TODO visit left node instead of just taking name
                # if isinstance(node.lvalue, type): # check if lvalue is a var
                self.pvisit(node.rvalue, node)
                self._assignment(node.lvalue.name, node)
        else:
            raise NotImplementedError()

    def visit_BinaryOp(self, node):  # BinaryOp: [op, left*, right*]
        """Call on each BinaryOp visit."""
        self.pvisit(node.left, node)
        self.instr("PUSHPP %RA")
        self.endl()
        self.pvisit(node.right, node)
        self.instr("POPPP %T0")
        self.endl()
        if node.op == "+":
            self.instr("ADD %T0, %RA", "+")
        elif node.op == "-":
            self.instr("SUB %RA, %T0", "-")
            self.instr("MOV %T0, %RA")
        elif node.op == "*":
            self.instr("MUL %T0, %RA", "*")
        elif node.op == "/":
            pass
        elif node.op == "%":
            pass
        elif node.op == "|":
            self.instr("OR %T0, %RA", "|")
        elif node.op == "&":
            self.instr("AND %T0, %RA", "&")
        elif node.op == "^":
            self.instr("XOR %T0, %RA", "^")
        elif node.op == "<<":
            pass
        elif node.op == ">>":
            pass
        elif node.op == "||":
            self.instr("CMPI $0, %T0", "||")
            self.instr("BEQ $3")
            self.instr("MOVI $1, %T1")
            self.instr("BUC $2")
            self.instr("MOVI $0, %T1")

            self.instr("CMPI $0, %RA")
            self.instr("BEQ $2")
            self.instr("MOVI $1, %T1")
            self.instr("MOV %T1, %RA")
        elif node.op == "&&":
            self.instr("CMPI $0, %T0", "&&")
            self.instr("BEQ $3")
            self.instr("MOVI $1, %T1")
            self.instr("BUC $2")
            self.instr("MOVI $0, %T1")

            self.instr("CMPI $0, %RA")
            self.instr("BNE $2")
            self.instr("MOVI $0, %T1")
            self.instr("MOV %T1, %RA")
        elif node.op == "<":
            self.instr("CMP %T0, %RA", "<")
            self.instr("BLT $3")
            self.instr("MOVI $0, %RA")
            self.instr("BUC $2")
            self.instr("MOVI $1, %RA")
        elif node.op == "<=":
            self.instr("CMP %T0, %RA", "<=")
            self.instr("BLE $3")
            self.instr("MOVI $0, %RA")
            self.instr("BUC $2")
            self.instr("MOVI $1, %RA")
        elif node.op == ">":
            self.instr("CMP %T0, %RA", ">")
            self.instr("BGT $3")
            self.instr("MOVI $0, %RA")
            self.instr("BUC $2")
            self.instr("MOVI $1, %RA")
        elif node.op == ">=":
            self.instr("CMP %T0, %RA", ">=")
            self.instr("BGE $3")
            self.instr("MOVI $0, %RA")
            self.instr("BUC $2")
            self.instr("MOVI $1, %RA")
        elif node.op == "==":
            self.instr("CMP %T0, %RA", "==")
            self.instr("BEQ $3")
            self.instr("MOVI $0, %RA")
            self.instr("BUC $2")
            self.instr("MOVI $1, %RA")
        elif node.op == "!=":
            self.instr("CMP %T0, %RA", "!=")
            self.instr("BNE $3")
            self.instr("MOVI $0, %RA")
            self.instr("BUC $2")
            self.instr("MOVI $1, %RA")
        self.endl()

    def visit_Break(self, node):  # Break: []
        """Call on each Break visit."""
        loop_num = self.num_loops - 1
        self.num_loops -= 1

        if loop_num == -1:
            self.error("Error, break statement outside of loop", node)

        self.instr("JUC @.loop{0}_end".format(loop_num), "break")

    def visit_Case(self, node):  # Case: [expr*, stmts**]
        """Call on each Case visit."""
        raise NotImplementedError()

    def visit_Cast(self, node):  # Cast: [to_type*, expr*]
        """Call on each Cast visit."""
        raise NotImplementedError()

    def visit_Compound(self, node):  # Compound: [block_items**]
        """Call on each Compound visit."""
        self.create_scope(node)
        for c in node:
            self.pvisit(c, node)

    def visit_CompoundLiteral(self, node):  # CompoundLiteral: [type*, init*]
        """Call on each CompoundLiteral visit."""
        raise NotImplementedError()

    def visit_Constant(self, node):  # Constant: [type, value]
        """Call on each Constant visit."""
        if node.type == "int":
            self.comment("constant: " + node.value, in_future=True)

            self._constant(node.value, "RA")
            # self.instr("MOVI ${0}, %RA".format(node.value), "constant")
        elif node.type == "char":
            raise NotImplementedError()
        elif node.type == "float":
            raise NotImplementedError()
        self.endl()

    def visit_Continue(self, node):  # Continue: []
        """Call on each Continue visit."""
        loop_num = self.num_loops - 1
        self.num_loops -= 1

        if loop_num == -1:
            self.error("Error, continue statement outside of loop", node)

        self.instr("JUC @.loop{0}_begin".format(loop_num), "continue")

    def visit_Decl(self, node):  # TODO make work with bitsizes
        # Decl: [name, quals, storage, funcspec, type*, init*, bitsize*]
        """Call on each Decl visit."""
        self.pvisit(node.type, node)

        if node.init is not None:
            self.pvisit(node.init, node)
            self._assignment(node.name, node)

    def visit_DeclList(self, node):  # DeclList: [decls**]
        """Call on each DeclList visit."""
        for c in node:
            self.pvisit(c, node)

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
        # do nothing

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
        self.create_scope(node)

        function_defs = []

        # do everything except function deffinitions first
        for c in node:
            if isinstance(node, pycparser.c_ast.FuncDef):
                function_defs.append(c)
            else:
                self.pvisit(c, node)

        for c in function_defs:
            self.pvisit(c, node)

    def visit_For(self, node):  # For: [init*, cond*, next*, stmt*]
        """Call on each For visit."""
        self.create_scope(node)

        loop_num = self.num_loops
        self.num_loops += 1

        if node.init is not None:
            self.pvisit(node.init, node)

        self.label(".loop{0}_begin".format(loop_num))
        if node.cond is not None:
            self.pvisit(node.cond, node)
            self.instr("CMPI $0, %RA", "loop{0}".format(loop_num))
            self.instr("JEQ @.loop{0}_end".format(loop_num))

        self.pvisit(node.stmt, node)

        if node.next is not None:
            self.pvisit(node.next, node)

        self.instr("JUC @.loop{0}_begin".format(loop_num))
        self.label(".loop{0}_end".format(loop_num))
        self.endl()

    def visit_FuncCall(self, node):  # FuncCall: [name*, args*]
        """Call on each FuncCall visit."""
        name = node.name.name
        argc = 0
        if node.args is not None:
            argc = len(node.args.exprs)

        if (name, argc) not in self.function_defs:
            self.error("Error, Function has not been defined: "
                       + name, node)

        if node.args is not None:
            for i, arg in enumerate(node.args):
                self.pvisit(arg, node)
                self.instr("PUSH %RA", "arg_"+str(i))
                self.endl()
        self.instr("JAL @{0}, %RA".format(node.name.name))
        if node.args is not None:
            self.instr("ADDI ${0}, %SP".format(len(node.args.exprs)))

    def visit_FuncDecl(self, node):  # FuncDecl: [args*, type*]
        """Call on each FuncDecl visit."""
        name = node.type.declname
        argc = 0

        self.comment("declaring func {0}".format(name), readability=2)

        # check if name is same as a variable
        scope = self.get_closest_scope(node)
        if name in scope.variables.keys():
            if scope.variables[name] != "@"+name:
                self.error(name + " variable exists!", node)
        scope.variables[name] = "@"+name

        if node.args is not None:
            argc = len(node.args.params)
        if (name, argc) in self.function_decs:
            self.error("Error, Function already declared elsewhere: "
                       + name, node)
        self.function_decs.append((name, argc))

    def visit_FuncDef(self, node):  # FuncDef: [decl*, param_decls**, body*]
        """Call on each FuncDef visit."""
        name = node.decl.name
        argc = 0
        if node.decl.type.args is not None:
            argc = len(node.decl.type.args.params)

        self.comment("defining func {0}".format(name), readability=2)

        # check if name is same as a variable
        scope = self.get_closest_scope(node)
        if name in scope.variables.keys():
            if scope.variables[name] != "@"+name:
                self.error(name + " variable exists!", node)
        scope.variables[name] = "@"+name

        if (name, argc) not in self.function_decs:
            self.function_decs.append((name, argc))

        if (name, argc) in self.function_defs:
            self.error("Error, Function already deffined elsewhere: "
                       + name, node)
        self.function_defs.append((name, argc))

        self.found_return = False

        self.create_scope(node)

        if node.decl.type.args is not None:
            scope = self.get_scope(node)
            for i, arg in enumerate(reversed(list(node.decl.type.args))):
                scope.variables[arg.name] = -3 - i

        if not self.jumped_to_main:
            self.instr("JUC @main")
            self.jumped_to_main = True

        self.label(node.decl.name)
        if node.decl.name != "main":
            self.comment("function prep here")
            self.instr("PUSH %RA")
            self.instr("PUSH %BP")
            self.instr("MOV %SP, %BP")

        for c in node.body:
            self.pvisit(c, node)

        if node.decl.name == "main":
            # self.found_main = True
            self.instr("MOVI $0, %RA")
            self.instr("JUC @{0}._cleanup".format(node.decl.name))

        self.label("{0}._cleanup".format(node.decl.name))

        if node.decl.name != "main":
            self.instr("MOV %BP, %SP")
            self.instr("POP %BP")
            self.instr("POP %T0")
            self.instr("ADDI $1, %T0")
            self.instr("JUC %T0")
        else:
            self.instr("JUC @.end")
        self.endl()
        self.endl()

    def visit_Goto(self, node):  # Goto: [name]
        """Call on each Goto visit."""
        raise NotImplementedError()

    def visit_ID(self, node):  # ID: [name]
        """Call on each ID visit."""
        dist = self.get_variable_location(node.name, node)
        if dist is None:
            self.error(node.name + " not found in scope", node)
        self.instr("MOV %BP, %T0", "load " + node.name)
        if dist >= 0:
            self._constant(dist, "T1", unsigned=False)
            self.instr("SUB %T1, %T0")  # todo make subu
        else:
            self._constant(-dist, "T1", unsigned=False)
            self.instr("ADD %T1, %T0")
        self.instr("LOAD %RA, %T0")
        self.endl()

    def visit_IdentifierType(self, node):  # IdentifierType: [names]
        """Call on each IdentifierType visit."""
        raise NotImplementedError()

    def visit_If(self, node):  # If: [cond*, iftrue*, iffalse*]
        """Call on each If visit."""
        if_num = self.num_ifs
        self.num_ifs += 1

        self.pvisit(node.cond, node)
        self.instr("CMPI $0, %RA", "if{0}".format(if_num))
        self.instr("JEQ @.if{0}_else".format(if_num))
        self.pvisit(node.iftrue, node)
        self.instr("JUC @.if{0}_end".format(if_num))
        self.label(".if{0}_else".format(if_num))
        if node.iffalse is not None:
            self.pvisit(node.iffalse, node)
        self.label(".if{0}_end".format(if_num))
        self.endl()

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
        self.found_return = True
        if node.expr is None:
            self.error("No value to return", node)
        self.pvisit(node.expr, node)
        func_name = self.get_closest_function(node)
        self.instr("JUC @{0}._cleanup".format(func_name))

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
        ter_num = self.num_ternaries
        self.num_ternaries += 1

        self.pvisit(node.cond, node)
        self.instr("CMPI $0, %RA", "ter{0}".format(ter_num))
        self.instr("JEQ @.ter{0}_false".format(ter_num))
        self.pvisit(node.iftrue, node)
        self.instr("JUC @.ter{0}_done".format(ter_num))
        self.label(".ter{0}_false".format(ter_num))
        self.pvisit(node.iffalse, node)
        self.label(".ter{0}_done".format(ter_num))
        self.endl()

    def visit_TypeDecl(self, node):  # TypeDecl: [declname, quals, type*]
        """Call on each TypeDecl visit."""
        # check if short, then:
        size_in_bytes = 1

        self.comment("declaring {0}".format(node.declname), readability=2)

        scope = self.get_closest_scope(node)
        if node.declname in scope.variables.keys():
            self.error(node.declname + " is already in scope!", node)
        scope.variables[node.declname] = scope.stack_index
        scope.stack_index += size_in_bytes

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
            self.instr("MOVI $0, %T0", "neg")
            self.instr("SUB %RA, %T0")
            self.instr("MOV %T0, %RA")
        elif node.op == "~":
            # self.instr("NOT %RA, %RA", "not")
            self.instr("XORI -1, %RA", "not")
        elif node.op == "!":
            self.instr("CMPI $0, %RA", "!")
            self.instr("BEQ $3")
            self.instr("MOVI $0, %RA")
            self.instr("BUC $2")
            self.instr("MOVI $1, %RA")
        elif node.op == "&":
            self.instr("MOV %T0, %RA")  # todo cur depend on visit
        elif node.op == "*":
            self.instr("LOAD %RA, %RA")  # todo probably broken
        elif node.op == "++":
            raise NotImplementedError()
        elif node.op == "--":
            raise NotImplementedError()
        else:
            raise Exception("Unknown Unary Operator:", node.op)
        self.endl()

    def visit_Union(self, node):  # Union: [name, decls**]
        """Call on each Union visit."""
        raise NotImplementedError()

    def visit_While(self, node):  # While: [cond*, stmt*]
        """Call on each While visit."""
        self.create_scope(node)

        loop_num = self.num_loops
        self.num_loops += 1

        self.label(".loop{0}_begin".format(loop_num))
        self.pvisit(node.cond, node)
        self.instr("CMPI $0, %RA", "loop{0}".format(loop_num))
        self.instr("JEQ @.loop{0}_end".format(loop_num))
        self.pvisit(node.stmt, node)
        self.instr("JUC @.loop{0}_begin".format(loop_num))
        self.label(".loop{0}_end".format(loop_num))
        self.endl()

    def visit_Pragma(self, node):  # Pragma: [string]
        """Call on each Pragma visit."""
        raise NotImplementedError()

    def _assignment(self, name, node):
        """Assign value to variable."""
        dist = self.get_variable_location(name, node)
        if dist is None:
            self.error(node.name + " not found in scope", node)
        self.instr("MOV %BP, %T0", "store " + name)
        self._constant(dist, "T1", unsigned=False)
        self.instr("SUB %T1, %T0")  # todo make sub u
        self.instr("STOR %RA, %T0")
        self.endl()

    def _constant(self, value, reg, unsigned=False):
        """Set register to constant."""
        value = str(value)

        if value == "0":
            value = "0x0000"

        try:
            bits = Bits(value, length=16)
        except ValueError:
            if unsigned:
                bits = Bits(uint=int(value), length=16)
            else:
                bits = Bits(int=int(value), length=16)

        if bits.length == 2:
            bits = Bits(int=bits.int, length=16)

        self.instr("LUI $0x{}, %{}".format(bits[:8].hex, reg))
        self.instr("ADDUI $0x{}, %{}".format(bits[8:].hex, reg))

    def _push(self, register):
        """Push the given register onto the stack."""

    def generate(self, ast, readability):
        """Wrap visit and return result."""
        self.readability = readability
        self.pvisit(ast, None)
        self.label(".end")
        return self.assembly_data

    def label(self, l):
        """Add label."""
        self.assembly_data += l + ":\n"

    def instr(self, i, comment=None, readability=1):
        """Add instruction."""
        if readability <= self.readability:
            if self.to_be_commented is not None:
                comment = self.to_be_commented
                self.to_be_commented = None
            if comment is not None:
                self.assembly_data += "    {0}".format(i)
                self.comment(comment)
            else:
                self.assembly_data += "    {0}\n".format(i)
        else:
            self.assembly_data += "    {0}\n".format(i)

    def comment(self, c, in_future=False, readability=1):
        """Add comment."""
        if readability <= self.readability:
            if not in_future:
                self.assembly_data += "    ; {0}\n".format(c)
            else:
                self.to_be_commented = c

    def endl(self, readability=2):
        """Print new line in assembly."""
        if readability <= self.readability:
            self.assembly_data += "\n"

    def error(self, message, node):
        """Throw correct exception if error."""
        # rse ParseError("line: {0}, No return value".format(node.coord.line))
        print("line: {0}, {1}".format(node.coord.line, message))
        sys.exit(3)


def generate(ast, readability=0):
    """Generate assembly code from abstract syntax tree."""
    av = AssemblyGenerator()
    assembly_data = av.generate(ast, readability)

    return assembly_data
