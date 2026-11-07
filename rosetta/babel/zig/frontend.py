from antlr4 import *
from rosetta.babel.base.base import BabelFrontend
from rosetta.babel.zig.grammar.ZigLexer import ZigLexer
from rosetta.babel.zig.grammar.ZigParser import ZigParser
from rosetta.babel.zig.antlr_visitor import RosettaZigVisitor
from rosetta.ir.nodes import Program

class ZigFrontend(BabelFrontend):
    @property
    def language_id(self) -> str:
        return "zig"

    @property
    def supported_version(self) -> str:
        return "Zig ^0.11"

    def parse(self, source: str) -> Program:
        input_stream = InputStream(source)
        lexer = ZigLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = ZigParser(stream)
        tree = parser.program()
        
        visitor = RosettaZigVisitor()
        return visitor.visit(tree)
