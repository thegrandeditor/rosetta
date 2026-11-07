# Generated from rosetta/babel/prolog/grammar/Prolog.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PrologParser import PrologParser
else:
    from PrologParser import PrologParser

# This class defines a complete generic visitor for a parse tree produced by PrologParser.

class PrologVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PrologParser#program.
    def visitProgram(self, ctx:PrologParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrologParser#clause.
    def visitClause(self, ctx:PrologParser.ClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrologParser#fact.
    def visitFact(self, ctx:PrologParser.FactContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrologParser#rule.
    def visitRule(self, ctx:PrologParser.RuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrologParser#query.
    def visitQuery(self, ctx:PrologParser.QueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrologParser#term_list.
    def visitTerm_list(self, ctx:PrologParser.Term_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrologParser#term.
    def visitTerm(self, ctx:PrologParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrologParser#structure.
    def visitStructure(self, ctx:PrologParser.StructureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrologParser#list.
    def visitList(self, ctx:PrologParser.ListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrologParser#atom.
    def visitAtom(self, ctx:PrologParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrologParser#variable.
    def visitVariable(self, ctx:PrologParser.VariableContext):
        return self.visitChildren(ctx)



del PrologParser