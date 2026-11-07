# Generated from rosetta/babel/eiffel/grammar/Eiffel.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .EiffelParser import EiffelParser
else:
    from EiffelParser import EiffelParser

# This class defines a complete generic visitor for a parse tree produced by EiffelParser.

class EiffelVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by EiffelParser#program.
    def visitProgram(self, ctx:EiffelParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EiffelParser#class_declaration.
    def visitClass_declaration(self, ctx:EiffelParser.Class_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EiffelParser#inheritance.
    def visitInheritance(self, ctx:EiffelParser.InheritanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EiffelParser#rename_clause.
    def visitRename_clause(self, ctx:EiffelParser.Rename_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EiffelParser#redefine_clause.
    def visitRedefine_clause(self, ctx:EiffelParser.Redefine_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EiffelParser#create_clause.
    def visitCreate_clause(self, ctx:EiffelParser.Create_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EiffelParser#feature_block.
    def visitFeature_block(self, ctx:EiffelParser.Feature_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EiffelParser#feature_declaration.
    def visitFeature_declaration(self, ctx:EiffelParser.Feature_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EiffelParser#formal_params.
    def visitFormal_params(self, ctx:EiffelParser.Formal_paramsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EiffelParser#param_list.
    def visitParam_list(self, ctx:EiffelParser.Param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EiffelParser#param_group.
    def visitParam_group(self, ctx:EiffelParser.Param_groupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EiffelParser#id_list.
    def visitId_list(self, ctx:EiffelParser.Id_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EiffelParser#type_.
    def visitType_(self, ctx:EiffelParser.Type_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EiffelParser#generic_type.
    def visitGeneric_type(self, ctx:EiffelParser.Generic_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EiffelParser#attribute_init.
    def visitAttribute_init(self, ctx:EiffelParser.Attribute_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EiffelParser#routine_body.
    def visitRoutine_body(self, ctx:EiffelParser.Routine_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EiffelParser#assertion_list.
    def visitAssertion_list(self, ctx:EiffelParser.Assertion_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EiffelParser#assertion.
    def visitAssertion(self, ctx:EiffelParser.AssertionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EiffelParser#declaration_list.
    def visitDeclaration_list(self, ctx:EiffelParser.Declaration_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EiffelParser#declaration.
    def visitDeclaration(self, ctx:EiffelParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EiffelParser#block.
    def visitBlock(self, ctx:EiffelParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EiffelParser#statement.
    def visitStatement(self, ctx:EiffelParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EiffelParser#assignment.
    def visitAssignment(self, ctx:EiffelParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EiffelParser#call_statement.
    def visitCall_statement(self, ctx:EiffelParser.Call_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EiffelParser#if_statement.
    def visitIf_statement(self, ctx:EiffelParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EiffelParser#loop_statement.
    def visitLoop_statement(self, ctx:EiffelParser.Loop_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EiffelParser#retry_statement.
    def visitRetry_statement(self, ctx:EiffelParser.Retry_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EiffelParser#check_statement.
    def visitCheck_statement(self, ctx:EiffelParser.Check_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EiffelParser#invariant_clause.
    def visitInvariant_clause(self, ctx:EiffelParser.Invariant_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EiffelParser#expression.
    def visitExpression(self, ctx:EiffelParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EiffelParser#logical_expr.
    def visitLogical_expr(self, ctx:EiffelParser.Logical_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EiffelParser#rel_expr.
    def visitRel_expr(self, ctx:EiffelParser.Rel_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EiffelParser#add_expr.
    def visitAdd_expr(self, ctx:EiffelParser.Add_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EiffelParser#mul_expr.
    def visitMul_expr(self, ctx:EiffelParser.Mul_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EiffelParser#unary_expr.
    def visitUnary_expr(self, ctx:EiffelParser.Unary_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EiffelParser#primary.
    def visitPrimary(self, ctx:EiffelParser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EiffelParser#call_expr.
    def visitCall_expr(self, ctx:EiffelParser.Call_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EiffelParser#actual_params.
    def visitActual_params(self, ctx:EiffelParser.Actual_paramsContext):
        return self.visitChildren(ctx)



del EiffelParser