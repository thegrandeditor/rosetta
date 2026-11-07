# Generated from rosetta/babel/pli/grammar/PLI.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PLIParser import PLIParser
else:
    from PLIParser import PLIParser

# This class defines a complete generic visitor for a parse tree produced by PLIParser.

class PLIVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PLIParser#program.
    def visitProgram(self, ctx:PLIParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#directive.
    def visitDirective(self, ctx:PLIParser.DirectiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#statement.
    def visitStatement(self, ctx:PLIParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#label.
    def visitLabel(self, ctx:PLIParser.LabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#content_no_semi.
    def visitContent_no_semi(self, ctx:PLIParser.Content_no_semiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#content_semi.
    def visitContent_semi(self, ctx:PLIParser.Content_semiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#procedure_def.
    def visitProcedure_def(self, ctx:PLIParser.Procedure_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#entry_stmt.
    def visitEntry_stmt(self, ctx:PLIParser.Entry_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#params.
    def visitParams(self, ctx:PLIParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#declare_stmt.
    def visitDeclare_stmt(self, ctx:PLIParser.Declare_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#declaration.
    def visitDeclaration(self, ctx:PLIParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#attribute.
    def visitAttribute(self, ctx:PLIParser.AttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#type_.
    def visitType_(self, ctx:PLIParser.Type_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#on_stmt.
    def visitOn_stmt(self, ctx:PLIParser.On_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#allocate_stmt.
    def visitAllocate_stmt(self, ctx:PLIParser.Allocate_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#free_stmt.
    def visitFree_stmt(self, ctx:PLIParser.Free_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#do_block.
    def visitDo_block(self, ctx:PLIParser.Do_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#do_spec.
    def visitDo_spec(self, ctx:PLIParser.Do_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#if_stmt.
    def visitIf_stmt(self, ctx:PLIParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#call_stmt.
    def visitCall_stmt(self, ctx:PLIParser.Call_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#args.
    def visitArgs(self, ctx:PLIParser.ArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#assignment.
    def visitAssignment(self, ctx:PLIParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#return_stmt.
    def visitReturn_stmt(self, ctx:PLIParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#action.
    def visitAction(self, ctx:PLIParser.ActionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#expression.
    def visitExpression(self, ctx:PLIParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#primary.
    def visitPrimary(self, ctx:PLIParser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#operator.
    def visitOperator(self, ctx:PLIParser.OperatorContext):
        return self.visitChildren(ctx)



del PLIParser