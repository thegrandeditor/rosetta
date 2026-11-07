import sys
from antlr4 import *
from rosetta.babel.fortran.grammar.FortranLexer import FortranLexer
from rosetta.babel.fortran.grammar.FortranParser import FortranParser
from rosetta.babel.fortran.antlr_visitor import RosettaFortranVisitor

def main():
    with open('rosetta/tests/fortran_hello.f90', 'r') as f:
        code = f.read()
    
    input_stream = InputStream(code)
    lexer = FortranLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = FortranParser(stream)
    tree = parser.program()
    
    if parser.getNumberOfSyntaxErrors() > 0:
        print(f"Syntax errors found: {parser.getNumberOfSyntaxErrors()}")
        return

    visitor = RosettaFortranVisitor()
    ir = visitor.visit(tree)
    print(ir)

if __name__ == "__main__":
    main()
