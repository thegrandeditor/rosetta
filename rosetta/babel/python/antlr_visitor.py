import sys
from antlr4 import *
from rosetta.babel.python.grammar.Python3Parser import Python3Parser
from rosetta.babel.python.grammar.Python3ParserVisitor import Python3ParserVisitor
from rosetta.ir.nodes import *

class RosettaPythonVisitor(Python3ParserVisitor):
    def visitFile_input(self, ctx: Python3Parser.File_inputContext):
        statements = []
        for child in ctx.children:
            if isinstance(child, Python3Parser.StmtContext):
                res = self.visit(child)
                if isinstance(res, list):
                    statements.extend(res)
                elif res:
                    statements.append(res)
        return Program(body=statements)

    def visitStmt(self, ctx: Python3Parser.StmtContext):
        if ctx.simple_stmts():
            return self.visit(ctx.simple_stmts())
        if ctx.compound_stmt():
            return self.visit(ctx.compound_stmt())
        return None

    def visitSimple_stmts(self, ctx: Python3Parser.Simple_stmtsContext):
        stmts = []
        for s in ctx.simple_stmt():
            res = self.visit(s)
            if res: stmts.append(res)
        return stmts

    def visitExpr_stmt(self, ctx: Python3Parser.Expr_stmtContext):
        if ctx.ASSIGN() and len(ctx.ASSIGN()) > 0:
            # target = value
            target = self.visit(ctx.testlist_star_expr(0))
            if ctx.yield_expr(0):
                value = self.visit(ctx.yield_expr(0))
            else:
                value = self.visit(ctx.testlist_star_expr(1))
            return Assignment(target=target, value=value)
        
        if ctx.annassign():
            target = self.visit(ctx.testlist_star_expr(0))
            # Handle type hint and optional value
            return None # Skip for now

        return self.visit(ctx.testlist_star_expr(0))

    def visitAnnassign(self, ctx: Python3Parser.AnnassignContext):
        # target: type = value
        # This is a bit complex in the grammar, skipping for basic demo
        return None

    def visitFuncdef(self, ctx: Python3Parser.FuncdefContext):
        name = self.visit(ctx.name())
        params = self.visit(ctx.parameters())
        body = self.visit(ctx.block())
        return FunctionDeclaration(name=name, params=params, body=body)

    def visitParameters(self, ctx: Python3Parser.ParametersContext):
        if ctx.typedargslist():
            return self.visit(ctx.typedargslist())
        return []

    def visitTypedargslist(self, ctx: Python3Parser.TypedargslistContext):
        params = []
        # Simplified: just getting the names
        for tfpdef in ctx.tfpdef():
            params.append(self.visit(tfpdef))
        return params

    def visitTfpdef(self, ctx: Python3Parser.TfpdefContext):
        name = self.visit(ctx.name())
        type_hint = None
        if ctx.test():
            type_hint = ctx.test().getText() # Simplified
        return Parameter(name=name, type_hint=type_hint)

    def visitBlock(self, ctx: Python3Parser.BlockContext):
        if ctx.simple_stmts():
            return self.visit(ctx.simple_stmts())
        stmts = []
        for stmt in ctx.stmt():
            res = self.visit(stmt)
            if isinstance(res, list):
                stmts.extend(res)
            elif res:
                stmts.append(res)
        return stmts

    def visitCompound_stmt(self, ctx: Python3Parser.Compound_stmtContext):
        if ctx.if_stmt(): return self.visit(ctx.if_stmt())
        if ctx.funcdef(): return self.visit(ctx.funcdef())
        if ctx.classdef(): return self.visit(ctx.classdef())
        if ctx.for_stmt(): return self.visit(ctx.for_stmt())
        return None

    def visitIf_stmt(self, ctx: Python3Parser.If_stmtContext):
        condition = self.visit(ctx.test(0))
        consequent = self.visit(ctx.block(0))
        alternate = None
        if ctx.block(1): # simplified else handling
            alternate = self.visit(ctx.block(1))
        return IfStatement(condition=condition, consequent=consequent, alternate=alternate)

    def visitName(self, ctx: Python3Parser.NameContext):
        return ctx.getText()

    def visitTestlist_star_expr(self, ctx: Python3Parser.Testlist_star_exprContext):
        return self.visit(ctx.test(0))

    def visitTest(self, ctx: Python3Parser.TestContext):
        if ctx.or_test():
            return self.visit(ctx.or_test(0))
        return None

    def visitOr_test(self, ctx: Python3Parser.Or_testContext):
        return self.visit(ctx.and_test(0))

    def visitAnd_test(self, ctx: Python3Parser.And_testContext):
        return self.visit(ctx.not_test(0))

    def visitNot_test(self, ctx: Python3Parser.Not_testContext):
        if ctx.comparison():
            return self.visit(ctx.comparison())
        return None

    def visitComparison(self, ctx: Python3Parser.ComparisonContext):
        return self.visit(ctx.expr(0))

    def visitExpr(self, ctx: Python3Parser.ExprContext):
        if ctx.atom_expr():
            return self.visit(ctx.atom_expr())
        
        # Binary expression: expr op expr
        if ctx.getChildCount() == 3:
            left = self.visit(ctx.expr(0))
            op = ctx.getChild(1).getText()
            right = self.visit(ctx.expr(1))
            return BinaryExpression(left=left, operator=op, right=right)
        
        # Unary expression: op expr
        if ctx.getChildCount() == 2:
            op = ctx.getChild(0).getText()
            arg = self.visit(ctx.expr(0))
            return UnaryExpression(operator=op, argument=arg)

        return None

    def visitAtom_expr(self, ctx: Python3Parser.Atom_exprContext):
        atom = self.visit(ctx.atom())
        # Handle trailers (calls, member access)
        if ctx.trailer():
            for trailer in ctx.trailer():
                if trailer.OPEN_PAREN():
                    # Call
                    args = [] # Simplified
                    atom = CallExpression(callee=atom, args=args)
                elif trailer.DOT():
                    # Member access
                    member = self.visit(trailer.name())
                    atom = MemberAccess(object=atom, member=member)
        return atom

    def visitAtom(self, ctx: Python3Parser.AtomContext):
        if ctx.name():
            return Identifier(name=self.visit(ctx.name()))
        if ctx.NUMBER():
            text = ctx.NUMBER().getText()
            try:
                val = int(text)
            except ValueError:
                val = float(text)
            return Literal(value=val)
        if ctx.STRING():
            # Handle multiple strings (concatenation)
            return Literal(value="".join(s.getText().strip("'\"") for s in ctx.STRING()))
        if ctx.getText() == 'None':
            return Literal(value=None)
        if ctx.getText() == 'True':
            return Literal(value=True)
        if ctx.getText() == 'False':
            return Literal(value=False)
        return None
