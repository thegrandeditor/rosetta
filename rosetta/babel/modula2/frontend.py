from antlr4 import *
from rosetta.babel.modula2.grammar.Modula2Lexer import Modula2Lexer
from rosetta.babel.modula2.grammar.Modula2Parser import Modula2Parser
from rosetta.babel.modula2.antlr_visitor import RosettaModula2Visitor
from rosetta.babel.base.base import BabelFrontend
from rosetta.ir.nodes import RosettaNode

class Modula2Frontend(BabelFrontend):
    @property
    def language_id(self) -> str:
        return "modula2"

    @property
    def supported_version(self) -> str:
        return "PIM4"

    def parse(self, source: str) -> RosettaNode:
        input_stream = InputStream(source)
        lexer = Modula2Lexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = Modula2Parser(stream)
        tree = parser.program()
        
        visitor = RosettaModula2Visitor()
        return visitor.visit(tree)
