# Generated from rosetta/babel/algol/grammar/Algol.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .AlgolParser import AlgolParser
else:
    from AlgolParser import AlgolParser

# This class defines a complete generic visitor for a parse tree produced by AlgolParser.

class AlgolVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by AlgolParser#program.
    def visitProgram(self, ctx:AlgolParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgolParser#block.
    def visitBlock(self, ctx:AlgolParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgolParser#declaration_list.
    def visitDeclaration_list(self, ctx:AlgolParser.Declaration_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgolParser#declaration.
    def visitDeclaration(self, ctx:AlgolParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgolParser#type_declaration.
    def visitType_declaration(self, ctx:AlgolParser.Type_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgolParser#own_declaration.
    def visitOwn_declaration(self, ctx:AlgolParser.Own_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgolParser#procedure_declaration.
    def visitProcedure_declaration(self, ctx:AlgolParser.Procedure_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgolParser#formal_parameter_list.
    def visitFormal_parameter_list(self, ctx:AlgolParser.Formal_parameter_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgolParser#statement_list.
    def visitStatement_list(self, ctx:AlgolParser.Statement_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgolParser#statement.
    def visitStatement(self, ctx:AlgolParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgolParser#assignment_statement.
    def visitAssignment_statement(self, ctx:AlgolParser.Assignment_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgolParser#procedure_call.
    def visitProcedure_call(self, ctx:AlgolParser.Procedure_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgolParser#if_statement.
    def visitIf_statement(self, ctx:AlgolParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgolParser#for_statement.
    def visitFor_statement(self, ctx:AlgolParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgolParser#while_statement.
    def visitWhile_statement(self, ctx:AlgolParser.While_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgolParser#expression.
    def visitExpression(self, ctx:AlgolParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgolParser#primary.
    def visitPrimary(self, ctx:AlgolParser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgolParser#literal.
    def visitLiteral(self, ctx:AlgolParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgolParser#type_hint.
    def visitType_hint(self, ctx:AlgolParser.Type_hintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgolParser#identifier.
    def visitIdentifier(self, ctx:AlgolParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgolParser#integer_literal.
    def visitInteger_literal(self, ctx:AlgolParser.Integer_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgolParser#real_literal.
    def visitReal_literal(self, ctx:AlgolParser.Real_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgolParser#string_literal.
    def visitString_literal(self, ctx:AlgolParser.String_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgolParser#logical_literal.
    def visitLogical_literal(self, ctx:AlgolParser.Logical_literalContext):
        return self.visitChildren(ctx)



del AlgolParser