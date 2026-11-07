# Generated from rosetta/babel/prolog/grammar/Prolog.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PrologParser import PrologParser
else:
    from PrologParser import PrologParser

# This class defines a complete listener for a parse tree produced by PrologParser.
class PrologListener(ParseTreeListener):

    # Enter a parse tree produced by PrologParser#program.
    def enterProgram(self, ctx:PrologParser.ProgramContext):
        pass

    # Exit a parse tree produced by PrologParser#program.
    def exitProgram(self, ctx:PrologParser.ProgramContext):
        pass


    # Enter a parse tree produced by PrologParser#clause.
    def enterClause(self, ctx:PrologParser.ClauseContext):
        pass

    # Exit a parse tree produced by PrologParser#clause.
    def exitClause(self, ctx:PrologParser.ClauseContext):
        pass


    # Enter a parse tree produced by PrologParser#fact.
    def enterFact(self, ctx:PrologParser.FactContext):
        pass

    # Exit a parse tree produced by PrologParser#fact.
    def exitFact(self, ctx:PrologParser.FactContext):
        pass


    # Enter a parse tree produced by PrologParser#rule.
    def enterRule(self, ctx:PrologParser.RuleContext):
        pass

    # Exit a parse tree produced by PrologParser#rule.
    def exitRule(self, ctx:PrologParser.RuleContext):
        pass


    # Enter a parse tree produced by PrologParser#query.
    def enterQuery(self, ctx:PrologParser.QueryContext):
        pass

    # Exit a parse tree produced by PrologParser#query.
    def exitQuery(self, ctx:PrologParser.QueryContext):
        pass


    # Enter a parse tree produced by PrologParser#term_list.
    def enterTerm_list(self, ctx:PrologParser.Term_listContext):
        pass

    # Exit a parse tree produced by PrologParser#term_list.
    def exitTerm_list(self, ctx:PrologParser.Term_listContext):
        pass


    # Enter a parse tree produced by PrologParser#term.
    def enterTerm(self, ctx:PrologParser.TermContext):
        pass

    # Exit a parse tree produced by PrologParser#term.
    def exitTerm(self, ctx:PrologParser.TermContext):
        pass


    # Enter a parse tree produced by PrologParser#structure.
    def enterStructure(self, ctx:PrologParser.StructureContext):
        pass

    # Exit a parse tree produced by PrologParser#structure.
    def exitStructure(self, ctx:PrologParser.StructureContext):
        pass


    # Enter a parse tree produced by PrologParser#list.
    def enterList(self, ctx:PrologParser.ListContext):
        pass

    # Exit a parse tree produced by PrologParser#list.
    def exitList(self, ctx:PrologParser.ListContext):
        pass


    # Enter a parse tree produced by PrologParser#atom.
    def enterAtom(self, ctx:PrologParser.AtomContext):
        pass

    # Exit a parse tree produced by PrologParser#atom.
    def exitAtom(self, ctx:PrologParser.AtomContext):
        pass


    # Enter a parse tree produced by PrologParser#variable.
    def enterVariable(self, ctx:PrologParser.VariableContext):
        pass

    # Exit a parse tree produced by PrologParser#variable.
    def exitVariable(self, ctx:PrologParser.VariableContext):
        pass



del PrologParser