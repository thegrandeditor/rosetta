# Generated from rosetta/babel/ml/grammar/ML.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MLParser import MLParser
else:
    from MLParser import MLParser

# This class defines a complete listener for a parse tree produced by MLParser.
class MLListener(ParseTreeListener):

    # Enter a parse tree produced by MLParser#program.
    def enterProgram(self, ctx:MLParser.ProgramContext):
        pass

    # Exit a parse tree produced by MLParser#program.
    def exitProgram(self, ctx:MLParser.ProgramContext):
        pass


    # Enter a parse tree produced by MLParser#declaration.
    def enterDeclaration(self, ctx:MLParser.DeclarationContext):
        pass

    # Exit a parse tree produced by MLParser#declaration.
    def exitDeclaration(self, ctx:MLParser.DeclarationContext):
        pass


    # Enter a parse tree produced by MLParser#val_decl.
    def enterVal_decl(self, ctx:MLParser.Val_declContext):
        pass

    # Exit a parse tree produced by MLParser#val_decl.
    def exitVal_decl(self, ctx:MLParser.Val_declContext):
        pass


    # Enter a parse tree produced by MLParser#fun_decl.
    def enterFun_decl(self, ctx:MLParser.Fun_declContext):
        pass

    # Exit a parse tree produced by MLParser#fun_decl.
    def exitFun_decl(self, ctx:MLParser.Fun_declContext):
        pass


    # Enter a parse tree produced by MLParser#datatype_decl.
    def enterDatatype_decl(self, ctx:MLParser.Datatype_declContext):
        pass

    # Exit a parse tree produced by MLParser#datatype_decl.
    def exitDatatype_decl(self, ctx:MLParser.Datatype_declContext):
        pass


    # Enter a parse tree produced by MLParser#constructor.
    def enterConstructor(self, ctx:MLParser.ConstructorContext):
        pass

    # Exit a parse tree produced by MLParser#constructor.
    def exitConstructor(self, ctx:MLParser.ConstructorContext):
        pass


    # Enter a parse tree produced by MLParser#param.
    def enterParam(self, ctx:MLParser.ParamContext):
        pass

    # Exit a parse tree produced by MLParser#param.
    def exitParam(self, ctx:MLParser.ParamContext):
        pass


    # Enter a parse tree produced by MLParser#IdPat.
    def enterIdPat(self, ctx:MLParser.IdPatContext):
        pass

    # Exit a parse tree produced by MLParser#IdPat.
    def exitIdPat(self, ctx:MLParser.IdPatContext):
        pass


    # Enter a parse tree produced by MLParser#LitPat.
    def enterLitPat(self, ctx:MLParser.LitPatContext):
        pass

    # Exit a parse tree produced by MLParser#LitPat.
    def exitLitPat(self, ctx:MLParser.LitPatContext):
        pass


    # Enter a parse tree produced by MLParser#ParenPat.
    def enterParenPat(self, ctx:MLParser.ParenPatContext):
        pass

    # Exit a parse tree produced by MLParser#ParenPat.
    def exitParenPat(self, ctx:MLParser.ParenPatContext):
        pass


    # Enter a parse tree produced by MLParser#TuplePat.
    def enterTuplePat(self, ctx:MLParser.TuplePatContext):
        pass

    # Exit a parse tree produced by MLParser#TuplePat.
    def exitTuplePat(self, ctx:MLParser.TuplePatContext):
        pass


    # Enter a parse tree produced by MLParser#ConstrPat.
    def enterConstrPat(self, ctx:MLParser.ConstrPatContext):
        pass

    # Exit a parse tree produced by MLParser#ConstrPat.
    def exitConstrPat(self, ctx:MLParser.ConstrPatContext):
        pass


    # Enter a parse tree produced by MLParser#LetExpr.
    def enterLetExpr(self, ctx:MLParser.LetExprContext):
        pass

    # Exit a parse tree produced by MLParser#LetExpr.
    def exitLetExpr(self, ctx:MLParser.LetExprContext):
        pass


    # Enter a parse tree produced by MLParser#AppExpr.
    def enterAppExpr(self, ctx:MLParser.AppExprContext):
        pass

    # Exit a parse tree produced by MLParser#AppExpr.
    def exitAppExpr(self, ctx:MLParser.AppExprContext):
        pass


    # Enter a parse tree produced by MLParser#PrimaryExpr.
    def enterPrimaryExpr(self, ctx:MLParser.PrimaryExprContext):
        pass

    # Exit a parse tree produced by MLParser#PrimaryExpr.
    def exitPrimaryExpr(self, ctx:MLParser.PrimaryExprContext):
        pass


    # Enter a parse tree produced by MLParser#BinExpr.
    def enterBinExpr(self, ctx:MLParser.BinExprContext):
        pass

    # Exit a parse tree produced by MLParser#BinExpr.
    def exitBinExpr(self, ctx:MLParser.BinExprContext):
        pass


    # Enter a parse tree produced by MLParser#CaseExpr.
    def enterCaseExpr(self, ctx:MLParser.CaseExprContext):
        pass

    # Exit a parse tree produced by MLParser#CaseExpr.
    def exitCaseExpr(self, ctx:MLParser.CaseExprContext):
        pass


    # Enter a parse tree produced by MLParser#branch.
    def enterBranch(self, ctx:MLParser.BranchContext):
        pass

    # Exit a parse tree produced by MLParser#branch.
    def exitBranch(self, ctx:MLParser.BranchContext):
        pass


    # Enter a parse tree produced by MLParser#primary.
    def enterPrimary(self, ctx:MLParser.PrimaryContext):
        pass

    # Exit a parse tree produced by MLParser#primary.
    def exitPrimary(self, ctx:MLParser.PrimaryContext):
        pass


    # Enter a parse tree produced by MLParser#literal.
    def enterLiteral(self, ctx:MLParser.LiteralContext):
        pass

    # Exit a parse tree produced by MLParser#literal.
    def exitLiteral(self, ctx:MLParser.LiteralContext):
        pass


    # Enter a parse tree produced by MLParser#type_expr.
    def enterType_expr(self, ctx:MLParser.Type_exprContext):
        pass

    # Exit a parse tree produced by MLParser#type_expr.
    def exitType_expr(self, ctx:MLParser.Type_exprContext):
        pass



del MLParser