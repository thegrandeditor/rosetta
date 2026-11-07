# Generated from Forth.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ForthParser import ForthParser
else:
    from ForthParser import ForthParser

# This class defines a complete listener for a parse tree produced by ForthParser.
class ForthListener(ParseTreeListener):

    # Enter a parse tree produced by ForthParser#program.
    def enterProgram(self, ctx:ForthParser.ProgramContext):
        pass

    # Exit a parse tree produced by ForthParser#program.
    def exitProgram(self, ctx:ForthParser.ProgramContext):
        pass


    # Enter a parse tree produced by ForthParser#element.
    def enterElement(self, ctx:ForthParser.ElementContext):
        pass

    # Exit a parse tree produced by ForthParser#element.
    def exitElement(self, ctx:ForthParser.ElementContext):
        pass


    # Enter a parse tree produced by ForthParser#definition.
    def enterDefinition(self, ctx:ForthParser.DefinitionContext):
        pass

    # Exit a parse tree produced by ForthParser#definition.
    def exitDefinition(self, ctx:ForthParser.DefinitionContext):
        pass


    # Enter a parse tree produced by ForthParser#if_stmt.
    def enterIf_stmt(self, ctx:ForthParser.If_stmtContext):
        pass

    # Exit a parse tree produced by ForthParser#if_stmt.
    def exitIf_stmt(self, ctx:ForthParser.If_stmtContext):
        pass


    # Enter a parse tree produced by ForthParser#do_loop.
    def enterDo_loop(self, ctx:ForthParser.Do_loopContext):
        pass

    # Exit a parse tree produced by ForthParser#do_loop.
    def exitDo_loop(self, ctx:ForthParser.Do_loopContext):
        pass


    # Enter a parse tree produced by ForthParser#begin_until.
    def enterBegin_until(self, ctx:ForthParser.Begin_untilContext):
        pass

    # Exit a parse tree produced by ForthParser#begin_until.
    def exitBegin_until(self, ctx:ForthParser.Begin_untilContext):
        pass


    # Enter a parse tree produced by ForthParser#stack_op.
    def enterStack_op(self, ctx:ForthParser.Stack_opContext):
        pass

    # Exit a parse tree produced by ForthParser#stack_op.
    def exitStack_op(self, ctx:ForthParser.Stack_opContext):
        pass


    # Enter a parse tree produced by ForthParser#literal.
    def enterLiteral(self, ctx:ForthParser.LiteralContext):
        pass

    # Exit a parse tree produced by ForthParser#literal.
    def exitLiteral(self, ctx:ForthParser.LiteralContext):
        pass


    # Enter a parse tree produced by ForthParser#call.
    def enterCall(self, ctx:ForthParser.CallContext):
        pass

    # Exit a parse tree produced by ForthParser#call.
    def exitCall(self, ctx:ForthParser.CallContext):
        pass



del ForthParser