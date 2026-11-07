from antlr4 import *
from rosetta.babel.eiffel.grammar.EiffelParser import EiffelParser
from rosetta.babel.eiffel.grammar.EiffelVisitor import EiffelVisitor
from rosetta.ir.nodes import *

class RosettaEiffelVisitor(EiffelVisitor):
    def visitProgram(self, ctx: EiffelParser.ProgramContext):
        body = [self.visit(c) for c in ctx.class_declaration()]
        return Program(body=body)

    def visitClass_declaration(self, ctx: EiffelParser.Class_declarationContext):
        name = ctx.ID().getText()
        bases = []
        if ctx.inheritance():
            bases.append(ctx.inheritance().ID().getText())
        
        body = []
        for block in ctx.feature_block():
            res = self.visit(block)
            if isinstance(res, list): body.extend(res)
            else: body.append(res)
            
        invariant = []
        if ctx.invariant_clause():
             invariant = self.visit(ctx.invariant_clause())
             
        return ContractedClass(name=name, bases=bases, body=body, invariant=invariant)

    def visitFeature_block(self, ctx: EiffelParser.Feature_blockContext):
        features = []
        for feat in ctx.feature_declaration():
            res = self.visit(feat)
            if res: features.append(res)
        return features

    def visitFeature_declaration(self, ctx: EiffelParser.Feature_declarationContext):
        name = ctx.ID().getText()
        params = []
        if ctx.formal_params():
             # Simplified extraction
             pass
        ret_type = ctx.type_().getText() if ctx.type_() else None
        
        # Determine if it's a function or attribute
        body = []
        contract = None
        if ctx.routine_body():
             body_ctx = ctx.routine_body()
             req = self.visit(body_ctx.assertion_list(0)) if body_ctx.REQUIRE_K() else []
             ens = self.visit(body_ctx.assertion_list(len(body_ctx.assertion_list())-1)) if body_ctx.ENSURE_K() else []
             contract = Contract(require=req, ensure=ens)
             if body_ctx.DO_K():
                 body = self.visit(body_ctx.block(0))
             return ContractedFunction(name=name, params=params, body=body, return_type=ret_type, contract=contract)
        else:
             return VariableDeclaration(name=name, type_hint=ret_type)

    def visitAssertion_list(self, ctx: EiffelParser.Assertion_listContext):
        return [self.visit(a) for a in ctx.assertion()]

    def visitAssertion(self, ctx: EiffelParser.AssertionContext):
        return self.visit(ctx.expression())

    def visitBlock(self, ctx: EiffelParser.BlockContext):
        return [self.visit(s) for s in ctx.statement() if self.visit(s)]

    def visitStatement(self, ctx: EiffelParser.StatementContext):
        return self.visit(ctx.getChild(0))

    def visitAssignment(self, ctx: EiffelParser.AssignmentContext):
        return Assignment(target=Identifier(name=ctx.ID().getText()), value=self.visit(ctx.expression()))

    def visitIf_statement(self, ctx: EiffelParser.If_statementContext):
        cond = self.visit(ctx.expression(0))
        consequent = self.visit(ctx.block(0))
        alternate = None
        if ctx.ELSE_K():
            alternate = self.visit(ctx.block(len(ctx.block()) - 1))
        return IfStatement(condition=cond, consequent=consequent, alternate=alternate)

    def visitLoop_statement(self, ctx: EiffelParser.Loop_statementContext):
        # from block until expr loop block
        # Map to WhileLoop with some prep
        init = self.visit(ctx.block(0))
        cond = UnaryExpression(operator="not", argument=self.visit(ctx.expression()))
        body = self.visit(ctx.block(1))
        # Return a list of nodes: init then the loop
        return init + [WhileLoop(condition=cond, body=body)]

    def visitInvariant_clause(self, ctx: EiffelParser.Invariant_clauseContext):
        return self.visit(ctx.assertion_list())

    def visitLogical_expr(self, ctx: EiffelParser.Logical_exprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.rel_expr(0))
        left = self.visit(ctx.rel_expr(0))
        # Simplified
        return left

    def visitRel_expr(self, ctx: EiffelParser.Rel_exprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.add_expr(0))
        left = self.visit(ctx.add_expr(0))
        op = ctx.getChild(1).getText()
        if op == "/=": op = "!="
        right = self.visit(ctx.add_expr(1))
        return BinaryExpression(left=left, operator=op, right=right)

    def visitAdd_expr(self, ctx: EiffelParser.Add_exprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.mul_expr(0))
        left = self.visit(ctx.mul_expr(0))
        # Simplified
        return left

    def visitMul_expr(self, ctx: EiffelParser.Mul_exprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.unary_expr(0))
        left = self.visit(ctx.unary_expr(0))
        # Simplified
        return left

    def visitUnary_expr(self, ctx: EiffelParser.Unary_exprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.primary())
        op = ctx.getChild(0).getText()
        arg = self.visit(ctx.primary())
        return UnaryExpression(operator=op, argument=arg)

    def visitPrimary(self, ctx: EiffelParser.PrimaryContext):
        if ctx.ID(): return Identifier(name=ctx.ID().getText())
        if ctx.NUMBER(): return Literal(value=float(ctx.NUMBER().getText()))
        if ctx.STRING(): return Literal(value=ctx.STRING().getText().strip("'\""))
        if ctx.expression(): return self.visit(ctx.expression())
        if ctx.call_expr(): return self.visit(ctx.call_expr())
        return None

    def visitCall_expr(self, ctx: EiffelParser.Call_exprContext):
        name = ctx.ID(len(ctx.ID()) - 1).getText()
        obj = Identifier(name=ctx.ID(0).getText()) if len(ctx.ID()) > 1 else None
        args = []
        if ctx.actual_params():
            args = [self.visit(e) for e in ctx.actual_params().expression()]
        
        callee = MemberAccess(object=obj, member=name) if obj else Identifier(name=name)
        return CallExpression(callee=callee, args=args)
