# Generated from rosetta/babel/fortran/grammar/Fortran.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .FortranParser import FortranParser
else:
    from FortranParser import FortranParser

# This class defines a complete generic visitor for a parse tree produced by FortranParser.

class FortranVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by FortranParser#program.
    def visitProgram(self, ctx:FortranParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FortranParser#executable_unit.
    def visitExecutable_unit(self, ctx:FortranParser.Executable_unitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FortranParser#main_program.
    def visitMain_program(self, ctx:FortranParser.Main_programContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FortranParser#subroutine_def.
    def visitSubroutine_def(self, ctx:FortranParser.Subroutine_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FortranParser#function_def.
    def visitFunction_def(self, ctx:FortranParser.Function_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FortranParser#program_stmt.
    def visitProgram_stmt(self, ctx:FortranParser.Program_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FortranParser#subroutine_stmt.
    def visitSubroutine_stmt(self, ctx:FortranParser.Subroutine_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FortranParser#function_stmt.
    def visitFunction_stmt(self, ctx:FortranParser.Function_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FortranParser#end_stmt.
    def visitEnd_stmt(self, ctx:FortranParser.End_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FortranParser#specification_part.
    def visitSpecification_part(self, ctx:FortranParser.Specification_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FortranParser#specification_stmt.
    def visitSpecification_stmt(self, ctx:FortranParser.Specification_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FortranParser#type_declaration_stmt.
    def visitType_declaration_stmt(self, ctx:FortranParser.Type_declaration_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FortranParser#type_spec.
    def visitType_spec(self, ctx:FortranParser.Type_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FortranParser#entity_decl.
    def visitEntity_decl(self, ctx:FortranParser.Entity_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FortranParser#array_spec.
    def visitArray_spec(self, ctx:FortranParser.Array_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FortranParser#dimension.
    def visitDimension(self, ctx:FortranParser.DimensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FortranParser#implicit_none_stmt.
    def visitImplicit_none_stmt(self, ctx:FortranParser.Implicit_none_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FortranParser#common_stmt.
    def visitCommon_stmt(self, ctx:FortranParser.Common_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FortranParser#dimension_stmt.
    def visitDimension_stmt(self, ctx:FortranParser.Dimension_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FortranParser#execution_part.
    def visitExecution_part(self, ctx:FortranParser.Execution_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FortranParser#executable_stmt.
    def visitExecutable_stmt(self, ctx:FortranParser.Executable_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FortranParser#action_stmt.
    def visitAction_stmt(self, ctx:FortranParser.Action_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FortranParser#assignment_stmt.
    def visitAssignment_stmt(self, ctx:FortranParser.Assignment_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FortranParser#if_stmt.
    def visitIf_stmt(self, ctx:FortranParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FortranParser#do_stmt.
    def visitDo_stmt(self, ctx:FortranParser.Do_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FortranParser#goto_stmt.
    def visitGoto_stmt(self, ctx:FortranParser.Goto_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FortranParser#call_stmt.
    def visitCall_stmt(self, ctx:FortranParser.Call_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FortranParser#return_stmt.
    def visitReturn_stmt(self, ctx:FortranParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FortranParser#write_stmt.
    def visitWrite_stmt(self, ctx:FortranParser.Write_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FortranParser#print_stmt.
    def visitPrint_stmt(self, ctx:FortranParser.Print_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FortranParser#format_stmt.
    def visitFormat_stmt(self, ctx:FortranParser.Format_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FortranParser#format_item.
    def visitFormat_item(self, ctx:FortranParser.Format_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FortranParser#label.
    def visitLabel(self, ctx:FortranParser.LabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FortranParser#identifier.
    def visitIdentifier(self, ctx:FortranParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FortranParser#expression.
    def visitExpression(self, ctx:FortranParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FortranParser#primary.
    def visitPrimary(self, ctx:FortranParser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FortranParser#literal.
    def visitLiteral(self, ctx:FortranParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FortranParser#integer_literal.
    def visitInteger_literal(self, ctx:FortranParser.Integer_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FortranParser#real_literal.
    def visitReal_literal(self, ctx:FortranParser.Real_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FortranParser#string_literal.
    def visitString_literal(self, ctx:FortranParser.String_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FortranParser#logical_literal.
    def visitLogical_literal(self, ctx:FortranParser.Logical_literalContext):
        return self.visitChildren(ctx)



del FortranParser