# Generated from Solidity.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SolidityParser import SolidityParser
else:
    from SolidityParser import SolidityParser

# This class defines a complete listener for a parse tree produced by SolidityParser.
class SolidityListener(ParseTreeListener):

    # Enter a parse tree produced by SolidityParser#program.
    def enterProgram(self, ctx:SolidityParser.ProgramContext):
        pass

    # Exit a parse tree produced by SolidityParser#program.
    def exitProgram(self, ctx:SolidityParser.ProgramContext):
        pass


    # Enter a parse tree produced by SolidityParser#source_unit.
    def enterSource_unit(self, ctx:SolidityParser.Source_unitContext):
        pass

    # Exit a parse tree produced by SolidityParser#source_unit.
    def exitSource_unit(self, ctx:SolidityParser.Source_unitContext):
        pass


    # Enter a parse tree produced by SolidityParser#pragma_directive.
    def enterPragma_directive(self, ctx:SolidityParser.Pragma_directiveContext):
        pass

    # Exit a parse tree produced by SolidityParser#pragma_directive.
    def exitPragma_directive(self, ctx:SolidityParser.Pragma_directiveContext):
        pass


    # Enter a parse tree produced by SolidityParser#import_directive.
    def enterImport_directive(self, ctx:SolidityParser.Import_directiveContext):
        pass

    # Exit a parse tree produced by SolidityParser#import_directive.
    def exitImport_directive(self, ctx:SolidityParser.Import_directiveContext):
        pass


    # Enter a parse tree produced by SolidityParser#contract_definition.
    def enterContract_definition(self, ctx:SolidityParser.Contract_definitionContext):
        pass

    # Exit a parse tree produced by SolidityParser#contract_definition.
    def exitContract_definition(self, ctx:SolidityParser.Contract_definitionContext):
        pass


    # Enter a parse tree produced by SolidityParser#interface_definition.
    def enterInterface_definition(self, ctx:SolidityParser.Interface_definitionContext):
        pass

    # Exit a parse tree produced by SolidityParser#interface_definition.
    def exitInterface_definition(self, ctx:SolidityParser.Interface_definitionContext):
        pass


    # Enter a parse tree produced by SolidityParser#library_definition.
    def enterLibrary_definition(self, ctx:SolidityParser.Library_definitionContext):
        pass

    # Exit a parse tree produced by SolidityParser#library_definition.
    def exitLibrary_definition(self, ctx:SolidityParser.Library_definitionContext):
        pass


    # Enter a parse tree produced by SolidityParser#id_list.
    def enterId_list(self, ctx:SolidityParser.Id_listContext):
        pass

    # Exit a parse tree produced by SolidityParser#id_list.
    def exitId_list(self, ctx:SolidityParser.Id_listContext):
        pass


    # Enter a parse tree produced by SolidityParser#contract_body_element.
    def enterContract_body_element(self, ctx:SolidityParser.Contract_body_elementContext):
        pass

    # Exit a parse tree produced by SolidityParser#contract_body_element.
    def exitContract_body_element(self, ctx:SolidityParser.Contract_body_elementContext):
        pass


    # Enter a parse tree produced by SolidityParser#state_variable_declaration.
    def enterState_variable_declaration(self, ctx:SolidityParser.State_variable_declarationContext):
        pass

    # Exit a parse tree produced by SolidityParser#state_variable_declaration.
    def exitState_variable_declaration(self, ctx:SolidityParser.State_variable_declarationContext):
        pass


    # Enter a parse tree produced by SolidityParser#event_definition.
    def enterEvent_definition(self, ctx:SolidityParser.Event_definitionContext):
        pass

    # Exit a parse tree produced by SolidityParser#event_definition.
    def exitEvent_definition(self, ctx:SolidityParser.Event_definitionContext):
        pass


    # Enter a parse tree produced by SolidityParser#modifier_definition.
    def enterModifier_definition(self, ctx:SolidityParser.Modifier_definitionContext):
        pass

    # Exit a parse tree produced by SolidityParser#modifier_definition.
    def exitModifier_definition(self, ctx:SolidityParser.Modifier_definitionContext):
        pass


    # Enter a parse tree produced by SolidityParser#function_definition.
    def enterFunction_definition(self, ctx:SolidityParser.Function_definitionContext):
        pass

    # Exit a parse tree produced by SolidityParser#function_definition.
    def exitFunction_definition(self, ctx:SolidityParser.Function_definitionContext):
        pass


    # Enter a parse tree produced by SolidityParser#constructor_definition.
    def enterConstructor_definition(self, ctx:SolidityParser.Constructor_definitionContext):
        pass

    # Exit a parse tree produced by SolidityParser#constructor_definition.
    def exitConstructor_definition(self, ctx:SolidityParser.Constructor_definitionContext):
        pass


    # Enter a parse tree produced by SolidityParser#mapping_declaration.
    def enterMapping_declaration(self, ctx:SolidityParser.Mapping_declarationContext):
        pass

    # Exit a parse tree produced by SolidityParser#mapping_declaration.
    def exitMapping_declaration(self, ctx:SolidityParser.Mapping_declarationContext):
        pass


    # Enter a parse tree produced by SolidityParser#key_type.
    def enterKey_type(self, ctx:SolidityParser.Key_typeContext):
        pass

    # Exit a parse tree produced by SolidityParser#key_type.
    def exitKey_type(self, ctx:SolidityParser.Key_typeContext):
        pass


    # Enter a parse tree produced by SolidityParser#type_name.
    def enterType_name(self, ctx:SolidityParser.Type_nameContext):
        pass

    # Exit a parse tree produced by SolidityParser#type_name.
    def exitType_name(self, ctx:SolidityParser.Type_nameContext):
        pass


    # Enter a parse tree produced by SolidityParser#visibility.
    def enterVisibility(self, ctx:SolidityParser.VisibilityContext):
        pass

    # Exit a parse tree produced by SolidityParser#visibility.
    def exitVisibility(self, ctx:SolidityParser.VisibilityContext):
        pass


    # Enter a parse tree produced by SolidityParser#mutability.
    def enterMutability(self, ctx:SolidityParser.MutabilityContext):
        pass

    # Exit a parse tree produced by SolidityParser#mutability.
    def exitMutability(self, ctx:SolidityParser.MutabilityContext):
        pass


    # Enter a parse tree produced by SolidityParser#event_param_list.
    def enterEvent_param_list(self, ctx:SolidityParser.Event_param_listContext):
        pass

    # Exit a parse tree produced by SolidityParser#event_param_list.
    def exitEvent_param_list(self, ctx:SolidityParser.Event_param_listContext):
        pass


    # Enter a parse tree produced by SolidityParser#event_param.
    def enterEvent_param(self, ctx:SolidityParser.Event_paramContext):
        pass

    # Exit a parse tree produced by SolidityParser#event_param.
    def exitEvent_param(self, ctx:SolidityParser.Event_paramContext):
        pass


    # Enter a parse tree produced by SolidityParser#param_list.
    def enterParam_list(self, ctx:SolidityParser.Param_listContext):
        pass

    # Exit a parse tree produced by SolidityParser#param_list.
    def exitParam_list(self, ctx:SolidityParser.Param_listContext):
        pass


    # Enter a parse tree produced by SolidityParser#parameter.
    def enterParameter(self, ctx:SolidityParser.ParameterContext):
        pass

    # Exit a parse tree produced by SolidityParser#parameter.
    def exitParameter(self, ctx:SolidityParser.ParameterContext):
        pass


    # Enter a parse tree produced by SolidityParser#storage_location.
    def enterStorage_location(self, ctx:SolidityParser.Storage_locationContext):
        pass

    # Exit a parse tree produced by SolidityParser#storage_location.
    def exitStorage_location(self, ctx:SolidityParser.Storage_locationContext):
        pass


    # Enter a parse tree produced by SolidityParser#block.
    def enterBlock(self, ctx:SolidityParser.BlockContext):
        pass

    # Exit a parse tree produced by SolidityParser#block.
    def exitBlock(self, ctx:SolidityParser.BlockContext):
        pass


    # Enter a parse tree produced by SolidityParser#statement.
    def enterStatement(self, ctx:SolidityParser.StatementContext):
        pass

    # Exit a parse tree produced by SolidityParser#statement.
    def exitStatement(self, ctx:SolidityParser.StatementContext):
        pass


    # Enter a parse tree produced by SolidityParser#expression_statement.
    def enterExpression_statement(self, ctx:SolidityParser.Expression_statementContext):
        pass

    # Exit a parse tree produced by SolidityParser#expression_statement.
    def exitExpression_statement(self, ctx:SolidityParser.Expression_statementContext):
        pass


    # Enter a parse tree produced by SolidityParser#if_statement.
    def enterIf_statement(self, ctx:SolidityParser.If_statementContext):
        pass

    # Exit a parse tree produced by SolidityParser#if_statement.
    def exitIf_statement(self, ctx:SolidityParser.If_statementContext):
        pass


    # Enter a parse tree produced by SolidityParser#for_statement.
    def enterFor_statement(self, ctx:SolidityParser.For_statementContext):
        pass

    # Exit a parse tree produced by SolidityParser#for_statement.
    def exitFor_statement(self, ctx:SolidityParser.For_statementContext):
        pass


    # Enter a parse tree produced by SolidityParser#while_statement.
    def enterWhile_statement(self, ctx:SolidityParser.While_statementContext):
        pass

    # Exit a parse tree produced by SolidityParser#while_statement.
    def exitWhile_statement(self, ctx:SolidityParser.While_statementContext):
        pass


    # Enter a parse tree produced by SolidityParser#return_statement.
    def enterReturn_statement(self, ctx:SolidityParser.Return_statementContext):
        pass

    # Exit a parse tree produced by SolidityParser#return_statement.
    def exitReturn_statement(self, ctx:SolidityParser.Return_statementContext):
        pass


    # Enter a parse tree produced by SolidityParser#emit_statement.
    def enterEmit_statement(self, ctx:SolidityParser.Emit_statementContext):
        pass

    # Exit a parse tree produced by SolidityParser#emit_statement.
    def exitEmit_statement(self, ctx:SolidityParser.Emit_statementContext):
        pass


    # Enter a parse tree produced by SolidityParser#variable_declaration_statement.
    def enterVariable_declaration_statement(self, ctx:SolidityParser.Variable_declaration_statementContext):
        pass

    # Exit a parse tree produced by SolidityParser#variable_declaration_statement.
    def exitVariable_declaration_statement(self, ctx:SolidityParser.Variable_declaration_statementContext):
        pass


    # Enter a parse tree produced by SolidityParser#expression.
    def enterExpression(self, ctx:SolidityParser.ExpressionContext):
        pass

    # Exit a parse tree produced by SolidityParser#expression.
    def exitExpression(self, ctx:SolidityParser.ExpressionContext):
        pass


    # Enter a parse tree produced by SolidityParser#argument_list.
    def enterArgument_list(self, ctx:SolidityParser.Argument_listContext):
        pass

    # Exit a parse tree produced by SolidityParser#argument_list.
    def exitArgument_list(self, ctx:SolidityParser.Argument_listContext):
        pass


    # Enter a parse tree produced by SolidityParser#primary.
    def enterPrimary(self, ctx:SolidityParser.PrimaryContext):
        pass

    # Exit a parse tree produced by SolidityParser#primary.
    def exitPrimary(self, ctx:SolidityParser.PrimaryContext):
        pass



del SolidityParser