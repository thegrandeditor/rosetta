# Generated from rosetta/babel/pascal/grammar/Pascal.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PascalParser import PascalParser
else:
    from PascalParser import PascalParser

# This class defines a complete generic visitor for a parse tree produced by PascalParser.

class PascalVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PascalParser#program.
    def visitProgram(self, ctx:PascalParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalParser#program_stmt.
    def visitProgram_stmt(self, ctx:PascalParser.Program_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalParser#block.
    def visitBlock(self, ctx:PascalParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalParser#declaration_part.
    def visitDeclaration_part(self, ctx:PascalParser.Declaration_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalParser#var_decl_part.
    def visitVar_decl_part(self, ctx:PascalParser.Var_decl_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalParser#var_decl.
    def visitVar_decl(self, ctx:PascalParser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalParser#type_decl_part.
    def visitType_decl_part(self, ctx:PascalParser.Type_decl_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalParser#type_decl.
    def visitType_decl(self, ctx:PascalParser.Type_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalParser#type_spec.
    def visitType_spec(self, ctx:PascalParser.Type_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalParser#range.
    def visitRange(self, ctx:PascalParser.RangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalParser#field_list.
    def visitField_list(self, ctx:PascalParser.Field_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalParser#procedure_decl.
    def visitProcedure_decl(self, ctx:PascalParser.Procedure_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalParser#function_decl.
    def visitFunction_decl(self, ctx:PascalParser.Function_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalParser#formal_parameter_list.
    def visitFormal_parameter_list(self, ctx:PascalParser.Formal_parameter_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalParser#formal_parameter.
    def visitFormal_parameter(self, ctx:PascalParser.Formal_parameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalParser#statement_part.
    def visitStatement_part(self, ctx:PascalParser.Statement_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalParser#statement.
    def visitStatement(self, ctx:PascalParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalParser#assignment_stmt.
    def visitAssignment_stmt(self, ctx:PascalParser.Assignment_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalParser#procedure_call.
    def visitProcedure_call(self, ctx:PascalParser.Procedure_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalParser#if_stmt.
    def visitIf_stmt(self, ctx:PascalParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalParser#for_stmt.
    def visitFor_stmt(self, ctx:PascalParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalParser#while_stmt.
    def visitWhile_stmt(self, ctx:PascalParser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalParser#repeat_stmt.
    def visitRepeat_stmt(self, ctx:PascalParser.Repeat_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalParser#with_stmt.
    def visitWith_stmt(self, ctx:PascalParser.With_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalParser#expression.
    def visitExpression(self, ctx:PascalParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalParser#primary.
    def visitPrimary(self, ctx:PascalParser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalParser#literal.
    def visitLiteral(self, ctx:PascalParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalParser#identifier.
    def visitIdentifier(self, ctx:PascalParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalParser#integer_literal.
    def visitInteger_literal(self, ctx:PascalParser.Integer_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalParser#real_literal.
    def visitReal_literal(self, ctx:PascalParser.Real_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalParser#string_literal.
    def visitString_literal(self, ctx:PascalParser.String_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalParser#logical_literal.
    def visitLogical_literal(self, ctx:PascalParser.Logical_literalContext):
        return self.visitChildren(ctx)



del PascalParser