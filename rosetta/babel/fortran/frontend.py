from antlr4 import *
from rosetta.babel.base.base import BabelFrontend
from rosetta.babel.fortran.grammar.FortranLexer import FortranLexer
from rosetta.babel.fortran.grammar.FortranParser import FortranParser
from rosetta.babel.fortran.antlr_visitor import RosettaFortranVisitor
from rosetta.ir.nodes import Program

class FortranAntlrFrontend(BabelFrontend):
    @property
    def language_id(self) -> str:
        return "fortran"

    @property
    def supported_version(self) -> str:
        return "Fortran 90 (Subset)"

    @property
    def source_extensions(self) -> list[str]:
        return [".f90", ".f", ".for"]

    def parse(self, source_code: str) -> Program:
        input_stream = InputStream(source_code)
        lexer = FortranLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = FortranParser(stream)
        tree = parser.program()
        
        visitor = RosettaFortranVisitor()
        return visitor.visit(tree)

# For backward compatibility and discovery
FortranFrontend = FortranAntlrFrontend
