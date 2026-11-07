from rosetta.babel.base.base import BabelFrontend
from rosetta.babel.base.modern_parser import ModernLanguageParser
from rosetta.ir.nodes import Program


class CFrontend(BabelFrontend):
    @property
    def language_id(self) -> str:
        return "c"

    @property
    def supported_version(self) -> str:
        return "ISO C17"

    def parse(self, source: str) -> Program:
        return ModernLanguageParser("c").parse(source)
