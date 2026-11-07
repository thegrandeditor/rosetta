# Generated from rosetta/babel/ml/grammar/ML.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,31,193,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,1,0,
        3,0,29,8,0,1,0,1,0,3,0,33,8,0,5,0,35,8,0,10,0,12,0,38,9,0,1,0,1,
        0,1,1,1,1,1,1,3,1,45,8,1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,4,3,55,
        8,3,11,3,12,3,56,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,5,4,68,8,4,
        10,4,12,4,71,9,4,1,5,1,5,1,5,3,5,76,8,5,1,6,1,6,1,7,1,7,1,7,1,7,
        1,7,1,7,1,7,1,7,1,7,1,7,5,7,90,8,7,10,7,12,7,93,9,7,1,7,1,7,1,7,
        1,7,3,7,99,8,7,1,8,1,8,1,8,1,8,1,8,3,8,106,8,8,5,8,108,8,8,10,8,
        12,8,111,9,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,5,8,123,8,8,
        10,8,12,8,126,9,8,3,8,128,8,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,
        8,1,8,1,8,1,8,1,8,1,8,5,8,144,8,8,10,8,12,8,147,9,8,1,9,1,9,1,9,
        1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,5,10,163,8,
        10,10,10,12,10,166,9,10,1,10,1,10,3,10,170,8,10,1,11,1,11,1,12,1,
        12,1,12,1,12,1,12,1,12,3,12,180,8,12,1,12,1,12,1,12,1,12,1,12,1,
        12,5,12,188,8,12,10,12,12,12,191,9,12,1,12,0,2,16,24,13,0,2,4,6,
        8,10,12,14,16,18,20,22,24,0,5,1,0,10,11,1,0,12,13,1,0,14,15,2,0,
        2,2,16,17,2,0,23,25,28,29,210,0,36,1,0,0,0,2,44,1,0,0,0,4,46,1,0,
        0,0,6,51,1,0,0,0,8,61,1,0,0,0,10,72,1,0,0,0,12,77,1,0,0,0,14,98,
        1,0,0,0,16,127,1,0,0,0,18,148,1,0,0,0,20,169,1,0,0,0,22,171,1,0,
        0,0,24,179,1,0,0,0,26,28,3,2,1,0,27,29,5,27,0,0,28,27,1,0,0,0,28,
        29,1,0,0,0,29,35,1,0,0,0,30,32,3,16,8,0,31,33,5,27,0,0,32,31,1,0,
        0,0,32,33,1,0,0,0,33,35,1,0,0,0,34,26,1,0,0,0,34,30,1,0,0,0,35,38,
        1,0,0,0,36,34,1,0,0,0,36,37,1,0,0,0,37,39,1,0,0,0,38,36,1,0,0,0,
        39,40,5,0,0,1,40,1,1,0,0,0,41,45,3,4,2,0,42,45,3,6,3,0,43,45,3,8,
        4,0,44,41,1,0,0,0,44,42,1,0,0,0,44,43,1,0,0,0,45,3,1,0,0,0,46,47,
        5,1,0,0,47,48,3,14,7,0,48,49,5,2,0,0,49,50,3,16,8,0,50,5,1,0,0,0,
        51,52,5,3,0,0,52,54,5,30,0,0,53,55,3,12,6,0,54,53,1,0,0,0,55,56,
        1,0,0,0,56,54,1,0,0,0,56,57,1,0,0,0,57,58,1,0,0,0,58,59,5,2,0,0,
        59,60,3,16,8,0,60,7,1,0,0,0,61,62,5,4,0,0,62,63,5,30,0,0,63,64,5,
        2,0,0,64,69,3,10,5,0,65,66,5,5,0,0,66,68,3,10,5,0,67,65,1,0,0,0,
        68,71,1,0,0,0,69,67,1,0,0,0,69,70,1,0,0,0,70,9,1,0,0,0,71,69,1,0,
        0,0,72,75,5,30,0,0,73,74,5,6,0,0,74,76,3,24,12,0,75,73,1,0,0,0,75,
        76,1,0,0,0,76,11,1,0,0,0,77,78,3,14,7,0,78,13,1,0,0,0,79,99,5,30,
        0,0,80,99,3,22,11,0,81,82,5,7,0,0,82,83,3,14,7,0,83,84,5,8,0,0,84,
        99,1,0,0,0,85,86,5,7,0,0,86,91,3,14,7,0,87,88,5,9,0,0,88,90,3,14,
        7,0,89,87,1,0,0,0,90,93,1,0,0,0,91,89,1,0,0,0,91,92,1,0,0,0,92,94,
        1,0,0,0,93,91,1,0,0,0,94,95,5,8,0,0,95,99,1,0,0,0,96,97,5,30,0,0,
        97,99,3,14,7,0,98,79,1,0,0,0,98,80,1,0,0,0,98,81,1,0,0,0,98,85,1,
        0,0,0,98,96,1,0,0,0,99,15,1,0,0,0,100,101,6,8,-1,0,101,128,3,20,
        10,0,102,109,5,18,0,0,103,105,3,2,1,0,104,106,5,27,0,0,105,104,1,
        0,0,0,105,106,1,0,0,0,106,108,1,0,0,0,107,103,1,0,0,0,108,111,1,
        0,0,0,109,107,1,0,0,0,109,110,1,0,0,0,110,112,1,0,0,0,111,109,1,
        0,0,0,112,113,5,19,0,0,113,114,3,16,8,0,114,115,5,20,0,0,115,128,
        1,0,0,0,116,117,5,21,0,0,117,118,3,16,8,0,118,119,5,6,0,0,119,124,
        3,18,9,0,120,121,5,5,0,0,121,123,3,18,9,0,122,120,1,0,0,0,123,126,
        1,0,0,0,124,122,1,0,0,0,124,125,1,0,0,0,125,128,1,0,0,0,126,124,
        1,0,0,0,127,100,1,0,0,0,127,102,1,0,0,0,127,116,1,0,0,0,128,145,
        1,0,0,0,129,130,10,6,0,0,130,131,7,0,0,0,131,144,3,16,8,7,132,133,
        10,5,0,0,133,134,7,1,0,0,134,144,3,16,8,6,135,136,10,4,0,0,136,137,
        7,2,0,0,137,144,3,16,8,5,138,139,10,3,0,0,139,140,7,3,0,0,140,144,
        3,16,8,4,141,142,10,7,0,0,142,144,3,20,10,0,143,129,1,0,0,0,143,
        132,1,0,0,0,143,135,1,0,0,0,143,138,1,0,0,0,143,141,1,0,0,0,144,
        147,1,0,0,0,145,143,1,0,0,0,145,146,1,0,0,0,146,17,1,0,0,0,147,145,
        1,0,0,0,148,149,3,14,7,0,149,150,5,22,0,0,150,151,3,16,8,0,151,19,
        1,0,0,0,152,170,3,22,11,0,153,170,5,30,0,0,154,155,5,7,0,0,155,156,
        3,16,8,0,156,157,5,8,0,0,157,170,1,0,0,0,158,159,5,7,0,0,159,164,
        3,16,8,0,160,161,5,9,0,0,161,163,3,16,8,0,162,160,1,0,0,0,163,166,
        1,0,0,0,164,162,1,0,0,0,164,165,1,0,0,0,165,167,1,0,0,0,166,164,
        1,0,0,0,167,168,5,8,0,0,168,170,1,0,0,0,169,152,1,0,0,0,169,153,
        1,0,0,0,169,154,1,0,0,0,169,158,1,0,0,0,170,21,1,0,0,0,171,172,7,
        4,0,0,172,23,1,0,0,0,173,174,6,12,-1,0,174,180,5,30,0,0,175,176,
        5,7,0,0,176,177,3,24,12,0,177,178,5,8,0,0,178,180,1,0,0,0,179,173,
        1,0,0,0,179,175,1,0,0,0,180,189,1,0,0,0,181,182,10,3,0,0,182,183,
        5,26,0,0,183,188,3,24,12,4,184,185,10,2,0,0,185,186,5,10,0,0,186,
        188,3,24,12,3,187,181,1,0,0,0,187,184,1,0,0,0,188,191,1,0,0,0,189,
        187,1,0,0,0,189,190,1,0,0,0,190,25,1,0,0,0,191,189,1,0,0,0,21,28,
        32,34,36,44,56,69,75,91,98,105,109,124,127,143,145,164,169,179,187,
        189
    ]

class MLParser ( Parser ):

    grammarFileName = "ML.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'val'", "'='", "'fun'", "'datatype'", 
                     "'|'", "'of'", "'('", "')'", "','", "'*'", "'/'", "'+'", 
                     "'-'", "'::'", "'@'", "'<'", "'>'", "'let'", "'in'", 
                     "'end'", "'case'", "'=>'", "'true'", "'false'", "'[]'", 
                     "'->'", "';'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "SEMI", "NUMBER", 
                      "STRING", "ID", "WS" ]

    RULE_program = 0
    RULE_declaration = 1
    RULE_val_decl = 2
    RULE_fun_decl = 3
    RULE_datatype_decl = 4
    RULE_constructor = 5
    RULE_param = 6
    RULE_pattern = 7
    RULE_expr = 8
    RULE_branch = 9
    RULE_primary = 10
    RULE_literal = 11
    RULE_type_expr = 12

    ruleNames =  [ "program", "declaration", "val_decl", "fun_decl", "datatype_decl", 
                   "constructor", "param", "pattern", "expr", "branch", 
                   "primary", "literal", "type_expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    SEMI=27
    NUMBER=28
    STRING=29
    ID=30
    WS=31

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MLParser.EOF, 0)

        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MLParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(MLParser.DeclarationContext,i)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MLParser.ExprContext)
            else:
                return self.getTypedRuleContext(MLParser.ExprContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(MLParser.SEMI)
            else:
                return self.getToken(MLParser.SEMI, i)

        def getRuleIndex(self):
            return MLParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1940127898) != 0):
                self.state = 34
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1, 3, 4]:
                    self.state = 26
                    self.declaration()
                    self.state = 28
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==27:
                        self.state = 27
                        self.match(MLParser.SEMI)


                    pass
                elif token in [7, 18, 21, 23, 24, 25, 28, 29, 30]:
                    self.state = 30
                    self.expr(0)
                    self.state = 32
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==27:
                        self.state = 31
                        self.match(MLParser.SEMI)


                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 38
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 39
            self.match(MLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def val_decl(self):
            return self.getTypedRuleContext(MLParser.Val_declContext,0)


        def fun_decl(self):
            return self.getTypedRuleContext(MLParser.Fun_declContext,0)


        def datatype_decl(self):
            return self.getTypedRuleContext(MLParser.Datatype_declContext,0)


        def getRuleIndex(self):
            return MLParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = MLParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaration)
        try:
            self.state = 44
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 41
                self.val_decl()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 42
                self.fun_decl()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 3)
                self.state = 43
                self.datatype_decl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Val_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pattern(self):
            return self.getTypedRuleContext(MLParser.PatternContext,0)


        def expr(self):
            return self.getTypedRuleContext(MLParser.ExprContext,0)


        def getRuleIndex(self):
            return MLParser.RULE_val_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVal_decl" ):
                listener.enterVal_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVal_decl" ):
                listener.exitVal_decl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVal_decl" ):
                return visitor.visitVal_decl(self)
            else:
                return visitor.visitChildren(self)




    def val_decl(self):

        localctx = MLParser.Val_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_val_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(MLParser.T__0)
            self.state = 47
            self.pattern()
            self.state = 48
            self.match(MLParser.T__1)
            self.state = 49
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Fun_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MLParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(MLParser.ExprContext,0)


        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MLParser.ParamContext)
            else:
                return self.getTypedRuleContext(MLParser.ParamContext,i)


        def getRuleIndex(self):
            return MLParser.RULE_fun_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFun_decl" ):
                listener.enterFun_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFun_decl" ):
                listener.exitFun_decl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFun_decl" ):
                return visitor.visitFun_decl(self)
            else:
                return visitor.visitChildren(self)




    def fun_decl(self):

        localctx = MLParser.Fun_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_fun_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(MLParser.T__2)
            self.state = 52
            self.match(MLParser.ID)
            self.state = 54 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 53
                self.param()
                self.state = 56 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1937768576) != 0)):
                    break

            self.state = 58
            self.match(MLParser.T__1)
            self.state = 59
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Datatype_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MLParser.ID, 0)

        def constructor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MLParser.ConstructorContext)
            else:
                return self.getTypedRuleContext(MLParser.ConstructorContext,i)


        def getRuleIndex(self):
            return MLParser.RULE_datatype_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDatatype_decl" ):
                listener.enterDatatype_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDatatype_decl" ):
                listener.exitDatatype_decl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDatatype_decl" ):
                return visitor.visitDatatype_decl(self)
            else:
                return visitor.visitChildren(self)




    def datatype_decl(self):

        localctx = MLParser.Datatype_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_datatype_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(MLParser.T__3)
            self.state = 62
            self.match(MLParser.ID)
            self.state = 63
            self.match(MLParser.T__1)
            self.state = 64
            self.constructor()
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 65
                self.match(MLParser.T__4)
                self.state = 66
                self.constructor()
                self.state = 71
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstructorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MLParser.ID, 0)

        def type_expr(self):
            return self.getTypedRuleContext(MLParser.Type_exprContext,0)


        def getRuleIndex(self):
            return MLParser.RULE_constructor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstructor" ):
                listener.enterConstructor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstructor" ):
                listener.exitConstructor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstructor" ):
                return visitor.visitConstructor(self)
            else:
                return visitor.visitChildren(self)




    def constructor(self):

        localctx = MLParser.ConstructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_constructor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(MLParser.ID)
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 73
                self.match(MLParser.T__5)
                self.state = 74
                self.type_expr(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pattern(self):
            return self.getTypedRuleContext(MLParser.PatternContext,0)


        def getRuleIndex(self):
            return MLParser.RULE_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam" ):
                listener.enterParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam" ):
                listener.exitParam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = MLParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.pattern()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PatternContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MLParser.RULE_pattern

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class TuplePatContext(PatternContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MLParser.PatternContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def pattern(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MLParser.PatternContext)
            else:
                return self.getTypedRuleContext(MLParser.PatternContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTuplePat" ):
                listener.enterTuplePat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTuplePat" ):
                listener.exitTuplePat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTuplePat" ):
                return visitor.visitTuplePat(self)
            else:
                return visitor.visitChildren(self)


    class LitPatContext(PatternContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MLParser.PatternContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def literal(self):
            return self.getTypedRuleContext(MLParser.LiteralContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLitPat" ):
                listener.enterLitPat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLitPat" ):
                listener.exitLitPat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLitPat" ):
                return visitor.visitLitPat(self)
            else:
                return visitor.visitChildren(self)


    class ConstrPatContext(PatternContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MLParser.PatternContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(MLParser.ID, 0)
        def pattern(self):
            return self.getTypedRuleContext(MLParser.PatternContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstrPat" ):
                listener.enterConstrPat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstrPat" ):
                listener.exitConstrPat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstrPat" ):
                return visitor.visitConstrPat(self)
            else:
                return visitor.visitChildren(self)


    class IdPatContext(PatternContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MLParser.PatternContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(MLParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdPat" ):
                listener.enterIdPat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdPat" ):
                listener.exitIdPat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdPat" ):
                return visitor.visitIdPat(self)
            else:
                return visitor.visitChildren(self)


    class ParenPatContext(PatternContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MLParser.PatternContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def pattern(self):
            return self.getTypedRuleContext(MLParser.PatternContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenPat" ):
                listener.enterParenPat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenPat" ):
                listener.exitParenPat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenPat" ):
                return visitor.visitParenPat(self)
            else:
                return visitor.visitChildren(self)



    def pattern(self):

        localctx = MLParser.PatternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_pattern)
        self._la = 0 # Token type
        try:
            self.state = 98
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                localctx = MLParser.IdPatContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 79
                self.match(MLParser.ID)
                pass

            elif la_ == 2:
                localctx = MLParser.LitPatContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 80
                self.literal()
                pass

            elif la_ == 3:
                localctx = MLParser.ParenPatContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 81
                self.match(MLParser.T__6)
                self.state = 82
                self.pattern()
                self.state = 83
                self.match(MLParser.T__7)
                pass

            elif la_ == 4:
                localctx = MLParser.TuplePatContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 85
                self.match(MLParser.T__6)
                self.state = 86
                self.pattern()
                self.state = 91
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==9:
                    self.state = 87
                    self.match(MLParser.T__8)
                    self.state = 88
                    self.pattern()
                    self.state = 93
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 94
                self.match(MLParser.T__7)
                pass

            elif la_ == 5:
                localctx = MLParser.ConstrPatContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 96
                self.match(MLParser.ID)
                self.state = 97
                self.pattern()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MLParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class LetExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(MLParser.ExprContext,0)

        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MLParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(MLParser.DeclarationContext,i)

        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(MLParser.SEMI)
            else:
                return self.getToken(MLParser.SEMI, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLetExpr" ):
                listener.enterLetExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLetExpr" ):
                listener.exitLetExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLetExpr" ):
                return visitor.visitLetExpr(self)
            else:
                return visitor.visitChildren(self)


    class AppExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(MLParser.ExprContext,0)

        def primary(self):
            return self.getTypedRuleContext(MLParser.PrimaryContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAppExpr" ):
                listener.enterAppExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAppExpr" ):
                listener.exitAppExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAppExpr" ):
                return visitor.visitAppExpr(self)
            else:
                return visitor.visitChildren(self)


    class PrimaryExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def primary(self):
            return self.getTypedRuleContext(MLParser.PrimaryContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimaryExpr" ):
                listener.enterPrimaryExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimaryExpr" ):
                listener.exitPrimaryExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimaryExpr" ):
                return visitor.visitPrimaryExpr(self)
            else:
                return visitor.visitChildren(self)


    class BinExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MLParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MLParser.ExprContext)
            else:
                return self.getTypedRuleContext(MLParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinExpr" ):
                listener.enterBinExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinExpr" ):
                listener.exitBinExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinExpr" ):
                return visitor.visitBinExpr(self)
            else:
                return visitor.visitChildren(self)


    class CaseExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(MLParser.ExprContext,0)

        def branch(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MLParser.BranchContext)
            else:
                return self.getTypedRuleContext(MLParser.BranchContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCaseExpr" ):
                listener.enterCaseExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCaseExpr" ):
                listener.exitCaseExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCaseExpr" ):
                return visitor.visitCaseExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MLParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7, 23, 24, 25, 28, 29, 30]:
                localctx = MLParser.PrimaryExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 101
                self.primary()
                pass
            elif token in [18]:
                localctx = MLParser.LetExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 102
                self.match(MLParser.T__17)
                self.state = 109
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 26) != 0):
                    self.state = 103
                    self.declaration()
                    self.state = 105
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==27:
                        self.state = 104
                        self.match(MLParser.SEMI)


                    self.state = 111
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 112
                self.match(MLParser.T__18)
                self.state = 113
                self.expr(0)
                self.state = 114
                self.match(MLParser.T__19)
                pass
            elif token in [21]:
                localctx = MLParser.CaseExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 116
                self.match(MLParser.T__20)
                self.state = 117
                self.expr(0)
                self.state = 118
                self.match(MLParser.T__5)
                self.state = 119
                self.branch()
                self.state = 124
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 120
                        self.match(MLParser.T__4)
                        self.state = 121
                        self.branch() 
                    self.state = 126
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 145
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 143
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                    if la_ == 1:
                        localctx = MLParser.BinExprContext(self, MLParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 129
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 130
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==10 or _la==11):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 131
                        self.expr(7)
                        pass

                    elif la_ == 2:
                        localctx = MLParser.BinExprContext(self, MLParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 132
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 133
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==12 or _la==13):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 134
                        self.expr(6)
                        pass

                    elif la_ == 3:
                        localctx = MLParser.BinExprContext(self, MLParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 135
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 136
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==14 or _la==15):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 137
                        self.expr(5)
                        pass

                    elif la_ == 4:
                        localctx = MLParser.BinExprContext(self, MLParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 138
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 139
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 196612) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 140
                        self.expr(4)
                        pass

                    elif la_ == 5:
                        localctx = MLParser.AppExprContext(self, MLParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 141
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 142
                        self.primary()
                        pass

             
                self.state = 147
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class BranchContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pattern(self):
            return self.getTypedRuleContext(MLParser.PatternContext,0)


        def expr(self):
            return self.getTypedRuleContext(MLParser.ExprContext,0)


        def getRuleIndex(self):
            return MLParser.RULE_branch

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBranch" ):
                listener.enterBranch(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBranch" ):
                listener.exitBranch(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBranch" ):
                return visitor.visitBranch(self)
            else:
                return visitor.visitChildren(self)




    def branch(self):

        localctx = MLParser.BranchContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_branch)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.pattern()
            self.state = 149
            self.match(MLParser.T__21)
            self.state = 150
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(MLParser.LiteralContext,0)


        def ID(self):
            return self.getToken(MLParser.ID, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MLParser.ExprContext)
            else:
                return self.getTypedRuleContext(MLParser.ExprContext,i)


        def getRuleIndex(self):
            return MLParser.RULE_primary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary" ):
                listener.enterPrimary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary" ):
                listener.exitPrimary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimary" ):
                return visitor.visitPrimary(self)
            else:
                return visitor.visitChildren(self)




    def primary(self):

        localctx = MLParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_primary)
        self._la = 0 # Token type
        try:
            self.state = 169
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 152
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 153
                self.match(MLParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 154
                self.match(MLParser.T__6)
                self.state = 155
                self.expr(0)
                self.state = 156
                self.match(MLParser.T__7)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 158
                self.match(MLParser.T__6)
                self.state = 159
                self.expr(0)
                self.state = 164
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==9:
                    self.state = 160
                    self.match(MLParser.T__8)
                    self.state = 161
                    self.expr(0)
                    self.state = 166
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 167
                self.match(MLParser.T__7)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(MLParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(MLParser.STRING, 0)

        def getRuleIndex(self):
            return MLParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = MLParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 864026624) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MLParser.ID, 0)

        def type_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MLParser.Type_exprContext)
            else:
                return self.getTypedRuleContext(MLParser.Type_exprContext,i)


        def getRuleIndex(self):
            return MLParser.RULE_type_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_expr" ):
                listener.enterType_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_expr" ):
                listener.exitType_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_expr" ):
                return visitor.visitType_expr(self)
            else:
                return visitor.visitChildren(self)



    def type_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MLParser.Type_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_type_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [30]:
                self.state = 174
                self.match(MLParser.ID)
                pass
            elif token in [7]:
                self.state = 175
                self.match(MLParser.T__6)
                self.state = 176
                self.type_expr(0)
                self.state = 177
                self.match(MLParser.T__7)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 189
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 187
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                    if la_ == 1:
                        localctx = MLParser.Type_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_type_expr)
                        self.state = 181
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 182
                        self.match(MLParser.T__25)
                        self.state = 183
                        self.type_expr(4)
                        pass

                    elif la_ == 2:
                        localctx = MLParser.Type_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_type_expr)
                        self.state = 184
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 185
                        self.match(MLParser.T__9)
                        self.state = 186
                        self.type_expr(3)
                        pass

             
                self.state = 191
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[8] = self.expr_sempred
        self._predicates[12] = self.type_expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 7)
         

    def type_expr_sempred(self, localctx:Type_exprContext, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         




