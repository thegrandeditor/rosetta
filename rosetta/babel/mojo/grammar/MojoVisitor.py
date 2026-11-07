# Generated from Mojo.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MojoParser import MojoParser
else:
    from MojoParser import MojoParser

# This class defines a complete generic visitor for a parse tree produced by MojoParser.

class MojoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MojoParser#program.
    def visitProgram(self, ctx:MojoParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MojoParser#element.
    def visitElement(self, ctx:MojoParser.ElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MojoParser#function_decl.
    def visitFunction_decl(self, ctx:MojoParser.Function_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MojoParser#decorator.
    def visitDecorator(self, ctx:MojoParser.DecoratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MojoParser#param_list.
    def visitParam_list(self, ctx:MojoParser.Param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MojoParser#parameter.
    def visitParameter(self, ctx:MojoParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MojoParser#struct_decl.
    def visitStruct_decl(self, ctx:MojoParser.Struct_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MojoParser#struct_element.
    def visitStruct_element(self, ctx:MojoParser.Struct_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MojoParser#var_decl.
    def visitVar_decl(self, ctx:MojoParser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MojoParser#assignment.
    def visitAssignment(self, ctx:MojoParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MojoParser#type_name.
    def visitType_name(self, ctx:MojoParser.Type_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MojoParser#block.
    def visitBlock(self, ctx:MojoParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MojoParser#statement.
    def visitStatement(self, ctx:MojoParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MojoParser#if_stmt.
    def visitIf_stmt(self, ctx:MojoParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MojoParser#while_stmt.
    def visitWhile_stmt(self, ctx:MojoParser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MojoParser#return_stmt.
    def visitReturn_stmt(self, ctx:MojoParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MojoParser#expression_stmt.
    def visitExpression_stmt(self, ctx:MojoParser.Expression_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MojoParser#expression.
    def visitExpression(self, ctx:MojoParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MojoParser#argument_list.
    def visitArgument_list(self, ctx:MojoParser.Argument_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MojoParser#primary.
    def visitPrimary(self, ctx:MojoParser.PrimaryContext):
        return self.visitChildren(ctx)



del MojoParser