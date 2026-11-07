from antlr4 import *
from rosetta.babel.basic.grammar.BasicLexer import BasicLexer
from rosetta.babel.basic.grammar.BasicParser import BasicParser
from rosetta.babel.basic.grammar.BasicVisitor import BasicVisitor
from rosetta.babel.base.base import BabelFrontend
from rosetta.ir.nodes import *

class RosettaBasicVisitor(BasicVisitor):
    def visitProgram(self, ctx: BasicParser.ProgramContext):
        body = []
        for child in ctx.children:
            res = self.visit(child)
            if isinstance(res, list):
                body.extend(res)
            elif res:
                body.append(res)
        return Program(body=body)

    def visitLine(self, ctx: BasicParser.LineContext):
        nodes = []
        if ctx.INTEGER():
            nodes.append(Label(name=ctx.INTEGER().getText()))
        
        stmt = self.visit(ctx.statement())
        if stmt:
            if isinstance(stmt, list):
                nodes.extend(stmt)
            else:
                nodes.append(stmt)
        return nodes

    def visitLet_stmt(self, ctx: BasicParser.Let_stmtContext):
        target = Identifier(name=ctx.identifier().getText())
        value = self.visit(ctx.expression())
        return Assignment(target=target, value=value)

    def visitPrint_stmt(self, ctx: BasicParser.Print_stmtContext):
        args = [self.visit(e) for e in ctx.expression()]
        return CallExpression(callee=Identifier(name="print"), args=args)

    def visitInput_stmt(self, ctx: BasicParser.Input_stmtContext):
        # BASIC INPUT "Prompt"; A, B
        prompt = ctx.string_literal().getText().strip('"') if ctx.string_literal() else ""
        targets = [Identifier(name=id.getText()) for id in ctx.identifier()]
        # For simplicity, map to multiple assignments from an input() call
        nodes = []
        for target in targets:
             nodes.append(Assignment(target=target, value=CallExpression(callee=Identifier(name="input"), args=[Literal(value=prompt)])))
        return nodes

    def visitGoto_stmt(self, ctx: BasicParser.Goto_stmtContext):
        target = ctx.getChild(1).getText()
        return GotoStatement(label=target)

    def visitGosub_stmt(self, ctx: BasicParser.Gosub_stmtContext):
        target = ctx.getChild(1).getText()
        # GOSUB is like a call, but for simplicity we can use a special IR node or just CallExpression
        return CallExpression(callee=Identifier(name=f"GOSUB_{target}"), args=[])

    def visitReturn_stmt(self, ctx: BasicParser.Return_stmtContext):
        return ReturnStatement()

    def visitIf_stmt(self, ctx: BasicParser.If_stmtContext):
        cond = self.visit(ctx.expression())
        
        # Then part can be a statement or a line number
        then_part = ctx.getChild(3)
        if isinstance(then_part, BasicParser.StatementContext):
            consequent = [self.visit(then_part)]
        else: # Integer (line number)
            consequent = [GotoStatement(label=then_part.getText())]
            
        alternate = None
        if ctx.ELSE_K():
            else_part = ctx.getChild(5)
            if isinstance(else_part, BasicParser.StatementContext):
                alternate = [self.visit(else_part)]
            else:
                alternate = [GotoStatement(label=else_part.getText())]
        
        return IfStatement(condition=cond, consequent=consequent, alternate=alternate)

    def visitFor_stmt(self, ctx: BasicParser.For_stmtContext):
        var = ctx.identifier().getText()
        start = self.visit(ctx.expression(0))
        end = self.visit(ctx.expression(1))
        step = self.visit(ctx.expression(2)) if ctx.expression(2) else Literal(value=1)
        
        # BASIC loops are a bit tricky because NEXT is separate.
        # For now, we'll assume standard nested structure or use labels.
        # To handle NEXT, we might need a multi-pass or just a simple ForLoop for now.
        return ForLoop(
            initializer=Assignment(target=Identifier(name=var), value=start),
            condition=BinaryExpression(left=Identifier(name=var), operator="<=", right=end),
            increment=Assignment(target=Identifier(name=var), value=BinaryExpression(left=Identifier(name=var), operator="+", right=step)),
            body=[] # Body will be filled by subsequent lines until NEXT?
            # Actually, this is hard with flat line-based grammar.
            # Let's simplify and assume structured BASIC for now if possible,
            # or we need to handle this in HERMES.
        )

    def visitWhile_stmt(self, ctx: BasicParser.While_stmtContext):
        cond = self.visit(ctx.expression())
        return WhileLoop(condition=cond, body=[])

    def visitNext_stmt(self, ctx: BasicParser.Next_stmtContext):
        return Identifier(name="NEXT_MARKER")

    def visitWend_stmt(self, ctx: BasicParser.Wend_stmtContext):
        return Identifier(name="WEND_MARKER")

    def visitExpression(self, ctx: BasicParser.ExpressionContext):
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

    def visitPrimary(self, ctx: BasicParser.PrimaryContext):
        if ctx.identifier():
            name = ctx.identifier().getText()
            if ctx.expression():
                args = [self.visit(e) for e in ctx.expression()]
                return ArrayAccess(object=Identifier(name=name), index=args)
            return Identifier(name=name)
        return self.visit(ctx.literal())

    def visitLiteral(self, ctx: BasicParser.LiteralContext):
        if ctx.integer_literal():
            return Literal(value=int(ctx.integer_literal().getText()))
        if ctx.real_literal():
            return Literal(value=float(ctx.real_literal().getText()))
        if ctx.string_literal():
            return Literal(value=ctx.string_literal().getText().strip('"'))
        return None

class BasicAntlrFrontend(BabelFrontend):
    @property
    def language_id(self) -> str:
        return "basic"

    @property
    def supported_version(self) -> str:
        return "Classic / Structured BASIC"

    @property
    def source_extensions(self) -> list[str]:
        return [".bas"]

    def parse(self, source_code: str) -> Program:
        input_stream = InputStream(source_code.upper())
        lexer = BasicLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = BasicParser(stream)
        tree = parser.program()
        
        visitor = RosettaBasicVisitor()
        flat_program = visitor.visit(tree)
        
        # Restructure flat statements into nested blocks
        return self._restructure(flat_program)

    def _restructure(self, prog: Program) -> Program:
        final_body = []
        current_body = final_body
        stack = [] # (node, old_body_list)
        
        for node in prog.body:
            if isinstance(node, ForLoop):
                current_body.append(node)
                stack.append((node, current_body))
                current_body = node.body
            elif isinstance(node, WhileLoop):
                current_body.append(node)
                stack.append((node, current_body))
                current_body = node.body
            elif isinstance(node, Identifier) and node.name == "NEXT_MARKER":
                if stack and isinstance(stack[-1][0], ForLoop):
                    _, current_body = stack.pop()
                else:
                    current_body.append(node)
            elif isinstance(node, Identifier) and node.name == "WEND_MARKER":
                if stack and isinstance(stack[-1][0], WhileLoop):
                    _, current_body = stack.pop()
                else:
                    current_body.append(node)
            else:
                current_body.append(node)
        
        while stack:
            _, current_body = stack.pop()

        return Program(body=final_body)

BasicFrontend = BasicAntlrFrontend
