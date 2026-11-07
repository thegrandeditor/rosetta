from rosetta.babel.base.base import BabelFrontend
from rosetta.babel.base.modern_parser import ModernLanguageParser
from rosetta.ir.nodes import Program


class JavaScriptFrontend(BabelFrontend):
    @property
    def language_id(self) -> str:
        return "javascript"

    @property
    def supported_version(self) -> str:
        return "ECMAScript 2024 (ES15)"

    def parse(self, source: str) -> Program:
        return ModernLanguageParser("javascript").parse(source)
