# Generated from Zig.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ZigParser import ZigParser
else:
    from ZigParser import ZigParser

# This class defines a complete generic visitor for a parse tree produced by ZigParser.

class ZigVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ZigParser#program.
    def visitProgram(self, ctx:ZigParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZigParser#element.
    def visitElement(self, ctx:ZigParser.ElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZigParser#function_decl.
    def visitFunction_decl(self, ctx:ZigParser.Function_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZigParser#param_list.
    def visitParam_list(self, ctx:ZigParser.Param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZigParser#parameter.
    def visitParameter(self, ctx:ZigParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZigParser#struct_decl.
    def visitStruct_decl(self, ctx:ZigParser.Struct_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZigParser#struct_element.
    def visitStruct_element(self, ctx:ZigParser.Struct_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZigParser#var_decl.
    def visitVar_decl(self, ctx:ZigParser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZigParser#assignment.
    def visitAssignment(self, ctx:ZigParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZigParser#type_name.
    def visitType_name(self, ctx:ZigParser.Type_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZigParser#block.
    def visitBlock(self, ctx:ZigParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZigParser#statement.
    def visitStatement(self, ctx:ZigParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZigParser#if_stmt.
    def visitIf_stmt(self, ctx:ZigParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZigParser#while_stmt.
    def visitWhile_stmt(self, ctx:ZigParser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZigParser#for_stmt.
    def visitFor_stmt(self, ctx:ZigParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZigParser#return_stmt.
    def visitReturn_stmt(self, ctx:ZigParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZigParser#defer_stmt.
    def visitDefer_stmt(self, ctx:ZigParser.Defer_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZigParser#expression_stmt.
    def visitExpression_stmt(self, ctx:ZigParser.Expression_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZigParser#expression.
    def visitExpression(self, ctx:ZigParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZigParser#argument_list.
    def visitArgument_list(self, ctx:ZigParser.Argument_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZigParser#primary.
    def visitPrimary(self, ctx:ZigParser.PrimaryContext):
        return self.visitChildren(ctx)



del ZigParser