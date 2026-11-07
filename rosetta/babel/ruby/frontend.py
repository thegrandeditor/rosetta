from rosetta.babel.base.base import BabelFrontend
from rosetta.babel.base.modern_parser import ModernLanguageParser
from rosetta.ir.nodes import Program


class RubyFrontend(BabelFrontend):
    @property
    def language_id(self) -> str:
        return "ruby"

    @property
    def supported_version(self) -> str:
        return "Ruby 3.3"

    def parse(self, source: str) -> Program:
        return ModernLanguageParser("ruby").parse(source)
