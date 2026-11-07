import sys
from antlr4 import *
from rosetta.babel.fortran.grammar.FortranLexer import FortranLexer

def main():
    with open('rosetta/tests/fortran_hello.f90', 'r') as f:
        code = f.read()
    
    input_stream = InputStream(code)
    lexer = FortranLexer(input_stream)
    for token in lexer.getAllTokens():
        text = token.text.replace('\n', '\\n').replace('\r', '\\r')
        type_name = lexer.symbolicNames[token.type] if token.type < len(lexer.symbolicNames) else "EOF"
        print(f"Token: {token.type}, Text: '{text}', TypeName: {type_name}")

if __name__ == "__main__":
    main()
