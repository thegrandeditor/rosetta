from antlr4 import *
from rosetta.babel.base.base import BabelFrontend
from rosetta.babel.ml.grammar.MLLexer import MLLexer
from rosetta.babel.ml.grammar.MLParser import MLParser
from rosetta.babel.ml.antlr_visitor import RosettaMLVisitor
from rosetta.ir.nodes import Program

class MLFrontend(BabelFrontend):
    @property
    def language_id(self) -> str:
        return "ml"

    @property
    def supported_version(self) -> str:
        return "Standard ML / OCaml subset"

    def parse(self, source: str) -> Program:
        input_stream = InputStream(source)
        lexer = MLLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = MLParser(stream)
        tree = parser.program()
        
        visitor = RosettaMLVisitor()
        return visitor.visit(tree)
