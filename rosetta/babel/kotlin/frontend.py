from rosetta.babel.base.base import BabelFrontend
from rosetta.babel.base.modern_parser import ModernLanguageParser
from rosetta.ir.nodes import Program


class KotlinFrontend(BabelFrontend):
    @property
    def language_id(self) -> str:
        return "kotlin"

    @property
    def supported_version(self) -> str:
        return "Kotlin 2.0"

    def parse(self, source: str) -> Program:
        return ModernLanguageParser("kotlin").parse(source)
