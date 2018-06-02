#!/usr/bin/env python3

# Example from:
# https://github.com/antlr/antlr4/blob/master/doc/python-target.md

import sys
from antlr4 import *
from .Chipy8Lexer import Chipy8Lexer
from .Chipy8Parser import Chipy8Parser
 
def main(argv):
    input = FileStream(argv[1])
    lexer = Chipy8Lexer(input)
    stream = CommonTokenStream(lexer)
    parser = Chipy8Parser(stream)
    tree = parser.startRule()
 
if __name__ == '__main__':
    main(sys.argv)
