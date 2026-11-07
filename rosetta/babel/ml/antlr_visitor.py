from antlr4 import *
from rosetta.babel.ml.grammar.MLParser import MLParser
from rosetta.babel.ml.grammar.MLVisitor import MLVisitor
from rosetta.ir.nodes import *

class RosettaMLVisitor(MLVisitor):
    def visitProgram(self, ctx: MLParser.ProgramContext):
        body = []
        for child in ctx.children:
            res = self.visit(child)
            if res:
                if isinstance(res, list): body.extend(res)
                else: body.append(res)
        return Program(body=body)

    def visitVal_decl(self, ctx: MLParser.Val_declContext):
        pattern = self.visit(ctx.pattern())
        expr = self.visit(ctx.expr())
        if isinstance(pattern, Identifier):
            return MLValDeclaration(name=pattern.name, initializer=expr)
        return MLValDeclaration(name="_", pattern=pattern, initializer=expr)

    def visitFun_decl(self, ctx: MLParser.Fun_declContext):
        name = ctx.ID().getText()
        params = [Parameter(name=p.getText()) for p in ctx.param()]
        body = self.visit(ctx.expr())
        return MLFunDeclaration(name=name, params=params, body=[ReturnStatement(value=body)])

    def visitDatatype_decl(self, ctx: MLParser.Datatype_declContext):
        name = ctx.ID().getText()
        constructors = [self.visit(c) for c in ctx.constructor()]
        return MLDataTypeDeclaration(name=name, constructors=constructors)

    def visitConstructor(self, ctx: MLParser.ConstructorContext):
        name = ctx.ID().getText()
        types = [ctx.type_expr().getText()] if ctx.type_expr() else []
        return MLConstructor(name=name, types=types)

    def visitPrimaryExpr(self, ctx: MLParser.PrimaryExprContext):
        return self.visit(ctx.primary())

    def visitAppExpr(self, ctx: MLParser.AppExprContext):
        callee = self.visit(ctx.expr())
        arg = self.visit(ctx.primary())
        return CallExpression(callee=callee, args=[arg])

    def visitBinExpr(self, ctx: MLParser.BinExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.op.text
        return BinaryExpression(left=left, operator=op, right=right)

    def visitLetExpr(self, ctx: MLParser.LetExprContext):
        bindings = [self.visit(d) for d in ctx.declaration()]
        body = self.visit(ctx.expr())
        return MLLetExpression(bindings=bindings, body=body)

    def visitCaseExpr(self, ctx: MLParser.CaseExprContext):
        expr = self.visit(ctx.expr())
        branches = [self.visit(b) for b in ctx.branch()]
        return MLCaseExpression(expression=expr, branches=branches)

    def visitBranch(self, ctx: MLParser.BranchContext):
        pattern = self.visit(ctx.pattern())
        body = self.visit(ctx.expr())
        return MLCaseBranch(pattern=pattern, body=body)

    def visitIdPat(self, ctx: MLParser.IdPatContext):
        return Identifier(name=ctx.ID().getText())

    def visitLitPat(self, ctx: MLParser.LitPatContext):
        return self.visit(ctx.literal())

    def visitParenPat(self, ctx: MLParser.ParenPatContext):
        return self.visit(ctx.pattern())

    def visitTuplePat(self, ctx: MLParser.TuplePatContext):
        elements = [self.visit(p) for p in ctx.pattern()]
        return Literal(value=elements) # Map to list for now

    def visitConstrPat(self, ctx: MLParser.ConstrPatContext):
        name = ctx.ID().getText()
        arg = self.visit(ctx.pattern())
        return CallExpression(callee=Identifier(name=name), args=[arg])

    def visitPrimary(self, ctx: MLParser.PrimaryContext):
        if ctx.literal():
            return self.visit(ctx.literal())
        if ctx.ID():
            return Identifier(name=ctx.ID().getText())
        if ctx.expr():
            if len(ctx.expr()) > 1:
                # Tuple
                return Literal(value=[self.visit(e) for e in ctx.expr()])
            return self.visit(ctx.expr(0))
        return None

    def visitLiteral(self, ctx: MLParser.LiteralContext):
        text = ctx.getText()
        if text == "true": return Literal(value=True)
        if text == "false": return Literal(value=False)
        if text == "[]": return Literal(value=[])
        if ctx.NUMBER(): return Literal(value=int(text))
        if ctx.STRING(): return Literal(value=text.strip('"'))
        return None
