from antlr4 import *
from rosetta.babel.modula2.grammar.Modula2Parser import Modula2Parser
from rosetta.babel.modula2.grammar.Modula2Visitor import Modula2Visitor
from rosetta.ir.nodes import *

class RosettaModula2Visitor(Modula2Visitor):
    def visitProgram(self, ctx: Modula2Parser.ProgramContext):
        body = []
        for unit in ctx.compilation_unit():
            res = self.visit(unit)
            if res:
                body.append(res)
        return Program(body=body)

    def visitMain_module(self, ctx: Modula2Parser.Main_moduleContext):
        name = ctx.ID(0).getText()
        body = self.visit(ctx.block())
        return ModuleDeclaration(name=name, body=body)

    def visitBlock(self, ctx: Modula2Parser.BlockContext):
        body = []
        for decl in ctx.declaration():
            res = self.visit(decl)
            if res:
                if isinstance(res, list): body.extend(res)
                else: body.append(res)
        
        if ctx.statement_sequence():
            body.extend(self.visit(ctx.statement_sequence()))
            
        return body

    def visitDeclaration(self, ctx: Modula2Parser.DeclarationContext):
        if ctx.procedure_declaration():
            return self.visit(ctx.procedure_declaration())
        
        nodes = []
        if ctx.CONST_K():
            for i in range(len(ctx.ID())):
                nodes.append(VariableDeclaration(name=ctx.ID(i).getText(), initializer=self.visit(ctx.expression(i)), is_const=True))
        elif ctx.TYPE_K():
            pass
        elif ctx.VAR_K():
            for i in range(len(ctx.id_list())):
                type_hint = ctx.type_(i).getText()
                for id_node in ctx.id_list(i).ID():
                    nodes.append(VariableDeclaration(name=id_node.getText(), type_hint=type_hint))
        return nodes

    def visitProcedure_declaration(self, ctx: Modula2Parser.Procedure_declarationContext):
        name = ctx.ID(0).getText()
        params = []
        if ctx.formal_params():
             for fp in ctx.formal_params().fp_section():
                 type_hint = fp.type_().getText()
                 for id_node in fp.id_list().ID():
                     params.append(Parameter(name=id_node.getText(), type_hint=type_hint))
                     
        ret_type = ctx.ID(1).getText() if ctx.getChildCount() > 5 and ctx.getChild(4).getText() == ':' else None
        body = self.visit(ctx.block())
        return FunctionDeclaration(name=name, params=params, body=body, return_type=ret_type)

    def visitStatement_sequence(self, ctx: Modula2Parser.Statement_sequenceContext):
        return [self.visit(s) for s in ctx.statement() if self.visit(s)]

    def visitAssignment(self, ctx: Modula2Parser.AssignmentContext):
        return Assignment(target=self.visit(ctx.designator()), value=self.visit(ctx.expression()))

    def visitProcedure_call(self, ctx: Modula2Parser.Procedure_callContext):
        callee = self.visit(ctx.designator())
        args = []
        if ctx.actual_params():
            args = [self.visit(e) for e in ctx.actual_params().expression()]
        return CallExpression(callee=callee, args=args)

    def visitIf_statement(self, ctx: Modula2Parser.If_statementContext):
        cond = self.visit(ctx.expression(0))
        consequent = self.visit(ctx.statement_sequence(0))
        alternate = None
        if ctx.ELSE_K():
            alternate = self.visit(ctx.statement_sequence(len(ctx.statement_sequence()) - 1))
        return IfStatement(condition=cond, consequent=consequent, alternate=alternate)

    def visitWhile_statement(self, ctx: Modula2Parser.While_statementContext):
        return WhileLoop(condition=self.visit(ctx.expression()), body=self.visit(ctx.statement_sequence()))

    def visitFor_statement(self, ctx: Modula2Parser.For_statementContext):
        var = ctx.ID().getText()
        start = self.visit(ctx.expression(0))
        end = self.visit(ctx.expression(1))
        step = self.visit(ctx.expression(2)) if len(ctx.expression()) > 2 else Literal(value=1)
        return ForLoop(
            initializer=Assignment(target=Identifier(name=var), value=start),
            condition=BinaryExpression(left=Identifier(name=var), operator="<=", right=end),
            increment=Assignment(target=Identifier(name=var), value=BinaryExpression(left=Identifier(name=var), operator="+", right=step)),
            body=self.visit(ctx.statement_sequence())
        )

    def visitReturn_statement(self, ctx: Modula2Parser.Return_statementContext):
        val = self.visit(ctx.expression()) if ctx.expression() else None
        return ReturnStatement(value=val)

    def visitDesignator(self, ctx: Modula2Parser.DesignatorContext):
        name = ctx.ID(0).getText()
        res = Identifier(name=name)
        return res

    def visitExpression(self, ctx: Modula2Parser.ExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.simple_expression(0))
        left = self.visit(ctx.simple_expression(0))
        op = ctx.rel_op().getText()
        right = self.visit(ctx.simple_expression(1))
        return BinaryExpression(left=left, operator=op, right=right)

    def visitSimple_expression(self, ctx: Modula2Parser.Simple_expressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.term(0))
        left = self.visit(ctx.term(0))
        return left

    def visitTerm(self, ctx: Modula2Parser.TermContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.factor(0))
        left = self.visit(ctx.factor(0))
        return left

    def visitFactor(self, ctx: Modula2Parser.FactorContext):
        if ctx.NUMBER(): return Literal(value=float(ctx.NUMBER().getText()))
        if ctx.STRING(): return Literal(value=ctx.STRING().getText().strip("'\""))
        if ctx.designator():
             res = self.visit(ctx.designator())
             if ctx.actual_params():
                 args = [self.visit(e) for e in ctx.actual_params().expression()]
                 return CallExpression(callee=res, args=args)
             return res
        if ctx.expression(): return self.visit(ctx.expression())
        return None
