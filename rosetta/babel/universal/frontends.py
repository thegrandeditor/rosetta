"""
rosetta/babel/universal/frontends.py
------------------------------------
BABEL frontends for the Rosetta universal language expansion. All of them
share the structural :class:`ModernLanguageParser`, which understands brace-
scoped, ``end``-scoped (Lua/Julia/Elixir), and shell-style (Bash) blocks.
"""
from __future__ import annotations

from rosetta.babel.base.base import BabelFrontend
from rosetta.babel.base.modern_parser import ModernLanguageParser
from rosetta.ir.nodes import Program


class ModernFrontend(BabelFrontend):
    LANG = "universal"
    VERSION = "Draft"

    @property
    def language_id(self) -> str:
        return self.LANG

    @property
    def supported_version(self) -> str:
        return self.VERSION

    def parse(self, source: str) -> Program:
        return ModernLanguageParser(self.LANG).parse(source)


def _make(lang: str, version: str, cls_name: str) -> type:
    return type(cls_name, (ModernFrontend,), {"LANG": lang, "VERSION": version})


CSharpFrontend = _make("csharp", "C# 12", "CSharpFrontend")
DartFrontend = _make("dart", "Dart 3", "DartFrontend")
LuaFrontend = _make("lua", "Lua 5.4", "LuaFrontend")
RFrontend = _make("r", "R 4.4", "RFrontend")
JuliaFrontend = _make("julia", "Julia 1.10", "JuliaFrontend")
ScalaFrontend = _make("scala", "Scala 3", "ScalaFrontend")
HaskellFrontend = _make("haskell", "Haskell 2010 (imperative subset)", "HaskellFrontend")
ElixirFrontend = _make("elixir", "Elixir 1.16", "ElixirFrontend")
BashFrontend = _make("bash", "Bash 5", "BashFrontend")
SQLFrontend = _make("sql", "T-SQL (procedural subset)", "SQLFrontend")
ObjectiveCFrontend = _make("objc", "Objective-C 2.0", "ObjectiveCFrontend")
MoveFrontend = _make("move", "Move 2", "MoveFrontend")
PerlFrontend = _make("perl", "Perl 5.38", "PerlFrontend")

# extension / alias -> Frontend class
UNIVERSAL_FRONTENDS = {
    ".cs": CSharpFrontend, ".csharp": CSharpFrontend,
    ".dart": DartFrontend,
    ".lua": LuaFrontend,
    ".r": RFrontend,
    ".jl": JuliaFrontend, ".julia": JuliaFrontend,
    ".scala": ScalaFrontend, ".sc": ScalaFrontend,
    ".hs": HaskellFrontend, ".haskell": HaskellFrontend,
    ".ex": ElixirFrontend, ".exs": ElixirFrontend, ".elixir": ElixirFrontend,
    ".sh": BashFrontend, ".bash": BashFrontend,
    ".sql": SQLFrontend,
    ".m": ObjectiveCFrontend, ".objc": ObjectiveCFrontend,
    ".move": MoveFrontend,
    ".pm": PerlFrontend, ".plx": PerlFrontend, ".perl": PerlFrontend,
}
