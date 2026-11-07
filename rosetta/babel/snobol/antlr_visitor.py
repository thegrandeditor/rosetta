from antlr4 import *
from rosetta.babel.snobol.grammar.Snobol4Parser import Snobol4Parser
from rosetta.babel.snobol.grammar.Snobol4Visitor import Snobol4Visitor
from rosetta.ir.nodes import *

class RosettaSnobolVisitor(Snobol4Visitor):
    def visitProgram(self, ctx: Snobol4Parser.ProgramContext):
        body = []
        for child in ctx.children:
            res = self.visit(child)
            if res:
                if isinstance(res, list):
                    body.extend(res)
                else:
                    body.append(res)
        return Program(body=body)

    def visitLine(self, ctx: Snobol4Parser.LineContext):
        if ctx.COMMENT():
            return None # Ignore comments for IR for now, or could map to a Comment node if we had one
        if ctx.statement():
            return self.visit(ctx.statement())
        return None

    def visitStatement(self, ctx: Snobol4Parser.StatementContext):
        label = ctx.label().getText() if ctx.label() else None
        content = self.visit(ctx.content()) if ctx.content() else None
        transfer = self.visit(ctx.transfer()) if ctx.transfer() else None
        return SNOBOLStatement(label=label, content=content, transfer=transfer)

    def visitContent(self, ctx: Snobol4Parser.ContentContext):
        return self.visit(ctx.getChild(0))

    def visitAssignment(self, ctx: Snobol4Parser.AssignmentContext):
        return Assignment(
            target=self.visit(ctx.subject()),
            value=self.visit(ctx.expression())
        )

    def visitPatternMatch(self, ctx: Snobol4Parser.PatternMatchContext):
        return PatternMatchStatement(
            subject=self.visit(ctx.subject()),
            pattern=self.visit(ctx.pattern()),
            replacement=self.visit(ctx.replacement()) if ctx.replacement() else None
        )

    def visitTransfer(self, ctx: Snobol4Parser.TransferContext):
        return self.visit(ctx.transfer_dest())

    def visitTransfer_dest(self, ctx: Snobol4Parser.Transfer_destContext):
        if ctx.direct_goto():
            return SNOBOLTransfer(unconditional_label=ctx.direct_goto().getText())
        return self.visit(ctx.conditional_gotos())

    def visitConditional_gotos(self, ctx: Snobol4Parser.Conditional_gotosContext):
        success = None
        failure = None
        if ctx.success_goto():
            success = ctx.success_goto(0).ID().getText()
        if ctx.failure_goto():
            failure = ctx.failure_goto(0).ID().getText()
        return SNOBOLTransfer(success_label=success, failure_label=failure)

    def visitExpression(self, ctx: Snobol4Parser.ExpressionContext):
        return self.visit(ctx.alternation_expr())

    def visitAlternation_expr(self, ctx: Snobol4Parser.Alternation_exprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.concatenation_expr(0))
        
        left = self.visit(ctx.concatenation_expr(0))
        for i in range(1, len(ctx.concatenation_expr())):
            right = self.visit(ctx.concatenation_expr(i))
            left = BinaryExpression(left=left, operator="|", right=right)
        return left

    def visitConcatenation_expr(self, ctx: Snobol4Parser.Concatenation_exprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.capture_expr(0))
        
        left = self.visit(ctx.capture_expr(0))
        for i in range(1, len(ctx.capture_expr())):
            right = self.visit(ctx.capture_expr(i))
            left = BinaryExpression(left=left, operator=" ", right=right)
        return left

    def visitCapture_expr(self, ctx: Snobol4Parser.Capture_exprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.additive_expr())
        
        children = [c for c in ctx.children if not isinstance(c, TerminalNode) or c.getText().strip()]
        left = self.visit(children[0])
        for i in range(1, len(children), 2):
            op = children[i].getText()
            right = Identifier(name=children[i+1].getText())
            left = BinaryExpression(left=left, operator=op, right=right)
        return left

    def visitAdditive_expr(self, ctx: Snobol4Parser.Additive_exprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.multiplicative_expr(0))
        
        children = [c for c in ctx.children if not isinstance(c, TerminalNode) or c.getText().strip()]
        left = self.visit(children[0])
        for i in range(1, len(children), 2):
            op = children[i].getText()
            right = self.visit(children[i+1])
            left = BinaryExpression(left=left, operator=op, right=right)
        return left

    def visitMultiplicative_expr(self, ctx: Snobol4Parser.Multiplicative_exprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.primary(0))
        
        children = [c for c in ctx.children if not isinstance(c, TerminalNode) or c.getText().strip()]
        left = self.visit(children[0])
        for i in range(1, len(children), 2):
            op = children[i].getText()
            right = self.visit(children[i+1])
            left = BinaryExpression(left=left, operator=op, right=right)
        return left

    def visitArray_access(self, ctx: Snobol4Parser.Array_accessContext):
        name = ctx.ID().getText()
        indices = [self.visit(e) for e in ctx.expression()]
        return ArrayAccess(object=Identifier(name=name), index=indices)

    def visitPrimary(self, ctx: Snobol4Parser.PrimaryContext):
        if ctx.ID():
            return Identifier(name=ctx.ID().getText())
        if ctx.STRING():
            return Literal(value=ctx.STRING().getText().strip("'\""))
        if ctx.NUMBER():
            return Literal(value=int(ctx.NUMBER().getText()))
        if ctx.expression():
            return self.visit(ctx.expression())
        if ctx.function_call():
            return self.visit(ctx.function_call())
        if ctx.unary_expr():
            return self.visit(ctx.unary_expr())
        if ctx.array_access():
            return self.visit(ctx.array_access())
        return None

    def visitUnary_expr(self, ctx: Snobol4Parser.Unary_exprContext):
        op = ctx.getChild(0).getText()
        arg = self.visit(ctx.primary())
        return UnaryExpression(operator=op, argument=arg)

    def visitFunction_call(self, ctx: Snobol4Parser.Function_callContext):
        name = ctx.ID().getText()
        args = [self.visit(e) for e in ctx.expression()]
        return CallExpression(callee=Identifier(name=name), args=args)
