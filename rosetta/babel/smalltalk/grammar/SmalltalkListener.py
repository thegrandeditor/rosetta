# Generated from rosetta/babel/smalltalk/grammar/Smalltalk.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SmalltalkParser import SmalltalkParser
else:
    from SmalltalkParser import SmalltalkParser

# This class defines a complete listener for a parse tree produced by SmalltalkParser.
class SmalltalkListener(ParseTreeListener):

    # Enter a parse tree produced by SmalltalkParser#program.
    def enterProgram(self, ctx:SmalltalkParser.ProgramContext):
        pass

    # Exit a parse tree produced by SmalltalkParser#program.
    def exitProgram(self, ctx:SmalltalkParser.ProgramContext):
        pass


    # Enter a parse tree produced by SmalltalkParser#executable_unit.
    def enterExecutable_unit(self, ctx:SmalltalkParser.Executable_unitContext):
        pass

    # Exit a parse tree produced by SmalltalkParser#executable_unit.
    def exitExecutable_unit(self, ctx:SmalltalkParser.Executable_unitContext):
        pass


    # Enter a parse tree produced by SmalltalkParser#class_definition.
    def enterClass_definition(self, ctx:SmalltalkParser.Class_definitionContext):
        pass

    # Exit a parse tree produced by SmalltalkParser#class_definition.
    def exitClass_definition(self, ctx:SmalltalkParser.Class_definitionContext):
        pass


    # Enter a parse tree produced by SmalltalkParser#method_definition.
    def enterMethod_definition(self, ctx:SmalltalkParser.Method_definitionContext):
        pass

    # Exit a parse tree produced by SmalltalkParser#method_definition.
    def exitMethod_definition(self, ctx:SmalltalkParser.Method_definitionContext):
        pass


    # Enter a parse tree produced by SmalltalkParser#expression.
    def enterExpression(self, ctx:SmalltalkParser.ExpressionContext):
        pass

    # Exit a parse tree produced by SmalltalkParser#expression.
    def exitExpression(self, ctx:SmalltalkParser.ExpressionContext):
        pass


    # Enter a parse tree produced by SmalltalkParser#assignment.
    def enterAssignment(self, ctx:SmalltalkParser.AssignmentContext):
        pass

    # Exit a parse tree produced by SmalltalkParser#assignment.
    def exitAssignment(self, ctx:SmalltalkParser.AssignmentContext):
        pass


    # Enter a parse tree produced by SmalltalkParser#cascade.
    def enterCascade(self, ctx:SmalltalkParser.CascadeContext):
        pass

    # Exit a parse tree produced by SmalltalkParser#cascade.
    def exitCascade(self, ctx:SmalltalkParser.CascadeContext):
        pass


    # Enter a parse tree produced by SmalltalkParser#message_expression.
    def enterMessage_expression(self, ctx:SmalltalkParser.Message_expressionContext):
        pass

    # Exit a parse tree produced by SmalltalkParser#message_expression.
    def exitMessage_expression(self, ctx:SmalltalkParser.Message_expressionContext):
        pass


    # Enter a parse tree produced by SmalltalkParser#messages.
    def enterMessages(self, ctx:SmalltalkParser.MessagesContext):
        pass

    # Exit a parse tree produced by SmalltalkParser#messages.
    def exitMessages(self, ctx:SmalltalkParser.MessagesContext):
        pass


    # Enter a parse tree produced by SmalltalkParser#keyword_message.
    def enterKeyword_message(self, ctx:SmalltalkParser.Keyword_messageContext):
        pass

    # Exit a parse tree produced by SmalltalkParser#keyword_message.
    def exitKeyword_message(self, ctx:SmalltalkParser.Keyword_messageContext):
        pass


    # Enter a parse tree produced by SmalltalkParser#binary_message.
    def enterBinary_message(self, ctx:SmalltalkParser.Binary_messageContext):
        pass

    # Exit a parse tree produced by SmalltalkParser#binary_message.
    def exitBinary_message(self, ctx:SmalltalkParser.Binary_messageContext):
        pass


    # Enter a parse tree produced by SmalltalkParser#unary_message.
    def enterUnary_message(self, ctx:SmalltalkParser.Unary_messageContext):
        pass

    # Exit a parse tree produced by SmalltalkParser#unary_message.
    def exitUnary_message(self, ctx:SmalltalkParser.Unary_messageContext):
        pass


    # Enter a parse tree produced by SmalltalkParser#primary.
    def enterPrimary(self, ctx:SmalltalkParser.PrimaryContext):
        pass

    # Exit a parse tree produced by SmalltalkParser#primary.
    def exitPrimary(self, ctx:SmalltalkParser.PrimaryContext):
        pass


    # Enter a parse tree produced by SmalltalkParser#block.
    def enterBlock(self, ctx:SmalltalkParser.BlockContext):
        pass

    # Exit a parse tree produced by SmalltalkParser#block.
    def exitBlock(self, ctx:SmalltalkParser.BlockContext):
        pass


    # Enter a parse tree produced by SmalltalkParser#literal.
    def enterLiteral(self, ctx:SmalltalkParser.LiteralContext):
        pass

    # Exit a parse tree produced by SmalltalkParser#literal.
    def exitLiteral(self, ctx:SmalltalkParser.LiteralContext):
        pass


    # Enter a parse tree produced by SmalltalkParser#number.
    def enterNumber(self, ctx:SmalltalkParser.NumberContext):
        pass

    # Exit a parse tree produced by SmalltalkParser#number.
    def exitNumber(self, ctx:SmalltalkParser.NumberContext):
        pass


    # Enter a parse tree produced by SmalltalkParser#string_literal.
    def enterString_literal(self, ctx:SmalltalkParser.String_literalContext):
        pass

    # Exit a parse tree produced by SmalltalkParser#string_literal.
    def exitString_literal(self, ctx:SmalltalkParser.String_literalContext):
        pass


    # Enter a parse tree produced by SmalltalkParser#symbol.
    def enterSymbol(self, ctx:SmalltalkParser.SymbolContext):
        pass

    # Exit a parse tree produced by SmalltalkParser#symbol.
    def exitSymbol(self, ctx:SmalltalkParser.SymbolContext):
        pass


    # Enter a parse tree produced by SmalltalkParser#array_literal.
    def enterArray_literal(self, ctx:SmalltalkParser.Array_literalContext):
        pass

    # Exit a parse tree produced by SmalltalkParser#array_literal.
    def exitArray_literal(self, ctx:SmalltalkParser.Array_literalContext):
        pass


    # Enter a parse tree produced by SmalltalkParser#identifier.
    def enterIdentifier(self, ctx:SmalltalkParser.IdentifierContext):
        pass

    # Exit a parse tree produced by SmalltalkParser#identifier.
    def exitIdentifier(self, ctx:SmalltalkParser.IdentifierContext):
        pass


    # Enter a parse tree produced by SmalltalkParser#keyword_selector.
    def enterKeyword_selector(self, ctx:SmalltalkParser.Keyword_selectorContext):
        pass

    # Exit a parse tree produced by SmalltalkParser#keyword_selector.
    def exitKeyword_selector(self, ctx:SmalltalkParser.Keyword_selectorContext):
        pass


    # Enter a parse tree produced by SmalltalkParser#binary_selector.
    def enterBinary_selector(self, ctx:SmalltalkParser.Binary_selectorContext):
        pass

    # Exit a parse tree produced by SmalltalkParser#binary_selector.
    def exitBinary_selector(self, ctx:SmalltalkParser.Binary_selectorContext):
        pass


    # Enter a parse tree produced by SmalltalkParser#unary_selector.
    def enterUnary_selector(self, ctx:SmalltalkParser.Unary_selectorContext):
        pass

    # Exit a parse tree produced by SmalltalkParser#unary_selector.
    def exitUnary_selector(self, ctx:SmalltalkParser.Unary_selectorContext):
        pass



del SmalltalkParser