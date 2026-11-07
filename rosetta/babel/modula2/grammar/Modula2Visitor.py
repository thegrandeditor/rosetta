# Generated from rosetta/babel/modula2/grammar/Modula2.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .Modula2Parser import Modula2Parser
else:
    from Modula2Parser import Modula2Parser

# This class defines a complete generic visitor for a parse tree produced by Modula2Parser.

class Modula2Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by Modula2Parser#program.
    def visitProgram(self, ctx:Modula2Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Modula2Parser#compilation_unit.
    def visitCompilation_unit(self, ctx:Modula2Parser.Compilation_unitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Modula2Parser#main_module.
    def visitMain_module(self, ctx:Modula2Parser.Main_moduleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Modula2Parser#definition_module.
    def visitDefinition_module(self, ctx:Modula2Parser.Definition_moduleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Modula2Parser#implementation_module.
    def visitImplementation_module(self, ctx:Modula2Parser.Implementation_moduleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Modula2Parser#import_list.
    def visitImport_list(self, ctx:Modula2Parser.Import_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Modula2Parser#export_list.
    def visitExport_list(self, ctx:Modula2Parser.Export_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Modula2Parser#id_list.
    def visitId_list(self, ctx:Modula2Parser.Id_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Modula2Parser#block.
    def visitBlock(self, ctx:Modula2Parser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Modula2Parser#declaration.
    def visitDeclaration(self, ctx:Modula2Parser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Modula2Parser#procedure_declaration.
    def visitProcedure_declaration(self, ctx:Modula2Parser.Procedure_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Modula2Parser#formal_params.
    def visitFormal_params(self, ctx:Modula2Parser.Formal_paramsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Modula2Parser#fp_section.
    def visitFp_section(self, ctx:Modula2Parser.Fp_sectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Modula2Parser#type_.
    def visitType_(self, ctx:Modula2Parser.Type_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Modula2Parser#array_type.
    def visitArray_type(self, ctx:Modula2Parser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Modula2Parser#pointer_type.
    def visitPointer_type(self, ctx:Modula2Parser.Pointer_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Modula2Parser#record_type.
    def visitRecord_type(self, ctx:Modula2Parser.Record_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Modula2Parser#statement_sequence.
    def visitStatement_sequence(self, ctx:Modula2Parser.Statement_sequenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Modula2Parser#statement.
    def visitStatement(self, ctx:Modula2Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Modula2Parser#assignment.
    def visitAssignment(self, ctx:Modula2Parser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Modula2Parser#procedure_call.
    def visitProcedure_call(self, ctx:Modula2Parser.Procedure_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Modula2Parser#actual_params.
    def visitActual_params(self, ctx:Modula2Parser.Actual_paramsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Modula2Parser#if_statement.
    def visitIf_statement(self, ctx:Modula2Parser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Modula2Parser#case_statement.
    def visitCase_statement(self, ctx:Modula2Parser.Case_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Modula2Parser#case_item.
    def visitCase_item(self, ctx:Modula2Parser.Case_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Modula2Parser#while_statement.
    def visitWhile_statement(self, ctx:Modula2Parser.While_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Modula2Parser#repeat_statement.
    def visitRepeat_statement(self, ctx:Modula2Parser.Repeat_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Modula2Parser#loop_statement.
    def visitLoop_statement(self, ctx:Modula2Parser.Loop_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Modula2Parser#for_statement.
    def visitFor_statement(self, ctx:Modula2Parser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Modula2Parser#return_statement.
    def visitReturn_statement(self, ctx:Modula2Parser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Modula2Parser#exit_statement.
    def visitExit_statement(self, ctx:Modula2Parser.Exit_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Modula2Parser#designator.
    def visitDesignator(self, ctx:Modula2Parser.DesignatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Modula2Parser#expression.
    def visitExpression(self, ctx:Modula2Parser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Modula2Parser#rel_op.
    def visitRel_op(self, ctx:Modula2Parser.Rel_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Modula2Parser#simple_expression.
    def visitSimple_expression(self, ctx:Modula2Parser.Simple_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Modula2Parser#add_op.
    def visitAdd_op(self, ctx:Modula2Parser.Add_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Modula2Parser#term.
    def visitTerm(self, ctx:Modula2Parser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Modula2Parser#mul_op.
    def visitMul_op(self, ctx:Modula2Parser.Mul_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Modula2Parser#factor.
    def visitFactor(self, ctx:Modula2Parser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Modula2Parser#element.
    def visitElement(self, ctx:Modula2Parser.ElementContext):
        return self.visitChildren(ctx)



del Modula2Parser