# Generated from Mojo.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MojoParser import MojoParser
else:
    from MojoParser import MojoParser

# This class defines a complete listener for a parse tree produced by MojoParser.
class MojoListener(ParseTreeListener):

    # Enter a parse tree produced by MojoParser#program.
    def enterProgram(self, ctx:MojoParser.ProgramContext):
        pass

    # Exit a parse tree produced by MojoParser#program.
    def exitProgram(self, ctx:MojoParser.ProgramContext):
        pass


    # Enter a parse tree produced by MojoParser#element.
    def enterElement(self, ctx:MojoParser.ElementContext):
        pass

    # Exit a parse tree produced by MojoParser#element.
    def exitElement(self, ctx:MojoParser.ElementContext):
        pass


    # Enter a parse tree produced by MojoParser#function_decl.
    def enterFunction_decl(self, ctx:MojoParser.Function_declContext):
        pass

    # Exit a parse tree produced by MojoParser#function_decl.
    def exitFunction_decl(self, ctx:MojoParser.Function_declContext):
        pass


    # Enter a parse tree produced by MojoParser#decorator.
    def enterDecorator(self, ctx:MojoParser.DecoratorContext):
        pass

    # Exit a parse tree produced by MojoParser#decorator.
    def exitDecorator(self, ctx:MojoParser.DecoratorContext):
        pass


    # Enter a parse tree produced by MojoParser#param_list.
    def enterParam_list(self, ctx:MojoParser.Param_listContext):
        pass

    # Exit a parse tree produced by MojoParser#param_list.
    def exitParam_list(self, ctx:MojoParser.Param_listContext):
        pass


    # Enter a parse tree produced by MojoParser#parameter.
    def enterParameter(self, ctx:MojoParser.ParameterContext):
        pass

    # Exit a parse tree produced by MojoParser#parameter.
    def exitParameter(self, ctx:MojoParser.ParameterContext):
        pass


    # Enter a parse tree produced by MojoParser#struct_decl.
    def enterStruct_decl(self, ctx:MojoParser.Struct_declContext):
        pass

    # Exit a parse tree produced by MojoParser#struct_decl.
    def exitStruct_decl(self, ctx:MojoParser.Struct_declContext):
        pass


    # Enter a parse tree produced by MojoParser#struct_element.
    def enterStruct_element(self, ctx:MojoParser.Struct_elementContext):
        pass

    # Exit a parse tree produced by MojoParser#struct_element.
    def exitStruct_element(self, ctx:MojoParser.Struct_elementContext):
        pass


    # Enter a parse tree produced by MojoParser#var_decl.
    def enterVar_decl(self, ctx:MojoParser.Var_declContext):
        pass

    # Exit a parse tree produced by MojoParser#var_decl.
    def exitVar_decl(self, ctx:MojoParser.Var_declContext):
        pass


    # Enter a parse tree produced by MojoParser#assignment.
    def enterAssignment(self, ctx:MojoParser.AssignmentContext):
        pass

    # Exit a parse tree produced by MojoParser#assignment.
    def exitAssignment(self, ctx:MojoParser.AssignmentContext):
        pass


    # Enter a parse tree produced by MojoParser#type_name.
    def enterType_name(self, ctx:MojoParser.Type_nameContext):
        pass

    # Exit a parse tree produced by MojoParser#type_name.
    def exitType_name(self, ctx:MojoParser.Type_nameContext):
        pass


    # Enter a parse tree produced by MojoParser#block.
    def enterBlock(self, ctx:MojoParser.BlockContext):
        pass

    # Exit a parse tree produced by MojoParser#block.
    def exitBlock(self, ctx:MojoParser.BlockContext):
        pass


    # Enter a parse tree produced by MojoParser#statement.
    def enterStatement(self, ctx:MojoParser.StatementContext):
        pass

    # Exit a parse tree produced by MojoParser#statement.
    def exitStatement(self, ctx:MojoParser.StatementContext):
        pass


    # Enter a parse tree produced by MojoParser#if_stmt.
    def enterIf_stmt(self, ctx:MojoParser.If_stmtContext):
        pass

    # Exit a parse tree produced by MojoParser#if_stmt.
    def exitIf_stmt(self, ctx:MojoParser.If_stmtContext):
        pass


    # Enter a parse tree produced by MojoParser#while_stmt.
    def enterWhile_stmt(self, ctx:MojoParser.While_stmtContext):
        pass

    # Exit a parse tree produced by MojoParser#while_stmt.
    def exitWhile_stmt(self, ctx:MojoParser.While_stmtContext):
        pass


    # Enter a parse tree produced by MojoParser#return_stmt.
    def enterReturn_stmt(self, ctx:MojoParser.Return_stmtContext):
        pass

    # Exit a parse tree produced by MojoParser#return_stmt.
    def exitReturn_stmt(self, ctx:MojoParser.Return_stmtContext):
        pass


    # Enter a parse tree produced by MojoParser#expression_stmt.
    def enterExpression_stmt(self, ctx:MojoParser.Expression_stmtContext):
        pass

    # Exit a parse tree produced by MojoParser#expression_stmt.
    def exitExpression_stmt(self, ctx:MojoParser.Expression_stmtContext):
        pass


    # Enter a parse tree produced by MojoParser#expression.
    def enterExpression(self, ctx:MojoParser.ExpressionContext):
        pass

    # Exit a parse tree produced by MojoParser#expression.
    def exitExpression(self, ctx:MojoParser.ExpressionContext):
        pass


    # Enter a parse tree produced by MojoParser#argument_list.
    def enterArgument_list(self, ctx:MojoParser.Argument_listContext):
        pass

    # Exit a parse tree produced by MojoParser#argument_list.
    def exitArgument_list(self, ctx:MojoParser.Argument_listContext):
        pass


    # Enter a parse tree produced by MojoParser#primary.
    def enterPrimary(self, ctx:MojoParser.PrimaryContext):
        pass

    # Exit a parse tree produced by MojoParser#primary.
    def exitPrimary(self, ctx:MojoParser.PrimaryContext):
        pass



del MojoParser