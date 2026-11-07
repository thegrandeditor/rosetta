# Generated from rosetta/babel/snobol/grammar/Snobol4.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .Snobol4Parser import Snobol4Parser
else:
    from Snobol4Parser import Snobol4Parser

# This class defines a complete listener for a parse tree produced by Snobol4Parser.
class Snobol4Listener(ParseTreeListener):

    # Enter a parse tree produced by Snobol4Parser#program.
    def enterProgram(self, ctx:Snobol4Parser.ProgramContext):
        pass

    # Exit a parse tree produced by Snobol4Parser#program.
    def exitProgram(self, ctx:Snobol4Parser.ProgramContext):
        pass


    # Enter a parse tree produced by Snobol4Parser#line.
    def enterLine(self, ctx:Snobol4Parser.LineContext):
        pass

    # Exit a parse tree produced by Snobol4Parser#line.
    def exitLine(self, ctx:Snobol4Parser.LineContext):
        pass


    # Enter a parse tree produced by Snobol4Parser#statement.
    def enterStatement(self, ctx:Snobol4Parser.StatementContext):
        pass

    # Exit a parse tree produced by Snobol4Parser#statement.
    def exitStatement(self, ctx:Snobol4Parser.StatementContext):
        pass


    # Enter a parse tree produced by Snobol4Parser#content.
    def enterContent(self, ctx:Snobol4Parser.ContentContext):
        pass

    # Exit a parse tree produced by Snobol4Parser#content.
    def exitContent(self, ctx:Snobol4Parser.ContentContext):
        pass


    # Enter a parse tree produced by Snobol4Parser#label.
    def enterLabel(self, ctx:Snobol4Parser.LabelContext):
        pass

    # Exit a parse tree produced by Snobol4Parser#label.
    def exitLabel(self, ctx:Snobol4Parser.LabelContext):
        pass


    # Enter a parse tree produced by Snobol4Parser#assignment.
    def enterAssignment(self, ctx:Snobol4Parser.AssignmentContext):
        pass

    # Exit a parse tree produced by Snobol4Parser#assignment.
    def exitAssignment(self, ctx:Snobol4Parser.AssignmentContext):
        pass


    # Enter a parse tree produced by Snobol4Parser#patternMatch.
    def enterPatternMatch(self, ctx:Snobol4Parser.PatternMatchContext):
        pass

    # Exit a parse tree produced by Snobol4Parser#patternMatch.
    def exitPatternMatch(self, ctx:Snobol4Parser.PatternMatchContext):
        pass


    # Enter a parse tree produced by Snobol4Parser#subject.
    def enterSubject(self, ctx:Snobol4Parser.SubjectContext):
        pass

    # Exit a parse tree produced by Snobol4Parser#subject.
    def exitSubject(self, ctx:Snobol4Parser.SubjectContext):
        pass


    # Enter a parse tree produced by Snobol4Parser#pattern.
    def enterPattern(self, ctx:Snobol4Parser.PatternContext):
        pass

    # Exit a parse tree produced by Snobol4Parser#pattern.
    def exitPattern(self, ctx:Snobol4Parser.PatternContext):
        pass


    # Enter a parse tree produced by Snobol4Parser#replacement.
    def enterReplacement(self, ctx:Snobol4Parser.ReplacementContext):
        pass

    # Exit a parse tree produced by Snobol4Parser#replacement.
    def exitReplacement(self, ctx:Snobol4Parser.ReplacementContext):
        pass


    # Enter a parse tree produced by Snobol4Parser#transfer.
    def enterTransfer(self, ctx:Snobol4Parser.TransferContext):
        pass

    # Exit a parse tree produced by Snobol4Parser#transfer.
    def exitTransfer(self, ctx:Snobol4Parser.TransferContext):
        pass


    # Enter a parse tree produced by Snobol4Parser#transfer_dest.
    def enterTransfer_dest(self, ctx:Snobol4Parser.Transfer_destContext):
        pass

    # Exit a parse tree produced by Snobol4Parser#transfer_dest.
    def exitTransfer_dest(self, ctx:Snobol4Parser.Transfer_destContext):
        pass


    # Enter a parse tree produced by Snobol4Parser#direct_goto.
    def enterDirect_goto(self, ctx:Snobol4Parser.Direct_gotoContext):
        pass

    # Exit a parse tree produced by Snobol4Parser#direct_goto.
    def exitDirect_goto(self, ctx:Snobol4Parser.Direct_gotoContext):
        pass


    # Enter a parse tree produced by Snobol4Parser#conditional_gotos.
    def enterConditional_gotos(self, ctx:Snobol4Parser.Conditional_gotosContext):
        pass

    # Exit a parse tree produced by Snobol4Parser#conditional_gotos.
    def exitConditional_gotos(self, ctx:Snobol4Parser.Conditional_gotosContext):
        pass


    # Enter a parse tree produced by Snobol4Parser#success_goto.
    def enterSuccess_goto(self, ctx:Snobol4Parser.Success_gotoContext):
        pass

    # Exit a parse tree produced by Snobol4Parser#success_goto.
    def exitSuccess_goto(self, ctx:Snobol4Parser.Success_gotoContext):
        pass


    # Enter a parse tree produced by Snobol4Parser#failure_goto.
    def enterFailure_goto(self, ctx:Snobol4Parser.Failure_gotoContext):
        pass

    # Exit a parse tree produced by Snobol4Parser#failure_goto.
    def exitFailure_goto(self, ctx:Snobol4Parser.Failure_gotoContext):
        pass


    # Enter a parse tree produced by Snobol4Parser#expression.
    def enterExpression(self, ctx:Snobol4Parser.ExpressionContext):
        pass

    # Exit a parse tree produced by Snobol4Parser#expression.
    def exitExpression(self, ctx:Snobol4Parser.ExpressionContext):
        pass


    # Enter a parse tree produced by Snobol4Parser#binary_expr.
    def enterBinary_expr(self, ctx:Snobol4Parser.Binary_exprContext):
        pass

    # Exit a parse tree produced by Snobol4Parser#binary_expr.
    def exitBinary_expr(self, ctx:Snobol4Parser.Binary_exprContext):
        pass


    # Enter a parse tree produced by Snobol4Parser#primary.
    def enterPrimary(self, ctx:Snobol4Parser.PrimaryContext):
        pass

    # Exit a parse tree produced by Snobol4Parser#primary.
    def exitPrimary(self, ctx:Snobol4Parser.PrimaryContext):
        pass


    # Enter a parse tree produced by Snobol4Parser#unary_expr.
    def enterUnary_expr(self, ctx:Snobol4Parser.Unary_exprContext):
        pass

    # Exit a parse tree produced by Snobol4Parser#unary_expr.
    def exitUnary_expr(self, ctx:Snobol4Parser.Unary_exprContext):
        pass


    # Enter a parse tree produced by Snobol4Parser#function_call.
    def enterFunction_call(self, ctx:Snobol4Parser.Function_callContext):
        pass

    # Exit a parse tree produced by Snobol4Parser#function_call.
    def exitFunction_call(self, ctx:Snobol4Parser.Function_callContext):
        pass



del Snobol4Parser