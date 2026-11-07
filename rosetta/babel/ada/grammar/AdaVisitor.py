# Generated from rosetta/babel/ada/grammar/Ada.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .AdaParser import AdaParser
else:
    from AdaParser import AdaParser

# This class defines a complete generic visitor for a parse tree produced by AdaParser.

class AdaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by AdaParser#program.
    def visitProgram(self, ctx:AdaParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#context_item.
    def visitContext_item(self, ctx:AdaParser.Context_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#qualified_name.
    def visitQualified_name(self, ctx:AdaParser.Qualified_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#compilation_unit.
    def visitCompilation_unit(self, ctx:AdaParser.Compilation_unitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#generic_declaration.
    def visitGeneric_declaration(self, ctx:AdaParser.Generic_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#generic_formal_part.
    def visitGeneric_formal_part(self, ctx:AdaParser.Generic_formal_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#package_declaration.
    def visitPackage_declaration(self, ctx:AdaParser.Package_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#package_body.
    def visitPackage_body(self, ctx:AdaParser.Package_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#package_item.
    def visitPackage_item(self, ctx:AdaParser.Package_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#subprogram_declaration.
    def visitSubprogram_declaration(self, ctx:AdaParser.Subprogram_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#subprogram_body.
    def visitSubprogram_body(self, ctx:AdaParser.Subprogram_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#subprogram_specification.
    def visitSubprogram_specification(self, ctx:AdaParser.Subprogram_specificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#formal_part.
    def visitFormal_part(self, ctx:AdaParser.Formal_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#parameter_specification.
    def visitParameter_specification(self, ctx:AdaParser.Parameter_specificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#type_declaration.
    def visitType_declaration(self, ctx:AdaParser.Type_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#type_definition.
    def visitType_definition(self, ctx:AdaParser.Type_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#component_list.
    def visitComponent_list(self, ctx:AdaParser.Component_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#variable_declaration.
    def visitVariable_declaration(self, ctx:AdaParser.Variable_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#task_declaration.
    def visitTask_declaration(self, ctx:AdaParser.Task_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#declaration.
    def visitDeclaration(self, ctx:AdaParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#statement.
    def visitStatement(self, ctx:AdaParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#assignment_statement.
    def visitAssignment_statement(self, ctx:AdaParser.Assignment_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#procedure_call_statement.
    def visitProcedure_call_statement(self, ctx:AdaParser.Procedure_call_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#if_statement.
    def visitIf_statement(self, ctx:AdaParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#case_statement.
    def visitCase_statement(self, ctx:AdaParser.Case_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#loop_statement.
    def visitLoop_statement(self, ctx:AdaParser.Loop_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#iteration_scheme.
    def visitIteration_scheme(self, ctx:AdaParser.Iteration_schemeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#return_statement.
    def visitReturn_statement(self, ctx:AdaParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#exit_statement.
    def visitExit_statement(self, ctx:AdaParser.Exit_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#exception_handler.
    def visitException_handler(self, ctx:AdaParser.Exception_handlerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#choice_list.
    def visitChoice_list(self, ctx:AdaParser.Choice_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#range_spec.
    def visitRange_spec(self, ctx:AdaParser.Range_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#type_mark.
    def visitType_mark(self, ctx:AdaParser.Type_markContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#access_definition.
    def visitAccess_definition(self, ctx:AdaParser.Access_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#private_type_definition.
    def visitPrivate_type_definition(self, ctx:AdaParser.Private_type_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#index_constraint.
    def visitIndex_constraint(self, ctx:AdaParser.Index_constraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#entry_call_statement.
    def visitEntry_call_statement(self, ctx:AdaParser.Entry_call_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#delay_statement.
    def visitDelay_statement(self, ctx:AdaParser.Delay_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#select_statement.
    def visitSelect_statement(self, ctx:AdaParser.Select_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#select_alternative.
    def visitSelect_alternative(self, ctx:AdaParser.Select_alternativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#accept_statement.
    def visitAccept_statement(self, ctx:AdaParser.Accept_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#expression.
    def visitExpression(self, ctx:AdaParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#primary.
    def visitPrimary(self, ctx:AdaParser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#literal.
    def visitLiteral(self, ctx:AdaParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#identifier.
    def visitIdentifier(self, ctx:AdaParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#integer_literal.
    def visitInteger_literal(self, ctx:AdaParser.Integer_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#real_literal.
    def visitReal_literal(self, ctx:AdaParser.Real_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#string_literal.
    def visitString_literal(self, ctx:AdaParser.String_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#logical_literal.
    def visitLogical_literal(self, ctx:AdaParser.Logical_literalContext):
        return self.visitChildren(ctx)



del AdaParser