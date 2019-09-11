"""
Contains tests to see if the tokenizer is working correctly.

This file is a part of Jake's C Compiler (JCC)
(c) Copyright 2019 Jacob Larkin
"""

import pytest

from jcc.token import *


def test_random1():
    """Tokenize program."""
    source = """
int main(){
    float foo = 4.2;
    return 0;

}

"""
    tokens = []

    tokens.append(Token(TokenType.KEYWORD, 'int'))
    tokens.append(Token(TokenType.IDENTIFIER, 'main'))
    tokens.append(Token(TokenType.OPEN_PARENTHESIS, '('))
    tokens.append(Token(TokenType.CLOSE_PARENTHESIS, ')'))
    tokens.append(Token(TokenType.OPEN_BRACE, '{'))
    tokens.append(Token(TokenType.KEYWORD, 'float'))
    tokens.append(Token(TokenType.IDENTIFIER, 'foo'))
    tokens.append(Token(TokenType.EQUALS, '='))
    tokens.append(Token(TokenType.LITERAL_FLOAT_DECIMAL, '4.2'))
    tokens.append(Token(TokenType.SEMICOLON, ';'))
    tokens.append(Token(TokenType.KEYWORD, 'return'))
    tokens.append(Token(TokenType.LITERAL_INTEGER_DECIMAL, '0'))
    tokens.append(Token(TokenType.SEMICOLON, ';'))
    tokens.append(Token(TokenType.CLOSE_BRACE, '}'))

    assert tokens == tokenize(source)


def test_random2():
    """Tokenize program."""
    source = """
int main(Chicken bill)
{
    Chicken foo = bill;
    return 0;
}

"""
    tokens = []

    tokens.append(Token(TokenType.KEYWORD, 'int'))
    tokens.append(Token(TokenType.IDENTIFIER, 'main'))
    tokens.append(Token(TokenType.OPEN_PARENTHESIS, '('))
    tokens.append(Token(TokenType.IDENTIFIER, 'Chicken'))
    tokens.append(Token(TokenType.IDENTIFIER, 'bill'))
    tokens.append(Token(TokenType.CLOSE_PARENTHESIS, ')'))
    tokens.append(Token(TokenType.OPEN_BRACE, '{'))
    tokens.append(Token(TokenType.IDENTIFIER, 'Chicken'))
    tokens.append(Token(TokenType.IDENTIFIER, 'foo'))
    tokens.append(Token(TokenType.EQUALS, '='))
    tokens.append(Token(TokenType.IDENTIFIER, 'bill'))
    tokens.append(Token(TokenType.SEMICOLON, ';'))
    tokens.append(Token(TokenType.KEYWORD, 'return'))
    tokens.append(Token(TokenType.LITERAL_INTEGER_DECIMAL, '0'))
    tokens.append(Token(TokenType.SEMICOLON, ';'))
    tokens.append(Token(TokenType.CLOSE_BRACE, '}'))

    assert tokens == tokenize(source)
