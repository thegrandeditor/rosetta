from rosetta.babel.base.base import BabelFrontend
from rosetta.babel.base.modern_parser import ModernLanguageParser
from rosetta.ir.nodes import Program


class CppFrontend(BabelFrontend):
    @property
    def language_id(self) -> str:
        return "cpp"

    @property
    def supported_version(self) -> str:
        return "ISO C++20"

    def parse(self, source: str) -> Program:
        return ModernLanguageParser("cpp").parse(source)
