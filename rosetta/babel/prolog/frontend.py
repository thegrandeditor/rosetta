from antlr4 import *
from rosetta.babel.prolog.grammar.PrologLexer import PrologLexer
from rosetta.babel.prolog.grammar.PrologParser import PrologParser
from rosetta.babel.prolog.grammar.PrologVisitor import PrologVisitor
from rosetta.babel.base.base import BabelFrontend
from rosetta.ir.nodes import *

class RosettaPrologVisitor(PrologVisitor):
    def visitProgram(self, ctx: PrologParser.ProgramContext):
        body = []
        for clause in ctx.clause():
            res = self.visit(clause)
            if res: body.append(res)
        return Program(body=body)

    def visitClause(self, ctx: PrologParser.ClauseContext):
        return self.visit(ctx.getChild(0))

    def visitFact(self, ctx: PrologParser.FactContext):
        term = self.visit(ctx.term())
        if isinstance(term, CallExpression):
             return Fact(predicate=term.callee.name, terms=term.args)
        return Fact(predicate=term.name if hasattr(term, 'name') else str(term), terms=[])

    def visitRule(self, ctx: PrologParser.RuleContext):
        head = self.visit(ctx.term())
        body = self.visit(ctx.term_list())
        # Re-wrap head if it's a CallExpression into a Fact for PrologClause
        if isinstance(head, CallExpression):
            head = Fact(predicate=head.callee.name, terms=head.args)
        elif isinstance(head, Identifier):
            head = Fact(predicate=head.name, terms=[])
        
        return PrologRule(clauses=[PrologClause(head=head, body=body)])

    def visitQuery(self, ctx: PrologParser.QueryContext):
        body = self.visit(ctx.term_list())
        return Query(predicate="query", terms=body)

    def visitTerm_list(self, ctx: PrologParser.Term_listContext):
        return [self.visit(t) for t in ctx.term()]

    def visitTerm(self, ctx: PrologParser.TermContext):
        if ctx.getText() == '!': return Identifier(name="!")
        if ctx.atom(): return Identifier(name=ctx.atom().getText())
        if ctx.variable(): return Identifier(name=ctx.variable().getText())
        if ctx.list_(): return self.visit(ctx.list_())
        if ctx.structure(): return self.visit(ctx.structure())
        if ctx.term(): return self.visit(ctx.term())
        return None

    def visitStructure(self, ctx: PrologParser.StructureContext):
        pred = ctx.atom().getText()
        args = self.visit(ctx.term_list())
        return CallExpression(callee=Identifier(name=pred), args=args)

    def visitList(self, ctx: PrologParser.ListContext):
        if ctx.getChildCount() == 2: # []
             return Literal(value=[])
        terms = self.visit(ctx.term_list())
        if ctx.term():
             tail = self.visit(ctx.term())
             return BinaryExpression(left=Literal(value=terms), operator="|", right=tail)
        return Literal(value=terms)

class PrologAntlrFrontend(BabelFrontend):
    @property
    def language_id(self) -> str:
        return "prolog"

    @property
    def supported_version(self) -> str:
        return "ISO Prolog"

    @property
    def source_extensions(self) -> list[str]:
        return [".pl", ".pro"]

    def parse(self, source_code: str) -> Program:
        input_stream = InputStream(source_code)
        lexer = PrologLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = PrologParser(stream)
        tree = parser.program()
        
        visitor = RosettaPrologVisitor()
        return visitor.visit(tree)

PrologFrontend = PrologAntlrFrontend
