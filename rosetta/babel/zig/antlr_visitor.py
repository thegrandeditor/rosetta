from antlr4 import *
from rosetta.babel.zig.grammar.ZigParser import ZigParser
from rosetta.babel.zig.grammar.ZigVisitor import ZigVisitor
from rosetta.ir.nodes import *

class RosettaZigVisitor(ZigVisitor):
    def visitProgram(self, ctx: ZigParser.ProgramContext):
        body = []
        for elem in ctx.element():
            res = self.visit(elem)
            if res:
                if isinstance(res, list): body.extend(res)
                else: body.append(res)
        return Program(body=body)

    def visitElement(self, ctx: ZigParser.ElementContext):
        return self.visitChildren(ctx)

    def visitFunction_decl(self, ctx: ZigParser.Function_declContext):
        name = ctx.ID().getText()
        params = []
        if ctx.param_list():
            for p in ctx.param_list().parameter():
                p_name = p.ID().getText()
                p_type = p.type_name().getText()
                params.append(Parameter(name=p_name, type_hint=p_type))
                
        body = self.visit(ctx.block())
        ret_type = ctx.type_name().getText() if ctx.type_name() else None
        
        func = FunctionDeclaration(name=name, params=params, body=body, return_type=ret_type)
        if ctx.getText().find("inline") != -1:
            func.metadata["is_inline"] = True
        return func

    def visitStruct_decl(self, ctx: ZigParser.Struct_declContext):
        # ANTLR grammar defines struct_decl: ( 'pub' )? ( 'packed' | 'extern' )? 'struct' '{' struct_element* '}'
        # So we can construct a StructDeclaration
        body = []
        for elem in ctx.struct_element():
            res = self.visit(elem)
            if res:
                if isinstance(res, list): body.extend(res)
                else: body.append(res)
                
        struct = StructDeclaration(name="AnonymousStruct", fields=body)
        if ctx.getText().find("packed") != -1:
            struct.metadata["is_packed"] = True
        elif ctx.getText().find("extern") != -1:
            struct.metadata["is_extern"] = True
        return struct

    def visitStruct_element(self, ctx: ZigParser.Struct_elementContext):
        return self.visitChildren(ctx)

    def visitVar_decl(self, ctx: ZigParser.Var_declContext):
        name = ctx.ID().getText()
        is_const = ctx.getText().find("const") != -1
        type_hint = ctx.type_name().getText() if ctx.type_name() else None
        init = self.visit(ctx.expression()) if ctx.expression() else None
        return VariableDeclaration(name=name, type_hint=type_hint, initializer=init, is_const=is_const)

    def visitAssignment(self, ctx: ZigParser.AssignmentContext):
        target = Identifier(name=ctx.ID().getText())
        val = self.visit(ctx.expression())
        return Assignment(target=target, value=val)

    def visitBlock(self, ctx: ZigParser.BlockContext):
        body = []
        for stmt in ctx.statement():
            res = self.visit(stmt)
            if res:
                if isinstance(res, list): body.extend(res)
                else: body.append(res)
        return body

    def visitStatement(self, ctx: ZigParser.StatementContext):
        return self.visitChildren(ctx)

    def visitIf_stmt(self, ctx: ZigParser.If_stmtContext):
        cond = self.visit(ctx.expression())
        conseq = self.visit(ctx.statement(0))
        if not isinstance(conseq, list): conseq = [conseq]
        alt = None
        if ctx.statement(1):
            alt = self.visit(ctx.statement(1))
            if not isinstance(alt, list): alt = [alt]
        return IfStatement(condition=cond, consequent=conseq, alternate=alt)

    def visitWhile_stmt(self, ctx: ZigParser.While_stmtContext):
        cond = self.visit(ctx.expression())
        body = self.visit(ctx.statement())
        if not isinstance(body, list): body = [body]
        loop = WhileLoop(condition=cond, body=body)
        if ctx.getText().find("inline") != -1:
            loop.metadata["is_inline"] = True
        return loop

    def visitFor_stmt(self, ctx: ZigParser.For_stmtContext):
        # Zig for loops can be mapped to ForInLoop
        # for (items) |item| { ... }
        expr = self.visit(ctx.expression())
        body = self.visit(ctx.statement())
        if not isinstance(body, list): body = [body]
        
        loop = ForInLoop(iterator=Identifier(name="item"), iterable=expr, body=body)
        if ctx.getText().find("inline") != -1:
            loop.metadata["is_inline"] = True
        return loop

    def visitReturn_stmt(self, ctx: ZigParser.Return_stmtContext):
        val = self.visit(ctx.expression()) if ctx.expression() else None
        return ReturnStatement(value=val)

    def visitDefer_stmt(self, ctx: ZigParser.Defer_stmtContext):
        is_err = ctx.getChild(0).getText() == "errdefer"
        stmt = self.visit(ctx.statement())
        body = stmt if isinstance(stmt, list) else [stmt]
        return DeferStatement(body=body, is_errdefer=is_err)

    def visitExpression_stmt(self, ctx: ZigParser.Expression_stmtContext):
        return self.visit(ctx.expression())

    def visitExpression(self, ctx: ZigParser.ExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.primary())
        if ctx.getChild(0).getText() == "try":
            expr = self.visit(ctx.expression(0))
            return CallExpression(callee=Identifier(name="try"), args=[expr])
        if ctx.getChild(0).getText() == "comptime":
            expr = self.visit(ctx.expression(0))
            return ComptimeExpression(expression=expr)
        if ctx.getChild(1).getText() == "catch":
            left = self.visit(ctx.expression(0))
            right = self.visit(ctx.expression(1))
            return BinaryExpression(left=left, operator="catch", right=right)
        if ctx.getChildCount() == 4 and ctx.getChild(1).getText() == '(':
            callee = self.visit(ctx.expression(0))
            args = []
            if ctx.argument_list():
                args = [self.visit(arg) for arg in ctx.argument_list().expression()]
            return CallExpression(callee=callee, args=args)
        if ctx.getChildCount() == 3:
            left = self.visit(ctx.expression(0))
            op = ctx.getChild(1).getText()
            right = self.visit(ctx.expression(1))
            return BinaryExpression(left=left, operator=op, right=right)
        return None

    def visitPrimary(self, ctx: ZigParser.PrimaryContext):
        if ctx.ID():
            return Identifier(name=ctx.ID().getText())
        if ctx.NUMBER():
            return Literal(value=int(ctx.NUMBER().getText()))
        if ctx.STRING():
            return Literal(value=ctx.STRING().getText().strip('"\''))
        if ctx.getText() == 'true':
            return Literal(value=True)
        if ctx.getText() == 'false':
            return Literal(value=False)
        if ctx.getText().startswith("@import"):
            # Import call
            return CallExpression(callee=Identifier(name="@import"), args=[Literal(value=ctx.STRING().getText().strip('"\''))])
        return None
