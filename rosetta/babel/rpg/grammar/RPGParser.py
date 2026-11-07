# Generated from rosetta/babel/rpg/grammar/RPG.g4 by ANTLR 4.13.2
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
        4,1,12,93,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,5,0,24,8,0,10,0,12,0,27,
        9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,38,8,1,1,2,1,2,3,2,42,
        8,2,1,2,1,2,1,3,1,3,3,3,48,8,3,1,3,1,3,1,4,1,4,3,4,54,8,4,1,4,1,
        4,1,5,1,5,3,5,60,8,5,1,5,1,5,1,6,1,6,3,6,66,8,6,1,6,1,6,3,6,70,8,
        6,1,6,3,6,73,8,6,1,6,3,6,76,8,6,1,6,1,6,1,7,1,7,1,8,1,8,1,8,1,9,
        1,9,1,10,1,10,3,10,89,8,10,1,10,1,10,1,10,0,0,11,0,2,4,6,8,10,12,
        14,16,18,20,0,1,1,0,7,9,97,0,25,1,0,0,0,2,37,1,0,0,0,4,39,1,0,0,
        0,6,45,1,0,0,0,8,51,1,0,0,0,10,57,1,0,0,0,12,63,1,0,0,0,14,79,1,
        0,0,0,16,81,1,0,0,0,18,84,1,0,0,0,20,86,1,0,0,0,22,24,3,2,1,0,23,
        22,1,0,0,0,24,27,1,0,0,0,25,23,1,0,0,0,25,26,1,0,0,0,26,28,1,0,0,
        0,27,25,1,0,0,0,28,29,5,0,0,1,29,1,1,0,0,0,30,38,3,4,2,0,31,38,3,
        6,3,0,32,38,3,8,4,0,33,38,3,12,6,0,34,38,3,10,5,0,35,38,3,20,10,
        0,36,38,5,12,0,0,37,30,1,0,0,0,37,31,1,0,0,0,37,32,1,0,0,0,37,33,
        1,0,0,0,37,34,1,0,0,0,37,35,1,0,0,0,37,36,1,0,0,0,38,3,1,0,0,0,39,
        41,5,1,0,0,40,42,5,10,0,0,41,40,1,0,0,0,41,42,1,0,0,0,42,43,1,0,
        0,0,43,44,5,12,0,0,44,5,1,0,0,0,45,47,5,2,0,0,46,48,5,10,0,0,47,
        46,1,0,0,0,47,48,1,0,0,0,48,49,1,0,0,0,49,50,5,12,0,0,50,7,1,0,0,
        0,51,53,5,3,0,0,52,54,5,10,0,0,53,52,1,0,0,0,53,54,1,0,0,0,54,55,
        1,0,0,0,55,56,5,12,0,0,56,9,1,0,0,0,57,59,5,4,0,0,58,60,5,10,0,0,
        59,58,1,0,0,0,59,60,1,0,0,0,60,61,1,0,0,0,61,62,5,12,0,0,62,11,1,
        0,0,0,63,65,5,5,0,0,64,66,3,14,7,0,65,64,1,0,0,0,65,66,1,0,0,0,66,
        67,1,0,0,0,67,69,3,18,9,0,68,70,3,14,7,0,69,68,1,0,0,0,69,70,1,0,
        0,0,70,72,1,0,0,0,71,73,5,7,0,0,72,71,1,0,0,0,72,73,1,0,0,0,73,75,
        1,0,0,0,74,76,3,16,8,0,75,74,1,0,0,0,75,76,1,0,0,0,76,77,1,0,0,0,
        77,78,5,12,0,0,78,13,1,0,0,0,79,80,7,0,0,0,80,15,1,0,0,0,81,82,5,
        6,0,0,82,83,5,7,0,0,83,17,1,0,0,0,84,85,5,7,0,0,85,19,1,0,0,0,86,
        88,5,6,0,0,87,89,5,10,0,0,88,87,1,0,0,0,88,89,1,0,0,0,89,90,1,0,
        0,0,90,91,5,12,0,0,91,21,1,0,0,0,11,25,37,41,47,53,59,65,69,72,75,
        88
    ]

class RPGParser ( Parser ):

    grammarFileName = "RPG.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'H'", "'F'", "'D'", "'O'", "'C'", "'*'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "ID", "NUMBER", 
                      "STRING", "OTHER", "WS", "NL" ]

    RULE_program = 0
    RULE_line = 1
    RULE_h_spec = 2
    RULE_f_spec = 3
    RULE_d_spec = 4
    RULE_o_spec = 5
    RULE_c_spec = 6
    RULE_factor = 7
    RULE_indicator = 8
    RULE_opcode = 9
    RULE_comment = 10

    ruleNames =  [ "program", "line", "h_spec", "f_spec", "d_spec", "o_spec", 
                   "c_spec", "factor", "indicator", "opcode", "comment" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    ID=7
    NUMBER=8
    STRING=9
    OTHER=10
    WS=11
    NL=12

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
            return self.getToken(RPGParser.EOF, 0)

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RPGParser.LineContext)
            else:
                return self.getTypedRuleContext(RPGParser.LineContext,i)


        def getRuleIndex(self):
            return RPGParser.RULE_program

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

        localctx = RPGParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4222) != 0):
                self.state = 22
                self.line()
                self.state = 27
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 28
            self.match(RPGParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def h_spec(self):
            return self.getTypedRuleContext(RPGParser.H_specContext,0)


        def f_spec(self):
            return self.getTypedRuleContext(RPGParser.F_specContext,0)


        def d_spec(self):
            return self.getTypedRuleContext(RPGParser.D_specContext,0)


        def c_spec(self):
            return self.getTypedRuleContext(RPGParser.C_specContext,0)


        def o_spec(self):
            return self.getTypedRuleContext(RPGParser.O_specContext,0)


        def comment(self):
            return self.getTypedRuleContext(RPGParser.CommentContext,0)


        def NL(self):
            return self.getToken(RPGParser.NL, 0)

        def getRuleIndex(self):
            return RPGParser.RULE_line

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLine" ):
                listener.enterLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLine" ):
                listener.exitLine(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLine" ):
                return visitor.visitLine(self)
            else:
                return visitor.visitChildren(self)




    def line(self):

        localctx = RPGParser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_line)
        try:
            self.state = 37
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 30
                self.h_spec()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 31
                self.f_spec()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 32
                self.d_spec()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 4)
                self.state = 33
                self.c_spec()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 5)
                self.state = 34
                self.o_spec()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 6)
                self.state = 35
                self.comment()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 7)
                self.state = 36
                self.match(RPGParser.NL)
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


    class H_specContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NL(self):
            return self.getToken(RPGParser.NL, 0)

        def OTHER(self):
            return self.getToken(RPGParser.OTHER, 0)

        def getRuleIndex(self):
            return RPGParser.RULE_h_spec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterH_spec" ):
                listener.enterH_spec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitH_spec" ):
                listener.exitH_spec(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitH_spec" ):
                return visitor.visitH_spec(self)
            else:
                return visitor.visitChildren(self)




    def h_spec(self):

        localctx = RPGParser.H_specContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_h_spec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(RPGParser.T__0)
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 40
                self.match(RPGParser.OTHER)


            self.state = 43
            self.match(RPGParser.NL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class F_specContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NL(self):
            return self.getToken(RPGParser.NL, 0)

        def OTHER(self):
            return self.getToken(RPGParser.OTHER, 0)

        def getRuleIndex(self):
            return RPGParser.RULE_f_spec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterF_spec" ):
                listener.enterF_spec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitF_spec" ):
                listener.exitF_spec(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitF_spec" ):
                return visitor.visitF_spec(self)
            else:
                return visitor.visitChildren(self)




    def f_spec(self):

        localctx = RPGParser.F_specContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_f_spec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(RPGParser.T__1)
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 46
                self.match(RPGParser.OTHER)


            self.state = 49
            self.match(RPGParser.NL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class D_specContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NL(self):
            return self.getToken(RPGParser.NL, 0)

        def OTHER(self):
            return self.getToken(RPGParser.OTHER, 0)

        def getRuleIndex(self):
            return RPGParser.RULE_d_spec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterD_spec" ):
                listener.enterD_spec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitD_spec" ):
                listener.exitD_spec(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitD_spec" ):
                return visitor.visitD_spec(self)
            else:
                return visitor.visitChildren(self)




    def d_spec(self):

        localctx = RPGParser.D_specContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_d_spec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(RPGParser.T__2)
            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 52
                self.match(RPGParser.OTHER)


            self.state = 55
            self.match(RPGParser.NL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class O_specContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NL(self):
            return self.getToken(RPGParser.NL, 0)

        def OTHER(self):
            return self.getToken(RPGParser.OTHER, 0)

        def getRuleIndex(self):
            return RPGParser.RULE_o_spec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterO_spec" ):
                listener.enterO_spec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitO_spec" ):
                listener.exitO_spec(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitO_spec" ):
                return visitor.visitO_spec(self)
            else:
                return visitor.visitChildren(self)




    def o_spec(self):

        localctx = RPGParser.O_specContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_o_spec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(RPGParser.T__3)
            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 58
                self.match(RPGParser.OTHER)


            self.state = 61
            self.match(RPGParser.NL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class C_specContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.f1 = None # FactorContext
            self.f2 = None # FactorContext
            self.res = None # Token
            self.ind = None # IndicatorContext

        def opcode(self):
            return self.getTypedRuleContext(RPGParser.OpcodeContext,0)


        def NL(self):
            return self.getToken(RPGParser.NL, 0)

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RPGParser.FactorContext)
            else:
                return self.getTypedRuleContext(RPGParser.FactorContext,i)


        def ID(self):
            return self.getToken(RPGParser.ID, 0)

        def indicator(self):
            return self.getTypedRuleContext(RPGParser.IndicatorContext,0)


        def getRuleIndex(self):
            return RPGParser.RULE_c_spec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterC_spec" ):
                listener.enterC_spec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitC_spec" ):
                listener.exitC_spec(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitC_spec" ):
                return visitor.visitC_spec(self)
            else:
                return visitor.visitChildren(self)




    def c_spec(self):

        localctx = RPGParser.C_specContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_c_spec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(RPGParser.T__4)
            self.state = 65
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 64
                localctx.f1 = self.factor()


            self.state = 67
            self.opcode()
            self.state = 69
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 68
                localctx.f2 = self.factor()


            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 71
                localctx.res = self.match(RPGParser.ID)


            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 74
                localctx.ind = self.indicator()


            self.state = 77
            self.match(RPGParser.NL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(RPGParser.ID, 0)

        def NUMBER(self):
            return self.getToken(RPGParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(RPGParser.STRING, 0)

        def getRuleIndex(self):
            return RPGParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = RPGParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 896) != 0)):
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


    class IndicatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(RPGParser.ID, 0)

        def getRuleIndex(self):
            return RPGParser.RULE_indicator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIndicator" ):
                listener.enterIndicator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIndicator" ):
                listener.exitIndicator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndicator" ):
                return visitor.visitIndicator(self)
            else:
                return visitor.visitChildren(self)




    def indicator(self):

        localctx = RPGParser.IndicatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_indicator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(RPGParser.T__5)
            self.state = 82
            self.match(RPGParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpcodeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(RPGParser.ID, 0)

        def getRuleIndex(self):
            return RPGParser.RULE_opcode

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpcode" ):
                listener.enterOpcode(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpcode" ):
                listener.exitOpcode(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpcode" ):
                return visitor.visitOpcode(self)
            else:
                return visitor.visitChildren(self)




    def opcode(self):

        localctx = RPGParser.OpcodeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_opcode)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(RPGParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NL(self):
            return self.getToken(RPGParser.NL, 0)

        def OTHER(self):
            return self.getToken(RPGParser.OTHER, 0)

        def getRuleIndex(self):
            return RPGParser.RULE_comment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComment" ):
                listener.enterComment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComment" ):
                listener.exitComment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComment" ):
                return visitor.visitComment(self)
            else:
                return visitor.visitChildren(self)




    def comment(self):

        localctx = RPGParser.CommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_comment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(RPGParser.T__5)
            self.state = 88
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 87
                self.match(RPGParser.OTHER)


            self.state = 90
            self.match(RPGParser.NL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





