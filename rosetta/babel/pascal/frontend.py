from antlr4 import *
from rosetta.babel.pascal.grammar.PascalLexer import PascalLexer
from rosetta.babel.pascal.grammar.PascalParser import PascalParser
from rosetta.babel.pascal.grammar.PascalVisitor import PascalVisitor
from rosetta.babel.base.base import BabelFrontend
from rosetta.ir.nodes import *

class RosettaPascalVisitor(PascalVisitor):
    def visitProgram(self, ctx: PascalParser.ProgramContext):
        body = self.visit(ctx.block())
        return Program(body=body if isinstance(body, list) else [body])

    def visitBlock(self, ctx: PascalParser.BlockContext):
        nodes = []
        if ctx.declaration_part():
            nodes.extend(self.visit(ctx.declaration_part()))
        nodes.extend(self.visit(ctx.statement_part()))
        return nodes

    def visitDeclaration_part(self, ctx: PascalParser.Declaration_partContext):
        nodes = []
        for child in ctx.children:
            res = self.visit(child)
            if isinstance(res, list):
                nodes.extend(res)
            elif res:
                nodes.append(res)
        return nodes

    def visitVar_decl_part(self, ctx: PascalParser.Var_decl_partContext):
        nodes = []
        for decl in ctx.var_decl():
            nodes.extend(self.visit(decl))
        return nodes

    def visitVar_decl(self, ctx: PascalParser.Var_declContext):
        type_spec = self.visit(ctx.type_spec())
        ids = ctx.identifier()
        nodes = []
        for id in ids:
            if isinstance(type_spec, (ArrayDeclaration, RecordDeclaration)):
                # Clone for each identifier
                import copy
                node = copy.deepcopy(type_spec)
                node.name = id.getText()
                nodes.append(node)
            else:
                nodes.append(VariableDeclaration(name=id.getText(), type_hint=str(type_spec)))
        return nodes

    def visitType_decl_part(self, ctx: PascalParser.Type_decl_partContext):
        nodes = []
        for td in ctx.type_decl():
            nodes.append(self.visit(td))
        return nodes

    def visitType_decl(self, ctx: PascalParser.Type_declContext):
        name = ctx.identifier().getText()
        type_spec = self.visit(ctx.type_spec())
        if isinstance(type_spec, RecordDeclaration):
            type_spec.name = name
            return type_spec
        elif isinstance(type_spec, ArrayDeclaration):
            type_spec.name = name
            return type_spec
        return VariableDeclaration(name=name, type_hint=str(type_spec))

    def visitType_spec(self, ctx: PascalParser.Type_specContext):
        if ctx.ARRAY_K():
            dims = [self.visit(r) for r in ctx.range()]
            base_type = self.visit(ctx.type_spec())
            return ArrayDeclaration(name="", type_hint=str(base_type), dimensions=dims)
        elif ctx.RECORD_K():
            fields = []
            if ctx.field_list():
                for vd in ctx.field_list().var_decl():
                    fields.extend(self.visit(vd))
            return RecordDeclaration(name="", fields=fields)
        return ctx.getText()

    def visitRange(self, ctx: PascalParser.RangeContext):
        return BinaryExpression(left=self.visit(ctx.expression(0)), operator="..", right=self.visit(ctx.expression(1)))

    def visitWith_stmt(self, ctx: PascalParser.With_stmtContext):
        objects = [Identifier(name=id.getText()) for id in ctx.identifier()]
        body = self.visit(ctx.statement())
        return WithStatement(objects=objects, body=[body] if not isinstance(body, list) else body)

    def visitProcedure_decl(self, ctx: PascalParser.Procedure_declContext):
        name = ctx.identifier().getText()
        params = self.visit(ctx.formal_parameter_list()) if ctx.formal_parameter_list() else []
        body = self.visit(ctx.block())
        return FunctionDeclaration(name=name, params=params, body=body)

    def visitFunction_decl(self, ctx: PascalParser.Function_declContext):
        name = ctx.identifier().getText()
        params = self.visit(ctx.formal_parameter_list()) if ctx.formal_parameter_list() else []
        ret_type = ctx.identifier(1).getText()
        body = self.visit(ctx.block())
        return FunctionDeclaration(name=name, params=params, body=body, return_type=ret_type)

    def visitFormal_parameter_list(self, ctx: PascalParser.Formal_parameter_listContext):
        params = []
        for fp in ctx.formal_parameter():
            params.extend(self.visit(fp))
        return params

    def visitFormal_parameter(self, ctx: PascalParser.Formal_parameterContext):
        ids = ctx.identifier()
        type_hint = ids[-1].getText()
        return [Parameter(name=id.getText(), type_hint=type_hint) for id in ids[:-1]]

    def visitStatement_part(self, ctx: PascalParser.Statement_partContext):
        nodes = []
        for stmt in ctx.statement():
            res = self.visit(stmt)
            if res:
                nodes.append(res)
        return nodes

    def visitStatement(self, ctx: PascalParser.StatementContext):
        if ctx.getChildCount() == 0: return None
        return self.visit(ctx.getChild(0))

    def visitAssignment_stmt(self, ctx: PascalParser.Assignment_stmtContext):
        target = Identifier(name=ctx.identifier().getText())
        value = self.visit(ctx.expression())
        return Assignment(target=target, value=value)

    def visitProcedure_call(self, ctx: PascalParser.Procedure_callContext):
        name = ctx.identifier().getText()
        args = [self.visit(e) for e in ctx.expression()]
        if name.lower() in ["writeln", "write"]:
             return CallExpression(callee=Identifier(name="print"), args=args)
        return CallExpression(callee=Identifier(name=name), args=args)

    def visitIf_stmt(self, ctx: PascalParser.If_stmtContext):
        cond = self.visit(ctx.expression())
        consequent = self.visit(ctx.statement(0))
        alternate = self.visit(ctx.statement(1)) if ctx.ELSE_K() else None
        return IfStatement(
            condition=cond,
            consequent=[consequent] if not isinstance(consequent, list) else consequent,
            alternate=[alternate] if alternate and not isinstance(alternate, list) else (alternate if isinstance(alternate, list) else None)
        )

    def visitFor_stmt(self, ctx: PascalParser.For_stmtContext):
        var = ctx.identifier().getText()
        start = self.visit(ctx.expression(0))
        end = self.visit(ctx.expression(1))
        body = self.visit(ctx.statement())
        return ForLoop(
            initializer=Assignment(target=Identifier(name=var), value=start),
            condition=BinaryExpression(left=Identifier(name=var), operator="<=", right=end),
            increment=Assignment(target=Identifier(name=var), value=BinaryExpression(left=Identifier(name=var), operator="+", right=Literal(value=1))),
            body=[body] if not isinstance(body, list) else body
        )

    def visitWhile_stmt(self, ctx: PascalParser.While_stmtContext):
        cond = self.visit(ctx.expression())
        body = self.visit(ctx.statement())
        return WhileLoop(condition=cond, body=[body] if not isinstance(body, list) else body)

    def visitRepeat_stmt(self, ctx: PascalParser.Repeat_stmtContext):
        # Maps REPEAT ... UNTIL cond to a WhileLoop or a special DoWhile if we had one
        # For now, let's use WhileLoop(True) with an IF at the end for simplicity
        body = []
        for stmt in ctx.statement():
            body.append(self.visit(stmt))
        cond = self.visit(ctx.expression())
        # repeat until cond => while not cond
        return WhileLoop(condition=UnaryExpression(operator="not", argument=cond), body=body)

    def visitExpression(self, ctx: PascalParser.ExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.primary())
        if ctx.getChildCount() == 3:
            if ctx.getChild(0).getText() == '(':
                return self.visit(ctx.expression(0))
            left = self.visit(ctx.expression(0))
            op = ctx.getChild(1).getText()
            right = self.visit(ctx.expression(1))
            return BinaryExpression(left=left, operator=op, right=right)
        if ctx.getChildCount() == 2:
            op = ctx.getChild(0).getText()
            arg = self.visit(ctx.expression(0))
            return UnaryExpression(operator=op, argument=arg)
        return None

    def visitPrimary(self, ctx: PascalParser.PrimaryContext):
        if ctx.identifier():
            name = ctx.identifier(0).getText()
            if ctx.getChildCount() > 1:
                if ctx.getChild(1).getText() == '(':
                    args = [self.visit(e) for e in ctx.expression()]
                    return CallExpression(callee=Identifier(name=name), args=args)
                if ctx.getChild(1).getText() == '.':
                    return RecordAccess(object=Identifier(name=name), field=ctx.identifier(1).getText())
            return Identifier(name=name)
        return self.visit(ctx.literal())

    def visitLiteral(self, ctx: PascalParser.LiteralContext):
        if ctx.integer_literal():
            return Literal(value=int(ctx.integer_literal().getText()))
        if ctx.real_literal():
            return Literal(value=float(ctx.real_literal().getText()))
        if ctx.string_literal():
            return Literal(value=ctx.string_literal().getText().strip("'"))
        if ctx.logical_literal():
            return Literal(value=ctx.logical_literal().getText().upper() == 'TRUE')
        return None

class PascalAntlrFrontend(BabelFrontend):
    @property
    def language_id(self) -> str:
        return "pascal"

    @property
    def supported_version(self) -> str:
        return "Standard Pascal"

    @property
    def source_extensions(self) -> list[str]:
        return [".pas"]

    def parse(self, source_code: str) -> Program:
        input_stream = InputStream(source_code.upper())
        lexer = PascalLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = PascalParser(stream)
        tree = parser.program()
        
        visitor = RosettaPascalVisitor()
        return visitor.visit(tree)

PascalFrontend = PascalAntlrFrontend
