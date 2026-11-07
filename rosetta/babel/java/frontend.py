from rosetta.babel.base.base import BabelFrontend
from rosetta.babel.base.modern_parser import ModernLanguageParser
from rosetta.ir.nodes import Program


class JavaFrontend(BabelFrontend):
    @property
    def language_id(self) -> str:
        return "java"

    @property
    def supported_version(self) -> str:
        return "Java 21 LTS"

    def parse(self, source: str) -> Program:
        return ModernLanguageParser("java").parse(source)
