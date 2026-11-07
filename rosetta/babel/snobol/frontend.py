from antlr4 import *
from rosetta.babel.base.base import BabelFrontend
from rosetta.babel.snobol.grammar.Snobol4Lexer import Snobol4Lexer
from rosetta.babel.snobol.grammar.Snobol4Parser import Snobol4Parser
from rosetta.babel.snobol.antlr_visitor import RosettaSnobolVisitor
from rosetta.ir.nodes import Program

class SnobolAntlrFrontend(BabelFrontend):
    @property
    def language_id(self) -> str:
        return "snobol"

    @property
    def supported_version(self) -> str:
        return "SNOBOL4"

    @property
    def source_extensions(self) -> list[str]:
        return [".sno", ".snobol"]

    def parse(self, source_code: str) -> Program:
        # Ensure it ends with a newline for the grammar
        if not source_code.endswith("\n"):
            source_code += "\n"
            
        input_stream = InputStream(source_code)
        lexer = Snobol4Lexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = Snobol4Parser(stream)
        tree = parser.program()
        
        visitor = RosettaSnobolVisitor()
        return visitor.visit(tree)

SnobolFrontend = SnobolAntlrFrontend
