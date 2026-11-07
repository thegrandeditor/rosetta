# Generated from rosetta/babel/rpg/grammar/RPG.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .RPGParser import RPGParser
else:
    from RPGParser import RPGParser

# This class defines a complete listener for a parse tree produced by RPGParser.
class RPGListener(ParseTreeListener):

    # Enter a parse tree produced by RPGParser#program.
    def enterProgram(self, ctx:RPGParser.ProgramContext):
        pass

    # Exit a parse tree produced by RPGParser#program.
    def exitProgram(self, ctx:RPGParser.ProgramContext):
        pass


    # Enter a parse tree produced by RPGParser#line.
    def enterLine(self, ctx:RPGParser.LineContext):
        pass

    # Exit a parse tree produced by RPGParser#line.
    def exitLine(self, ctx:RPGParser.LineContext):
        pass


    # Enter a parse tree produced by RPGParser#h_spec.
    def enterH_spec(self, ctx:RPGParser.H_specContext):
        pass

    # Exit a parse tree produced by RPGParser#h_spec.
    def exitH_spec(self, ctx:RPGParser.H_specContext):
        pass


    # Enter a parse tree produced by RPGParser#f_spec.
    def enterF_spec(self, ctx:RPGParser.F_specContext):
        pass

    # Exit a parse tree produced by RPGParser#f_spec.
    def exitF_spec(self, ctx:RPGParser.F_specContext):
        pass


    # Enter a parse tree produced by RPGParser#d_spec.
    def enterD_spec(self, ctx:RPGParser.D_specContext):
        pass

    # Exit a parse tree produced by RPGParser#d_spec.
    def exitD_spec(self, ctx:RPGParser.D_specContext):
        pass


    # Enter a parse tree produced by RPGParser#o_spec.
    def enterO_spec(self, ctx:RPGParser.O_specContext):
        pass

    # Exit a parse tree produced by RPGParser#o_spec.
    def exitO_spec(self, ctx:RPGParser.O_specContext):
        pass


    # Enter a parse tree produced by RPGParser#c_spec.
    def enterC_spec(self, ctx:RPGParser.C_specContext):
        pass

    # Exit a parse tree produced by RPGParser#c_spec.
    def exitC_spec(self, ctx:RPGParser.C_specContext):
        pass


    # Enter a parse tree produced by RPGParser#factor.
    def enterFactor(self, ctx:RPGParser.FactorContext):
        pass

    # Exit a parse tree produced by RPGParser#factor.
    def exitFactor(self, ctx:RPGParser.FactorContext):
        pass


    # Enter a parse tree produced by RPGParser#indicator.
    def enterIndicator(self, ctx:RPGParser.IndicatorContext):
        pass

    # Exit a parse tree produced by RPGParser#indicator.
    def exitIndicator(self, ctx:RPGParser.IndicatorContext):
        pass


    # Enter a parse tree produced by RPGParser#opcode.
    def enterOpcode(self, ctx:RPGParser.OpcodeContext):
        pass

    # Exit a parse tree produced by RPGParser#opcode.
    def exitOpcode(self, ctx:RPGParser.OpcodeContext):
        pass


    # Enter a parse tree produced by RPGParser#comment.
    def enterComment(self, ctx:RPGParser.CommentContext):
        pass

    # Exit a parse tree produced by RPGParser#comment.
    def exitComment(self, ctx:RPGParser.CommentContext):
        pass



del RPGParser