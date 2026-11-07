from antlr4 import *
from rosetta.babel.base.base import BabelFrontend
from rosetta.babel.pli.grammar.PLILexer import PLILexer
from rosetta.babel.pli.grammar.PLIParser import PLIParser
from rosetta.babel.pli.antlr_visitor import RosettaPLIVisitor
from rosetta.ir.nodes import Program

class PLIAntlrFrontend(BabelFrontend):
    @property
    def language_id(self) -> str:
        return "pli"

    @property
    def supported_version(self) -> str:
        return "PL/I (Simplified)"

    @property
    def source_extensions(self) -> list[str]:
        return [".pli", ".pl1"]

    def parse(self, source_code: str) -> Program:
        input_stream = InputStream(source_code)
        lexer = PLILexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = PLIParser(stream)
        tree = parser.program()
        
        visitor = RosettaPLIVisitor()
        return visitor.visit(tree)

PLIFrontend = PLIAntlrFrontend
