"""
Contains Token class.

This file is a part of Jake's C Compiler (JCC)
(c) Copyright 2019 Jacob Larkin
"""

import re
from enum import Enum, auto


class TokenType(Enum):
    """Enum with all types of tokens."""

    KEYWORD = auto(),
    LITERAL_INTEGER_DECIMAL = auto(),
    LITERAL_INTEGER_HEXADECIMAL = auto(),
    LITERAL_INTEGER_OCTAL = auto(),
    LITERAL_FLOAT_DECIMAL = auto(),
    LITERAL_FLOAT_EXPONENTIAL = auto(),
    LITERAL_CHAR = auto(),
    LITERAL_STRING = auto(),
    OPEN_BRACE = auto(),
    CLOSE_BRACE = auto(),
    OPEN_PARENTHESIS = auto(),
    CLOSE_PARENTHESIS = auto(),
    OPEN_BRACKET = auto(),
    CLOSE_BRACKET = auto(),

    PLUS = auto(),
    MINUS = auto(),
    ASTERISK = auto(),
    SLASH = auto(),
    PERCENT = auto(),
    EQUALS = auto(),
    GREATER = auto(),
    LESS = auto(),
    EXCLAMATION = auto(),

    AMPERSAND = auto(),
    PIPE = auto(),
    CARET = auto(),
    TILDE = auto(),

    PERIOD = auto(),
    COMMA = auto(),
    COLON = auto(),
    SEMICOLON = auto(),
    OCTOTHORPE = auto(),
    QUESTION = auto(),

    IDENTIFIER = auto()

token_patterns = {
    TokenType.KEYWORD: ("auto|case|break|char|const|continut|default|do|"
                        "double|else|enum|extern|float|for|goto|if|int|long|"
                        "register|return|short|signed|sizeof|static|struct|"
                        "switch|typedef|union|unsigned|void|volitile|while,"),
    TokenType.LITERAL_INTEGER_DECIMAL: "[1-9][0-9]?(?!\\.)|0(?!\\.)",
    TokenType.LITERAL_INTEGER_HEXADECIMAL: "0[xX][0-9a-fA-F]+",
    TokenType.LITERAL_INTEGER_OCTAL: "0[0-9]+",
    TokenType.LITERAL_FLOAT_DECIMAL: "[0-9]*\\.[0-9]*",
    TokenType.LITERAL_FLOAT_EXPONENTIAL: "<TODO::1>",
    TokenType.LITERAL_CHAR: "<TODO::2>",
    TokenType.LITERAL_STRING: "<TODO::3>",
    TokenType.OPEN_BRACE: "{",
    TokenType.CLOSE_BRACE: "}",
    TokenType.OPEN_PARENTHESIS: "\\(",
    TokenType.CLOSE_PARENTHESIS: "\\)",
    TokenType.OPEN_BRACKET: "\\[",
    TokenType.CLOSE_BRACKET: "]",

    TokenType.PLUS: "\\+",
    TokenType.MINUS: "-",
    TokenType.ASTERISK: "\\*",
    TokenType.SLASH: "/",
    TokenType.PERCENT: "%",
    TokenType.EQUALS: "=",
    TokenType.LESS: "<",
    TokenType.GREATER: ">",
    TokenType.EXCLAMATION: "!",

    TokenType.AMPERSAND: "&",
    TokenType.PIPE: "\\|",
    TokenType.CARET: "\\^",
    TokenType.TILDE: "~",

    TokenType.PERIOD: "\\.",
    TokenType.COMMA: ",",
    TokenType.COLON: ":",
    TokenType.SEMICOLON: ";",
    TokenType.OCTOTHORPE: "#",
    TokenType.QUESTION: "\\?",

    TokenType.IDENTIFIER: "[a-zA-Z]\\w*"
    }


class Token():
    """Describes a complete token."""

    def __init__(self, type, source):
        """Override default constructor."""
        self.type = type
        self.source = source

    def __repr__(self):
        """Override default repr for testing."""
        return "<{}: '{}'>".format(self.type, self.source)

    def __eq__(self, obj):
        """Override default equality operator."""
        return self.type == obj.type and self.source == obj.source

for token in token_patterns:  # Compile patterns
    token_patterns[token] = re.compile(token_patterns[token])


def tokenize(source):
    """Return given source as a list of tokens."""
    tokens = []
    words = source.split()

    for raw_word in words:
        word = raw_word.strip()
        if word == "":
            continue

        while word != "":
            for type, pattern in token_patterns.items():
                match = pattern.match(word)
                if match:
                    tokens.append(Token(type, word[:match.end()]))
                    word = word[match.end():]
                    break

            if not match:  # Finished loop without matching
                print("Error, not found: '" + word + "'")
                break

    return tokens
