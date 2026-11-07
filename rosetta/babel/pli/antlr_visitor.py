from antlr4 import *
from rosetta.babel.pli.grammar.PLIParser import PLIParser
from rosetta.babel.pli.grammar.PLIVisitor import PLIVisitor
from rosetta.ir.nodes import *

class RosettaPLIVisitor(PLIVisitor):
    def visitProgram(self, ctx: PLIParser.ProgramContext):
        body = []
        for child in ctx.children:
            res = self.visit(child)
            if res:
                if isinstance(res, list):
                    body.extend(res)
                else:
                    body.append(res)
        return Program(body=body)

    def visitDirective(self, ctx: PLIParser.DirectiveContext):
        # We can map compiler directives to specialized GlobalBlock or just ignore
        return None

    def visitProcedure_def(self, ctx: PLIParser.Procedure_defContext):
        name = "anonymous"
        parent = ctx.parentCtx # content_no_semi
        grandparent = parent.parentCtx # statement
        if isinstance(grandparent, PLIParser.StatementContext) and grandparent.label():
             name = grandparent.label().getText()

        params = []
        if ctx.params():
            params = [Parameter(name=p.getText()) for p in ctx.params().ID()]
            
        return_type = ctx.type_().getText() if ctx.RETURNS_K() else None
        
        body = []
        for stmt in ctx.statement():
            res = self.visit(stmt)
            if res:
                if isinstance(res, list):
                    body.extend(res)
                else:
                    body.append(res)
        
        return FunctionDeclaration(name=name, params=params, body=body, return_type=return_type)

    def visitStatement(self, ctx: PLIParser.StatementContext):
        nodes = []
        if ctx.label():
            nodes.append(Label(name=ctx.label().getText()))
        
        if ctx.content_no_semi():
            res = self.visit(ctx.content_no_semi())
        elif ctx.content_semi():
            res = self.visit(ctx.content_semi())
        elif ctx.entry_stmt():
            res = self.visit(ctx.entry_stmt())
        else:
            res = None

        if res:
            if isinstance(res, list):
                nodes.extend(res)
            else:
                nodes.append(res)
        return nodes

    def visitContent_no_semi(self, ctx: PLIParser.Content_no_semiContext):
        return self.visit(ctx.getChild(0))

    def visitContent_semi(self, ctx: PLIParser.Content_semiContext):
        return self.visit(ctx.getChild(0))

    def visitDeclare_stmt(self, ctx: PLIParser.Declare_stmtContext):
        nodes = []
        for decl in ctx.declaration():
            name = decl.ID().getText()
            type_hint = None
            dims = []
            init = None
            for attr in decl.attribute():
                if attr.type_():
                    type_hint = attr.type_().getText()
                elif attr.PICTURE_K():
                    type_hint = f"PICTURE {attr.STRING().getText()}"
                elif attr.TASK_K():
                    type_hint = "TASK"
                elif attr.getChildCount() > 1 and attr.getChild(0).getText() == '(':
                    # Dimensions
                    dims = [self.visit(e) for e in attr.expression()]
                elif attr.INIT_K():
                    init = self.visit(attr.expression(0))
            
            if dims:
                nodes.append(ArrayDeclaration(name=name, type_hint=type_hint, dimensions=dims, initializer=init))
            elif type_hint == "TASK":
                 nodes.append(TaskDeclaration(name=name, body=[])) # Simplified
            else:
                nodes.append(VariableDeclaration(name=name, type_hint=type_hint, initializer=init))
        return nodes

    def visitOn_stmt(self, ctx: PLIParser.On_stmtContext):
        cond = ctx.ID().getText()
        body = self.visit(ctx.statement())
        if not isinstance(body, list): body = [body]
        return OnCondition(condition=cond, body=body)

    def visitAllocate_stmt(self, ctx: PLIParser.Allocate_stmtContext):
        if ctx.ID(0):
            name = ctx.ID(0).getText()
        else:
            name = ctx.type_().getText()
        return MemoryAllocation(size=Literal(value=1), type_hint=name) # Simplified

    def visitFree_stmt(self, ctx: PLIParser.Free_stmtContext):
        return MemoryFree(argument=Identifier(name=ctx.ID().getText()))

    def visitDo_block(self, ctx: PLIParser.Do_blockContext):
        body = []
        for stmt in ctx.statement():
            res = self.visit(stmt)
            if res:
                if isinstance(res, list):
                    body.extend(res)
                else:
                    body.append(res)
        
        if ctx.do_spec():
            spec = ctx.do_spec()
            var = spec.ID().getText()
            start = self.visit(spec.expression(0))
            end = self.visit(spec.expression(1)) if len(spec.expression()) > 1 else None
            step = self.visit(spec.expression(2)) if len(spec.expression()) > 2 else Literal(value=1)
            
            if end:
                return ForLoop(
                    initializer=Assignment(target=Identifier(name=var), value=start),
                    condition=BinaryExpression(left=Identifier(name=var), operator="<=", right=end),
                    increment=Assignment(target=Identifier(name=var), value=BinaryExpression(left=Identifier(name=var), operator="+", right=step)),
                    body=body
                )
            else:
                return WhileLoop(condition=BinaryExpression(left=Identifier(name=var), operator="=", right=start), body=body)
        
        return body # Just a block

    def visitIf_stmt(self, ctx: PLIParser.If_stmtContext):
        cond = self.visit(ctx.expression())
        consequent = self.visit(ctx.statement(0))
        if not isinstance(consequent, list): consequent = [consequent]
        
        alternate = None
        if ctx.ELSE_K():
            alternate = self.visit(ctx.statement(1))
            if not isinstance(alternate, list): alternate = [alternate]
            
        return IfStatement(condition=cond, consequent=consequent, alternate=alternate)

    def visitCall_stmt(self, ctx: PLIParser.Call_stmtContext):
        name = ctx.ID().getText()
        args = []
        if ctx.args():
            args = [self.visit(e) for e in ctx.args().expression()]
        return CallExpression(callee=Identifier(name=name), args=args)

    def visitAssignment(self, ctx: PLIParser.AssignmentContext):
        return Assignment(target=self.visit(ctx.primary()), value=self.visit(ctx.expression()))

    def visitReturn_stmt(self, ctx: PLIParser.Return_stmtContext):
        val = self.visit(ctx.expression()) if ctx.expression() else None
        return ReturnStatement(value=val)

    def visitAction(self, ctx: PLIParser.ActionContext):
        name = "put" if ctx.PUT_K() else "get"
        args = []
        if ctx.args():
            args = [self.visit(e) for e in ctx.args().expression()]
        return CallExpression(callee=Identifier(name=name), args=args)

    def visitExpression(self, ctx: PLIParser.ExpressionContext):
        primaries = ctx.primary()
        if len(primaries) == 1:
            return self.visit(primaries[0])
        
        left = self.visit(primaries[0])
        for i in range(1, len(primaries)):
            op = ctx.operator(i-1).getText()
            right = self.visit(primaries[i])
            left = BinaryExpression(left=left, operator=op, right=right)
        return left

    def visitPrimary(self, ctx: PLIParser.PrimaryContext):
        if ctx.ID():
            name = ctx.ID().getText()
            if ctx.args():
                args = [self.visit(e) for e in ctx.args().expression()]
                # We'll treat it as ArrayAccess or CallExpression based on name if we had more info,
                # but ArrayAccess is safer for PL/I variables with parentheses.
                return ArrayAccess(object=Identifier(name=name), index=args)
            return Identifier(name=name)
        if ctx.STRING():
            return Literal(value=ctx.STRING().getText().strip("'"))
        if ctx.NUMBER():
            val = ctx.NUMBER().getText()
            return Literal(value=float(val) if '.' in val else int(val))
        if ctx.expression():
            return self.visit(ctx.expression())
        return None
