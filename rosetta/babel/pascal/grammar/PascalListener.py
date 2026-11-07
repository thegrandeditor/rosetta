# Generated from rosetta/babel/pascal/grammar/Pascal.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PascalParser import PascalParser
else:
    from PascalParser import PascalParser

# This class defines a complete listener for a parse tree produced by PascalParser.
class PascalListener(ParseTreeListener):

    # Enter a parse tree produced by PascalParser#program.
    def enterProgram(self, ctx:PascalParser.ProgramContext):
        pass

    # Exit a parse tree produced by PascalParser#program.
    def exitProgram(self, ctx:PascalParser.ProgramContext):
        pass


    # Enter a parse tree produced by PascalParser#program_stmt.
    def enterProgram_stmt(self, ctx:PascalParser.Program_stmtContext):
        pass

    # Exit a parse tree produced by PascalParser#program_stmt.
    def exitProgram_stmt(self, ctx:PascalParser.Program_stmtContext):
        pass


    # Enter a parse tree produced by PascalParser#block.
    def enterBlock(self, ctx:PascalParser.BlockContext):
        pass

    # Exit a parse tree produced by PascalParser#block.
    def exitBlock(self, ctx:PascalParser.BlockContext):
        pass


    # Enter a parse tree produced by PascalParser#declaration_part.
    def enterDeclaration_part(self, ctx:PascalParser.Declaration_partContext):
        pass

    # Exit a parse tree produced by PascalParser#declaration_part.
    def exitDeclaration_part(self, ctx:PascalParser.Declaration_partContext):
        pass


    # Enter a parse tree produced by PascalParser#var_decl_part.
    def enterVar_decl_part(self, ctx:PascalParser.Var_decl_partContext):
        pass

    # Exit a parse tree produced by PascalParser#var_decl_part.
    def exitVar_decl_part(self, ctx:PascalParser.Var_decl_partContext):
        pass


    # Enter a parse tree produced by PascalParser#var_decl.
    def enterVar_decl(self, ctx:PascalParser.Var_declContext):
        pass

    # Exit a parse tree produced by PascalParser#var_decl.
    def exitVar_decl(self, ctx:PascalParser.Var_declContext):
        pass


    # Enter a parse tree produced by PascalParser#type_decl_part.
    def enterType_decl_part(self, ctx:PascalParser.Type_decl_partContext):
        pass

    # Exit a parse tree produced by PascalParser#type_decl_part.
    def exitType_decl_part(self, ctx:PascalParser.Type_decl_partContext):
        pass


    # Enter a parse tree produced by PascalParser#type_decl.
    def enterType_decl(self, ctx:PascalParser.Type_declContext):
        pass

    # Exit a parse tree produced by PascalParser#type_decl.
    def exitType_decl(self, ctx:PascalParser.Type_declContext):
        pass


    # Enter a parse tree produced by PascalParser#type_spec.
    def enterType_spec(self, ctx:PascalParser.Type_specContext):
        pass

    # Exit a parse tree produced by PascalParser#type_spec.
    def exitType_spec(self, ctx:PascalParser.Type_specContext):
        pass


    # Enter a parse tree produced by PascalParser#range.
    def enterRange(self, ctx:PascalParser.RangeContext):
        pass

    # Exit a parse tree produced by PascalParser#range.
    def exitRange(self, ctx:PascalParser.RangeContext):
        pass


    # Enter a parse tree produced by PascalParser#field_list.
    def enterField_list(self, ctx:PascalParser.Field_listContext):
        pass

    # Exit a parse tree produced by PascalParser#field_list.
    def exitField_list(self, ctx:PascalParser.Field_listContext):
        pass


    # Enter a parse tree produced by PascalParser#procedure_decl.
    def enterProcedure_decl(self, ctx:PascalParser.Procedure_declContext):
        pass

    # Exit a parse tree produced by PascalParser#procedure_decl.
    def exitProcedure_decl(self, ctx:PascalParser.Procedure_declContext):
        pass


    # Enter a parse tree produced by PascalParser#function_decl.
    def enterFunction_decl(self, ctx:PascalParser.Function_declContext):
        pass

    # Exit a parse tree produced by PascalParser#function_decl.
    def exitFunction_decl(self, ctx:PascalParser.Function_declContext):
        pass


    # Enter a parse tree produced by PascalParser#formal_parameter_list.
    def enterFormal_parameter_list(self, ctx:PascalParser.Formal_parameter_listContext):
        pass

    # Exit a parse tree produced by PascalParser#formal_parameter_list.
    def exitFormal_parameter_list(self, ctx:PascalParser.Formal_parameter_listContext):
        pass


    # Enter a parse tree produced by PascalParser#formal_parameter.
    def enterFormal_parameter(self, ctx:PascalParser.Formal_parameterContext):
        pass

    # Exit a parse tree produced by PascalParser#formal_parameter.
    def exitFormal_parameter(self, ctx:PascalParser.Formal_parameterContext):
        pass


    # Enter a parse tree produced by PascalParser#statement_part.
    def enterStatement_part(self, ctx:PascalParser.Statement_partContext):
        pass

    # Exit a parse tree produced by PascalParser#statement_part.
    def exitStatement_part(self, ctx:PascalParser.Statement_partContext):
        pass


    # Enter a parse tree produced by PascalParser#statement.
    def enterStatement(self, ctx:PascalParser.StatementContext):
        pass

    # Exit a parse tree produced by PascalParser#statement.
    def exitStatement(self, ctx:PascalParser.StatementContext):
        pass


    # Enter a parse tree produced by PascalParser#assignment_stmt.
    def enterAssignment_stmt(self, ctx:PascalParser.Assignment_stmtContext):
        pass

    # Exit a parse tree produced by PascalParser#assignment_stmt.
    def exitAssignment_stmt(self, ctx:PascalParser.Assignment_stmtContext):
        pass


    # Enter a parse tree produced by PascalParser#procedure_call.
    def enterProcedure_call(self, ctx:PascalParser.Procedure_callContext):
        pass

    # Exit a parse tree produced by PascalParser#procedure_call.
    def exitProcedure_call(self, ctx:PascalParser.Procedure_callContext):
        pass


    # Enter a parse tree produced by PascalParser#if_stmt.
    def enterIf_stmt(self, ctx:PascalParser.If_stmtContext):
        pass

    # Exit a parse tree produced by PascalParser#if_stmt.
    def exitIf_stmt(self, ctx:PascalParser.If_stmtContext):
        pass


    # Enter a parse tree produced by PascalParser#for_stmt.
    def enterFor_stmt(self, ctx:PascalParser.For_stmtContext):
        pass

    # Exit a parse tree produced by PascalParser#for_stmt.
    def exitFor_stmt(self, ctx:PascalParser.For_stmtContext):
        pass


    # Enter a parse tree produced by PascalParser#while_stmt.
    def enterWhile_stmt(self, ctx:PascalParser.While_stmtContext):
        pass

    # Exit a parse tree produced by PascalParser#while_stmt.
    def exitWhile_stmt(self, ctx:PascalParser.While_stmtContext):
        pass


    # Enter a parse tree produced by PascalParser#repeat_stmt.
    def enterRepeat_stmt(self, ctx:PascalParser.Repeat_stmtContext):
        pass

    # Exit a parse tree produced by PascalParser#repeat_stmt.
    def exitRepeat_stmt(self, ctx:PascalParser.Repeat_stmtContext):
        pass


    # Enter a parse tree produced by PascalParser#with_stmt.
    def enterWith_stmt(self, ctx:PascalParser.With_stmtContext):
        pass

    # Exit a parse tree produced by PascalParser#with_stmt.
    def exitWith_stmt(self, ctx:PascalParser.With_stmtContext):
        pass


    # Enter a parse tree produced by PascalParser#expression.
    def enterExpression(self, ctx:PascalParser.ExpressionContext):
        pass

    # Exit a parse tree produced by PascalParser#expression.
    def exitExpression(self, ctx:PascalParser.ExpressionContext):
        pass


    # Enter a parse tree produced by PascalParser#primary.
    def enterPrimary(self, ctx:PascalParser.PrimaryContext):
        pass

    # Exit a parse tree produced by PascalParser#primary.
    def exitPrimary(self, ctx:PascalParser.PrimaryContext):
        pass


    # Enter a parse tree produced by PascalParser#literal.
    def enterLiteral(self, ctx:PascalParser.LiteralContext):
        pass

    # Exit a parse tree produced by PascalParser#literal.
    def exitLiteral(self, ctx:PascalParser.LiteralContext):
        pass


    # Enter a parse tree produced by PascalParser#identifier.
    def enterIdentifier(self, ctx:PascalParser.IdentifierContext):
        pass

    # Exit a parse tree produced by PascalParser#identifier.
    def exitIdentifier(self, ctx:PascalParser.IdentifierContext):
        pass


    # Enter a parse tree produced by PascalParser#integer_literal.
    def enterInteger_literal(self, ctx:PascalParser.Integer_literalContext):
        pass

    # Exit a parse tree produced by PascalParser#integer_literal.
    def exitInteger_literal(self, ctx:PascalParser.Integer_literalContext):
        pass


    # Enter a parse tree produced by PascalParser#real_literal.
    def enterReal_literal(self, ctx:PascalParser.Real_literalContext):
        pass

    # Exit a parse tree produced by PascalParser#real_literal.
    def exitReal_literal(self, ctx:PascalParser.Real_literalContext):
        pass


    # Enter a parse tree produced by PascalParser#string_literal.
    def enterString_literal(self, ctx:PascalParser.String_literalContext):
        pass

    # Exit a parse tree produced by PascalParser#string_literal.
    def exitString_literal(self, ctx:PascalParser.String_literalContext):
        pass


    # Enter a parse tree produced by PascalParser#logical_literal.
    def enterLogical_literal(self, ctx:PascalParser.Logical_literalContext):
        pass

    # Exit a parse tree produced by PascalParser#logical_literal.
    def exitLogical_literal(self, ctx:PascalParser.Logical_literalContext):
        pass



del PascalParser