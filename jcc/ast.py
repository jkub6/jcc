"""
Create and manage an abstract syntax tree from a token list.

This file is a part of Jake's C Compiler (JCC)
(c) Copyright 2019 Jacob Larkin
"""

from jcc.token import TokenType


def parse_statement():
    """Parse a statement node."""


def parse(tokens):
    """Parse token list into an AST."""


class Node:
    """A node for use wilthin an abstract syntax tree."""

    def __init__(self):
        """Override default constructor."""
        self.children = []


class Program():
    """Describes a program node."""

    def __init__(self):
        """Override default constructor."""


class AST:
    """Describes an abstract syntax tree."""

    def __init__(self):
        """Override default constructor."""
        self.root = None
