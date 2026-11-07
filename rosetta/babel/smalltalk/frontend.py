from antlr4 import *
from rosetta.babel.smalltalk.grammar.SmalltalkLexer import SmalltalkLexer
from rosetta.babel.smalltalk.grammar.SmalltalkParser import SmalltalkParser
from rosetta.babel.smalltalk.grammar.SmalltalkVisitor import SmalltalkVisitor
from rosetta.babel.base.base import BabelFrontend
from rosetta.ir.nodes import *

class RosettaSmalltalkVisitor(SmalltalkVisitor):
    def visitProgram(self, ctx: SmalltalkParser.ProgramContext):
        body = []
        for unit in ctx.executable_unit():
            res = self.visit(unit)
            if isinstance(res, list): body.extend(res)
            elif res: body.append(res)
        return Program(body=body)

    def visitExecutable_unit(self, ctx: SmalltalkParser.Executable_unitContext):
        if ctx.class_definition():
            return self.visit(ctx.class_definition())
        if ctx.expression():
            return self.visit(ctx.expression())
        return None

    def visitClass_definition(self, ctx: SmalltalkParser.Class_definitionContext):
        super_class = ctx.identifier(0).getText()
        name_ctx = ctx.getChild(2)
        name = self.visit(name_ctx).name if hasattr(self.visit(name_ctx), 'name') else name_ctx.getText().strip('#')
        methods = [self.visit(m) for m in ctx.method_definition()]
        return ClassDeclaration(name=name, bases=[super_class], body=methods)

    def visitMethod_definition(self, ctx: SmalltalkParser.Method_definitionContext):
        name_ctx = ctx.getChild(0)
        class_name = self.visit(name_ctx).name if hasattr(self.visit(name_ctx), 'name') else name_ctx.getText().strip('#')
        selector = ctx.getChild(1).getText().replace(':', '_')
        body_node = self.visit(ctx.block())
        return MethodDeclaration(name=f"{class_name}_{selector}", params=body_node.params if isinstance(body_node, LambdaExpression) else [], body=body_node.body if isinstance(body_node, LambdaExpression) else [body_node])

    def visitExpression(self, ctx: SmalltalkParser.ExpressionContext):
        if ctx.assignment(): return self.visit(ctx.assignment())
        if ctx.cascade(): return self.visit(ctx.cascade())
        if ctx.message_expression(): return self.visit(ctx.message_expression())
        return None

    def visitCascade(self, ctx: SmalltalkParser.CascadeContext):
        receiver = self.visit(ctx.message_expression())
        # In Smalltalk, a cascade returns the receiver or the result of the last message?
        # Actually, it sends messages to the same receiver.
        # We can map it to a sequence of statements or nested calls if they return receiver.
        # For simplicity, let's return a list of calls if we're in a statement context.
        # But IR CallExpression returns a single node.
        # Let's map it to a sequence of calls.
        
        # We need a way to refer to the receiver without re-evaluating it.
        # For now, let's just emit them as separate calls.
        nodes = [receiver]
        for msg_ctx in ctx.messages():
             # The receiver for each message in the cascade is the same as the first one.
             # But the 'receiver' here might already have some messages applied.
             # Wait, Smalltalk cascade: (receiver msg1) msg2; msg3 => msg2 and msg3 are sent to the result of (receiver msg1)? 
             # No, 'a b; c' is 'a b' then 'a c'.
             
             # Re-extract the true receiver of the message_expression
             true_receiver = self.visit(ctx.message_expression().primary())
             nodes.append(self._handle_message(true_receiver, msg_ctx))
        return nodes

    def visitAssignment(self, ctx: SmalltalkParser.AssignmentContext):
        target = Identifier(name=ctx.identifier().getText())
        value = self.visit(ctx.expression())
        return Assignment(target=target, value=value)

    def visitMessage_expression(self, ctx: SmalltalkParser.Message_expressionContext):
        receiver = self.visit(ctx.primary())
        for msg_ctx in ctx.messages():
            receiver = self._handle_message(receiver, msg_ctx)
        return receiver

    def _handle_message(self, receiver, ctx: SmalltalkParser.MessagesContext):
        if ctx.keyword_message():
            return self._handle_keyword_message(receiver, ctx.keyword_message())
        if ctx.binary_message():
            return self._handle_binary_message(receiver, ctx.binary_message())
        if ctx.unary_message():
            return self._handle_unary_message(receiver, ctx.unary_message())
        return receiver

    def _handle_keyword_message(self, receiver, ctx: SmalltalkParser.Keyword_messageContext):
        keywords = [k.getText() for k in ctx.KEYWORD()]
        args = [self.visit(e) for e in ctx.expression()]
        selector = "".join(keywords)
        
        if selector == "ifTrue:":
            return IfStatement(condition=receiver, consequent=self._extract_block_body(args[0]))
        if selector == "ifFalse:":
            return IfStatement(condition=UnaryExpression(operator="not", argument=receiver), consequent=self._extract_block_body(args[0]))
        if selector == "ifTrue:ifFalse:":
            return IfStatement(condition=receiver, consequent=self._extract_block_body(args[0]), alternate=self._extract_block_body(args[1]))
        if selector == "whileTrue:":
             return WhileLoop(condition=receiver, body=self._extract_block_body(args[0]))
        if selector == "transcript:show:" or selector == "show:":
             return CallExpression(callee=Identifier(name="print"), args=args)
        
        return CallExpression(callee=MemberAccess(object=receiver, member=selector.replace(':', '_')), args=args)

    def _handle_binary_message(self, receiver, ctx: SmalltalkParser.Binary_messageContext):
        op = ctx.BINARY_SELECTOR().getText()
        right = self.visit(ctx.primary())
        return BinaryExpression(left=receiver, operator=op, right=right)

    def _handle_unary_message(self, receiver, ctx: SmalltalkParser.Unary_messageContext):
        name = ctx.identifier().getText()
        return CallExpression(callee=MemberAccess(object=receiver, member=name), args=[])

    def _extract_block_body(self, node):
        if isinstance(node, LambdaExpression):
            return node.body if isinstance(node.body, list) else [node.body]
        return [node]

    def visitBlock(self, ctx: SmalltalkParser.BlockContext):
        params = [Parameter(name=id.getText()) for id in ctx.identifier()]
        body = [self.visit(e) for e in ctx.expression()]
        return LambdaExpression(params=params, body=body)

    def visitPrimary(self, ctx: SmalltalkParser.PrimaryContext):
        if ctx.identifier(): return Identifier(name=ctx.identifier().getText())
        if ctx.literal(): return self.visit(ctx.literal())
        if ctx.block(): return self.visit(ctx.block())
        if ctx.expression(): return self.visit(ctx.expression())
        return None

    def visitLiteral(self, ctx: SmalltalkParser.LiteralContext):
        if ctx.number():
            val = ctx.number().getText()
            return Literal(value=float(val) if '.' in val else int(val))
        if ctx.string_literal():
            return Literal(value=ctx.string_literal().getText().strip("'"))
        if ctx.symbol():
            return Identifier(name=ctx.symbol().getText().strip('#'))
        return None

    def visitSymbol(self, ctx: SmalltalkParser.SymbolContext):
        return Identifier(name=ctx.getText().strip('#'))

class SmalltalkAntlrFrontend(BabelFrontend):
    @property
    def language_id(self) -> str:
        return "smalltalk"

    @property
    def supported_version(self) -> str:
        return "ANSI Smalltalk"

    @property
    def source_extensions(self) -> list[str]:
        return [".st"]

    def parse(self, source_code: str) -> Program:
        input_stream = InputStream(source_code)
        lexer = SmalltalkLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = SmalltalkParser(stream)
        tree = parser.program()
        
        visitor = RosettaSmalltalkVisitor()
        return visitor.visit(tree)

SmalltalkFrontend = SmalltalkAntlrFrontend
