from antlr4 import *
from rosetta.babel.rpg.grammar.RPGParser import RPGParser
from rosetta.babel.rpg.grammar.RPGVisitor import RPGVisitor
from rosetta.ir.nodes import *

class RosettaRPGVisitor(RPGVisitor):
    def visitProgram(self, ctx: RPGParser.ProgramContext):
        body = []
        for child in ctx.line():
            res = self.visit(child)
            if res:
                if isinstance(res, list): body.extend(res)
                else: body.append(res)
        return Program(body=body)

    def visitC_spec(self, ctx: RPGParser.C_specContext):
        opcode = ctx.opcode().getText().upper()
        f1 = self.visit(ctx.f1) if ctx.f1 else None
        f2 = self.visit(ctx.f2) if ctx.f2 else None
        res = Identifier(name=ctx.res.getText()) if ctx.res else None
        indicators = [ctx.ind.getText()] if ctx.ind else []
        
        return RPGOperation(opcode=opcode, factor1=f1, factor2=f2, result=res, indicators=indicators)

    def visitFactor(self, ctx: RPGParser.FactorContext):
        if ctx.ID(): return Identifier(name=ctx.ID().getText())
        if ctx.NUMBER(): return Literal(value=int(ctx.NUMBER().getText()))
        if ctx.STRING(): return Literal(value=ctx.STRING().getText().strip("'"))
        return None

    def visitLine(self, ctx: RPGParser.LineContext):
        if ctx.c_spec(): return self.visit(ctx.c_spec())
        return None # Ignore other specs for now or map to generic nodes
