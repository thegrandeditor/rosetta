# Generated from rosetta/babel/algol/grammar/Algol.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .AlgolParser import AlgolParser
else:
    from AlgolParser import AlgolParser

# This class defines a complete listener for a parse tree produced by AlgolParser.
class AlgolListener(ParseTreeListener):

    # Enter a parse tree produced by AlgolParser#program.
    def enterProgram(self, ctx:AlgolParser.ProgramContext):
        pass

    # Exit a parse tree produced by AlgolParser#program.
    def exitProgram(self, ctx:AlgolParser.ProgramContext):
        pass


    # Enter a parse tree produced by AlgolParser#block.
    def enterBlock(self, ctx:AlgolParser.BlockContext):
        pass

    # Exit a parse tree produced by AlgolParser#block.
    def exitBlock(self, ctx:AlgolParser.BlockContext):
        pass


    # Enter a parse tree produced by AlgolParser#declaration_list.
    def enterDeclaration_list(self, ctx:AlgolParser.Declaration_listContext):
        pass

    # Exit a parse tree produced by AlgolParser#declaration_list.
    def exitDeclaration_list(self, ctx:AlgolParser.Declaration_listContext):
        pass


    # Enter a parse tree produced by AlgolParser#declaration.
    def enterDeclaration(self, ctx:AlgolParser.DeclarationContext):
        pass

    # Exit a parse tree produced by AlgolParser#declaration.
    def exitDeclaration(self, ctx:AlgolParser.DeclarationContext):
        pass


    # Enter a parse tree produced by AlgolParser#type_declaration.
    def enterType_declaration(self, ctx:AlgolParser.Type_declarationContext):
        pass

    # Exit a parse tree produced by AlgolParser#type_declaration.
    def exitType_declaration(self, ctx:AlgolParser.Type_declarationContext):
        pass


    # Enter a parse tree produced by AlgolParser#own_declaration.
    def enterOwn_declaration(self, ctx:AlgolParser.Own_declarationContext):
        pass

    # Exit a parse tree produced by AlgolParser#own_declaration.
    def exitOwn_declaration(self, ctx:AlgolParser.Own_declarationContext):
        pass


    # Enter a parse tree produced by AlgolParser#procedure_declaration.
    def enterProcedure_declaration(self, ctx:AlgolParser.Procedure_declarationContext):
        pass

    # Exit a parse tree produced by AlgolParser#procedure_declaration.
    def exitProcedure_declaration(self, ctx:AlgolParser.Procedure_declarationContext):
        pass


    # Enter a parse tree produced by AlgolParser#formal_parameter_list.
    def enterFormal_parameter_list(self, ctx:AlgolParser.Formal_parameter_listContext):
        pass

    # Exit a parse tree produced by AlgolParser#formal_parameter_list.
    def exitFormal_parameter_list(self, ctx:AlgolParser.Formal_parameter_listContext):
        pass


    # Enter a parse tree produced by AlgolParser#statement_list.
    def enterStatement_list(self, ctx:AlgolParser.Statement_listContext):
        pass

    # Exit a parse tree produced by AlgolParser#statement_list.
    def exitStatement_list(self, ctx:AlgolParser.Statement_listContext):
        pass


    # Enter a parse tree produced by AlgolParser#statement.
    def enterStatement(self, ctx:AlgolParser.StatementContext):
        pass

    # Exit a parse tree produced by AlgolParser#statement.
    def exitStatement(self, ctx:AlgolParser.StatementContext):
        pass


    # Enter a parse tree produced by AlgolParser#assignment_statement.
    def enterAssignment_statement(self, ctx:AlgolParser.Assignment_statementContext):
        pass

    # Exit a parse tree produced by AlgolParser#assignment_statement.
    def exitAssignment_statement(self, ctx:AlgolParser.Assignment_statementContext):
        pass


    # Enter a parse tree produced by AlgolParser#procedure_call.
    def enterProcedure_call(self, ctx:AlgolParser.Procedure_callContext):
        pass

    # Exit a parse tree produced by AlgolParser#procedure_call.
    def exitProcedure_call(self, ctx:AlgolParser.Procedure_callContext):
        pass


    # Enter a parse tree produced by AlgolParser#if_statement.
    def enterIf_statement(self, ctx:AlgolParser.If_statementContext):
        pass

    # Exit a parse tree produced by AlgolParser#if_statement.
    def exitIf_statement(self, ctx:AlgolParser.If_statementContext):
        pass


    # Enter a parse tree produced by AlgolParser#for_statement.
    def enterFor_statement(self, ctx:AlgolParser.For_statementContext):
        pass

    # Exit a parse tree produced by AlgolParser#for_statement.
    def exitFor_statement(self, ctx:AlgolParser.For_statementContext):
        pass


    # Enter a parse tree produced by AlgolParser#while_statement.
    def enterWhile_statement(self, ctx:AlgolParser.While_statementContext):
        pass

    # Exit a parse tree produced by AlgolParser#while_statement.
    def exitWhile_statement(self, ctx:AlgolParser.While_statementContext):
        pass


    # Enter a parse tree produced by AlgolParser#expression.
    def enterExpression(self, ctx:AlgolParser.ExpressionContext):
        pass

    # Exit a parse tree produced by AlgolParser#expression.
    def exitExpression(self, ctx:AlgolParser.ExpressionContext):
        pass


    # Enter a parse tree produced by AlgolParser#primary.
    def enterPrimary(self, ctx:AlgolParser.PrimaryContext):
        pass

    # Exit a parse tree produced by AlgolParser#primary.
    def exitPrimary(self, ctx:AlgolParser.PrimaryContext):
        pass


    # Enter a parse tree produced by AlgolParser#literal.
    def enterLiteral(self, ctx:AlgolParser.LiteralContext):
        pass

    # Exit a parse tree produced by AlgolParser#literal.
    def exitLiteral(self, ctx:AlgolParser.LiteralContext):
        pass


    # Enter a parse tree produced by AlgolParser#type_hint.
    def enterType_hint(self, ctx:AlgolParser.Type_hintContext):
        pass

    # Exit a parse tree produced by AlgolParser#type_hint.
    def exitType_hint(self, ctx:AlgolParser.Type_hintContext):
        pass


    # Enter a parse tree produced by AlgolParser#identifier.
    def enterIdentifier(self, ctx:AlgolParser.IdentifierContext):
        pass

    # Exit a parse tree produced by AlgolParser#identifier.
    def exitIdentifier(self, ctx:AlgolParser.IdentifierContext):
        pass


    # Enter a parse tree produced by AlgolParser#integer_literal.
    def enterInteger_literal(self, ctx:AlgolParser.Integer_literalContext):
        pass

    # Exit a parse tree produced by AlgolParser#integer_literal.
    def exitInteger_literal(self, ctx:AlgolParser.Integer_literalContext):
        pass


    # Enter a parse tree produced by AlgolParser#real_literal.
    def enterReal_literal(self, ctx:AlgolParser.Real_literalContext):
        pass

    # Exit a parse tree produced by AlgolParser#real_literal.
    def exitReal_literal(self, ctx:AlgolParser.Real_literalContext):
        pass


    # Enter a parse tree produced by AlgolParser#string_literal.
    def enterString_literal(self, ctx:AlgolParser.String_literalContext):
        pass

    # Exit a parse tree produced by AlgolParser#string_literal.
    def exitString_literal(self, ctx:AlgolParser.String_literalContext):
        pass


    # Enter a parse tree produced by AlgolParser#logical_literal.
    def enterLogical_literal(self, ctx:AlgolParser.Logical_literalContext):
        pass

    # Exit a parse tree produced by AlgolParser#logical_literal.
    def exitLogical_literal(self, ctx:AlgolParser.Logical_literalContext):
        pass



del AlgolParser