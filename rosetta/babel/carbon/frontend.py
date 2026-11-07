from antlr4 import *
from rosetta.babel.base.base import BabelFrontend
from rosetta.babel.carbon.grammar.CarbonLexer import CarbonLexer
from rosetta.babel.carbon.grammar.CarbonParser import CarbonParser
from rosetta.babel.carbon.antlr_visitor import RosettaCarbonVisitor
from rosetta.ir.nodes import Program

class CarbonFrontend(BabelFrontend):
    @property
    def language_id(self) -> str:
        return "carbon"

    @property
    def supported_version(self) -> str:
        return "0.1"

    def parse(self, source: str) -> Program:
        input_stream = InputStream(source)
        lexer = CarbonLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = CarbonParser(stream)
        tree = parser.program()
        
        visitor = RosettaCarbonVisitor()
        return visitor.visit(tree)
