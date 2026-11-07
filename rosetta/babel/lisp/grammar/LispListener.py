# Generated from rosetta/babel/lisp/grammar/Lisp.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .LispParser import LispParser
else:
    from LispParser import LispParser

# This class defines a complete listener for a parse tree produced by LispParser.
class LispListener(ParseTreeListener):

    # Enter a parse tree produced by LispParser#program.
    def enterProgram(self, ctx:LispParser.ProgramContext):
        pass

    # Exit a parse tree produced by LispParser#program.
    def exitProgram(self, ctx:LispParser.ProgramContext):
        pass


    # Enter a parse tree produced by LispParser#expression.
    def enterExpression(self, ctx:LispParser.ExpressionContext):
        pass

    # Exit a parse tree produced by LispParser#expression.
    def exitExpression(self, ctx:LispParser.ExpressionContext):
        pass


    # Enter a parse tree produced by LispParser#atom.
    def enterAtom(self, ctx:LispParser.AtomContext):
        pass

    # Exit a parse tree produced by LispParser#atom.
    def exitAtom(self, ctx:LispParser.AtomContext):
        pass


    # Enter a parse tree produced by LispParser#list.
    def enterList(self, ctx:LispParser.ListContext):
        pass

    # Exit a parse tree produced by LispParser#list.
    def exitList(self, ctx:LispParser.ListContext):
        pass


    # Enter a parse tree produced by LispParser#quote.
    def enterQuote(self, ctx:LispParser.QuoteContext):
        pass

    # Exit a parse tree produced by LispParser#quote.
    def exitQuote(self, ctx:LispParser.QuoteContext):
        pass


    # Enter a parse tree produced by LispParser#identifier.
    def enterIdentifier(self, ctx:LispParser.IdentifierContext):
        pass

    # Exit a parse tree produced by LispParser#identifier.
    def exitIdentifier(self, ctx:LispParser.IdentifierContext):
        pass


    # Enter a parse tree produced by LispParser#number.
    def enterNumber(self, ctx:LispParser.NumberContext):
        pass

    # Exit a parse tree produced by LispParser#number.
    def exitNumber(self, ctx:LispParser.NumberContext):
        pass


    # Enter a parse tree produced by LispParser#string.
    def enterString(self, ctx:LispParser.StringContext):
        pass

    # Exit a parse tree produced by LispParser#string.
    def exitString(self, ctx:LispParser.StringContext):
        pass



del LispParser