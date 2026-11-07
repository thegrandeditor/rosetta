# Generated from rosetta/babel/basic/grammar/Basic.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .BasicParser import BasicParser
else:
    from BasicParser import BasicParser

# This class defines a complete listener for a parse tree produced by BasicParser.
class BasicListener(ParseTreeListener):

    # Enter a parse tree produced by BasicParser#program.
    def enterProgram(self, ctx:BasicParser.ProgramContext):
        pass

    # Exit a parse tree produced by BasicParser#program.
    def exitProgram(self, ctx:BasicParser.ProgramContext):
        pass


    # Enter a parse tree produced by BasicParser#line.
    def enterLine(self, ctx:BasicParser.LineContext):
        pass

    # Exit a parse tree produced by BasicParser#line.
    def exitLine(self, ctx:BasicParser.LineContext):
        pass


    # Enter a parse tree produced by BasicParser#statement.
    def enterStatement(self, ctx:BasicParser.StatementContext):
        pass

    # Exit a parse tree produced by BasicParser#statement.
    def exitStatement(self, ctx:BasicParser.StatementContext):
        pass


    # Enter a parse tree produced by BasicParser#let_stmt.
    def enterLet_stmt(self, ctx:BasicParser.Let_stmtContext):
        pass

    # Exit a parse tree produced by BasicParser#let_stmt.
    def exitLet_stmt(self, ctx:BasicParser.Let_stmtContext):
        pass


    # Enter a parse tree produced by BasicParser#print_stmt.
    def enterPrint_stmt(self, ctx:BasicParser.Print_stmtContext):
        pass

    # Exit a parse tree produced by BasicParser#print_stmt.
    def exitPrint_stmt(self, ctx:BasicParser.Print_stmtContext):
        pass


    # Enter a parse tree produced by BasicParser#input_stmt.
    def enterInput_stmt(self, ctx:BasicParser.Input_stmtContext):
        pass

    # Exit a parse tree produced by BasicParser#input_stmt.
    def exitInput_stmt(self, ctx:BasicParser.Input_stmtContext):
        pass


    # Enter a parse tree produced by BasicParser#goto_stmt.
    def enterGoto_stmt(self, ctx:BasicParser.Goto_stmtContext):
        pass

    # Exit a parse tree produced by BasicParser#goto_stmt.
    def exitGoto_stmt(self, ctx:BasicParser.Goto_stmtContext):
        pass


    # Enter a parse tree produced by BasicParser#gosub_stmt.
    def enterGosub_stmt(self, ctx:BasicParser.Gosub_stmtContext):
        pass

    # Exit a parse tree produced by BasicParser#gosub_stmt.
    def exitGosub_stmt(self, ctx:BasicParser.Gosub_stmtContext):
        pass


    # Enter a parse tree produced by BasicParser#return_stmt.
    def enterReturn_stmt(self, ctx:BasicParser.Return_stmtContext):
        pass

    # Exit a parse tree produced by BasicParser#return_stmt.
    def exitReturn_stmt(self, ctx:BasicParser.Return_stmtContext):
        pass


    # Enter a parse tree produced by BasicParser#if_stmt.
    def enterIf_stmt(self, ctx:BasicParser.If_stmtContext):
        pass

    # Exit a parse tree produced by BasicParser#if_stmt.
    def exitIf_stmt(self, ctx:BasicParser.If_stmtContext):
        pass


    # Enter a parse tree produced by BasicParser#for_stmt.
    def enterFor_stmt(self, ctx:BasicParser.For_stmtContext):
        pass

    # Exit a parse tree produced by BasicParser#for_stmt.
    def exitFor_stmt(self, ctx:BasicParser.For_stmtContext):
        pass


    # Enter a parse tree produced by BasicParser#next_stmt.
    def enterNext_stmt(self, ctx:BasicParser.Next_stmtContext):
        pass

    # Exit a parse tree produced by BasicParser#next_stmt.
    def exitNext_stmt(self, ctx:BasicParser.Next_stmtContext):
        pass


    # Enter a parse tree produced by BasicParser#while_stmt.
    def enterWhile_stmt(self, ctx:BasicParser.While_stmtContext):
        pass

    # Exit a parse tree produced by BasicParser#while_stmt.
    def exitWhile_stmt(self, ctx:BasicParser.While_stmtContext):
        pass


    # Enter a parse tree produced by BasicParser#wend_stmt.
    def enterWend_stmt(self, ctx:BasicParser.Wend_stmtContext):
        pass

    # Exit a parse tree produced by BasicParser#wend_stmt.
    def exitWend_stmt(self, ctx:BasicParser.Wend_stmtContext):
        pass


    # Enter a parse tree produced by BasicParser#end_stmt.
    def enterEnd_stmt(self, ctx:BasicParser.End_stmtContext):
        pass

    # Exit a parse tree produced by BasicParser#end_stmt.
    def exitEnd_stmt(self, ctx:BasicParser.End_stmtContext):
        pass


    # Enter a parse tree produced by BasicParser#remark_stmt.
    def enterRemark_stmt(self, ctx:BasicParser.Remark_stmtContext):
        pass

    # Exit a parse tree produced by BasicParser#remark_stmt.
    def exitRemark_stmt(self, ctx:BasicParser.Remark_stmtContext):
        pass


    # Enter a parse tree produced by BasicParser#identifier.
    def enterIdentifier(self, ctx:BasicParser.IdentifierContext):
        pass

    # Exit a parse tree produced by BasicParser#identifier.
    def exitIdentifier(self, ctx:BasicParser.IdentifierContext):
        pass


    # Enter a parse tree produced by BasicParser#expression.
    def enterExpression(self, ctx:BasicParser.ExpressionContext):
        pass

    # Exit a parse tree produced by BasicParser#expression.
    def exitExpression(self, ctx:BasicParser.ExpressionContext):
        pass


    # Enter a parse tree produced by BasicParser#primary.
    def enterPrimary(self, ctx:BasicParser.PrimaryContext):
        pass

    # Exit a parse tree produced by BasicParser#primary.
    def exitPrimary(self, ctx:BasicParser.PrimaryContext):
        pass


    # Enter a parse tree produced by BasicParser#literal.
    def enterLiteral(self, ctx:BasicParser.LiteralContext):
        pass

    # Exit a parse tree produced by BasicParser#literal.
    def exitLiteral(self, ctx:BasicParser.LiteralContext):
        pass


    # Enter a parse tree produced by BasicParser#integer_literal.
    def enterInteger_literal(self, ctx:BasicParser.Integer_literalContext):
        pass

    # Exit a parse tree produced by BasicParser#integer_literal.
    def exitInteger_literal(self, ctx:BasicParser.Integer_literalContext):
        pass


    # Enter a parse tree produced by BasicParser#real_literal.
    def enterReal_literal(self, ctx:BasicParser.Real_literalContext):
        pass

    # Exit a parse tree produced by BasicParser#real_literal.
    def exitReal_literal(self, ctx:BasicParser.Real_literalContext):
        pass


    # Enter a parse tree produced by BasicParser#string_literal.
    def enterString_literal(self, ctx:BasicParser.String_literalContext):
        pass

    # Exit a parse tree produced by BasicParser#string_literal.
    def exitString_literal(self, ctx:BasicParser.String_literalContext):
        pass



del BasicParser