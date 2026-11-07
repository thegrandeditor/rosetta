# Generated from Carbon.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CarbonParser import CarbonParser
else:
    from CarbonParser import CarbonParser

# This class defines a complete listener for a parse tree produced by CarbonParser.
class CarbonListener(ParseTreeListener):

    # Enter a parse tree produced by CarbonParser#program.
    def enterProgram(self, ctx:CarbonParser.ProgramContext):
        pass

    # Exit a parse tree produced by CarbonParser#program.
    def exitProgram(self, ctx:CarbonParser.ProgramContext):
        pass


    # Enter a parse tree produced by CarbonParser#element.
    def enterElement(self, ctx:CarbonParser.ElementContext):
        pass

    # Exit a parse tree produced by CarbonParser#element.
    def exitElement(self, ctx:CarbonParser.ElementContext):
        pass


    # Enter a parse tree produced by CarbonParser#package_decl.
    def enterPackage_decl(self, ctx:CarbonParser.Package_declContext):
        pass

    # Exit a parse tree produced by CarbonParser#package_decl.
    def exitPackage_decl(self, ctx:CarbonParser.Package_declContext):
        pass


    # Enter a parse tree produced by CarbonParser#function_decl.
    def enterFunction_decl(self, ctx:CarbonParser.Function_declContext):
        pass

    # Exit a parse tree produced by CarbonParser#function_decl.
    def exitFunction_decl(self, ctx:CarbonParser.Function_declContext):
        pass


    # Enter a parse tree produced by CarbonParser#param_list.
    def enterParam_list(self, ctx:CarbonParser.Param_listContext):
        pass

    # Exit a parse tree produced by CarbonParser#param_list.
    def exitParam_list(self, ctx:CarbonParser.Param_listContext):
        pass


    # Enter a parse tree produced by CarbonParser#parameter.
    def enterParameter(self, ctx:CarbonParser.ParameterContext):
        pass

    # Exit a parse tree produced by CarbonParser#parameter.
    def exitParameter(self, ctx:CarbonParser.ParameterContext):
        pass


    # Enter a parse tree produced by CarbonParser#class_decl.
    def enterClass_decl(self, ctx:CarbonParser.Class_declContext):
        pass

    # Exit a parse tree produced by CarbonParser#class_decl.
    def exitClass_decl(self, ctx:CarbonParser.Class_declContext):
        pass


    # Enter a parse tree produced by CarbonParser#class_element.
    def enterClass_element(self, ctx:CarbonParser.Class_elementContext):
        pass

    # Exit a parse tree produced by CarbonParser#class_element.
    def exitClass_element(self, ctx:CarbonParser.Class_elementContext):
        pass


    # Enter a parse tree produced by CarbonParser#interface_decl.
    def enterInterface_decl(self, ctx:CarbonParser.Interface_declContext):
        pass

    # Exit a parse tree produced by CarbonParser#interface_decl.
    def exitInterface_decl(self, ctx:CarbonParser.Interface_declContext):
        pass


    # Enter a parse tree produced by CarbonParser#interface_element.
    def enterInterface_element(self, ctx:CarbonParser.Interface_elementContext):
        pass

    # Exit a parse tree produced by CarbonParser#interface_element.
    def exitInterface_element(self, ctx:CarbonParser.Interface_elementContext):
        pass


    # Enter a parse tree produced by CarbonParser#impl_decl.
    def enterImpl_decl(self, ctx:CarbonParser.Impl_declContext):
        pass

    # Exit a parse tree produced by CarbonParser#impl_decl.
    def exitImpl_decl(self, ctx:CarbonParser.Impl_declContext):
        pass


    # Enter a parse tree produced by CarbonParser#var_decl.
    def enterVar_decl(self, ctx:CarbonParser.Var_declContext):
        pass

    # Exit a parse tree produced by CarbonParser#var_decl.
    def exitVar_decl(self, ctx:CarbonParser.Var_declContext):
        pass


    # Enter a parse tree produced by CarbonParser#assignment.
    def enterAssignment(self, ctx:CarbonParser.AssignmentContext):
        pass

    # Exit a parse tree produced by CarbonParser#assignment.
    def exitAssignment(self, ctx:CarbonParser.AssignmentContext):
        pass


    # Enter a parse tree produced by CarbonParser#type_name.
    def enterType_name(self, ctx:CarbonParser.Type_nameContext):
        pass

    # Exit a parse tree produced by CarbonParser#type_name.
    def exitType_name(self, ctx:CarbonParser.Type_nameContext):
        pass


    # Enter a parse tree produced by CarbonParser#block.
    def enterBlock(self, ctx:CarbonParser.BlockContext):
        pass

    # Exit a parse tree produced by CarbonParser#block.
    def exitBlock(self, ctx:CarbonParser.BlockContext):
        pass


    # Enter a parse tree produced by CarbonParser#statement.
    def enterStatement(self, ctx:CarbonParser.StatementContext):
        pass

    # Exit a parse tree produced by CarbonParser#statement.
    def exitStatement(self, ctx:CarbonParser.StatementContext):
        pass


    # Enter a parse tree produced by CarbonParser#if_stmt.
    def enterIf_stmt(self, ctx:CarbonParser.If_stmtContext):
        pass

    # Exit a parse tree produced by CarbonParser#if_stmt.
    def exitIf_stmt(self, ctx:CarbonParser.If_stmtContext):
        pass


    # Enter a parse tree produced by CarbonParser#while_stmt.
    def enterWhile_stmt(self, ctx:CarbonParser.While_stmtContext):
        pass

    # Exit a parse tree produced by CarbonParser#while_stmt.
    def exitWhile_stmt(self, ctx:CarbonParser.While_stmtContext):
        pass


    # Enter a parse tree produced by CarbonParser#return_stmt.
    def enterReturn_stmt(self, ctx:CarbonParser.Return_stmtContext):
        pass

    # Exit a parse tree produced by CarbonParser#return_stmt.
    def exitReturn_stmt(self, ctx:CarbonParser.Return_stmtContext):
        pass


    # Enter a parse tree produced by CarbonParser#match_stmt.
    def enterMatch_stmt(self, ctx:CarbonParser.Match_stmtContext):
        pass

    # Exit a parse tree produced by CarbonParser#match_stmt.
    def exitMatch_stmt(self, ctx:CarbonParser.Match_stmtContext):
        pass


    # Enter a parse tree produced by CarbonParser#match_case.
    def enterMatch_case(self, ctx:CarbonParser.Match_caseContext):
        pass

    # Exit a parse tree produced by CarbonParser#match_case.
    def exitMatch_case(self, ctx:CarbonParser.Match_caseContext):
        pass


    # Enter a parse tree produced by CarbonParser#expression_stmt.
    def enterExpression_stmt(self, ctx:CarbonParser.Expression_stmtContext):
        pass

    # Exit a parse tree produced by CarbonParser#expression_stmt.
    def exitExpression_stmt(self, ctx:CarbonParser.Expression_stmtContext):
        pass


    # Enter a parse tree produced by CarbonParser#expression.
    def enterExpression(self, ctx:CarbonParser.ExpressionContext):
        pass

    # Exit a parse tree produced by CarbonParser#expression.
    def exitExpression(self, ctx:CarbonParser.ExpressionContext):
        pass


    # Enter a parse tree produced by CarbonParser#argument_list.
    def enterArgument_list(self, ctx:CarbonParser.Argument_listContext):
        pass

    # Exit a parse tree produced by CarbonParser#argument_list.
    def exitArgument_list(self, ctx:CarbonParser.Argument_listContext):
        pass


    # Enter a parse tree produced by CarbonParser#primary.
    def enterPrimary(self, ctx:CarbonParser.PrimaryContext):
        pass

    # Exit a parse tree produced by CarbonParser#primary.
    def exitPrimary(self, ctx:CarbonParser.PrimaryContext):
        pass



del CarbonParser