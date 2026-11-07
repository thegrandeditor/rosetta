# Generated from rosetta/babel/smalltalk/grammar/Smalltalk.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SmalltalkParser import SmalltalkParser
else:
    from SmalltalkParser import SmalltalkParser

# This class defines a complete generic visitor for a parse tree produced by SmalltalkParser.

class SmalltalkVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SmalltalkParser#program.
    def visitProgram(self, ctx:SmalltalkParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmalltalkParser#executable_unit.
    def visitExecutable_unit(self, ctx:SmalltalkParser.Executable_unitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmalltalkParser#class_definition.
    def visitClass_definition(self, ctx:SmalltalkParser.Class_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmalltalkParser#method_definition.
    def visitMethod_definition(self, ctx:SmalltalkParser.Method_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmalltalkParser#expression.
    def visitExpression(self, ctx:SmalltalkParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmalltalkParser#assignment.
    def visitAssignment(self, ctx:SmalltalkParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmalltalkParser#cascade.
    def visitCascade(self, ctx:SmalltalkParser.CascadeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmalltalkParser#message_expression.
    def visitMessage_expression(self, ctx:SmalltalkParser.Message_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmalltalkParser#messages.
    def visitMessages(self, ctx:SmalltalkParser.MessagesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmalltalkParser#keyword_message.
    def visitKeyword_message(self, ctx:SmalltalkParser.Keyword_messageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmalltalkParser#binary_message.
    def visitBinary_message(self, ctx:SmalltalkParser.Binary_messageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmalltalkParser#unary_message.
    def visitUnary_message(self, ctx:SmalltalkParser.Unary_messageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmalltalkParser#primary.
    def visitPrimary(self, ctx:SmalltalkParser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmalltalkParser#block.
    def visitBlock(self, ctx:SmalltalkParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmalltalkParser#literal.
    def visitLiteral(self, ctx:SmalltalkParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmalltalkParser#number.
    def visitNumber(self, ctx:SmalltalkParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmalltalkParser#string_literal.
    def visitString_literal(self, ctx:SmalltalkParser.String_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmalltalkParser#symbol.
    def visitSymbol(self, ctx:SmalltalkParser.SymbolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmalltalkParser#array_literal.
    def visitArray_literal(self, ctx:SmalltalkParser.Array_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmalltalkParser#identifier.
    def visitIdentifier(self, ctx:SmalltalkParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmalltalkParser#keyword_selector.
    def visitKeyword_selector(self, ctx:SmalltalkParser.Keyword_selectorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmalltalkParser#binary_selector.
    def visitBinary_selector(self, ctx:SmalltalkParser.Binary_selectorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmalltalkParser#unary_selector.
    def visitUnary_selector(self, ctx:SmalltalkParser.Unary_selectorContext):
        return self.visitChildren(ctx)



del SmalltalkParser