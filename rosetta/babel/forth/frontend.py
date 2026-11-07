from antlr4 import *
from rosetta.babel.base.base import BabelFrontend
from rosetta.babel.forth.grammar.ForthLexer import ForthLexer
from rosetta.babel.forth.grammar.ForthParser import ForthParser
from rosetta.babel.forth.antlr_visitor import RosettaForthVisitor
from rosetta.ir.nodes import Program

class ForthFrontend(BabelFrontend):
    @property
    def language_id(self) -> str:
        return "forth"

    @property
    def supported_version(self) -> str:
        return "ANS Forth"

    def parse(self, source: str) -> Program:
        input_stream = InputStream(source)
        lexer = ForthLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = ForthParser(stream)
        tree = parser.program()
        
        visitor = RosettaForthVisitor()
        return visitor.visit(tree)
