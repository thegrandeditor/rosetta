from rosetta.babel.base.base import BabelFrontend
from rosetta.babel.base.modern_parser import ModernLanguageParser
from rosetta.ir.nodes import Program


class RustFrontend(BabelFrontend):
    @property
    def language_id(self) -> str:
        return "rust"

    @property
    def supported_version(self) -> str:
        return "Rust 2021 Edition"

    def parse(self, source: str) -> Program:
        return ModernLanguageParser("rust").parse(source)
