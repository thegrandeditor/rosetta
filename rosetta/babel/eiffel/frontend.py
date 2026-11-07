from antlr4 import *
from rosetta.babel.eiffel.grammar.EiffelLexer import EiffelLexer
from rosetta.babel.eiffel.grammar.EiffelParser import EiffelParser
from rosetta.babel.eiffel.antlr_visitor import RosettaEiffelVisitor
from rosetta.babel.base.base import BabelFrontend
from rosetta.ir.nodes import RosettaNode

class EiffelFrontend(BabelFrontend):
    @property
    def language_id(self) -> str:
        return "eiffel"

    @property
    def supported_version(self) -> str:
        return "ECMA-367"

    def parse(self, source: str) -> RosettaNode:
        input_stream = InputStream(source)
        lexer = EiffelLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = EiffelParser(stream)
        tree = parser.program()
        
        visitor = RosettaEiffelVisitor()
        return visitor.visit(tree)
