# Generated from Forth.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ForthParser import ForthParser
else:
    from ForthParser import ForthParser

# This class defines a complete generic visitor for a parse tree produced by ForthParser.

class ForthVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ForthParser#program.
    def visitProgram(self, ctx:ForthParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ForthParser#element.
    def visitElement(self, ctx:ForthParser.ElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ForthParser#definition.
    def visitDefinition(self, ctx:ForthParser.DefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ForthParser#if_stmt.
    def visitIf_stmt(self, ctx:ForthParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ForthParser#do_loop.
    def visitDo_loop(self, ctx:ForthParser.Do_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ForthParser#begin_until.
    def visitBegin_until(self, ctx:ForthParser.Begin_untilContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ForthParser#stack_op.
    def visitStack_op(self, ctx:ForthParser.Stack_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ForthParser#literal.
    def visitLiteral(self, ctx:ForthParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ForthParser#call.
    def visitCall(self, ctx:ForthParser.CallContext):
        return self.visitChildren(ctx)



del ForthParser