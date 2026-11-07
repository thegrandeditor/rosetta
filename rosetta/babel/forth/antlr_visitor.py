from antlr4 import *
from rosetta.babel.forth.grammar.ForthParser import ForthParser
from rosetta.babel.forth.grammar.ForthVisitor import ForthVisitor
from rosetta.ir.nodes import *

class RosettaForthVisitor(ForthVisitor):
    def visitProgram(self, ctx: ForthParser.ProgramContext):
        body = []
        for child in ctx.element():
            res = self.visit(child)
            if res:
                if isinstance(res, list): body.extend(res)
                else: body.append(res)
        return Program(body=body)

    def visitDefinition(self, ctx: ForthParser.DefinitionContext):
        name = ctx.name.text
        body = []
        for child in ctx.body:
            res = self.visit(child)
            if res:
                if isinstance(res, list): body.extend(res)
                else: body.append(res)
        return ForthWordDefinition(name=name, params=[], body=body)

    def visitIf_stmt(self, ctx: ForthParser.If_stmtContext):
        consequent = []
        for child in ctx.consequent:
            res = self.visit(child)
            if res:
                if isinstance(res, list): consequent.extend(res)
                else: consequent.append(res)
        
        alternate = None
        if ctx.alternate:
            alternate = []
            for child in ctx.alternate:
                res = self.visit(child)
                if res:
                    if isinstance(res, list): alternate.extend(res)
                    else: alternate.append(res)
        
        # In Forth, IF pops the top of stack.
        # We can map it to an IfStatement with a pseudo-condition
        return IfStatement(condition=ForthStackOp(operation="POP"), consequent=consequent, alternate=alternate)

    def visitDo_loop(self, ctx: ForthParser.Do_loopContext):
        body = []
        for child in ctx.body:
            res = self.visit(child)
            if res:
                if isinstance(res, list): body.extend(res)
                else: body.append(res)
        return ForLoop(initializer=None, condition=None, increment=None, body=body)

    def visitBegin_until(self, ctx: ForthParser.Begin_untilContext):
        body = []
        for child in ctx.body:
            res = self.visit(child)
            if res:
                if isinstance(res, list): body.extend(res)
                else: body.append(res)
        return WhileLoop(condition=ForthStackOp(operation="POP"), body=body)

    def visitStack_op(self, ctx: ForthParser.Stack_opContext):
        return ForthStackOp(operation=ctx.op.text)

    def visitLiteral(self, ctx: ForthParser.LiteralContext):
        return Literal(value=int(ctx.val.text))

    def visitCall(self, ctx: ForthParser.CallContext):
        return CallExpression(callee=Identifier(name=ctx.name.text), args=[])
