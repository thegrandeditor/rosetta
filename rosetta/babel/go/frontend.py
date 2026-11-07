from rosetta.babel.base.base import BabelFrontend
from rosetta.babel.base.modern_parser import ModernLanguageParser
from rosetta.ir.nodes import Program


class GoFrontend(BabelFrontend):
    @property
    def language_id(self) -> str:
        return "go"

    @property
    def supported_version(self) -> str:
        return "Go 1.22"

    def parse(self, source: str) -> Program:
        return ModernLanguageParser("go").parse(source)
