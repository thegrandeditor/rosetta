# Generated from rosetta/babel/ada/grammar/Ada.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .AdaParser import AdaParser
else:
    from AdaParser import AdaParser

# This class defines a complete listener for a parse tree produced by AdaParser.
class AdaListener(ParseTreeListener):

    # Enter a parse tree produced by AdaParser#program.
    def enterProgram(self, ctx:AdaParser.ProgramContext):
        pass

    # Exit a parse tree produced by AdaParser#program.
    def exitProgram(self, ctx:AdaParser.ProgramContext):
        pass


    # Enter a parse tree produced by AdaParser#context_item.
    def enterContext_item(self, ctx:AdaParser.Context_itemContext):
        pass

    # Exit a parse tree produced by AdaParser#context_item.
    def exitContext_item(self, ctx:AdaParser.Context_itemContext):
        pass


    # Enter a parse tree produced by AdaParser#qualified_name.
    def enterQualified_name(self, ctx:AdaParser.Qualified_nameContext):
        pass

    # Exit a parse tree produced by AdaParser#qualified_name.
    def exitQualified_name(self, ctx:AdaParser.Qualified_nameContext):
        pass


    # Enter a parse tree produced by AdaParser#compilation_unit.
    def enterCompilation_unit(self, ctx:AdaParser.Compilation_unitContext):
        pass

    # Exit a parse tree produced by AdaParser#compilation_unit.
    def exitCompilation_unit(self, ctx:AdaParser.Compilation_unitContext):
        pass


    # Enter a parse tree produced by AdaParser#generic_declaration.
    def enterGeneric_declaration(self, ctx:AdaParser.Generic_declarationContext):
        pass

    # Exit a parse tree produced by AdaParser#generic_declaration.
    def exitGeneric_declaration(self, ctx:AdaParser.Generic_declarationContext):
        pass


    # Enter a parse tree produced by AdaParser#generic_formal_part.
    def enterGeneric_formal_part(self, ctx:AdaParser.Generic_formal_partContext):
        pass

    # Exit a parse tree produced by AdaParser#generic_formal_part.
    def exitGeneric_formal_part(self, ctx:AdaParser.Generic_formal_partContext):
        pass


    # Enter a parse tree produced by AdaParser#package_declaration.
    def enterPackage_declaration(self, ctx:AdaParser.Package_declarationContext):
        pass

    # Exit a parse tree produced by AdaParser#package_declaration.
    def exitPackage_declaration(self, ctx:AdaParser.Package_declarationContext):
        pass


    # Enter a parse tree produced by AdaParser#package_body.
    def enterPackage_body(self, ctx:AdaParser.Package_bodyContext):
        pass

    # Exit a parse tree produced by AdaParser#package_body.
    def exitPackage_body(self, ctx:AdaParser.Package_bodyContext):
        pass


    # Enter a parse tree produced by AdaParser#package_item.
    def enterPackage_item(self, ctx:AdaParser.Package_itemContext):
        pass

    # Exit a parse tree produced by AdaParser#package_item.
    def exitPackage_item(self, ctx:AdaParser.Package_itemContext):
        pass


    # Enter a parse tree produced by AdaParser#subprogram_declaration.
    def enterSubprogram_declaration(self, ctx:AdaParser.Subprogram_declarationContext):
        pass

    # Exit a parse tree produced by AdaParser#subprogram_declaration.
    def exitSubprogram_declaration(self, ctx:AdaParser.Subprogram_declarationContext):
        pass


    # Enter a parse tree produced by AdaParser#subprogram_body.
    def enterSubprogram_body(self, ctx:AdaParser.Subprogram_bodyContext):
        pass

    # Exit a parse tree produced by AdaParser#subprogram_body.
    def exitSubprogram_body(self, ctx:AdaParser.Subprogram_bodyContext):
        pass


    # Enter a parse tree produced by AdaParser#subprogram_specification.
    def enterSubprogram_specification(self, ctx:AdaParser.Subprogram_specificationContext):
        pass

    # Exit a parse tree produced by AdaParser#subprogram_specification.
    def exitSubprogram_specification(self, ctx:AdaParser.Subprogram_specificationContext):
        pass


    # Enter a parse tree produced by AdaParser#formal_part.
    def enterFormal_part(self, ctx:AdaParser.Formal_partContext):
        pass

    # Exit a parse tree produced by AdaParser#formal_part.
    def exitFormal_part(self, ctx:AdaParser.Formal_partContext):
        pass


    # Enter a parse tree produced by AdaParser#parameter_specification.
    def enterParameter_specification(self, ctx:AdaParser.Parameter_specificationContext):
        pass

    # Exit a parse tree produced by AdaParser#parameter_specification.
    def exitParameter_specification(self, ctx:AdaParser.Parameter_specificationContext):
        pass


    # Enter a parse tree produced by AdaParser#type_declaration.
    def enterType_declaration(self, ctx:AdaParser.Type_declarationContext):
        pass

    # Exit a parse tree produced by AdaParser#type_declaration.
    def exitType_declaration(self, ctx:AdaParser.Type_declarationContext):
        pass


    # Enter a parse tree produced by AdaParser#type_definition.
    def enterType_definition(self, ctx:AdaParser.Type_definitionContext):
        pass

    # Exit a parse tree produced by AdaParser#type_definition.
    def exitType_definition(self, ctx:AdaParser.Type_definitionContext):
        pass


    # Enter a parse tree produced by AdaParser#component_list.
    def enterComponent_list(self, ctx:AdaParser.Component_listContext):
        pass

    # Exit a parse tree produced by AdaParser#component_list.
    def exitComponent_list(self, ctx:AdaParser.Component_listContext):
        pass


    # Enter a parse tree produced by AdaParser#variable_declaration.
    def enterVariable_declaration(self, ctx:AdaParser.Variable_declarationContext):
        pass

    # Exit a parse tree produced by AdaParser#variable_declaration.
    def exitVariable_declaration(self, ctx:AdaParser.Variable_declarationContext):
        pass


    # Enter a parse tree produced by AdaParser#task_declaration.
    def enterTask_declaration(self, ctx:AdaParser.Task_declarationContext):
        pass

    # Exit a parse tree produced by AdaParser#task_declaration.
    def exitTask_declaration(self, ctx:AdaParser.Task_declarationContext):
        pass


    # Enter a parse tree produced by AdaParser#declaration.
    def enterDeclaration(self, ctx:AdaParser.DeclarationContext):
        pass

    # Exit a parse tree produced by AdaParser#declaration.
    def exitDeclaration(self, ctx:AdaParser.DeclarationContext):
        pass


    # Enter a parse tree produced by AdaParser#statement.
    def enterStatement(self, ctx:AdaParser.StatementContext):
        pass

    # Exit a parse tree produced by AdaParser#statement.
    def exitStatement(self, ctx:AdaParser.StatementContext):
        pass


    # Enter a parse tree produced by AdaParser#assignment_statement.
    def enterAssignment_statement(self, ctx:AdaParser.Assignment_statementContext):
        pass

    # Exit a parse tree produced by AdaParser#assignment_statement.
    def exitAssignment_statement(self, ctx:AdaParser.Assignment_statementContext):
        pass


    # Enter a parse tree produced by AdaParser#procedure_call_statement.
    def enterProcedure_call_statement(self, ctx:AdaParser.Procedure_call_statementContext):
        pass

    # Exit a parse tree produced by AdaParser#procedure_call_statement.
    def exitProcedure_call_statement(self, ctx:AdaParser.Procedure_call_statementContext):
        pass


    # Enter a parse tree produced by AdaParser#if_statement.
    def enterIf_statement(self, ctx:AdaParser.If_statementContext):
        pass

    # Exit a parse tree produced by AdaParser#if_statement.
    def exitIf_statement(self, ctx:AdaParser.If_statementContext):
        pass


    # Enter a parse tree produced by AdaParser#case_statement.
    def enterCase_statement(self, ctx:AdaParser.Case_statementContext):
        pass

    # Exit a parse tree produced by AdaParser#case_statement.
    def exitCase_statement(self, ctx:AdaParser.Case_statementContext):
        pass


    # Enter a parse tree produced by AdaParser#loop_statement.
    def enterLoop_statement(self, ctx:AdaParser.Loop_statementContext):
        pass

    # Exit a parse tree produced by AdaParser#loop_statement.
    def exitLoop_statement(self, ctx:AdaParser.Loop_statementContext):
        pass


    # Enter a parse tree produced by AdaParser#iteration_scheme.
    def enterIteration_scheme(self, ctx:AdaParser.Iteration_schemeContext):
        pass

    # Exit a parse tree produced by AdaParser#iteration_scheme.
    def exitIteration_scheme(self, ctx:AdaParser.Iteration_schemeContext):
        pass


    # Enter a parse tree produced by AdaParser#return_statement.
    def enterReturn_statement(self, ctx:AdaParser.Return_statementContext):
        pass

    # Exit a parse tree produced by AdaParser#return_statement.
    def exitReturn_statement(self, ctx:AdaParser.Return_statementContext):
        pass


    # Enter a parse tree produced by AdaParser#exit_statement.
    def enterExit_statement(self, ctx:AdaParser.Exit_statementContext):
        pass

    # Exit a parse tree produced by AdaParser#exit_statement.
    def exitExit_statement(self, ctx:AdaParser.Exit_statementContext):
        pass


    # Enter a parse tree produced by AdaParser#exception_handler.
    def enterException_handler(self, ctx:AdaParser.Exception_handlerContext):
        pass

    # Exit a parse tree produced by AdaParser#exception_handler.
    def exitException_handler(self, ctx:AdaParser.Exception_handlerContext):
        pass


    # Enter a parse tree produced by AdaParser#choice_list.
    def enterChoice_list(self, ctx:AdaParser.Choice_listContext):
        pass

    # Exit a parse tree produced by AdaParser#choice_list.
    def exitChoice_list(self, ctx:AdaParser.Choice_listContext):
        pass


    # Enter a parse tree produced by AdaParser#range_spec.
    def enterRange_spec(self, ctx:AdaParser.Range_specContext):
        pass

    # Exit a parse tree produced by AdaParser#range_spec.
    def exitRange_spec(self, ctx:AdaParser.Range_specContext):
        pass


    # Enter a parse tree produced by AdaParser#type_mark.
    def enterType_mark(self, ctx:AdaParser.Type_markContext):
        pass

    # Exit a parse tree produced by AdaParser#type_mark.
    def exitType_mark(self, ctx:AdaParser.Type_markContext):
        pass


    # Enter a parse tree produced by AdaParser#access_definition.
    def enterAccess_definition(self, ctx:AdaParser.Access_definitionContext):
        pass

    # Exit a parse tree produced by AdaParser#access_definition.
    def exitAccess_definition(self, ctx:AdaParser.Access_definitionContext):
        pass


    # Enter a parse tree produced by AdaParser#private_type_definition.
    def enterPrivate_type_definition(self, ctx:AdaParser.Private_type_definitionContext):
        pass

    # Exit a parse tree produced by AdaParser#private_type_definition.
    def exitPrivate_type_definition(self, ctx:AdaParser.Private_type_definitionContext):
        pass


    # Enter a parse tree produced by AdaParser#index_constraint.
    def enterIndex_constraint(self, ctx:AdaParser.Index_constraintContext):
        pass

    # Exit a parse tree produced by AdaParser#index_constraint.
    def exitIndex_constraint(self, ctx:AdaParser.Index_constraintContext):
        pass


    # Enter a parse tree produced by AdaParser#entry_call_statement.
    def enterEntry_call_statement(self, ctx:AdaParser.Entry_call_statementContext):
        pass

    # Exit a parse tree produced by AdaParser#entry_call_statement.
    def exitEntry_call_statement(self, ctx:AdaParser.Entry_call_statementContext):
        pass


    # Enter a parse tree produced by AdaParser#delay_statement.
    def enterDelay_statement(self, ctx:AdaParser.Delay_statementContext):
        pass

    # Exit a parse tree produced by AdaParser#delay_statement.
    def exitDelay_statement(self, ctx:AdaParser.Delay_statementContext):
        pass


    # Enter a parse tree produced by AdaParser#select_statement.
    def enterSelect_statement(self, ctx:AdaParser.Select_statementContext):
        pass

    # Exit a parse tree produced by AdaParser#select_statement.
    def exitSelect_statement(self, ctx:AdaParser.Select_statementContext):
        pass


    # Enter a parse tree produced by AdaParser#select_alternative.
    def enterSelect_alternative(self, ctx:AdaParser.Select_alternativeContext):
        pass

    # Exit a parse tree produced by AdaParser#select_alternative.
    def exitSelect_alternative(self, ctx:AdaParser.Select_alternativeContext):
        pass


    # Enter a parse tree produced by AdaParser#accept_statement.
    def enterAccept_statement(self, ctx:AdaParser.Accept_statementContext):
        pass

    # Exit a parse tree produced by AdaParser#accept_statement.
    def exitAccept_statement(self, ctx:AdaParser.Accept_statementContext):
        pass


    # Enter a parse tree produced by AdaParser#expression.
    def enterExpression(self, ctx:AdaParser.ExpressionContext):
        pass

    # Exit a parse tree produced by AdaParser#expression.
    def exitExpression(self, ctx:AdaParser.ExpressionContext):
        pass


    # Enter a parse tree produced by AdaParser#primary.
    def enterPrimary(self, ctx:AdaParser.PrimaryContext):
        pass

    # Exit a parse tree produced by AdaParser#primary.
    def exitPrimary(self, ctx:AdaParser.PrimaryContext):
        pass


    # Enter a parse tree produced by AdaParser#literal.
    def enterLiteral(self, ctx:AdaParser.LiteralContext):
        pass

    # Exit a parse tree produced by AdaParser#literal.
    def exitLiteral(self, ctx:AdaParser.LiteralContext):
        pass


    # Enter a parse tree produced by AdaParser#identifier.
    def enterIdentifier(self, ctx:AdaParser.IdentifierContext):
        pass

    # Exit a parse tree produced by AdaParser#identifier.
    def exitIdentifier(self, ctx:AdaParser.IdentifierContext):
        pass


    # Enter a parse tree produced by AdaParser#integer_literal.
    def enterInteger_literal(self, ctx:AdaParser.Integer_literalContext):
        pass

    # Exit a parse tree produced by AdaParser#integer_literal.
    def exitInteger_literal(self, ctx:AdaParser.Integer_literalContext):
        pass


    # Enter a parse tree produced by AdaParser#real_literal.
    def enterReal_literal(self, ctx:AdaParser.Real_literalContext):
        pass

    # Exit a parse tree produced by AdaParser#real_literal.
    def exitReal_literal(self, ctx:AdaParser.Real_literalContext):
        pass


    # Enter a parse tree produced by AdaParser#string_literal.
    def enterString_literal(self, ctx:AdaParser.String_literalContext):
        pass

    # Exit a parse tree produced by AdaParser#string_literal.
    def exitString_literal(self, ctx:AdaParser.String_literalContext):
        pass


    # Enter a parse tree produced by AdaParser#logical_literal.
    def enterLogical_literal(self, ctx:AdaParser.Logical_literalContext):
        pass

    # Exit a parse tree produced by AdaParser#logical_literal.
    def exitLogical_literal(self, ctx:AdaParser.Logical_literalContext):
        pass



del AdaParser