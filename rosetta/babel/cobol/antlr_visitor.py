from antlr4 import *
from rosetta.babel.cobol.grammar.CobolParser import CobolParser
from rosetta.babel.cobol.grammar.CobolVisitor import CobolVisitor
from rosetta.ir.nodes import *


def _name(ctx):
    if ctx is None:
        return "temp"
    if ctx.IDENTIFIER():
        name = ctx.IDENTIFIER().getText().replace('-', '_')
    elif ctx.NUMID():
        name = ctx.NUMID().getText().replace('-', '_')
    else:
        name = ctx.getText().replace('-', '_')
    if name and name[0].isdigit():
        name = '_' + name
    return name


class RosettaCobolVisitor(CobolVisitor):

    def visitProgram(self, ctx: CobolParser.ProgramContext):
        body = []
        for child in ctx.children:
            res = self.visit(child)
            if isinstance(res, list):
                body.extend(res)
            elif res is not None:
                body.append(res)
        return Program(body=body)

    def visitIdentificationDivision(self, ctx: CobolParser.IdentificationDivisionContext):
        return None

    def visitIdentificationEntry(self, ctx: CobolParser.IdentificationEntryContext):
        return None

    def visitEnvironmentDivision(self, ctx: CobolParser.EnvironmentDivisionContext):
        return None

    def visitDataDivision(self, ctx: CobolParser.DataDivisionContext):
        nodes = []
        for child in ctx.children:
            res = self.visit(child)
            if isinstance(res, list):
                nodes.extend(res)
            elif res is not None:
                nodes.append(res)
        return nodes

    def visitFileSection(self, ctx: CobolParser.FileSectionContext):
        nodes = []
        for entry in ctx.fileDescriptionEntry():
            res = self.visit(entry)
            if isinstance(res, list):
                nodes.extend(res)
        return nodes

    def _group_data_entries(self, entries):
        parsed = []
        for entry in entries:
            if entry.LEVEL_88():
                continue
            level_text = entry.getChild(0).getText()
            try:
                level = int(level_text)
            except ValueError:
                continue
                
            name = _name(entry.cobolName())
            init = None
            type_hint = 'any'
            
            for clause in entry.dataClause():
                txt = clause.getText().upper()
                if clause.PICTURE_STRING():
                    pic = clause.PICTURE_STRING().getText().upper()
                    if 'X' in pic or 'A' in pic:
                        type_hint = 'str'
                    elif '9' in pic:
                        type_hint = 'int'
                if txt.startswith('VALUE') and clause.literal():
                    init = self.visit(clause.literal())
            
            parsed.append({
                'level': level,
                'name': name,
                'type_hint': type_hint,
                'initializer': init,
                'children': []
            })
            
        # Build hierarchy
        roots = []
        stack = []
        for item in parsed:
            while stack and stack[-1]['level'] >= item['level']:
                stack.pop()
            if stack:
                stack[-1]['children'].append(item)
            else:
                roots.append(item)
            stack.append(item)
            
        # Convert to Rosetta AST nodes
        def to_node(item):
            if item['children']:
                body_nodes = [to_node(child) for child in item['children']]
                return ClassDeclaration(name=item['name'], bases=[], body=body_nodes)
            else:
                return VariableDeclaration(
                    name=item['name'], 
                    type_hint=item['type_hint'], 
                    initializer=item['initializer']
                )
                
        return [to_node(r) for r in roots]

    def visitFileDescriptionEntry(self, ctx: CobolParser.FileDescriptionEntryContext):
        return self._group_data_entries(ctx.dataDescriptionEntry())

    def visitWorkingStorageSection(self, ctx: CobolParser.WorkingStorageSectionContext):
        return self._group_data_entries(ctx.dataDescriptionEntry())

    def visitLinkageSection(self, ctx: CobolParser.LinkageSectionContext):
        return self._group_data_entries(ctx.dataDescriptionEntry())

    def visitDataDescriptionEntry(self, ctx: CobolParser.DataDescriptionEntryContext):
        if ctx.LEVEL_88():
            return None
        name = _name(ctx.cobolName())
        init = None
        type_hint = 'any'
        for clause in ctx.dataClause():
            txt = clause.getText().upper()
            if clause.PICTURE_STRING():
                pic = clause.PICTURE_STRING().getText().upper()
                if 'X' in pic or 'A' in pic:
                    type_hint = 'str'
                elif '9' in pic:
                    type_hint = 'int'
            if txt.startswith('VALUE') and clause.literal():
                init = self.visit(clause.literal())
        return VariableDeclaration(name=name, type_hint=type_hint, initializer=init)

    def visitProcedureDivision(self, ctx: CobolParser.ProcedureDivisionContext):
        return self.visit(ctx.procedureBody())

    def visitProcedureBody(self, ctx: CobolParser.ProcedureBodyContext):
        nodes = []
        for para in ctx.paragraph():
            res = self.visit(para)
            if res is not None:
                nodes.append(res)
        return nodes

    def visitParagraph(self, ctx: CobolParser.ParagraphContext):
        name = _name(ctx.cobolName())
        body = []
        for stmt in ctx.statement():
            res = self.visit(stmt)
            if isinstance(res, list):
                body.extend(res)
            elif res is not None:
                body.append(res)
        return FunctionDeclaration(name=name, params=[], body=body)

    def visitStatement(self, ctx: CobolParser.StatementContext):
        return self.visit(ctx.getChild(0))

    def visitMoveStatement(self, ctx: CobolParser.MoveStatementContext):
        val = self.visit(ctx.expression())
        targets = [Identifier(name=_name(cn)) for cn in ctx.cobolName()]
        if len(targets) == 1:
            return Assignment(target=targets[0], value=val)
        return [Assignment(target=t, value=val) for t in targets]

    def visitDisplayStatement(self, ctx: CobolParser.DisplayStatementContext):
        args = [self.visit(e) for e in ctx.expression()]
        return CallExpression(callee=Identifier(name='print'), args=args)

    def visitStopRunStatement(self, ctx: CobolParser.StopRunStatementContext):
        return CallExpression(callee=Identifier(name='exit'), args=[Literal(value=0)])

    def visitAddStatement(self, ctx: CobolParser.AddStatementContext):
        target_name = _name(ctx.cobolName())
        exprs = [self.visit(e) for e in ctx.expression()]
        rhs = exprs[0] if len(exprs) == 1 else exprs[0]
        for e in exprs[1:]:
            rhs = BinaryExpression(left=rhs, operator='+', right=e)
        value = BinaryExpression(left=Identifier(name=target_name), operator='+', right=rhs)
        return Assignment(target=Identifier(name=target_name), value=value)

    def visitSubtractStatement(self, ctx: CobolParser.SubtractStatementContext):
        target_name = _name(ctx.cobolName())
        exprs = [self.visit(e) for e in ctx.expression()]
        rhs = exprs[0]
        value = BinaryExpression(left=Identifier(name=target_name), operator='-', right=rhs)
        return Assignment(target=Identifier(name=target_name), value=value)

    def visitMultiplyStatement(self, ctx: CobolParser.MultiplyStatementContext):
        target_name = _name(ctx.cobolName())
        val = self.visit(ctx.expression())
        value = BinaryExpression(left=Identifier(name=target_name), operator='*', right=val)
        return Assignment(target=Identifier(name=target_name), value=value)

    def visitDivideStatement(self, ctx: CobolParser.DivideStatementContext):
        target_name = _name(ctx.cobolName())
        val = self.visit(ctx.expression())
        value = BinaryExpression(left=Identifier(name=target_name), operator='/', right=val)
        return Assignment(target=Identifier(name=target_name), value=value)

    def visitComputeStatement(self, ctx: CobolParser.ComputeStatementContext):
        target = Identifier(name=_name(ctx.cobolName()))
        val = self.visit(ctx.expression())
        return Assignment(target=target, value=val)

    def visitInitializeStatement(self, ctx: CobolParser.InitializeStatementContext):
        names = [_name(cn) for cn in ctx.cobolName()]
        return CallExpression(callee=Identifier(name='INITIALIZE'), args=[Identifier(name=n) for n in names])

    def visitSetStatement(self, ctx: CobolParser.SetStatementContext):
        targets = [Identifier(name=_name(cn)) for cn in ctx.cobolName()]
        if ctx.expression():
            val = self.visit(ctx.expression())
        elif ctx.getChild(ctx.getChildCount() - 1).getText().upper() == 'TRUE':
            val = Literal(value=True)
        else:
            val = Literal(value=False)
        if len(targets) == 1:
            return Assignment(target=targets[0], value=val)
        return [Assignment(target=t, value=val) for t in targets]

    def visitIfStatement(self, ctx: CobolParser.IfStatementContext):
        cond = self.visit(ctx.condition())
        stmts = ctx.statement()
        mid = None
        for i, child in enumerate(ctx.children):
            if hasattr(child, 'getText') and child.getText().upper() == 'ELSE':
                mid = i
                break
        if mid is None:
            consequent = []
            for s in stmts:
                res = self.visit(s)
                if isinstance(res, list):
                    consequent.extend(res)
                elif res is not None:
                    consequent.append(res)
            return IfStatement(condition=cond, consequent=consequent)
        else:
            consequent = []
            alternate = []
            past_else = False
            for child in ctx.children:
                txt = child.getText().upper() if hasattr(child, 'getText') else ''
                if txt == 'ELSE':
                    past_else = True
                elif hasattr(child, 'getRuleIndex'):
                    if isinstance(child, CobolParser.StatementContext):
                        res = self.visit(child)
                        if res is not None:
                            if isinstance(res, list):
                                if past_else:
                                    alternate.extend(res)
                                else:
                                    consequent.extend(res)
                            else:
                                if past_else:
                                    alternate.append(res)
                                else:
                                    consequent.append(res)
            return IfStatement(condition=cond, consequent=consequent, alternate=alternate)

    def visitPerformStatement(self, ctx: CobolParser.PerformStatementContext):
        if ctx.cobolName() and len(ctx.cobolName()) > 0:
            name = _name(ctx.cobolName(0))
            if ctx.condition():
                cond = self.visit(ctx.condition())
                return WhileLoop(condition=UnaryExpression(operator='not', argument=cond), body=[CallExpression(callee=Identifier(name=name))])
            return CallExpression(callee=Identifier(name=name))
        else:
            cond = self.visit(ctx.condition()) if ctx.condition() else Literal(value=True)
            body = []
            for s in ctx.statement():
                res = self.visit(s)
                if isinstance(res, list):
                    body.extend(res)
                elif res is not None:
                    body.append(res)
            return WhileLoop(condition=UnaryExpression(operator='not', argument=cond), body=body)

    def visitEvaluateStatement(self, ctx: CobolParser.EvaluateStatementContext):
        subject = self.visit(ctx.expression()) if ctx.expression() else Identifier(name="subject")
        nodes = []
        for wc in ctx.whenClause():
            res = self.visit(wc)
            if res is not None:
                nodes.append(res)
        if ctx.whenOtherClause():
            res = self.visit(ctx.whenOtherClause())
            if res is not None:
                nodes.append(res)
        return nodes if nodes else None

    def visitWhenClause(self, ctx: CobolParser.WhenClauseContext):
        cond_val = self.visit(ctx.expression())
        body = []
        for s in ctx.statement():
            res = self.visit(s)
            if isinstance(res, list):
                body.extend(res)
            elif res is not None:
                body.append(res)
        return IfStatement(condition=cond_val, consequent=body)

    def visitWhenOtherClause(self, ctx: CobolParser.WhenOtherClauseContext):
        body = []
        for s in ctx.statement():
            res = self.visit(s)
            if isinstance(res, list):
                body.extend(res)
            elif res is not None:
                body.append(res)
        return IfStatement(condition=Literal(value=True), consequent=body)

    def visitCallStatement(self, ctx: CobolParser.CallStatementContext):
        callee_name = self.visit(ctx.literal())
        args = [self.visit(e) for e in ctx.expression()]
        return CallExpression(callee=Identifier(name=str(callee_name.value) if isinstance(callee_name, Literal) else callee_name), args=args)

    def visitGoToStatement(self, ctx: CobolParser.GoToStatementContext):
        name = _name(ctx.cobolName())
        return CallExpression(callee=Identifier(name=name))

    def visitSqlStatement(self, ctx: CobolParser.SqlStatementContext):
        sql = ctx.EXEC_SQL_BLOCK().getText()
        sql_body = sql.replace('END-EXEC', '').strip()
        sql_body = sql_body[4:].strip() if sql_body.upper().startswith('EXEC') else sql_body
        sql_body = sql_body[3:].strip() if sql_body.upper().startswith('SQL') else sql_body
        return CallExpression(callee=Identifier(name='EXEC_SQL'), args=[Literal(value=sql_body.strip())])

    def visitFileStatement(self, ctx: CobolParser.FileStatementContext):
        first = ctx.getChild(0).getText().upper()
        if first == 'OPEN':
            nodes = []
            for phrase in ctx.openPhrase():
                mode = phrase.getChild(0).getText()
                for cn in phrase.cobolName():
                    nodes.append(CallExpression(callee=Identifier(name='OPEN'), args=[Identifier(name=_name(cn)), Literal(value=mode)]))
            return nodes
        elif first == 'READ':
            target = _name(ctx.cobolName(0))
            return CallExpression(callee=Identifier(name='READ'), args=[Identifier(name=target)])
        elif first == 'WRITE':
            target = _name(ctx.cobolName(0))
            return CallExpression(callee=Identifier(name='WRITE'), args=[Identifier(name=target)])
        elif first == 'CLOSE':
            nodes = [CallExpression(callee=Identifier(name='CLOSE'), args=[Identifier(name=_name(cn))]) for cn in ctx.cobolName()]
            return nodes
        return None

    def visitCopyStatement(self, ctx: CobolParser.CopyStatementContext):
        name = _name(ctx.cobolName(0))
        return ModuleDeclaration(name=name, body=[])

    def visitCondition(self, ctx: CobolParser.ConditionContext):
        if ctx.getChildCount() == 1:
            return Identifier(name=_name(ctx.cobolName()))
        if ctx.getChildCount() == 2:
            arg = self.visit(ctx.condition(0))
            return UnaryExpression(operator='not', argument=arg)
        if ctx.operator():
            left = self.visit(ctx.expression(0))
            op = ctx.operator().getText()
            if op == '=': op = '=='
            elif op == 'NOT=': op = '!='
            elif op == 'NOT<': op = '>='
            elif op == 'NOT>': op = '<='
            right = self.visit(ctx.expression(1))
            return BinaryExpression(left=left, operator=op, right=right)
        left = self.visit(ctx.condition(0))
        op = ctx.getChild(1).getText().lower()
        right = self.visit(ctx.condition(1))
        return BinaryExpression(left=left, operator=op, right=right)

    def visitExpression(self, ctx: CobolParser.ExpressionContext):
        if ctx is None:
            return None
        if ctx.getChildCount() == 1:
            if ctx.cobolName():
                return Identifier(name=_name(ctx.cobolName()))
            if ctx.literal():
                return self.visit(ctx.literal())
            return Literal(value=ctx.getText())
        if ctx.getChildCount() == 3:
            if ctx.getChild(0).getText() == '(':
                return self.visit(ctx.expression(0)) if ctx.expression(0) else None
            left = self.visit(ctx.expression(0)) if ctx.expression(0) else Identifier(name="unknown")
            op = ctx.getChild(1).getText()
            right = self.visit(ctx.expression(1)) if ctx.expression(1) else Identifier(name="unknown")
            return BinaryExpression(left=left, operator=op, right=right)
        return Literal(value=ctx.getText())

    def visitLiteral(self, ctx: CobolParser.LiteralContext):
        if ctx is None:
            return None
        if ctx.STRING():
            return Literal(value=ctx.STRING().getText().strip("\u0027\u0022"))
        if ctx.anyNumber():
            return self.visit(ctx.anyNumber())
        if ctx.specialLiteral():
            return self.visit(ctx.specialLiteral())
        return Literal(value=ctx.getText())

    def visitAnyNumber(self, ctx: CobolParser.AnyNumberContext):
        txt = ctx.getText()
        try:
            return Literal(value=float(txt) if '.' in txt else int(txt))
        except ValueError:
            return Literal(value=0)

    def visitSpecialLiteral(self, ctx: CobolParser.SpecialLiteralContext):
        txt = ctx.getText().upper()
        if txt in ('SPACES', 'SPACE'):
            return Literal(value=' ')
        if txt in ('ZEROS', 'ZERO', 'ZEROES'):
            return Literal(value=0)
        if txt == 'TRUE':
            return Literal(value=True)
        if txt == 'FALSE':
            return Literal(value=False)
        return Literal(value=txt)

    def visitCobolName(self, ctx: CobolParser.CobolNameContext):
        return Identifier(name=_name(ctx))
