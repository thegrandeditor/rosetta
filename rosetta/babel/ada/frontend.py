from antlr4 import *
from rosetta.babel.ada.grammar.AdaLexer import AdaLexer
from rosetta.babel.ada.grammar.AdaParser import AdaParser
from rosetta.babel.ada.grammar.AdaVisitor import AdaVisitor
from rosetta.babel.base.base import BabelFrontend
from rosetta.ir.nodes import *

class RosettaAdaVisitor(AdaVisitor):
    def visitProgram(self, ctx: AdaParser.ProgramContext):
        body = []
        for unit in ctx.compilation_unit():
            res = self.visit(unit)
            if isinstance(res, list):
                body.extend(res)
            elif res:
                body.append(res)
        return Program(body=body)

    def visitPackage_declaration(self, ctx: AdaParser.Package_declarationContext):
        name = ctx.identifier(0).getText()
        body = []
        for item in ctx.package_item():
            res = self.visit(item)
            if isinstance(res, list):
                body.extend(res)
            elif res:
                body.append(res)
        return ModuleDeclaration(name=name, body=body)

    def visitPackage_body(self, ctx: AdaParser.Package_bodyContext):
        name = ctx.identifier(0).getText()
        body = []
        for item in ctx.package_item():
             res = self.visit(item)
             if isinstance(res, list): body.extend(res)
             elif res: body.append(res)
        if ctx.statement():
            for stmt in ctx.statement():
                body.append(self.visit(stmt))
        return ModuleDeclaration(name=name, body=body)

    def visitSubprogram_body(self, ctx: AdaParser.Subprogram_bodyContext):
        spec = ctx.subprogram_specification()
        name = spec.identifier().getText()
        params = self.visit(spec.formal_part()) if spec.formal_part() else []
        ret_type = spec.type_mark().getText() if spec.FUNCTION_K() else None
        
        body = []
        for decl in ctx.declaration():
            res = self.visit(decl)
            if isinstance(res, list): body.extend(res)
            elif res: body.append(res)
        
        for stmt in ctx.statement():
            body.append(self.visit(stmt))
            
        if ctx.EXCEPTION_K():
            handlers = [self.visit(h) for h in ctx.exception_handler()]
            body = [TryCatch(body=body, handlers=handlers)]
            
        return FunctionDeclaration(name=name, params=params, body=body, return_type=ret_type)

    def visitFormal_part(self, ctx: AdaParser.Formal_partContext):
        params = []
        for ps in ctx.parameter_specification():
            params.extend(self.visit(ps))
        return params

    def visitParameter_specification(self, ctx: AdaParser.Parameter_specificationContext):
        type_hint = ctx.type_mark().getText()
        ids = ctx.identifier()
        return [Parameter(name=id.getText(), type_hint=type_hint) for id in ids]

    def visitVariable_declaration(self, ctx: AdaParser.Variable_declarationContext):
        type_hint = ctx.type_mark().getText()
        init = self.visit(ctx.expression()) if ctx.expression() else None
        ids = ctx.identifier()
        return [VariableDeclaration(name=id.getText(), type_hint=type_hint, initializer=init) for id in ids]

    def visitTask_declaration(self, ctx: AdaParser.Task_declarationContext):
        name = ctx.identifier(0).getText()
        body = []
        # Simplified handling
        return TaskDeclaration(name=name, body=body)

    def visitAssignment_statement(self, ctx: AdaParser.Assignment_statementContext):
        target = Identifier(name=ctx.identifier().getText())
        value = self.visit(ctx.expression())
        return Assignment(target=target, value=value)

    def visitProcedure_call_statement(self, ctx: AdaParser.Procedure_call_statementContext):
        name = ctx.qualified_name().getText()
        args = [self.visit(e) for e in ctx.expression()]
        if name.lower() == "put_line":
             return CallExpression(callee=Identifier(name="print"), args=args)
        return CallExpression(callee=Identifier(name=name), args=args)

    def visitIf_statement(self, ctx: AdaParser.If_statementContext):
        cond = self.visit(ctx.expression(0))
        # Reconstructing Ada IF/ELSIF/ELSE
        consequent = [self.visit(s) for s in ctx.statement()]
        # This needs more logic to separate ELSIF/ELSE blocks
        return IfStatement(condition=cond, consequent=consequent)

    def visitGeneric_declaration(self, ctx: AdaParser.Generic_declarationContext):
        params = self.visit(ctx.generic_formal_part()) if ctx.generic_formal_part() else []
        decl = self.visit(ctx.getChild(ctx.getChildCount()-1))
        return GenericDeclaration(name="", parameters=params, declaration=decl)

    def visitType_declaration(self, ctx: AdaParser.Type_declarationContext):
        name = ctx.identifier().getText()
        defn = self.visit(ctx.type_definition())
        if isinstance(defn, RecordDeclaration):
            defn.name = name
            return defn
        elif isinstance(defn, ArrayDeclaration):
            defn.name = name
            return defn
        return VariableDeclaration(name=name, type_hint=str(defn))

    def visitType_definition(self, ctx: AdaParser.Type_definitionContext):
        if ctx.RECORD_K():
            fields = []
            if ctx.component_list():
                for vd in ctx.component_list().variable_declaration():
                    fields.extend(self.visit(vd))
            return RecordDeclaration(name="", fields=fields)
        elif ctx.ARRAY_K():
            # ARRAY (1..10) OF Integer
            dims = [self.visit(ctx.index_constraint().range_spec(0))]
            base_type = ctx.type_mark().getText()
            return ArrayDeclaration(name="", type_hint=base_type, dimensions=dims)
        return ctx.getText()

    def visitRange_spec(self, ctx: AdaParser.Range_specContext):
        return BinaryExpression(left=self.visit(ctx.expression(0)), operator="..", right=self.visit(ctx.expression(1)))

    def visitLoop_statement(self, ctx: AdaParser.Loop_statementContext):
        body = [self.visit(s) for s in ctx.statement()]
        if ctx.iteration_scheme():
            scheme = ctx.iteration_scheme()
            if scheme.WHILE_K():
                return WhileLoop(condition=self.visit(scheme.expression()), body=body)
            else: # FOR
                var = scheme.identifier().getText()
                return ForInLoop(iterator=Identifier(name=var), iterable=self.visit(scheme.range_spec()), body=body)
        return WhileLoop(condition=Literal(value=True), body=body)

    def visitQualified_name(self, ctx: AdaParser.Qualified_nameContext):
        return Identifier(name=ctx.getText())

    def visitException_handler(self, ctx: AdaParser.Exception_handlerContext):
        body = [self.visit(s) for s in ctx.statement()]
        return ExceptionHandler(exception_type=None, variable=None, body=body)

    def visitExpression(self, ctx: AdaParser.ExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.primary())
        if ctx.getChildCount() == 3:
            if ctx.getChild(0).getText() == '(':
                return self.visit(ctx.expression(0))
            left = self.visit(ctx.expression(0))
            op = ctx.getChild(1).getText()
            right = self.visit(ctx.expression(1))
            return BinaryExpression(left=left, operator=op, right=right)
        return self.visit(ctx.primary())

    def visitPrimary(self, ctx: AdaParser.PrimaryContext):
        if ctx.identifier():
            name = ctx.identifier(0).getText()
            if ctx.getChildCount() > 1:
                if ctx.getChild(1).getText() == '(':
                    args = [self.visit(e) for e in ctx.expression()]
                    return CallExpression(callee=Identifier(name=name), args=args)
                if ctx.getChild(1).getText() == '.':
                    return MemberAccess(object=Identifier(name=name), member=ctx.identifier(1).getText())
            return Identifier(name=name)
        return self.visit(ctx.literal())

    def visitLiteral(self, ctx: AdaParser.LiteralContext):
        if ctx.integer_literal():
            return Literal(value=int(ctx.integer_literal().getText()))
        if ctx.real_literal():
            return Literal(value=float(ctx.real_literal().getText()))
        if ctx.string_literal():
            return Literal(value=ctx.string_literal().getText().strip('"'))
        if ctx.logical_literal():
            return Literal(value=ctx.logical_literal().getText().upper() == 'TRUE')
        return None

class AdaAntlrFrontend(BabelFrontend):
    @property
    def language_id(self) -> str:
        return "ada"

    @property
    def supported_version(self) -> str:
        return "Ada 95 / 2005"

    @property
    def source_extensions(self) -> list[str]:
        return [".adb", ".ads"]

    def parse(self, source_code: str) -> Program:
        input_stream = InputStream(source_code.upper())
        lexer = AdaLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = AdaParser(stream)
        tree = parser.program()
        
        visitor = RosettaAdaVisitor()
        return visitor.visit(tree)

AdaFrontend = AdaAntlrFrontend
