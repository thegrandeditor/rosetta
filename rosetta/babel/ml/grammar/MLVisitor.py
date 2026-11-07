# Generated from rosetta/babel/ml/grammar/ML.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MLParser import MLParser
else:
    from MLParser import MLParser

# This class defines a complete generic visitor for a parse tree produced by MLParser.

class MLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MLParser#program.
    def visitProgram(self, ctx:MLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLParser#declaration.
    def visitDeclaration(self, ctx:MLParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLParser#val_decl.
    def visitVal_decl(self, ctx:MLParser.Val_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLParser#fun_decl.
    def visitFun_decl(self, ctx:MLParser.Fun_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLParser#datatype_decl.
    def visitDatatype_decl(self, ctx:MLParser.Datatype_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLParser#constructor.
    def visitConstructor(self, ctx:MLParser.ConstructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLParser#param.
    def visitParam(self, ctx:MLParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLParser#IdPat.
    def visitIdPat(self, ctx:MLParser.IdPatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLParser#LitPat.
    def visitLitPat(self, ctx:MLParser.LitPatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLParser#ParenPat.
    def visitParenPat(self, ctx:MLParser.ParenPatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLParser#TuplePat.
    def visitTuplePat(self, ctx:MLParser.TuplePatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLParser#ConstrPat.
    def visitConstrPat(self, ctx:MLParser.ConstrPatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLParser#LetExpr.
    def visitLetExpr(self, ctx:MLParser.LetExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLParser#AppExpr.
    def visitAppExpr(self, ctx:MLParser.AppExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLParser#PrimaryExpr.
    def visitPrimaryExpr(self, ctx:MLParser.PrimaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLParser#BinExpr.
    def visitBinExpr(self, ctx:MLParser.BinExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLParser#CaseExpr.
    def visitCaseExpr(self, ctx:MLParser.CaseExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLParser#branch.
    def visitBranch(self, ctx:MLParser.BranchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLParser#primary.
    def visitPrimary(self, ctx:MLParser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLParser#literal.
    def visitLiteral(self, ctx:MLParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLParser#type_expr.
    def visitType_expr(self, ctx:MLParser.Type_exprContext):
        return self.visitChildren(ctx)



del MLParser