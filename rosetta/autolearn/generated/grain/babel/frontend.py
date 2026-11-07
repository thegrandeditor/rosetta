from rosetta.babel.base.modern_parser import ModernLanguageParser
try:
    from antlr4 import *  # noqa: F401,F403  (used once ANTLR parser classes are generated)
except ImportError:  # pragma: no cover
    pass
from rosetta.babel.base.base import BabelFrontend
from rosetta.ir.nodes import *

class RosettaGrainVisitor(object):
    def visit(self, tree):
        if not tree:
            return None
        return tree.accept(self)

    def visitChildren(self, node):
        result = []
        for i in range(node.getChildCount()):
            child = node.getChild(i)
            res = self.visit(child)
            if res:
                if isinstance(res, list):
                    result.extend(res)
                else:
                    result.append(res)
        return result

    def visitProgram(self, ctx):
        body = []
        for i in range(ctx.getChildCount()):
            res = self.visit(ctx.getChild(i))
            if res:
                if isinstance(res, list):
                    body.extend(res)
                else:
                    body.append(res)
        return Program(body=body)

    def visitProg(self, ctx):
        return self.visitChildren(ctx)

    def visitExpr(self, ctx):
        # Automatically identified expression rule
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        return Literal(value=ctx.getText())

class GrainFrontend(BabelFrontend):
    @property
    def language_id(self) -> str:
        return "grain"

    @property
    def supported_version(self) -> str:
        return "Draft Standard"

    def parse(self, source: str) -> Program:
        # If ANTLR has generated GrainLexer/GrainParser next to the
        # grammar, the visitor above can be wired in. Until then, use Rosetta's
        # universal structural parser so the learned language works immediately.
        return ModernLanguageParser("grain").parse(source)
