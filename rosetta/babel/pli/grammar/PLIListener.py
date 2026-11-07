# Generated from rosetta/babel/pli/grammar/PLI.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PLIParser import PLIParser
else:
    from PLIParser import PLIParser

# This class defines a complete listener for a parse tree produced by PLIParser.
class PLIListener(ParseTreeListener):

    # Enter a parse tree produced by PLIParser#program.
    def enterProgram(self, ctx:PLIParser.ProgramContext):
        pass

    # Exit a parse tree produced by PLIParser#program.
    def exitProgram(self, ctx:PLIParser.ProgramContext):
        pass


    # Enter a parse tree produced by PLIParser#statement.
    def enterStatement(self, ctx:PLIParser.StatementContext):
        pass

    # Exit a parse tree produced by PLIParser#statement.
    def exitStatement(self, ctx:PLIParser.StatementContext):
        pass


    # Enter a parse tree produced by PLIParser#label.
    def enterLabel(self, ctx:PLIParser.LabelContext):
        pass

    # Exit a parse tree produced by PLIParser#label.
    def exitLabel(self, ctx:PLIParser.LabelContext):
        pass


    # Enter a parse tree produced by PLIParser#content_no_semi.
    def enterContent_no_semi(self, ctx:PLIParser.Content_no_semiContext):
        pass

    # Exit a parse tree produced by PLIParser#content_no_semi.
    def exitContent_no_semi(self, ctx:PLIParser.Content_no_semiContext):
        pass


    # Enter a parse tree produced by PLIParser#content_semi.
    def enterContent_semi(self, ctx:PLIParser.Content_semiContext):
        pass

    # Exit a parse tree produced by PLIParser#content_semi.
    def exitContent_semi(self, ctx:PLIParser.Content_semiContext):
        pass


    # Enter a parse tree produced by PLIParser#procedure_def.
    def enterProcedure_def(self, ctx:PLIParser.Procedure_defContext):
        pass

    # Exit a parse tree produced by PLIParser#procedure_def.
    def exitProcedure_def(self, ctx:PLIParser.Procedure_defContext):
        pass


    # Enter a parse tree produced by PLIParser#params.
    def enterParams(self, ctx:PLIParser.ParamsContext):
        pass

    # Exit a parse tree produced by PLIParser#params.
    def exitParams(self, ctx:PLIParser.ParamsContext):
        pass


    # Enter a parse tree produced by PLIParser#declare_stmt.
    def enterDeclare_stmt(self, ctx:PLIParser.Declare_stmtContext):
        pass

    # Exit a parse tree produced by PLIParser#declare_stmt.
    def exitDeclare_stmt(self, ctx:PLIParser.Declare_stmtContext):
        pass


    # Enter a parse tree produced by PLIParser#declaration.
    def enterDeclaration(self, ctx:PLIParser.DeclarationContext):
        pass

    # Exit a parse tree produced by PLIParser#declaration.
    def exitDeclaration(self, ctx:PLIParser.DeclarationContext):
        pass


    # Enter a parse tree produced by PLIParser#attribute.
    def enterAttribute(self, ctx:PLIParser.AttributeContext):
        pass

    # Exit a parse tree produced by PLIParser#attribute.
    def exitAttribute(self, ctx:PLIParser.AttributeContext):
        pass


    # Enter a parse tree produced by PLIParser#type_.
    def enterType_(self, ctx:PLIParser.Type_Context):
        pass

    # Exit a parse tree produced by PLIParser#type_.
    def exitType_(self, ctx:PLIParser.Type_Context):
        pass


    # Enter a parse tree produced by PLIParser#on_stmt.
    def enterOn_stmt(self, ctx:PLIParser.On_stmtContext):
        pass

    # Exit a parse tree produced by PLIParser#on_stmt.
    def exitOn_stmt(self, ctx:PLIParser.On_stmtContext):
        pass


    # Enter a parse tree produced by PLIParser#allocate_stmt.
    def enterAllocate_stmt(self, ctx:PLIParser.Allocate_stmtContext):
        pass

    # Exit a parse tree produced by PLIParser#allocate_stmt.
    def exitAllocate_stmt(self, ctx:PLIParser.Allocate_stmtContext):
        pass


    # Enter a parse tree produced by PLIParser#free_stmt.
    def enterFree_stmt(self, ctx:PLIParser.Free_stmtContext):
        pass

    # Exit a parse tree produced by PLIParser#free_stmt.
    def exitFree_stmt(self, ctx:PLIParser.Free_stmtContext):
        pass


    # Enter a parse tree produced by PLIParser#do_block.
    def enterDo_block(self, ctx:PLIParser.Do_blockContext):
        pass

    # Exit a parse tree produced by PLIParser#do_block.
    def exitDo_block(self, ctx:PLIParser.Do_blockContext):
        pass


    # Enter a parse tree produced by PLIParser#do_spec.
    def enterDo_spec(self, ctx:PLIParser.Do_specContext):
        pass

    # Exit a parse tree produced by PLIParser#do_spec.
    def exitDo_spec(self, ctx:PLIParser.Do_specContext):
        pass


    # Enter a parse tree produced by PLIParser#if_stmt.
    def enterIf_stmt(self, ctx:PLIParser.If_stmtContext):
        pass

    # Exit a parse tree produced by PLIParser#if_stmt.
    def exitIf_stmt(self, ctx:PLIParser.If_stmtContext):
        pass


    # Enter a parse tree produced by PLIParser#call_stmt.
    def enterCall_stmt(self, ctx:PLIParser.Call_stmtContext):
        pass

    # Exit a parse tree produced by PLIParser#call_stmt.
    def exitCall_stmt(self, ctx:PLIParser.Call_stmtContext):
        pass


    # Enter a parse tree produced by PLIParser#args.
    def enterArgs(self, ctx:PLIParser.ArgsContext):
        pass

    # Exit a parse tree produced by PLIParser#args.
    def exitArgs(self, ctx:PLIParser.ArgsContext):
        pass


    # Enter a parse tree produced by PLIParser#assignment.
    def enterAssignment(self, ctx:PLIParser.AssignmentContext):
        pass

    # Exit a parse tree produced by PLIParser#assignment.
    def exitAssignment(self, ctx:PLIParser.AssignmentContext):
        pass


    # Enter a parse tree produced by PLIParser#return_stmt.
    def enterReturn_stmt(self, ctx:PLIParser.Return_stmtContext):
        pass

    # Exit a parse tree produced by PLIParser#return_stmt.
    def exitReturn_stmt(self, ctx:PLIParser.Return_stmtContext):
        pass


    # Enter a parse tree produced by PLIParser#action.
    def enterAction(self, ctx:PLIParser.ActionContext):
        pass

    # Exit a parse tree produced by PLIParser#action.
    def exitAction(self, ctx:PLIParser.ActionContext):
        pass


    # Enter a parse tree produced by PLIParser#expression.
    def enterExpression(self, ctx:PLIParser.ExpressionContext):
        pass

    # Exit a parse tree produced by PLIParser#expression.
    def exitExpression(self, ctx:PLIParser.ExpressionContext):
        pass


    # Enter a parse tree produced by PLIParser#primary.
    def enterPrimary(self, ctx:PLIParser.PrimaryContext):
        pass

    # Exit a parse tree produced by PLIParser#primary.
    def exitPrimary(self, ctx:PLIParser.PrimaryContext):
        pass


    # Enter a parse tree produced by PLIParser#operator.
    def enterOperator(self, ctx:PLIParser.OperatorContext):
        pass

    # Exit a parse tree produced by PLIParser#operator.
    def exitOperator(self, ctx:PLIParser.OperatorContext):
        pass



del PLIParser