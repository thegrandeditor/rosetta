# Generated from rosetta/babel/lisp/grammar/Lisp.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .LispParser import LispParser
else:
    from LispParser import LispParser

# This class defines a complete generic visitor for a parse tree produced by LispParser.

class LispVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LispParser#program.
    def visitProgram(self, ctx:LispParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LispParser#expression.
    def visitExpression(self, ctx:LispParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LispParser#atom.
    def visitAtom(self, ctx:LispParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LispParser#list.
    def visitList(self, ctx:LispParser.ListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LispParser#quote.
    def visitQuote(self, ctx:LispParser.QuoteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LispParser#identifier.
    def visitIdentifier(self, ctx:LispParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LispParser#number.
    def visitNumber(self, ctx:LispParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LispParser#string.
    def visitString(self, ctx:LispParser.StringContext):
        return self.visitChildren(ctx)



del LispParser