from antlr4 import *
from rosetta.babel.base.base import BabelFrontend
from rosetta.babel.python.grammar.Python3Lexer import Python3Lexer
from rosetta.babel.python.grammar.Python3Parser import Python3Parser
from rosetta.babel.python.antlr_visitor import RosettaPythonVisitor
from rosetta.ir.nodes import Program

class PythonAntlrFrontend(BabelFrontend):
    @property
    def language_id(self) -> str:
        return "python"

    @property
    def supported_version(self) -> str:
        return "3.11+"

    @property
    def source_extensions(self) -> list[str]:
        return [".py"]

    def parse(self, source_code: str) -> Program:
        input_stream = InputStream(source_code)
        lexer = Python3Lexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = Python3Parser(stream)
        tree = parser.file_input()
        
        visitor = RosettaPythonVisitor()
        return visitor.visit(tree)
