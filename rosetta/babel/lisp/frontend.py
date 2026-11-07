from antlr4 import *
from rosetta.babel.lisp.grammar.LispLexer import LispLexer
from rosetta.babel.lisp.grammar.LispParser import LispParser
from rosetta.babel.lisp.grammar.LispVisitor import LispVisitor
from rosetta.babel.base.base import BabelFrontend
from rosetta.ir.nodes import *

class RosettaLispVisitor(LispVisitor):
    def visitProgram(self, ctx: LispParser.ProgramContext):
        body = []
        for expr in ctx.expression():
            res = self.visit(expr)
            if res:
                body.append(res)
        return Program(body=body)

    def visitExpression(self, ctx: LispParser.ExpressionContext):
        if ctx.atom():
            return self.visit(ctx.atom())
        if ctx.list_():
            return self.visit(ctx.list_())
        if ctx.quote():
            # For now, treat quote as a literal list or symbol
            return self.visit(ctx.quote())
        return None

    def visitAtom(self, ctx: LispParser.AtomContext):
        if ctx.number():
            val = ctx.number().getText()
            return Literal(value=float(val) if '.' in val else int(val))
        if ctx.string():
            return Literal(value=ctx.string().getText().strip('"'))
        if ctx.identifier():
            return Identifier(name=ctx.identifier().getText())
        return None

    def visitList(self, ctx: LispParser.ListContext):
        exprs = ctx.expression()
        if not exprs:
            return Literal(value=[])
        
        first = self.visit(exprs[0])
        if isinstance(first, Identifier):
            name = first.name.lower()
            if name == "defun":
                return self._handle_defun(exprs[1:])
            if name == "let" or name == "let*":
                return self._handle_let(exprs[1:])
            if name == "if":
                return self._handle_if(exprs[1:])
            if name == "when":
                return self._handle_if(exprs[1:]) # IF cond then (body...)
            if name == "unless":
                # IF (NOT cond) then (body...)
                cond = self.visit(exprs[1])
                body = [self.visit(e) for e in exprs[2:]]
                return IfStatement(condition=UnaryExpression(operator="not", argument=cond), consequent=body)
            if name == "cond":
                return self._handle_cond(exprs[1:])
            if name == "lambda":
                return self._handle_lambda(exprs[1:])
            if name == "defmacro":
                return self._handle_defmacro(exprs[1:])
            
            # Binary operations
            if name in ["+", "-", "*", "/", "=", "<", ">", "<=", ">="]:
                return self._handle_binary_op(name, exprs[1:])
            
            # Primitives
            if name in ["car", "cdr", "cons", "mapcar", "reduce", "apply"]:
                 return CallExpression(callee=Identifier(name=name), args=[self.visit(e) for e in exprs[1:]])
            
            # General function call
            return CallExpression(callee=first, args=[self.visit(e) for e in exprs[1:]])
            
        return CallExpression(callee=first, args=[self.visit(e) for e in exprs[1:]])

    def _handle_defun(self, args):
        name = self.visit(args[0]).name
        params_list = args[1].list_().expression()
        params = [Parameter(name=self.visit(p).name) for p in params_list]
        body = [self.visit(e) for e in args[2:]]
        return FunctionDeclaration(name=name, params=params, body=body)

    def _handle_let(self, args):
        bindings = args[0].list_().expression()
        nodes = []
        for b in bindings:
            # (var val)
            b_exprs = b.list_().expression()
            var = self.visit(b_exprs[0]).name
            val = self.visit(b_exprs[1])
            nodes.append(VariableDeclaration(name=var, initializer=val))
        
        body = [self.visit(e) for e in args[1:]]
        nodes.extend(body)
        return nodes

    def _handle_if(self, args):
        cond = self.visit(args[0])
        then_part = self.visit(args[1])
        else_part = self.visit(args[2]) if len(args) > 2 else None
        return IfStatement(condition=cond, consequent=[then_part], alternate=[else_part] if else_part else None)

    def _handle_cond(self, args):
        # cond ((c1 b1) (c2 b2) ...)
        # map to nested IfStatements
        if not args: return None
        clause = args[0].list_().expression()
        cond = self.visit(clause[0])
        body = [self.visit(e) for e in clause[1:]]
        
        alternate = self._handle_cond(args[1:])
        return IfStatement(condition=cond, consequent=body, alternate=[alternate] if alternate else None)

    def _handle_lambda(self, args):
        params_list = args[0].list_().expression()
        params = [Parameter(name=self.visit(p).name) for p in params_list]
        body = self.visit(args[1]) # Simplified
        return LambdaExpression(params=params, body=body)

    def _handle_defmacro(self, args):
        name = self.visit(args[0]).name
        params_list = args[1].list_().expression()
        params = [Parameter(name=self.visit(p).name) for p in params_list]
        body = self.visit(args[2])
        return MacroDeclaration(name=name, params=params, body=body)

    def _handle_binary_op(self, name, args):
        if len(args) < 2: return None
        left = self.visit(args[0])
        right = self.visit(args[1])
        # For LISP (+ 1 2 3) => nested binary ops
        res = BinaryExpression(left=left, operator=name, right=right)
        for i in range(2, len(args)):
            res = BinaryExpression(left=res, operator=name, right=self.visit(args[i]))
        return res

    def visitQuote(self, ctx: LispParser.QuoteContext):
        # Treat as literal
        return Literal(value=ctx.expression().getText())

class LispAntlrFrontend(BabelFrontend):
    @property
    def language_id(self) -> str:
        return "lisp"

    @property
    def supported_version(self) -> str:
        return "Common Lisp"

    @property
    def source_extensions(self) -> list[str]:
        return [".lisp", ".cl"]

    def parse(self, source_code: str) -> Program:
        input_stream = InputStream(source_code)
        lexer = LispLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = LispParser(stream)
        tree = parser.program()
        
        visitor = RosettaLispVisitor()
        return visitor.visit(tree)

LispFrontend = LispAntlrFrontend
