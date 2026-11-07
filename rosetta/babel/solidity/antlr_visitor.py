from antlr4 import *
from rosetta.babel.solidity.grammar.SolidityParser import SolidityParser
from rosetta.babel.solidity.grammar.SolidityVisitor import SolidityVisitor
from rosetta.ir.nodes import *

class RosettaSolidityVisitor(SolidityVisitor):
    def visitProgram(self, ctx: SolidityParser.ProgramContext):
        body = []
        for unit in ctx.source_unit():
            res = self.visit(unit)
            if res:
                if isinstance(res, list): body.extend(res)
                else: body.append(res)
        return Program(body=body)

    def visitSource_unit(self, ctx: SolidityParser.Source_unitContext):
        return self.visitChildren(ctx)

    def visitContract_definition(self, ctx: SolidityParser.Contract_definitionContext):
        name = ctx.ID().getText()
        bases = []
        if ctx.id_list():
            bases = [id.getText() for id in ctx.id_list().ID()]
        body = []
        for elem in ctx.contract_body_element():
            res = self.visit(elem)
            if res:
                if isinstance(res, list): body.extend(res)
                else: body.append(res)
        return SmartContractDeclaration(name=name, bases=bases, body=body, is_interface=False, is_library=False)

    def visitInterface_definition(self, ctx: SolidityParser.Interface_definitionContext):
        name = ctx.ID().getText()
        body = []
        for elem in ctx.contract_body_element():
            res = self.visit(elem)
            if res:
                if isinstance(res, list): body.extend(res)
                else: body.append(res)
        return SmartContractDeclaration(name=name, bases=[], body=body, is_interface=True, is_library=False)

    def visitLibrary_definition(self, ctx: SolidityParser.Library_definitionContext):
        name = ctx.ID().getText()
        body = []
        for elem in ctx.contract_body_element():
            res = self.visit(elem)
            if res:
                if isinstance(res, list): body.extend(res)
                else: body.append(res)
        return SmartContractDeclaration(name=name, bases=[], body=body, is_interface=False, is_library=True)

    def visitContract_body_element(self, ctx: SolidityParser.Contract_body_elementContext):
        return self.visitChildren(ctx)

    def visitState_variable_declaration(self, ctx: SolidityParser.State_variable_declarationContext):
        name = ctx.ID().getText()
        type_hint = ctx.type_name().getText()
        initializer = self.visit(ctx.expression()) if ctx.expression() else None
        is_const = ctx.getText().find("constant") != -1 or ctx.getText().find("immutable") != -1
        return VariableDeclaration(name=name, type_hint=type_hint, initializer=initializer, is_const=is_const)

    def visitEvent_definition(self, ctx: SolidityParser.Event_definitionContext):
        name = ctx.ID().getText()
        params = []
        if ctx.event_param_list():
            for param in ctx.event_param_list().event_param():
                p_name = param.ID().getText() if param.ID() else "param"
                p_type = param.type_name().getText()
                params.append(Parameter(name=p_name, type_hint=p_type))
        return EventDeclaration(name=name, params=params)

    def visitModifier_definition(self, ctx: SolidityParser.Modifier_definitionContext):
        name = ctx.ID().getText()
        params = []
        if ctx.param_list():
            for p in ctx.param_list().parameter():
                p_name = p.ID().getText() if p.ID() else "param"
                p_type = p.type_name().getText()
                params.append(Parameter(name=p_name, type_hint=p_type))
        body = self.visit(ctx.block())
        return ModifierDeclaration(name=name, params=params, body=body)

    def visitFunction_definition(self, ctx: SolidityParser.Function_definitionContext):
        name = ctx.ID().getText()
        params = []
        if ctx.param_list(0):
            for p in ctx.param_list(0).parameter():
                p_name = p.ID().getText() if p.ID() else "param"
                p_type = p.type_name().getText()
                params.append(Parameter(name=p_name, type_hint=p_type))
        
        body = self.visit(ctx.block()) if ctx.block() else []
        
        decorators = []
        if ctx.visibility():
            decorators.append(Identifier(name=ctx.visibility().getText()))
        if ctx.mutability():
            decorators.append(Identifier(name=ctx.mutability().getText()))
            
        ret_type = None
        if ctx.param_list(1):
            ret_types = [p.type_name().getText() for p in ctx.param_list(1).parameter()]
            ret_type = ", ".join(ret_types)
            
        return FunctionDeclaration(name=name, params=params, body=body, return_type=ret_type, decorators=decorators)

    def visitConstructor_definition(self, ctx: SolidityParser.Constructor_definitionContext):
        params = []
        if ctx.param_list():
            for p in ctx.param_list().parameter():
                p_name = p.ID().getText() if p.ID() else "param"
                p_type = p.type_name().getText()
                params.append(Parameter(name=p_name, type_hint=p_type))
        body = self.visit(ctx.block())
        decorators = []
        if ctx.visibility():
            decorators.append(Identifier(name=ctx.visibility().getText()))
        if ctx.mutability():
            decorators.append(Identifier(name=ctx.mutability().getText()))
        return FunctionDeclaration(name="constructor", params=params, body=body, decorators=decorators)

    def visitMapping_declaration(self, ctx: SolidityParser.Mapping_declarationContext):
        name = ctx.ID().getText()
        key_t = ctx.key_type().getText()
        val_t = ctx.type_name().getText()
        return VariableDeclaration(name=name, type_hint=f"mapping({key_t} => {val_t})")

    def visitBlock(self, ctx: SolidityParser.BlockContext):
        body = []
        for stmt in ctx.statement():
            res = self.visit(stmt)
            if res:
                if isinstance(res, list): body.extend(res)
                else: body.append(res)
        return body

    def visitStatement(self, ctx: SolidityParser.StatementContext):
        return self.visitChildren(ctx)

    def visitExpression_statement(self, ctx: SolidityParser.Expression_statementContext):
        return self.visit(ctx.expression())

    def visitIf_statement(self, ctx: SolidityParser.If_statementContext):
        cond = self.visit(ctx.expression())
        conseq = self.visit(ctx.statement(0))
        if not isinstance(conseq, list): conseq = [conseq]
        alt = None
        if ctx.statement(1):
            alt = self.visit(ctx.statement(1))
            if not isinstance(alt, list): alt = [alt]
        return IfStatement(condition=cond, consequent=conseq, alternate=alt)

    def visitFor_statement(self, ctx: SolidityParser.For_statementContext):
        init = self.visit(ctx.getChild(2))
        if init == ';': init = None
        cond = self.visit(ctx.expression(0)) if ctx.expression(0) else None
        incr = self.visit(ctx.expression(1)) if ctx.expression(1) else None
        body = self.visit(ctx.statement())
        if not isinstance(body, list): body = [body]
        return ForLoop(initializer=init, condition=cond, increment=incr, body=body)

    def visitWhile_statement(self, ctx: SolidityParser.While_statementContext):
        cond = self.visit(ctx.expression())
        body = self.visit(ctx.statement())
        if not isinstance(body, list): body = [body]
        return WhileLoop(condition=cond, body=body)

    def visitReturn_statement(self, ctx: SolidityParser.Return_statementContext):
        val = self.visit(ctx.expression()) if ctx.expression() else None
        return ReturnStatement(value=val)

    def visitEmit_statement(self, ctx: SolidityParser.Emit_statementContext):
        event_call = self.visit(ctx.expression())
        return EmitStatement(event_call=event_call)

    def visitVariable_declaration_statement(self, ctx: SolidityParser.Variable_declaration_statementContext):
        name = ctx.ID().getText()
        type_hint = ctx.type_name().getText()
        init = self.visit(ctx.expression()) if ctx.expression() else None
        return VariableDeclaration(name=name, type_hint=type_hint, initializer=init)

    def visitExpression(self, ctx: SolidityParser.ExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.primary())
        if ctx.getChildCount() == 4 and ctx.getChild(1).getText() == '(':
            callee = self.visit(ctx.expression(0)) if ctx.expression(0) else Identifier(name="callee")
            args = []
            if ctx.argument_list():
                args = [self.visit(arg) for arg in ctx.argument_list().expression() if arg]
            return CallExpression(callee=callee, args=args)
        if ctx.getChildCount() == 3:
            if ctx.getChild(0).getText() == '(':
                return self.visit(ctx.expression(0)) if ctx.expression(0) else None
            if ctx.getChild(1).getText() == '=':
                target = self.visit(ctx.expression(0)) if ctx.expression(0) else Identifier(name="target")
                val = self.visit(ctx.expression(1)) if ctx.expression(1) else Literal(value="")
                return Assignment(target=target, value=val)
            left = self.visit(ctx.expression(0)) if ctx.expression(0) else Identifier(name="left")
            op = ctx.getChild(1).getText()
            right = self.visit(ctx.expression(1)) if ctx.expression(1) else None
            
            if right is None:
                return left
                
            if isinstance(left, Identifier) and left.name in ["require", "assert"]:
                return CallExpression(callee=left, args=[right])
                
            return BinaryExpression(left=left, operator=op, right=right)
        return Literal(value=ctx.getText())

    def visitPrimary(self, ctx: SolidityParser.PrimaryContext):
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
        if ctx.expression():
            return self.visit(ctx.expression())
        return None
