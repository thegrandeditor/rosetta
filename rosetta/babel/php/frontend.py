from rosetta.babel.base.base import BabelFrontend
from rosetta.babel.base.modern_parser import ModernLanguageParser
from rosetta.ir.nodes import Program


class PHPFrontend(BabelFrontend):
    @property
    def language_id(self) -> str:
        return "php"

    @property
    def supported_version(self) -> str:
        return "PHP 8.3"

    def parse(self, source: str) -> Program:
        return ModernLanguageParser("php").parse(source)
