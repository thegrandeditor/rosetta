from antlr4 import *
from rosetta.babel.carbon.grammar.CarbonParser import CarbonParser
from rosetta.babel.carbon.grammar.CarbonVisitor import CarbonVisitor
from rosetta.ir.nodes import *

class RosettaCarbonVisitor(CarbonVisitor):
    def visitProgram(self, ctx: CarbonParser.ProgramContext):
        body = []
        for elem in ctx.element():
            res = self.visit(elem)
            if res:
                if isinstance(res, list):
                    body.extend(res)
                else:
                    body.append(res)
        return Program(body=body)

    def visitElement(self, ctx: CarbonParser.ElementContext):
        return self.visitChildren(ctx)

    def visitPackage_decl(self, ctx: CarbonParser.Package_declContext):
        name = ctx.ID().getText()
        # Map Carbon packages to ModuleDeclarations
        return ModuleDeclaration(name=name, body=[])

    def visitFunction_decl(self, ctx: CarbonParser.Function_declContext):
        name = ctx.ID().getText()
        params = []
        if ctx.param_list():
            for p in ctx.param_list().parameter():
                p_name = p.ID().getText()
                p_type = p.type_name().getText()
                params.append(Parameter(name=p_name, type_hint=p_type))
        
        body = self.visit(ctx.block()) if ctx.block() else []
        ret_type = ctx.type_name().getText() if ctx.type_name() else None
        
        # Determine if this function declaration is within a class or is a method
        return FunctionDeclaration(name=name, params=params, body=body, return_type=ret_type)

    def visitClass_decl(self, ctx: CarbonParser.Class_declContext):
        name = ctx.ID().getText()
        body = []
        for elem in ctx.class_element():
            res = self.visit(elem)
            if res:
                if isinstance(res, list):
                    body.extend(res)
                else:
                    body.append(res)
        return ClassDeclaration(name=name, body=body)

    def visitClass_element(self, ctx: CarbonParser.Class_elementContext):
        return self.visitChildren(ctx)

    def visitInterface_decl(self, ctx: CarbonParser.Interface_declContext):
        name = ctx.ID().getText()
        body = []
        for elem in ctx.interface_element():
            res = self.visit(elem)
            if res:
                if isinstance(res, list):
                    body.extend(res)
                else:
                    body.append(res)
        return InterfaceDeclaration(name=name, body=body)

    def visitInterface_element(self, ctx: CarbonParser.Interface_elementContext):
        return self.visitChildren(ctx)

    def visitImpl_decl(self, ctx: CarbonParser.Impl_declContext):
        # impl target_type as interface_name
        target_type = ctx.type_name(0).getText()
        interface_name = ctx.type_name(1).getText()
        body = []
        for elem in ctx.class_element():
            res = self.visit(elem)
            if res:
                if isinstance(res, list):
                    body.extend(res)
                else:
                    body.append(res)
        return ImplDeclaration(interface_name=interface_name, target_type=target_type, body=body)

    def visitVar_decl(self, ctx: CarbonParser.Var_declContext):
        name = ctx.ID().getText()
        is_const = ctx.getChild(0).getText() == "let"
        type_hint = ctx.type_name().getText() if ctx.type_name() else None
        init = self.visit(ctx.expression()) if ctx.expression() else None
        return VariableDeclaration(name=name, type_hint=type_hint, initializer=init, is_const=is_const)

    def visitAssignment(self, ctx: CarbonParser.AssignmentContext):
        target = Identifier(name=ctx.ID().getText())
        val = self.visit(ctx.expression())
        return Assignment(target=target, value=val)

    def visitBlock(self, ctx: CarbonParser.BlockContext):
        body = []
        for stmt in ctx.statement():
            res = self.visit(stmt)
            if res:
                if isinstance(res, list):
                    body.extend(res)
                else:
                    body.append(res)
        return body

    def visitStatement(self, ctx: CarbonParser.StatementContext):
        return self.visitChildren(ctx)

    def visitIf_stmt(self, ctx: CarbonParser.If_stmtContext):
        cond = self.visit(ctx.expression())
        conseq = self.visit(ctx.statement(0))
        if not isinstance(conseq, list):
            conseq = [conseq]
        alt = None
        if ctx.statement(1):
            alt = self.visit(ctx.statement(1))
            if not isinstance(alt, list):
                alt = [alt]
        return IfStatement(condition=cond, consequent=conseq, alternate=alt)

    def visitWhile_stmt(self, ctx: CarbonParser.While_stmtContext):
        cond = self.visit(ctx.expression())
        body = self.visit(ctx.statement())
        if not isinstance(body, list):
            body = [body]
        return WhileLoop(condition=cond, body=body)

    def visitReturn_stmt(self, ctx: CarbonParser.Return_stmtContext):
        val = self.visit(ctx.expression()) if ctx.expression() else None
        return ReturnStatement(value=val)

    def visitMatch_stmt(self, ctx: CarbonParser.Match_stmtContext):
        expr = self.visit(ctx.expression())
        branches = []
        for case in ctx.match_case():
            branches.append(self.visit(case))
        return MLCaseExpression(expression=expr, branches=branches)

    def visitMatch_case(self, ctx: CarbonParser.Match_caseContext):
        pattern = self.visit(ctx.expression())
        stmt = self.visit(ctx.statement())
        if isinstance(stmt, list):
            stmt = stmt[0] if stmt else None
        if isinstance(stmt, ReturnStatement):
            body = stmt.value
        else:
            body = stmt
        return MLCaseBranch(pattern=pattern, body=body)

    def visitExpression_stmt(self, ctx: CarbonParser.Expression_stmtContext):
        return self.visit(ctx.expression())

    def visitExpression(self, ctx: CarbonParser.ExpressionContext):
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

    def visitPrimary(self, ctx: CarbonParser.PrimaryContext):
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
        return None
