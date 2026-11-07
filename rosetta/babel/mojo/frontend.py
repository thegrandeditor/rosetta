from antlr4 import *
from rosetta.babel.base.base import BabelFrontend
from rosetta.babel.mojo.grammar.MojoLexer import MojoLexer
from rosetta.babel.mojo.grammar.MojoParser import MojoParser
from rosetta.babel.mojo.antlr_visitor import RosettaMojoVisitor
from rosetta.ir.nodes import Program

class MojoFrontend(BabelFrontend):
    @property
    def language_id(self) -> str:
        return "mojo"

    @property
    def supported_version(self) -> str:
        return "Mojo ^24.1"

    def parse(self, source: str) -> Program:
        input_stream = InputStream(source)
        lexer = MojoLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = MojoParser(stream)
        tree = parser.program()
        
        visitor = RosettaMojoVisitor()
        return visitor.visit(tree)
