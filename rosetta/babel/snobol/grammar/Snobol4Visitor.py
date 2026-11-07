# Generated from rosetta/babel/snobol/grammar/Snobol4.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .Snobol4Parser import Snobol4Parser
else:
    from Snobol4Parser import Snobol4Parser

# This class defines a complete generic visitor for a parse tree produced by Snobol4Parser.

class Snobol4Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by Snobol4Parser#program.
    def visitProgram(self, ctx:Snobol4Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Snobol4Parser#line.
    def visitLine(self, ctx:Snobol4Parser.LineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Snobol4Parser#statement.
    def visitStatement(self, ctx:Snobol4Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Snobol4Parser#content.
    def visitContent(self, ctx:Snobol4Parser.ContentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Snobol4Parser#label.
    def visitLabel(self, ctx:Snobol4Parser.LabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Snobol4Parser#assignment.
    def visitAssignment(self, ctx:Snobol4Parser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Snobol4Parser#patternMatch.
    def visitPatternMatch(self, ctx:Snobol4Parser.PatternMatchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Snobol4Parser#subject.
    def visitSubject(self, ctx:Snobol4Parser.SubjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Snobol4Parser#pattern.
    def visitPattern(self, ctx:Snobol4Parser.PatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Snobol4Parser#replacement.
    def visitReplacement(self, ctx:Snobol4Parser.ReplacementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Snobol4Parser#transfer.
    def visitTransfer(self, ctx:Snobol4Parser.TransferContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Snobol4Parser#transfer_dest.
    def visitTransfer_dest(self, ctx:Snobol4Parser.Transfer_destContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Snobol4Parser#direct_goto.
    def visitDirect_goto(self, ctx:Snobol4Parser.Direct_gotoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Snobol4Parser#conditional_gotos.
    def visitConditional_gotos(self, ctx:Snobol4Parser.Conditional_gotosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Snobol4Parser#success_goto.
    def visitSuccess_goto(self, ctx:Snobol4Parser.Success_gotoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Snobol4Parser#failure_goto.
    def visitFailure_goto(self, ctx:Snobol4Parser.Failure_gotoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Snobol4Parser#expression.
    def visitExpression(self, ctx:Snobol4Parser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Snobol4Parser#alternation_expr.
    def visitAlternation_expr(self, ctx:Snobol4Parser.Alternation_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Snobol4Parser#concatenation_expr.
    def visitConcatenation_expr(self, ctx:Snobol4Parser.Concatenation_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Snobol4Parser#capture_expr.
    def visitCapture_expr(self, ctx:Snobol4Parser.Capture_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Snobol4Parser#additive_expr.
    def visitAdditive_expr(self, ctx:Snobol4Parser.Additive_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Snobol4Parser#multiplicative_expr.
    def visitMultiplicative_expr(self, ctx:Snobol4Parser.Multiplicative_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Snobol4Parser#primary.
    def visitPrimary(self, ctx:Snobol4Parser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Snobol4Parser#array_access.
    def visitArray_access(self, ctx:Snobol4Parser.Array_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Snobol4Parser#unary_expr.
    def visitUnary_expr(self, ctx:Snobol4Parser.Unary_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Snobol4Parser#function_call.
    def visitFunction_call(self, ctx:Snobol4Parser.Function_callContext):
        return self.visitChildren(ctx)



del Snobol4Parser