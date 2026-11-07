# Generated from rosetta/babel/eiffel/grammar/Eiffel.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .EiffelParser import EiffelParser
else:
    from EiffelParser import EiffelParser

# This class defines a complete listener for a parse tree produced by EiffelParser.
class EiffelListener(ParseTreeListener):

    # Enter a parse tree produced by EiffelParser#program.
    def enterProgram(self, ctx:EiffelParser.ProgramContext):
        pass

    # Exit a parse tree produced by EiffelParser#program.
    def exitProgram(self, ctx:EiffelParser.ProgramContext):
        pass


    # Enter a parse tree produced by EiffelParser#class_declaration.
    def enterClass_declaration(self, ctx:EiffelParser.Class_declarationContext):
        pass

    # Exit a parse tree produced by EiffelParser#class_declaration.
    def exitClass_declaration(self, ctx:EiffelParser.Class_declarationContext):
        pass


    # Enter a parse tree produced by EiffelParser#inheritance.
    def enterInheritance(self, ctx:EiffelParser.InheritanceContext):
        pass

    # Exit a parse tree produced by EiffelParser#inheritance.
    def exitInheritance(self, ctx:EiffelParser.InheritanceContext):
        pass


    # Enter a parse tree produced by EiffelParser#rename_clause.
    def enterRename_clause(self, ctx:EiffelParser.Rename_clauseContext):
        pass

    # Exit a parse tree produced by EiffelParser#rename_clause.
    def exitRename_clause(self, ctx:EiffelParser.Rename_clauseContext):
        pass


    # Enter a parse tree produced by EiffelParser#redefine_clause.
    def enterRedefine_clause(self, ctx:EiffelParser.Redefine_clauseContext):
        pass

    # Exit a parse tree produced by EiffelParser#redefine_clause.
    def exitRedefine_clause(self, ctx:EiffelParser.Redefine_clauseContext):
        pass


    # Enter a parse tree produced by EiffelParser#create_clause.
    def enterCreate_clause(self, ctx:EiffelParser.Create_clauseContext):
        pass

    # Exit a parse tree produced by EiffelParser#create_clause.
    def exitCreate_clause(self, ctx:EiffelParser.Create_clauseContext):
        pass


    # Enter a parse tree produced by EiffelParser#feature_block.
    def enterFeature_block(self, ctx:EiffelParser.Feature_blockContext):
        pass

    # Exit a parse tree produced by EiffelParser#feature_block.
    def exitFeature_block(self, ctx:EiffelParser.Feature_blockContext):
        pass


    # Enter a parse tree produced by EiffelParser#feature_declaration.
    def enterFeature_declaration(self, ctx:EiffelParser.Feature_declarationContext):
        pass

    # Exit a parse tree produced by EiffelParser#feature_declaration.
    def exitFeature_declaration(self, ctx:EiffelParser.Feature_declarationContext):
        pass


    # Enter a parse tree produced by EiffelParser#formal_params.
    def enterFormal_params(self, ctx:EiffelParser.Formal_paramsContext):
        pass

    # Exit a parse tree produced by EiffelParser#formal_params.
    def exitFormal_params(self, ctx:EiffelParser.Formal_paramsContext):
        pass


    # Enter a parse tree produced by EiffelParser#param_list.
    def enterParam_list(self, ctx:EiffelParser.Param_listContext):
        pass

    # Exit a parse tree produced by EiffelParser#param_list.
    def exitParam_list(self, ctx:EiffelParser.Param_listContext):
        pass


    # Enter a parse tree produced by EiffelParser#param_group.
    def enterParam_group(self, ctx:EiffelParser.Param_groupContext):
        pass

    # Exit a parse tree produced by EiffelParser#param_group.
    def exitParam_group(self, ctx:EiffelParser.Param_groupContext):
        pass


    # Enter a parse tree produced by EiffelParser#id_list.
    def enterId_list(self, ctx:EiffelParser.Id_listContext):
        pass

    # Exit a parse tree produced by EiffelParser#id_list.
    def exitId_list(self, ctx:EiffelParser.Id_listContext):
        pass


    # Enter a parse tree produced by EiffelParser#type_.
    def enterType_(self, ctx:EiffelParser.Type_Context):
        pass

    # Exit a parse tree produced by EiffelParser#type_.
    def exitType_(self, ctx:EiffelParser.Type_Context):
        pass


    # Enter a parse tree produced by EiffelParser#generic_type.
    def enterGeneric_type(self, ctx:EiffelParser.Generic_typeContext):
        pass

    # Exit a parse tree produced by EiffelParser#generic_type.
    def exitGeneric_type(self, ctx:EiffelParser.Generic_typeContext):
        pass


    # Enter a parse tree produced by EiffelParser#attribute_init.
    def enterAttribute_init(self, ctx:EiffelParser.Attribute_initContext):
        pass

    # Exit a parse tree produced by EiffelParser#attribute_init.
    def exitAttribute_init(self, ctx:EiffelParser.Attribute_initContext):
        pass


    # Enter a parse tree produced by EiffelParser#routine_body.
    def enterRoutine_body(self, ctx:EiffelParser.Routine_bodyContext):
        pass

    # Exit a parse tree produced by EiffelParser#routine_body.
    def exitRoutine_body(self, ctx:EiffelParser.Routine_bodyContext):
        pass


    # Enter a parse tree produced by EiffelParser#assertion_list.
    def enterAssertion_list(self, ctx:EiffelParser.Assertion_listContext):
        pass

    # Exit a parse tree produced by EiffelParser#assertion_list.
    def exitAssertion_list(self, ctx:EiffelParser.Assertion_listContext):
        pass


    # Enter a parse tree produced by EiffelParser#assertion.
    def enterAssertion(self, ctx:EiffelParser.AssertionContext):
        pass

    # Exit a parse tree produced by EiffelParser#assertion.
    def exitAssertion(self, ctx:EiffelParser.AssertionContext):
        pass


    # Enter a parse tree produced by EiffelParser#declaration_list.
    def enterDeclaration_list(self, ctx:EiffelParser.Declaration_listContext):
        pass

    # Exit a parse tree produced by EiffelParser#declaration_list.
    def exitDeclaration_list(self, ctx:EiffelParser.Declaration_listContext):
        pass


    # Enter a parse tree produced by EiffelParser#declaration.
    def enterDeclaration(self, ctx:EiffelParser.DeclarationContext):
        pass

    # Exit a parse tree produced by EiffelParser#declaration.
    def exitDeclaration(self, ctx:EiffelParser.DeclarationContext):
        pass


    # Enter a parse tree produced by EiffelParser#block.
    def enterBlock(self, ctx:EiffelParser.BlockContext):
        pass

    # Exit a parse tree produced by EiffelParser#block.
    def exitBlock(self, ctx:EiffelParser.BlockContext):
        pass


    # Enter a parse tree produced by EiffelParser#statement.
    def enterStatement(self, ctx:EiffelParser.StatementContext):
        pass

    # Exit a parse tree produced by EiffelParser#statement.
    def exitStatement(self, ctx:EiffelParser.StatementContext):
        pass


    # Enter a parse tree produced by EiffelParser#assignment.
    def enterAssignment(self, ctx:EiffelParser.AssignmentContext):
        pass

    # Exit a parse tree produced by EiffelParser#assignment.
    def exitAssignment(self, ctx:EiffelParser.AssignmentContext):
        pass


    # Enter a parse tree produced by EiffelParser#call_statement.
    def enterCall_statement(self, ctx:EiffelParser.Call_statementContext):
        pass

    # Exit a parse tree produced by EiffelParser#call_statement.
    def exitCall_statement(self, ctx:EiffelParser.Call_statementContext):
        pass


    # Enter a parse tree produced by EiffelParser#if_statement.
    def enterIf_statement(self, ctx:EiffelParser.If_statementContext):
        pass

    # Exit a parse tree produced by EiffelParser#if_statement.
    def exitIf_statement(self, ctx:EiffelParser.If_statementContext):
        pass


    # Enter a parse tree produced by EiffelParser#loop_statement.
    def enterLoop_statement(self, ctx:EiffelParser.Loop_statementContext):
        pass

    # Exit a parse tree produced by EiffelParser#loop_statement.
    def exitLoop_statement(self, ctx:EiffelParser.Loop_statementContext):
        pass


    # Enter a parse tree produced by EiffelParser#retry_statement.
    def enterRetry_statement(self, ctx:EiffelParser.Retry_statementContext):
        pass

    # Exit a parse tree produced by EiffelParser#retry_statement.
    def exitRetry_statement(self, ctx:EiffelParser.Retry_statementContext):
        pass


    # Enter a parse tree produced by EiffelParser#check_statement.
    def enterCheck_statement(self, ctx:EiffelParser.Check_statementContext):
        pass

    # Exit a parse tree produced by EiffelParser#check_statement.
    def exitCheck_statement(self, ctx:EiffelParser.Check_statementContext):
        pass


    # Enter a parse tree produced by EiffelParser#invariant_clause.
    def enterInvariant_clause(self, ctx:EiffelParser.Invariant_clauseContext):
        pass

    # Exit a parse tree produced by EiffelParser#invariant_clause.
    def exitInvariant_clause(self, ctx:EiffelParser.Invariant_clauseContext):
        pass


    # Enter a parse tree produced by EiffelParser#expression.
    def enterExpression(self, ctx:EiffelParser.ExpressionContext):
        pass

    # Exit a parse tree produced by EiffelParser#expression.
    def exitExpression(self, ctx:EiffelParser.ExpressionContext):
        pass


    # Enter a parse tree produced by EiffelParser#logical_expr.
    def enterLogical_expr(self, ctx:EiffelParser.Logical_exprContext):
        pass

    # Exit a parse tree produced by EiffelParser#logical_expr.
    def exitLogical_expr(self, ctx:EiffelParser.Logical_exprContext):
        pass


    # Enter a parse tree produced by EiffelParser#rel_expr.
    def enterRel_expr(self, ctx:EiffelParser.Rel_exprContext):
        pass

    # Exit a parse tree produced by EiffelParser#rel_expr.
    def exitRel_expr(self, ctx:EiffelParser.Rel_exprContext):
        pass


    # Enter a parse tree produced by EiffelParser#add_expr.
    def enterAdd_expr(self, ctx:EiffelParser.Add_exprContext):
        pass

    # Exit a parse tree produced by EiffelParser#add_expr.
    def exitAdd_expr(self, ctx:EiffelParser.Add_exprContext):
        pass


    # Enter a parse tree produced by EiffelParser#mul_expr.
    def enterMul_expr(self, ctx:EiffelParser.Mul_exprContext):
        pass

    # Exit a parse tree produced by EiffelParser#mul_expr.
    def exitMul_expr(self, ctx:EiffelParser.Mul_exprContext):
        pass


    # Enter a parse tree produced by EiffelParser#unary_expr.
    def enterUnary_expr(self, ctx:EiffelParser.Unary_exprContext):
        pass

    # Exit a parse tree produced by EiffelParser#unary_expr.
    def exitUnary_expr(self, ctx:EiffelParser.Unary_exprContext):
        pass


    # Enter a parse tree produced by EiffelParser#primary.
    def enterPrimary(self, ctx:EiffelParser.PrimaryContext):
        pass

    # Exit a parse tree produced by EiffelParser#primary.
    def exitPrimary(self, ctx:EiffelParser.PrimaryContext):
        pass


    # Enter a parse tree produced by EiffelParser#call_expr.
    def enterCall_expr(self, ctx:EiffelParser.Call_exprContext):
        pass

    # Exit a parse tree produced by EiffelParser#call_expr.
    def exitCall_expr(self, ctx:EiffelParser.Call_exprContext):
        pass


    # Enter a parse tree produced by EiffelParser#actual_params.
    def enterActual_params(self, ctx:EiffelParser.Actual_paramsContext):
        pass

    # Exit a parse tree produced by EiffelParser#actual_params.
    def exitActual_params(self, ctx:EiffelParser.Actual_paramsContext):
        pass



del EiffelParser