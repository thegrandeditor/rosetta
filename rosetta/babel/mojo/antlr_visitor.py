from antlr4 import *
from rosetta.babel.mojo.grammar.MojoParser import MojoParser
from rosetta.babel.mojo.grammar.MojoVisitor import MojoVisitor
from rosetta.ir.nodes import *

class RosettaMojoVisitor(MojoVisitor):
    def visitProgram(self, ctx: MojoParser.ProgramContext):
        body = []
        for elem in ctx.element():
            res = self.visit(elem)
            if res:
                if isinstance(res, list): body.extend(res)
                else: body.append(res)
        return Program(body=body)

    def visitElement(self, ctx: MojoParser.ElementContext):
        return self.visitChildren(ctx)

    def visitFunction_decl(self, ctx: MojoParser.Function_declContext):
        is_fn = ctx.getChild(len(ctx.decorator()) or 0).getText() == "fn"
        name = ctx.ID().getText()
        
        params = []
        if ctx.param_list():
            for p in ctx.param_list().parameter():
                p_name = p.ID().getText()
                p_type = p.type_name().getText() if p.type_name() else None
                # Check for parameter ownership/mode in parameter text
                mode = None
                p_text = p.getText()
                if p_text.startswith("owned"): mode = "owned"
                elif p_text.startswith("borrowed"): mode = "borrowed"
                elif p_text.startswith("inout"): mode = "inout"
                
                param = Parameter(name=p_name, type_hint=p_type)
                if mode:
                    param.metadata["mojo_mode"] = mode
                params.append(param)
                
        body = self.visit(ctx.block())
        ret_type = ctx.type_name().getText() if ctx.type_name() else None
        
        decorators = []
        for dec in ctx.decorator():
            decorators.append(Identifier(name=dec.ID().getText()))
            
        func = FunctionDeclaration(name=name, params=params, body=body, return_type=ret_type, decorators=decorators)
        func.metadata["is_mojo_fn"] = is_fn
        return func

    def visitDecorator(self, ctx: MojoParser.DecoratorContext):
        return Identifier(name=ctx.ID().getText())

    def visitStruct_decl(self, ctx: MojoParser.Struct_declContext):
        name = ctx.ID().getText()
        body = []
        for elem in ctx.struct_element():
            res = self.visit(elem)
            if res:
                if isinstance(res, list): body.extend(res)
                else: body.append(res)
        return MojoStructDeclaration(name=name, fields=body)

    def visitStruct_element(self, ctx: MojoParser.Struct_elementContext):
        return self.visitChildren(ctx)

    def visitVar_decl(self, ctx: MojoParser.Var_declContext):
        name = ctx.ID().getText()
        is_const = ctx.getChild(0).getText() == "let"
        type_hint = ctx.type_name().getText() if ctx.type_name() else None
        init = self.visit(ctx.expression()) if ctx.expression() else None
        return VariableDeclaration(name=name, type_hint=type_hint, initializer=init, is_const=is_const)

    def visitAssignment(self, ctx: MojoParser.AssignmentContext):
        target = Identifier(name=ctx.ID().getText())
        val = self.visit(ctx.expression())
        return Assignment(target=target, value=val)

    def visitType_name(self, ctx: MojoParser.Type_nameContext):
        return ctx.getText()

    def visitBlock(self, ctx: MojoParser.BlockContext):
        body = []
        for stmt in ctx.statement():
            res = self.visit(stmt)
            if res:
                if isinstance(res, list): body.extend(res)
                else: body.append(res)
        return body

    def visitStatement(self, ctx: MojoParser.StatementContext):
        return self.visitChildren(ctx)

    def visitIf_stmt(self, ctx: MojoParser.If_stmtContext):
        cond = self.visit(ctx.expression())
        conseq = self.visit(ctx.block(0))
        alt = None
        if ctx.block(1):
            alt = self.visit(ctx.block(1))
        return IfStatement(condition=cond, consequent=conseq, alternate=alt)

    def visitWhile_stmt(self, ctx: MojoParser.While_stmtContext):
        cond = self.visit(ctx.expression())
        body = self.visit(ctx.block())
        return WhileLoop(condition=cond, body=body)

    def visitReturn_stmt(self, ctx: MojoParser.Return_stmtContext):
        val = self.visit(ctx.expression()) if ctx.expression() else None
        return ReturnStatement(value=val)

    def visitExpression_stmt(self, ctx: MojoParser.Expression_stmtContext):
        return self.visit(ctx.expression())

    def visitExpression(self, ctx: MojoParser.ExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.primary())
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

    def visitPrimary(self, ctx: MojoParser.PrimaryContext):
        if ctx.ID():
            return Identifier(name=ctx.ID().getText())
        if ctx.NUMBER():
            return Literal(value=int(ctx.NUMBER().getText()) if ctx.NUMBER().getText().isdigit() else float(ctx.NUMBER().getText()))
        if ctx.STRING():
            return Literal(value=ctx.STRING().getText().strip('"\''))
        if ctx.getText() == 'true':
            return Literal(value=True)
        if ctx.getText() == 'false':
            return Literal(value=False)
        return None
