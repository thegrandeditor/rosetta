# Generated from rosetta/babel/basic/grammar/Basic.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .BasicParser import BasicParser
else:
    from BasicParser import BasicParser

# This class defines a complete generic visitor for a parse tree produced by BasicParser.

class BasicVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BasicParser#program.
    def visitProgram(self, ctx:BasicParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#line.
    def visitLine(self, ctx:BasicParser.LineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#statement.
    def visitStatement(self, ctx:BasicParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#let_stmt.
    def visitLet_stmt(self, ctx:BasicParser.Let_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#print_stmt.
    def visitPrint_stmt(self, ctx:BasicParser.Print_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#input_stmt.
    def visitInput_stmt(self, ctx:BasicParser.Input_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#goto_stmt.
    def visitGoto_stmt(self, ctx:BasicParser.Goto_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#gosub_stmt.
    def visitGosub_stmt(self, ctx:BasicParser.Gosub_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#return_stmt.
    def visitReturn_stmt(self, ctx:BasicParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#if_stmt.
    def visitIf_stmt(self, ctx:BasicParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#for_stmt.
    def visitFor_stmt(self, ctx:BasicParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#next_stmt.
    def visitNext_stmt(self, ctx:BasicParser.Next_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#while_stmt.
    def visitWhile_stmt(self, ctx:BasicParser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#wend_stmt.
    def visitWend_stmt(self, ctx:BasicParser.Wend_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#end_stmt.
    def visitEnd_stmt(self, ctx:BasicParser.End_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#remark_stmt.
    def visitRemark_stmt(self, ctx:BasicParser.Remark_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#identifier.
    def visitIdentifier(self, ctx:BasicParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#expression.
    def visitExpression(self, ctx:BasicParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#primary.
    def visitPrimary(self, ctx:BasicParser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#literal.
    def visitLiteral(self, ctx:BasicParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#integer_literal.
    def visitInteger_literal(self, ctx:BasicParser.Integer_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#real_literal.
    def visitReal_literal(self, ctx:BasicParser.Real_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#string_literal.
    def visitString_literal(self, ctx:BasicParser.String_literalContext):
        return self.visitChildren(ctx)



del BasicParser