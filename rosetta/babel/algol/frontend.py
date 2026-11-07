from antlr4 import *
from rosetta.babel.algol.grammar.AlgolLexer import AlgolLexer
from rosetta.babel.algol.grammar.AlgolParser import AlgolParser
from rosetta.babel.algol.grammar.AlgolVisitor import AlgolVisitor
from rosetta.babel.base.base import BabelFrontend
from rosetta.ir.nodes import *

class RosettaAlgolVisitor(AlgolVisitor):
    def visitProgram(self, ctx: AlgolParser.ProgramContext):
        return Program(body=self.visit(ctx.block()))

    def visitBlock(self, ctx: AlgolParser.BlockContext):
        body = []
        if ctx.declaration_list():
            body.extend(self.visit(ctx.declaration_list()))
        if ctx.statement_list():
            body.extend(self.visit(ctx.statement_list()))
        # Map block to a ModuleDeclaration or just a list of nodes
        # In ALGOL, blocks are also scopes.
        return body

    def visitDeclaration_list(self, ctx: AlgolParser.Declaration_listContext):
        nodes = []
        for decl in ctx.declaration():
            res = self.visit(decl)
            if isinstance(res, list): nodes.extend(res)
            elif res: nodes.append(res)
        return nodes

    def visitType_declaration(self, ctx: AlgolParser.Type_declarationContext):
        type_hint = ctx.type_hint().getText()
        ids = ctx.identifier()
        return [VariableDeclaration(name=id.getText(), type_hint=type_hint) for id in ids]

    def visitOwn_declaration(self, ctx: AlgolParser.Own_declarationContext):
        decls = self.visit(ctx.type_declaration())
        for d in decls:
            d.metadata["is_static"] = True
        return decls

    def visitProcedure_declaration(self, ctx: AlgolParser.Procedure_declarationContext):
        name = ctx.identifier().getText()
        params = []
        if ctx.formal_parameter_list():
            params = [Parameter(name=id.getText()) for id in ctx.formal_parameter_list().identifier()]
        body = self.visit(ctx.statement())
        return FunctionDeclaration(name=name, params=params, body=[body] if not isinstance(body, list) else body)

    def visitStatement_list(self, ctx: AlgolParser.Statement_listContext):
        nodes = []
        for stmt in ctx.statement():
            res = self.visit(stmt)
            if res:
                nodes.append(res)
        return nodes

    def visitStatement(self, ctx: AlgolParser.StatementContext):
        if ctx.getChildCount() == 0: return None
        return self.visit(ctx.getChild(0))

    def visitAssignment_statement(self, ctx: AlgolParser.Assignment_statementContext):
        target = Identifier(name=ctx.identifier().getText())
        value = self.visit(ctx.expression())
        return Assignment(target=target, value=value)

    def visitProcedure_call(self, ctx: AlgolParser.Procedure_callContext):
        name = ctx.identifier().getText()
        args = [self.visit(e) for e in ctx.expression()]
        if name.lower() in ["outstring", "outreal", "print"]:
             return CallExpression(callee=Identifier(name="print"), args=args)
        return CallExpression(callee=Identifier(name=name), args=args)

    def visitIf_statement(self, ctx: AlgolParser.If_statementContext):
        cond = self.visit(ctx.expression())
        consequent = [self.visit(ctx.statement(0))]
        alternate = [self.visit(ctx.statement(1))] if ctx.ELSE_K() else None
        return IfStatement(condition=cond, consequent=consequent, alternate=alternate)

    def visitFor_statement(self, ctx: AlgolParser.For_statementContext):
        var = ctx.identifier().getText()
        start = self.visit(ctx.expression(0))
        step = self.visit(ctx.expression(1))
        limit = self.visit(ctx.expression(2))
        body = self.visit(ctx.statement())
        return ForLoop(
            initializer=Assignment(target=Identifier(name=var), value=start),
            condition=BinaryExpression(left=Identifier(name=var), operator="<=", right=limit),
            increment=Assignment(target=Identifier(name=var), value=BinaryExpression(left=Identifier(name=var), operator="+", right=step)),
            body=[body] if not isinstance(body, list) else body
        )

    def visitWhile_statement(self, ctx: AlgolParser.While_statementContext):
        cond = self.visit(ctx.expression())
        body = self.visit(ctx.statement())
        return WhileLoop(condition=cond, body=[body] if not isinstance(body, list) else body)

    def visitExpression(self, ctx: AlgolParser.ExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.primary())
        if ctx.getChildCount() == 3:
            if ctx.getChild(0).getText() == '(':
                return self.visit(ctx.expression(0))
            left = self.visit(ctx.expression(0))
            op = ctx.getChild(1).getText()
            right = self.visit(ctx.expression(1))
            return BinaryExpression(left=left, operator=op, right=right)
        return self.visit(ctx.primary())

    def visitPrimary(self, ctx: AlgolParser.PrimaryContext):
        if ctx.identifier():
            name = ctx.identifier().getText()
            if ctx.expression():
                args = [self.visit(e) for e in ctx.expression()]
                return CallExpression(callee=Identifier(name=name), args=args)
            return Identifier(name=name)
        return self.visit(ctx.literal())

    def visitLiteral(self, ctx: AlgolParser.LiteralContext):
        if ctx.integer_literal():
            return Literal(value=int(ctx.integer_literal().getText()))
        if ctx.real_literal():
            return Literal(value=float(ctx.real_literal().getText()))
        if ctx.string_literal():
            return Literal(value=ctx.string_literal().getText().strip('"'))
        if ctx.logical_literal():
            return Literal(value=ctx.logical_literal().getText().upper() == 'TRUE')
        return None

class AlgolAntlrFrontend(BabelFrontend):
    @property
    def language_id(self) -> str:
        return "algol"

    @property
    def supported_version(self) -> str:
        return "ALGOL 60"

    @property
    def source_extensions(self) -> list[str]:
        return [".alg"]

    def parse(self, source_code: str) -> Program:
        input_stream = InputStream(source_code.upper())
        lexer = AlgolLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = AlgolParser(stream)
        tree = parser.program()
        
        visitor = RosettaAlgolVisitor()
        return visitor.visit(tree)

AlgolFrontend = AlgolAntlrFrontend
