# Generated from Carbon.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CarbonParser import CarbonParser
else:
    from CarbonParser import CarbonParser

# This class defines a complete generic visitor for a parse tree produced by CarbonParser.

class CarbonVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CarbonParser#program.
    def visitProgram(self, ctx:CarbonParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CarbonParser#element.
    def visitElement(self, ctx:CarbonParser.ElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CarbonParser#package_decl.
    def visitPackage_decl(self, ctx:CarbonParser.Package_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CarbonParser#function_decl.
    def visitFunction_decl(self, ctx:CarbonParser.Function_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CarbonParser#param_list.
    def visitParam_list(self, ctx:CarbonParser.Param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CarbonParser#parameter.
    def visitParameter(self, ctx:CarbonParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CarbonParser#class_decl.
    def visitClass_decl(self, ctx:CarbonParser.Class_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CarbonParser#class_element.
    def visitClass_element(self, ctx:CarbonParser.Class_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CarbonParser#interface_decl.
    def visitInterface_decl(self, ctx:CarbonParser.Interface_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CarbonParser#interface_element.
    def visitInterface_element(self, ctx:CarbonParser.Interface_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CarbonParser#impl_decl.
    def visitImpl_decl(self, ctx:CarbonParser.Impl_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CarbonParser#var_decl.
    def visitVar_decl(self, ctx:CarbonParser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CarbonParser#assignment.
    def visitAssignment(self, ctx:CarbonParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CarbonParser#type_name.
    def visitType_name(self, ctx:CarbonParser.Type_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CarbonParser#block.
    def visitBlock(self, ctx:CarbonParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CarbonParser#statement.
    def visitStatement(self, ctx:CarbonParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CarbonParser#if_stmt.
    def visitIf_stmt(self, ctx:CarbonParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CarbonParser#while_stmt.
    def visitWhile_stmt(self, ctx:CarbonParser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CarbonParser#return_stmt.
    def visitReturn_stmt(self, ctx:CarbonParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CarbonParser#match_stmt.
    def visitMatch_stmt(self, ctx:CarbonParser.Match_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CarbonParser#match_case.
    def visitMatch_case(self, ctx:CarbonParser.Match_caseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CarbonParser#expression_stmt.
    def visitExpression_stmt(self, ctx:CarbonParser.Expression_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CarbonParser#expression.
    def visitExpression(self, ctx:CarbonParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CarbonParser#argument_list.
    def visitArgument_list(self, ctx:CarbonParser.Argument_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CarbonParser#primary.
    def visitPrimary(self, ctx:CarbonParser.PrimaryContext):
        return self.visitChildren(ctx)



del CarbonParser