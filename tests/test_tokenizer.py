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
    correct_tokens = []

    correct_tokens.append(Token(TokenType.KEYWORD, 'int'))
    correct_tokens.append(Token(TokenType.IDENTIFIER, 'main'))
    correct_tokens.append(Token(TokenType.OPEN_PARENTHESIS, '('))
    correct_tokens.append(Token(TokenType.CLOSE_PARENTHESIS, ')'))
    correct_tokens.append(Token(TokenType.OPEN_BRACE, '{'))
    correct_tokens.append(Token(TokenType.KEYWORD, 'float'))
    correct_tokens.append(Token(TokenType.IDENTIFIER, 'foo'))
    correct_tokens.append(Token(TokenType.EQUALS, '='))
    correct_tokens.append(Token(TokenType.LITERAL_FLOAT_DECIMAL, '4.2'))
    correct_tokens.append(Token(TokenType.SEMICOLON, ';'))
    correct_tokens.append(Token(TokenType.KEYWORD, 'return'))
    correct_tokens.append(Token(TokenType.LITERAL_INTEGER_DECIMAL, '0'))
    correct_tokens.append(Token(TokenType.SEMICOLON, ';'))
    correct_tokens.append(Token(TokenType.CLOSE_BRACE, '}'))

    tokens = tokenize(source)
    assert correct_tokens == tokens


def test_random2():
    """Tokenize program."""
    source = """
int main(Chicken bill)
{
    Chicken foo = bill;
    return 0;
}

"""
    correct_tokens = []

    correct_tokens.append(Token(TokenType.KEYWORD, 'int'))
    correct_tokens.append(Token(TokenType.IDENTIFIER, 'main'))
    correct_tokens.append(Token(TokenType.OPEN_PARENTHESIS, '('))
    correct_tokens.append(Token(TokenType.IDENTIFIER, 'Chicken'))
    correct_tokens.append(Token(TokenType.IDENTIFIER, 'bill'))
    correct_tokens.append(Token(TokenType.CLOSE_PARENTHESIS, ')'))
    correct_tokens.append(Token(TokenType.OPEN_BRACE, '{'))
    correct_tokens.append(Token(TokenType.IDENTIFIER, 'Chicken'))
    correct_tokens.append(Token(TokenType.IDENTIFIER, 'foo'))
    correct_tokens.append(Token(TokenType.EQUALS, '='))
    correct_tokens.append(Token(TokenType.IDENTIFIER, 'bill'))
    correct_tokens.append(Token(TokenType.SEMICOLON, ';'))
    correct_tokens.append(Token(TokenType.KEYWORD, 'return'))
    correct_tokens.append(Token(TokenType.LITERAL_INTEGER_DECIMAL, '0'))
    correct_tokens.append(Token(TokenType.SEMICOLON, ';'))
    correct_tokens.append(Token(TokenType.CLOSE_BRACE, '}'))

    tokens = tokenize(source)
    assert correct_tokens == tokens
