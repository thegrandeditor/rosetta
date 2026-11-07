from rosetta.babel.base.base import BabelFrontend
from rosetta.babel.base.modern_parser import ModernLanguageParser
from rosetta.ir.nodes import Program


class SwiftFrontend(BabelFrontend):
    @property
    def language_id(self) -> str:
        return "swift"

    @property
    def supported_version(self) -> str:
        return "Swift 5.10"

    def parse(self, source: str) -> Program:
        return ModernLanguageParser("swift").parse(source)
