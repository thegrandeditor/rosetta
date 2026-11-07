# Generated from rosetta/babel/rpg/grammar/RPG.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .RPGParser import RPGParser
else:
    from RPGParser import RPGParser

# This class defines a complete generic visitor for a parse tree produced by RPGParser.

class RPGVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by RPGParser#program.
    def visitProgram(self, ctx:RPGParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RPGParser#line.
    def visitLine(self, ctx:RPGParser.LineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RPGParser#h_spec.
    def visitH_spec(self, ctx:RPGParser.H_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RPGParser#f_spec.
    def visitF_spec(self, ctx:RPGParser.F_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RPGParser#d_spec.
    def visitD_spec(self, ctx:RPGParser.D_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RPGParser#o_spec.
    def visitO_spec(self, ctx:RPGParser.O_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RPGParser#c_spec.
    def visitC_spec(self, ctx:RPGParser.C_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RPGParser#factor.
    def visitFactor(self, ctx:RPGParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RPGParser#indicator.
    def visitIndicator(self, ctx:RPGParser.IndicatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RPGParser#opcode.
    def visitOpcode(self, ctx:RPGParser.OpcodeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RPGParser#comment.
    def visitComment(self, ctx:RPGParser.CommentContext):
        return self.visitChildren(ctx)



del RPGParser