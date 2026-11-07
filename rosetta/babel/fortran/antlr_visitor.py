from antlr4 import *
from rosetta.babel.fortran.grammar.FortranParser import FortranParser
from rosetta.babel.fortran.grammar.FortranVisitor import FortranVisitor
from rosetta.ir.nodes import *

class RosettaFortranVisitor(FortranVisitor):
    def visitTerminal(self, node):
        return None

    def visitProgram(self, ctx: FortranParser.ProgramContext):
        body = []
        for child in ctx.children:
            res = self.visit(child)
            if isinstance(res, list):
                body.extend(res)
            elif res:
                body.append(res)
        return Program(body=body)

    def visitMain_program(self, ctx: FortranParser.Main_programContext):
        nodes = []
        if ctx.program_stmt():
            # Could add metadata about program name if needed
            pass
        if ctx.specification_part():
            nodes.extend(self.visit(ctx.specification_part()))
        if ctx.execution_part():
            nodes.extend(self.visit(ctx.execution_part()))
        return nodes

    def visitSubroutine_def(self, ctx: FortranParser.Subroutine_defContext):
        stmt = ctx.subroutine_stmt()
        name = stmt.identifier(0).getText()
        params = []
        if stmt.getChildCount() > 3: # Has parentheses
            ids = stmt.identifier()
            params = [Parameter(name=ids[i].getText()) for i in range(1, len(ids))]
        
        body = []
        if ctx.specification_part():
            body.extend(self.visit(ctx.specification_part()))
        if ctx.execution_part():
            body.extend(self.visit(ctx.execution_part()))
            
        return FunctionDeclaration(name=name, params=params, body=body)

    def visitFunction_def(self, ctx: FortranParser.Function_defContext):
        stmt = ctx.function_stmt()
        name = stmt.identifier(0).getText()
        ids = stmt.identifier()
        params = [Parameter(name=ids[i].getText()) for i in range(1, len(ids))]
        
        body = []
        if ctx.specification_part():
            body.extend(self.visit(ctx.specification_part()))
        if ctx.execution_part():
            body.extend(self.visit(ctx.execution_part()))
            
        return FunctionDeclaration(name=name, params=params, body=body, return_type=ctx.function_stmt().type_spec().getText() if ctx.function_stmt().type_spec() else None)

    def visitSpecification_part(self, ctx: FortranParser.Specification_partContext):
        nodes = []
        for stmt in ctx.specification_stmt():
            res = self.visit(stmt)
            if isinstance(res, list):
                nodes.extend(res)
            elif res:
                nodes.append(res)
        return nodes

    def visitSpecification_stmt(self, ctx: FortranParser.Specification_stmtContext):
        return self.visit(ctx.getChild(0))

    def visitType_declaration_stmt(self, ctx: FortranParser.Type_declaration_stmtContext):
        type_hint = ctx.type_spec().getText()
        nodes = []
        for entity in ctx.entity_decl():
            name = entity.identifier().getText()
            init = self.visit(entity.expression()) if entity.expression() else None
            if entity.array_spec():
                dims = [self.visit(d) for d in entity.array_spec().dimension()]
                nodes.append(ArrayDeclaration(name=name, type_hint=type_hint, initializer=init, dimensions=dims))
            else:
                nodes.append(VariableDeclaration(name=name, type_hint=type_hint, initializer=init))
        return nodes

    def visitDimension(self, ctx: FortranParser.DimensionContext):
        if ctx.getText() == '*':
            return Identifier(name="*")
        exprs = ctx.expression()
        if len(exprs) == 2:
            # lower:upper
            return BinaryExpression(left=self.visit(exprs[0]), operator=":", right=self.visit(exprs[1]))
        return self.visit(exprs[0])

    def visitImplicit_none_stmt(self, ctx: FortranParser.Implicit_none_stmtContext):
        # Could use metadata to signal implicit none
        return None

    def visitCommon_stmt(self, ctx: FortranParser.Common_stmtContext):
        name = ctx.identifier(0).getText() if ctx.getChild(1).getText() == '/' else None
        start_idx = 1 if name else 0
        members = []
        for i in range(start_idx, len(ctx.identifier())):
             members.append(VariableDeclaration(name=ctx.identifier(i).getText()))
        return GlobalBlock(name=name, members=members)

    def visitDimension_stmt(self, ctx: FortranParser.Dimension_stmtContext):
        # DIMENSION A(10), B(20)
        # This usually supplements type declarations.
        # For simplicity, we'll map to ArrayDeclarations
        nodes = []
        ids = ctx.identifier()
        specs = ctx.array_spec()
        for i in range(len(ids)):
            name = ids[i].getText()
            dims = [self.visit(d) for d in specs[i].dimension()]
            nodes.append(ArrayDeclaration(name=name, dimensions=dims))
        return nodes

    def visitExecution_part(self, ctx: FortranParser.Execution_partContext):
        nodes = []
        for stmt in ctx.executable_stmt():
            res = self.visit(stmt)
            if isinstance(res, list):
                nodes.extend(res)
            elif res:
                nodes.append(res)
        return nodes

    def visitExecutable_stmt(self, ctx: FortranParser.Executable_stmtContext):
        nodes = []
        if ctx.label():
            nodes.append(Label(name=ctx.label().getText()))
        
        if ctx.action_stmt():
            res = self.visit(ctx.action_stmt())
        elif ctx.assignment_stmt():
            res = self.visit(ctx.assignment_stmt())
        elif ctx.if_stmt():
            res = self.visit(ctx.if_stmt())
        elif ctx.do_stmt():
            res = self.visit(ctx.do_stmt())
        elif ctx.goto_stmt():
            res = self.visit(ctx.goto_stmt())
        elif ctx.call_stmt():
            res = self.visit(ctx.call_stmt())
        elif ctx.write_stmt():
            res = self.visit(ctx.write_stmt())
        elif ctx.print_stmt():
            res = self.visit(ctx.print_stmt())
        elif ctx.format_stmt():
            res = self.visit(ctx.format_stmt())
        else:
            res = None

        if res:
            if isinstance(res, list):
                nodes.extend(res)
            else:
                nodes.append(res)
        return nodes

    def visitAction_stmt(self, ctx: FortranParser.Action_stmtContext):
        return self.visit(ctx.getChild(0))

    def visitPrint_stmt(self, ctx: FortranParser.Print_stmtContext):
        args = []
        for expr in ctx.expression():
            args.append(self.visit(expr))
        return CallExpression(callee=Identifier(name="print"), args=args)

    def visitAssignment_stmt(self, ctx: FortranParser.Assignment_stmtContext):
        target_name = ctx.identifier().getText()
        if ctx.expression(1): 
            # Array access
            all_exprs = ctx.expression()
            indices = [self.visit(e) for e in all_exprs[:-1]]
            rhs = self.visit(all_exprs[-1])
            return Assignment(target=ArrayAccess(object=Identifier(name=target_name), index=indices), value=rhs)
        
        return Assignment(target=Identifier(name=target_name), value=self.visit(ctx.expression(0)))

    def visitIf_stmt(self, ctx: FortranParser.If_stmtContext):
        cond = self.visit(ctx.expression(0))
        if ctx.THEN_K():
            consequent = self.visit(ctx.execution_part(0)) if ctx.execution_part(0) else []
            
            # Reconstruct the IF/ELSE IF/ELSE chain
            # execution_part(0) is the THEN block
            # subsequent execution_parts are for ELSE IF and ELSE
            # subsequent expressions are for ELSE IF
            
            alternate = None
            expr_idx = 1
            part_idx = 1
            
            # Helper to build nested IfStatements for ELSE IF
            def build_else_if(e_idx, p_idx):
                if e_idx < len(ctx.expression()):
                    c = self.visit(ctx.expression(e_idx))
                    cons = self.visit(ctx.execution_part(p_idx)) if p_idx < len(ctx.execution_part()) else []
                    alt = build_else_if(e_idx + 1, p_idx + 1)
                    return [IfStatement(condition=c, consequent=cons, alternate=alt)]
                elif p_idx < len(ctx.execution_part()):
                    # The last execution_part must be the ELSE block
                    return self.visit(ctx.execution_part(p_idx))
                return None

            alternate = build_else_if(expr_idx, part_idx)
            
            return IfStatement(condition=cond, consequent=consequent, alternate=alternate)
        else:
            consequent = [self.visit(ctx.action_stmt())]
            return IfStatement(condition=cond, consequent=consequent)

    def visitDo_stmt(self, ctx: FortranParser.Do_stmtContext):
        if ctx.identifier():
            # DO i = start, end, step
            var = ctx.identifier().getText()
            start = self.visit(ctx.expression(0))
            end = self.visit(ctx.expression(1))
            step = self.visit(ctx.expression(2)) if ctx.expression(2) else Literal(value=1)
            body = self.visit(ctx.execution_part()) if ctx.execution_part() else []
            return ForLoop(
                initializer=Assignment(target=Identifier(name=var), value=start),
                condition=BinaryExpression(left=Identifier(name=var), operator="<=", right=end),
                increment=Assignment(target=Identifier(name=var), value=BinaryExpression(left=Identifier(name=var), operator="+", right=step)),
                body=body
            )
        else:
            # DO WHILE or just DO
            body = self.visit(ctx.execution_part()) if ctx.execution_part() else []
            return WhileLoop(condition=Literal(value=True), body=body)

    def visitGoto_stmt(self, ctx: FortranParser.Goto_stmtContext):
        return GotoStatement(label=ctx.label().getText())

    def visitCall_stmt(self, ctx: FortranParser.Call_stmtContext):
        name = ctx.identifier().getText()
        args = [self.visit(e) for e in ctx.expression()]
        return CallExpression(callee=Identifier(name=name), args=args)

    def visitWrite_stmt(self, ctx: FortranParser.Write_stmtContext):
        args = [self.visit(e) for e in ctx.expression()]
        # unit and fmt are in parentheses, but our grammar is simple for now
        return CallExpression(callee=Identifier(name="print"), args=args)

    def visitFormat_stmt(self, ctx: FortranParser.Format_stmtContext):
        items = [item.getText() for item in ctx.format_item()]
        return FormatDeclaration(label=ctx.label().getText(), items=items)

    def visitReturn_stmt(self, ctx: FortranParser.Return_stmtContext):
        return ReturnStatement()

    def visitExpression(self, ctx: FortranParser.ExpressionContext):
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

    def visitPrimary(self, ctx: FortranParser.PrimaryContext):
        if ctx.identifier():
            name = ctx.identifier().getText()
            if ctx.expression():
                # Array access or function call
                args = [self.visit(e) for e in ctx.expression()]
                return ArrayAccess(object=Identifier(name=name), index=args)
            return Identifier(name=name)
        return self.visit(ctx.literal())

    def visitLiteral(self, ctx: FortranParser.LiteralContext):
        if ctx.integer_literal():
            return Literal(value=int(ctx.integer_literal().getText()))
        if ctx.real_literal():
            return Literal(value=float(ctx.real_literal().getText()))
        if ctx.string_literal():
            return Literal(value=ctx.string_literal().getText().strip("'\""))
        if ctx.logical_literal():
            return Literal(value=ctx.logical_literal().getText().upper() == '.TRUE.')
        return None
