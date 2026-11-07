# Generated from Zig.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ZigParser import ZigParser
else:
    from ZigParser import ZigParser

# This class defines a complete listener for a parse tree produced by ZigParser.
class ZigListener(ParseTreeListener):

    # Enter a parse tree produced by ZigParser#program.
    def enterProgram(self, ctx:ZigParser.ProgramContext):
        pass

    # Exit a parse tree produced by ZigParser#program.
    def exitProgram(self, ctx:ZigParser.ProgramContext):
        pass


    # Enter a parse tree produced by ZigParser#element.
    def enterElement(self, ctx:ZigParser.ElementContext):
        pass

    # Exit a parse tree produced by ZigParser#element.
    def exitElement(self, ctx:ZigParser.ElementContext):
        pass


    # Enter a parse tree produced by ZigParser#function_decl.
    def enterFunction_decl(self, ctx:ZigParser.Function_declContext):
        pass

    # Exit a parse tree produced by ZigParser#function_decl.
    def exitFunction_decl(self, ctx:ZigParser.Function_declContext):
        pass


    # Enter a parse tree produced by ZigParser#param_list.
    def enterParam_list(self, ctx:ZigParser.Param_listContext):
        pass

    # Exit a parse tree produced by ZigParser#param_list.
    def exitParam_list(self, ctx:ZigParser.Param_listContext):
        pass


    # Enter a parse tree produced by ZigParser#parameter.
    def enterParameter(self, ctx:ZigParser.ParameterContext):
        pass

    # Exit a parse tree produced by ZigParser#parameter.
    def exitParameter(self, ctx:ZigParser.ParameterContext):
        pass


    # Enter a parse tree produced by ZigParser#struct_decl.
    def enterStruct_decl(self, ctx:ZigParser.Struct_declContext):
        pass

    # Exit a parse tree produced by ZigParser#struct_decl.
    def exitStruct_decl(self, ctx:ZigParser.Struct_declContext):
        pass


    # Enter a parse tree produced by ZigParser#struct_element.
    def enterStruct_element(self, ctx:ZigParser.Struct_elementContext):
        pass

    # Exit a parse tree produced by ZigParser#struct_element.
    def exitStruct_element(self, ctx:ZigParser.Struct_elementContext):
        pass


    # Enter a parse tree produced by ZigParser#var_decl.
    def enterVar_decl(self, ctx:ZigParser.Var_declContext):
        pass

    # Exit a parse tree produced by ZigParser#var_decl.
    def exitVar_decl(self, ctx:ZigParser.Var_declContext):
        pass


    # Enter a parse tree produced by ZigParser#assignment.
    def enterAssignment(self, ctx:ZigParser.AssignmentContext):
        pass

    # Exit a parse tree produced by ZigParser#assignment.
    def exitAssignment(self, ctx:ZigParser.AssignmentContext):
        pass


    # Enter a parse tree produced by ZigParser#type_name.
    def enterType_name(self, ctx:ZigParser.Type_nameContext):
        pass

    # Exit a parse tree produced by ZigParser#type_name.
    def exitType_name(self, ctx:ZigParser.Type_nameContext):
        pass


    # Enter a parse tree produced by ZigParser#block.
    def enterBlock(self, ctx:ZigParser.BlockContext):
        pass

    # Exit a parse tree produced by ZigParser#block.
    def exitBlock(self, ctx:ZigParser.BlockContext):
        pass


    # Enter a parse tree produced by ZigParser#statement.
    def enterStatement(self, ctx:ZigParser.StatementContext):
        pass

    # Exit a parse tree produced by ZigParser#statement.
    def exitStatement(self, ctx:ZigParser.StatementContext):
        pass


    # Enter a parse tree produced by ZigParser#if_stmt.
    def enterIf_stmt(self, ctx:ZigParser.If_stmtContext):
        pass

    # Exit a parse tree produced by ZigParser#if_stmt.
    def exitIf_stmt(self, ctx:ZigParser.If_stmtContext):
        pass


    # Enter a parse tree produced by ZigParser#while_stmt.
    def enterWhile_stmt(self, ctx:ZigParser.While_stmtContext):
        pass

    # Exit a parse tree produced by ZigParser#while_stmt.
    def exitWhile_stmt(self, ctx:ZigParser.While_stmtContext):
        pass


    # Enter a parse tree produced by ZigParser#for_stmt.
    def enterFor_stmt(self, ctx:ZigParser.For_stmtContext):
        pass

    # Exit a parse tree produced by ZigParser#for_stmt.
    def exitFor_stmt(self, ctx:ZigParser.For_stmtContext):
        pass


    # Enter a parse tree produced by ZigParser#return_stmt.
    def enterReturn_stmt(self, ctx:ZigParser.Return_stmtContext):
        pass

    # Exit a parse tree produced by ZigParser#return_stmt.
    def exitReturn_stmt(self, ctx:ZigParser.Return_stmtContext):
        pass


    # Enter a parse tree produced by ZigParser#defer_stmt.
    def enterDefer_stmt(self, ctx:ZigParser.Defer_stmtContext):
        pass

    # Exit a parse tree produced by ZigParser#defer_stmt.
    def exitDefer_stmt(self, ctx:ZigParser.Defer_stmtContext):
        pass


    # Enter a parse tree produced by ZigParser#expression_stmt.
    def enterExpression_stmt(self, ctx:ZigParser.Expression_stmtContext):
        pass

    # Exit a parse tree produced by ZigParser#expression_stmt.
    def exitExpression_stmt(self, ctx:ZigParser.Expression_stmtContext):
        pass


    # Enter a parse tree produced by ZigParser#expression.
    def enterExpression(self, ctx:ZigParser.ExpressionContext):
        pass

    # Exit a parse tree produced by ZigParser#expression.
    def exitExpression(self, ctx:ZigParser.ExpressionContext):
        pass


    # Enter a parse tree produced by ZigParser#argument_list.
    def enterArgument_list(self, ctx:ZigParser.Argument_listContext):
        pass

    # Exit a parse tree produced by ZigParser#argument_list.
    def exitArgument_list(self, ctx:ZigParser.Argument_listContext):
        pass


    # Enter a parse tree produced by ZigParser#primary.
    def enterPrimary(self, ctx:ZigParser.PrimaryContext):
        pass

    # Exit a parse tree produced by ZigParser#primary.
    def exitPrimary(self, ctx:ZigParser.PrimaryContext):
        pass



del ZigParser