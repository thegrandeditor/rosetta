# Generated from Solidity.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SolidityParser import SolidityParser
else:
    from SolidityParser import SolidityParser

# This class defines a complete generic visitor for a parse tree produced by SolidityParser.

class SolidityVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SolidityParser#program.
    def visitProgram(self, ctx:SolidityParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityParser#source_unit.
    def visitSource_unit(self, ctx:SolidityParser.Source_unitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityParser#pragma_directive.
    def visitPragma_directive(self, ctx:SolidityParser.Pragma_directiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityParser#import_directive.
    def visitImport_directive(self, ctx:SolidityParser.Import_directiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityParser#contract_definition.
    def visitContract_definition(self, ctx:SolidityParser.Contract_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityParser#interface_definition.
    def visitInterface_definition(self, ctx:SolidityParser.Interface_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityParser#library_definition.
    def visitLibrary_definition(self, ctx:SolidityParser.Library_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityParser#id_list.
    def visitId_list(self, ctx:SolidityParser.Id_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityParser#contract_body_element.
    def visitContract_body_element(self, ctx:SolidityParser.Contract_body_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityParser#state_variable_declaration.
    def visitState_variable_declaration(self, ctx:SolidityParser.State_variable_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityParser#event_definition.
    def visitEvent_definition(self, ctx:SolidityParser.Event_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityParser#modifier_definition.
    def visitModifier_definition(self, ctx:SolidityParser.Modifier_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityParser#function_definition.
    def visitFunction_definition(self, ctx:SolidityParser.Function_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityParser#constructor_definition.
    def visitConstructor_definition(self, ctx:SolidityParser.Constructor_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityParser#mapping_declaration.
    def visitMapping_declaration(self, ctx:SolidityParser.Mapping_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityParser#key_type.
    def visitKey_type(self, ctx:SolidityParser.Key_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityParser#type_name.
    def visitType_name(self, ctx:SolidityParser.Type_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityParser#visibility.
    def visitVisibility(self, ctx:SolidityParser.VisibilityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityParser#mutability.
    def visitMutability(self, ctx:SolidityParser.MutabilityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityParser#event_param_list.
    def visitEvent_param_list(self, ctx:SolidityParser.Event_param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityParser#event_param.
    def visitEvent_param(self, ctx:SolidityParser.Event_paramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityParser#param_list.
    def visitParam_list(self, ctx:SolidityParser.Param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityParser#parameter.
    def visitParameter(self, ctx:SolidityParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityParser#storage_location.
    def visitStorage_location(self, ctx:SolidityParser.Storage_locationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityParser#block.
    def visitBlock(self, ctx:SolidityParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityParser#statement.
    def visitStatement(self, ctx:SolidityParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityParser#expression_statement.
    def visitExpression_statement(self, ctx:SolidityParser.Expression_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityParser#if_statement.
    def visitIf_statement(self, ctx:SolidityParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityParser#for_statement.
    def visitFor_statement(self, ctx:SolidityParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityParser#while_statement.
    def visitWhile_statement(self, ctx:SolidityParser.While_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityParser#return_statement.
    def visitReturn_statement(self, ctx:SolidityParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityParser#emit_statement.
    def visitEmit_statement(self, ctx:SolidityParser.Emit_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityParser#variable_declaration_statement.
    def visitVariable_declaration_statement(self, ctx:SolidityParser.Variable_declaration_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityParser#expression.
    def visitExpression(self, ctx:SolidityParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityParser#argument_list.
    def visitArgument_list(self, ctx:SolidityParser.Argument_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityParser#primary.
    def visitPrimary(self, ctx:SolidityParser.PrimaryContext):
        return self.visitChildren(ctx)



del SolidityParser