from rosetta.babel.base.base import BabelFrontend
from rosetta.babel.base.modern_parser import ModernLanguageParser
from rosetta.ir.nodes import Program


class TypeScriptFrontend(BabelFrontend):
    @property
    def language_id(self) -> str:
        return "typescript"

    @property
    def supported_version(self) -> str:
        return "TypeScript 5.x"

    def parse(self, source: str) -> Program:
        return ModernLanguageParser("typescript").parse(source)
