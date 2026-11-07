# Generated from rosetta/babel/basic/grammar/Basic.g4 by ANTLR 4.13.2
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
        4,1,42,224,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,1,0,1,0,5,0,49,8,0,10,0,12,0,52,9,0,1,0,
        1,0,1,1,3,1,57,8,1,1,1,1,1,4,1,61,8,1,11,1,12,1,62,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,78,8,2,1,3,3,3,81,8,3,
        1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,5,4,91,8,4,10,4,12,4,94,9,4,3,4,
        96,8,4,1,5,1,5,3,5,100,8,5,1,5,3,5,103,8,5,1,5,1,5,1,5,5,5,108,8,
        5,10,5,12,5,111,9,5,1,6,1,6,1,6,3,6,116,8,6,1,7,1,7,1,7,3,7,121,
        8,7,1,8,1,8,1,9,1,9,1,9,1,9,1,9,3,9,130,8,9,1,9,1,9,1,9,3,9,135,
        8,9,3,9,137,8,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,147,
        8,10,1,11,1,11,3,11,151,8,11,1,12,1,12,1,12,1,13,1,13,1,14,1,14,
        1,15,1,15,1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,
        1,17,3,17,174,8,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,
        1,17,1,17,1,17,1,17,1,17,1,17,5,17,191,8,17,10,17,12,17,194,9,17,
        1,18,1,18,1,18,1,18,1,18,5,18,201,8,18,10,18,12,18,204,9,18,1,18,
        1,18,3,18,208,8,18,1,18,3,18,211,8,18,1,19,1,19,1,19,3,19,216,8,
        19,1,20,1,20,1,21,1,21,1,22,1,22,1,22,0,1,34,23,0,2,4,6,8,10,12,
        14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,0,4,1,0,6,7,1,0,
        9,14,1,0,15,16,1,0,17,18,242,0,50,1,0,0,0,2,56,1,0,0,0,4,77,1,0,
        0,0,6,80,1,0,0,0,8,86,1,0,0,0,10,97,1,0,0,0,12,112,1,0,0,0,14,117,
        1,0,0,0,16,122,1,0,0,0,18,124,1,0,0,0,20,138,1,0,0,0,22,148,1,0,
        0,0,24,152,1,0,0,0,26,155,1,0,0,0,28,157,1,0,0,0,30,159,1,0,0,0,
        32,161,1,0,0,0,34,173,1,0,0,0,36,210,1,0,0,0,38,215,1,0,0,0,40,217,
        1,0,0,0,42,219,1,0,0,0,44,221,1,0,0,0,46,49,3,2,1,0,47,49,5,41,0,
        0,48,46,1,0,0,0,48,47,1,0,0,0,49,52,1,0,0,0,50,48,1,0,0,0,50,51,
        1,0,0,0,51,53,1,0,0,0,52,50,1,0,0,0,53,54,5,0,0,1,54,1,1,0,0,0,55,
        57,5,38,0,0,56,55,1,0,0,0,56,57,1,0,0,0,57,58,1,0,0,0,58,60,3,4,
        2,0,59,61,5,41,0,0,60,59,1,0,0,0,61,62,1,0,0,0,62,60,1,0,0,0,62,
        63,1,0,0,0,63,3,1,0,0,0,64,78,3,6,3,0,65,78,3,8,4,0,66,78,3,10,5,
        0,67,78,3,12,6,0,68,78,3,14,7,0,69,78,3,16,8,0,70,78,3,18,9,0,71,
        78,3,20,10,0,72,78,3,22,11,0,73,78,3,24,12,0,74,78,3,26,13,0,75,
        78,3,28,14,0,76,78,3,30,15,0,77,64,1,0,0,0,77,65,1,0,0,0,77,66,1,
        0,0,0,77,67,1,0,0,0,77,68,1,0,0,0,77,69,1,0,0,0,77,70,1,0,0,0,77,
        71,1,0,0,0,77,72,1,0,0,0,77,73,1,0,0,0,77,74,1,0,0,0,77,75,1,0,0,
        0,77,76,1,0,0,0,78,5,1,0,0,0,79,81,5,20,0,0,80,79,1,0,0,0,80,81,
        1,0,0,0,81,82,1,0,0,0,82,83,3,32,16,0,83,84,5,1,0,0,84,85,3,34,17,
        0,85,7,1,0,0,0,86,95,5,21,0,0,87,92,3,34,17,0,88,89,5,2,0,0,89,91,
        3,34,17,0,90,88,1,0,0,0,91,94,1,0,0,0,92,90,1,0,0,0,92,93,1,0,0,
        0,93,96,1,0,0,0,94,92,1,0,0,0,95,87,1,0,0,0,95,96,1,0,0,0,96,9,1,
        0,0,0,97,99,5,22,0,0,98,100,3,44,22,0,99,98,1,0,0,0,99,100,1,0,0,
        0,100,102,1,0,0,0,101,103,5,3,0,0,102,101,1,0,0,0,102,103,1,0,0,
        0,103,104,1,0,0,0,104,109,3,32,16,0,105,106,5,2,0,0,106,108,3,32,
        16,0,107,105,1,0,0,0,108,111,1,0,0,0,109,107,1,0,0,0,109,110,1,0,
        0,0,110,11,1,0,0,0,111,109,1,0,0,0,112,115,5,23,0,0,113,116,3,32,
        16,0,114,116,5,38,0,0,115,113,1,0,0,0,115,114,1,0,0,0,116,13,1,0,
        0,0,117,120,5,24,0,0,118,121,3,32,16,0,119,121,5,38,0,0,120,118,
        1,0,0,0,120,119,1,0,0,0,121,15,1,0,0,0,122,123,5,25,0,0,123,17,1,
        0,0,0,124,125,5,26,0,0,125,126,3,34,17,0,126,129,5,27,0,0,127,130,
        3,4,2,0,128,130,5,38,0,0,129,127,1,0,0,0,129,128,1,0,0,0,130,136,
        1,0,0,0,131,134,5,28,0,0,132,135,3,4,2,0,133,135,5,38,0,0,134,132,
        1,0,0,0,134,133,1,0,0,0,135,137,1,0,0,0,136,131,1,0,0,0,136,137,
        1,0,0,0,137,19,1,0,0,0,138,139,5,29,0,0,139,140,3,32,16,0,140,141,
        5,1,0,0,141,142,3,34,17,0,142,143,5,30,0,0,143,146,3,34,17,0,144,
        145,5,31,0,0,145,147,3,34,17,0,146,144,1,0,0,0,146,147,1,0,0,0,147,
        21,1,0,0,0,148,150,5,32,0,0,149,151,3,32,16,0,150,149,1,0,0,0,150,
        151,1,0,0,0,151,23,1,0,0,0,152,153,5,33,0,0,153,154,3,34,17,0,154,
        25,1,0,0,0,155,156,5,34,0,0,156,27,1,0,0,0,157,158,5,35,0,0,158,
        29,1,0,0,0,159,160,5,36,0,0,160,31,1,0,0,0,161,162,5,37,0,0,162,
        33,1,0,0,0,163,164,6,17,-1,0,164,165,5,8,0,0,165,174,3,34,17,8,166,
        167,5,16,0,0,167,174,3,34,17,3,168,169,5,4,0,0,169,170,3,34,17,0,
        170,171,5,5,0,0,171,174,1,0,0,0,172,174,3,36,18,0,173,163,1,0,0,
        0,173,166,1,0,0,0,173,168,1,0,0,0,173,172,1,0,0,0,174,192,1,0,0,
        0,175,176,10,9,0,0,176,177,7,0,0,0,177,191,3,34,17,10,178,179,10,
        7,0,0,179,180,7,1,0,0,180,191,3,34,17,8,181,182,10,6,0,0,182,183,
        7,2,0,0,183,191,3,34,17,7,184,185,10,5,0,0,185,186,7,3,0,0,186,191,
        3,34,17,6,187,188,10,4,0,0,188,189,5,19,0,0,189,191,3,34,17,5,190,
        175,1,0,0,0,190,178,1,0,0,0,190,181,1,0,0,0,190,184,1,0,0,0,190,
        187,1,0,0,0,191,194,1,0,0,0,192,190,1,0,0,0,192,193,1,0,0,0,193,
        35,1,0,0,0,194,192,1,0,0,0,195,207,3,32,16,0,196,197,5,4,0,0,197,
        202,3,34,17,0,198,199,5,2,0,0,199,201,3,34,17,0,200,198,1,0,0,0,
        201,204,1,0,0,0,202,200,1,0,0,0,202,203,1,0,0,0,203,205,1,0,0,0,
        204,202,1,0,0,0,205,206,5,5,0,0,206,208,1,0,0,0,207,196,1,0,0,0,
        207,208,1,0,0,0,208,211,1,0,0,0,209,211,3,38,19,0,210,195,1,0,0,
        0,210,209,1,0,0,0,211,37,1,0,0,0,212,216,3,40,20,0,213,216,3,42,
        21,0,214,216,3,44,22,0,215,212,1,0,0,0,215,213,1,0,0,0,215,214,1,
        0,0,0,216,39,1,0,0,0,217,218,5,38,0,0,218,41,1,0,0,0,219,220,5,39,
        0,0,220,43,1,0,0,0,221,222,5,40,0,0,222,45,1,0,0,0,25,48,50,56,62,
        77,80,92,95,99,102,109,115,120,129,134,136,146,150,173,190,192,202,
        207,210,215
    ]

class BasicParser ( Parser ):

    grammarFileName = "Basic.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "','", "';'", "'('", "')'", "'OR'", 
                     "'AND'", "'NOT'", "<INVALID>", "<INVALID>", "'<'", 
                     "'<='", "'>'", "'>='", "'+'", "'-'", "'*'", "'/'", 
                     "<INVALID>", "'LET'", "<INVALID>", "'INPUT'", "'GOTO'", 
                     "'GOSUB'", "'RETURN'", "'IF'", "'THEN'", "'ELSE'", 
                     "'FOR'", "'TO'", "'STEP'", "'NEXT'", "'WHILE'", "'WEND'", 
                     "'END'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "OR", "AND", "NOT", "EQ", 
                      "NE", "LT", "LE", "GT", "GE", "PLUS", "MINUS", "STAR", 
                      "SLASH", "POWER", "LET_K", "PRINT_K", "INPUT_K", "GOTO_K", 
                      "GOSUB_K", "RETURN_K", "IF_K", "THEN_K", "ELSE_K", 
                      "FOR_K", "TO_K", "STEP_K", "NEXT_K", "WHILE_K", "WEND_K", 
                      "END_K", "REMARK", "IDENTIFIER", "INTEGER", "REAL", 
                      "STRING", "NEWLINE", "WS" ]

    RULE_program = 0
    RULE_line = 1
    RULE_statement = 2
    RULE_let_stmt = 3
    RULE_print_stmt = 4
    RULE_input_stmt = 5
    RULE_goto_stmt = 6
    RULE_gosub_stmt = 7
    RULE_return_stmt = 8
    RULE_if_stmt = 9
    RULE_for_stmt = 10
    RULE_next_stmt = 11
    RULE_while_stmt = 12
    RULE_wend_stmt = 13
    RULE_end_stmt = 14
    RULE_remark_stmt = 15
    RULE_identifier = 16
    RULE_expression = 17
    RULE_primary = 18
    RULE_literal = 19
    RULE_integer_literal = 20
    RULE_real_literal = 21
    RULE_string_literal = 22

    ruleNames =  [ "program", "line", "statement", "let_stmt", "print_stmt", 
                   "input_stmt", "goto_stmt", "gosub_stmt", "return_stmt", 
                   "if_stmt", "for_stmt", "next_stmt", "while_stmt", "wend_stmt", 
                   "end_stmt", "remark_stmt", "identifier", "expression", 
                   "primary", "literal", "integer_literal", "real_literal", 
                   "string_literal" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    OR=6
    AND=7
    NOT=8
    EQ=9
    NE=10
    LT=11
    LE=12
    GT=13
    GE=14
    PLUS=15
    MINUS=16
    STAR=17
    SLASH=18
    POWER=19
    LET_K=20
    PRINT_K=21
    INPUT_K=22
    GOTO_K=23
    GOSUB_K=24
    RETURN_K=25
    IF_K=26
    THEN_K=27
    ELSE_K=28
    FOR_K=29
    TO_K=30
    STEP_K=31
    NEXT_K=32
    WHILE_K=33
    WEND_K=34
    END_K=35
    REMARK=36
    IDENTIFIER=37
    INTEGER=38
    REAL=39
    STRING=40
    NEWLINE=41
    WS=42

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
            return self.getToken(BasicParser.EOF, 0)

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicParser.LineContext)
            else:
                return self.getTypedRuleContext(BasicParser.LineContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(BasicParser.NEWLINE)
            else:
                return self.getToken(BasicParser.NEWLINE, i)

        def getRuleIndex(self):
            return BasicParser.RULE_program

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

        localctx = BasicParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2745154142208) != 0):
                self.state = 48
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [20, 21, 22, 23, 24, 25, 26, 29, 32, 33, 34, 35, 36, 37, 38]:
                    self.state = 46
                    self.line()
                    pass
                elif token in [41]:
                    self.state = 47
                    self.match(BasicParser.NEWLINE)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 52
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 53
            self.match(BasicParser.EOF)
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

        def statement(self):
            return self.getTypedRuleContext(BasicParser.StatementContext,0)


        def INTEGER(self):
            return self.getToken(BasicParser.INTEGER, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(BasicParser.NEWLINE)
            else:
                return self.getToken(BasicParser.NEWLINE, i)

        def getRuleIndex(self):
            return BasicParser.RULE_line

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

        localctx = BasicParser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_line)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==38:
                self.state = 55
                self.match(BasicParser.INTEGER)


            self.state = 58
            self.statement()
            self.state = 60 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 59
                    self.match(BasicParser.NEWLINE)

                else:
                    raise NoViableAltException(self)
                self.state = 62 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def let_stmt(self):
            return self.getTypedRuleContext(BasicParser.Let_stmtContext,0)


        def print_stmt(self):
            return self.getTypedRuleContext(BasicParser.Print_stmtContext,0)


        def input_stmt(self):
            return self.getTypedRuleContext(BasicParser.Input_stmtContext,0)


        def goto_stmt(self):
            return self.getTypedRuleContext(BasicParser.Goto_stmtContext,0)


        def gosub_stmt(self):
            return self.getTypedRuleContext(BasicParser.Gosub_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(BasicParser.Return_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(BasicParser.If_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(BasicParser.For_stmtContext,0)


        def next_stmt(self):
            return self.getTypedRuleContext(BasicParser.Next_stmtContext,0)


        def while_stmt(self):
            return self.getTypedRuleContext(BasicParser.While_stmtContext,0)


        def wend_stmt(self):
            return self.getTypedRuleContext(BasicParser.Wend_stmtContext,0)


        def end_stmt(self):
            return self.getTypedRuleContext(BasicParser.End_stmtContext,0)


        def remark_stmt(self):
            return self.getTypedRuleContext(BasicParser.Remark_stmtContext,0)


        def getRuleIndex(self):
            return BasicParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = BasicParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 77
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20, 37]:
                self.enterOuterAlt(localctx, 1)
                self.state = 64
                self.let_stmt()
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 65
                self.print_stmt()
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 3)
                self.state = 66
                self.input_stmt()
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 4)
                self.state = 67
                self.goto_stmt()
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 5)
                self.state = 68
                self.gosub_stmt()
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 6)
                self.state = 69
                self.return_stmt()
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 7)
                self.state = 70
                self.if_stmt()
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 8)
                self.state = 71
                self.for_stmt()
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 9)
                self.state = 72
                self.next_stmt()
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 10)
                self.state = 73
                self.while_stmt()
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 11)
                self.state = 74
                self.wend_stmt()
                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 12)
                self.state = 75
                self.end_stmt()
                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 13)
                self.state = 76
                self.remark_stmt()
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


    class Let_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(BasicParser.IdentifierContext,0)


        def expression(self):
            return self.getTypedRuleContext(BasicParser.ExpressionContext,0)


        def LET_K(self):
            return self.getToken(BasicParser.LET_K, 0)

        def getRuleIndex(self):
            return BasicParser.RULE_let_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLet_stmt" ):
                listener.enterLet_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLet_stmt" ):
                listener.exitLet_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLet_stmt" ):
                return visitor.visitLet_stmt(self)
            else:
                return visitor.visitChildren(self)




    def let_stmt(self):

        localctx = BasicParser.Let_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_let_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 79
                self.match(BasicParser.LET_K)


            self.state = 82
            self.identifier()
            self.state = 83
            self.match(BasicParser.T__0)
            self.state = 84
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Print_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT_K(self):
            return self.getToken(BasicParser.PRINT_K, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BasicParser.ExpressionContext,i)


        def getRuleIndex(self):
            return BasicParser.RULE_print_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint_stmt" ):
                listener.enterPrint_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint_stmt" ):
                listener.exitPrint_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint_stmt" ):
                return visitor.visitPrint_stmt(self)
            else:
                return visitor.visitChildren(self)




    def print_stmt(self):

        localctx = BasicParser.Print_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_print_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(BasicParser.PRINT_K)
            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2061584367888) != 0):
                self.state = 87
                self.expression(0)
                self.state = 92
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 88
                    self.match(BasicParser.T__1)
                    self.state = 89
                    self.expression(0)
                    self.state = 94
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Input_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INPUT_K(self):
            return self.getToken(BasicParser.INPUT_K, 0)

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(BasicParser.IdentifierContext,i)


        def string_literal(self):
            return self.getTypedRuleContext(BasicParser.String_literalContext,0)


        def getRuleIndex(self):
            return BasicParser.RULE_input_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInput_stmt" ):
                listener.enterInput_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInput_stmt" ):
                listener.exitInput_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInput_stmt" ):
                return visitor.visitInput_stmt(self)
            else:
                return visitor.visitChildren(self)




    def input_stmt(self):

        localctx = BasicParser.Input_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_input_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(BasicParser.INPUT_K)
            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==40:
                self.state = 98
                self.string_literal()


            self.state = 102
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 101
                self.match(BasicParser.T__2)


            self.state = 104
            self.identifier()
            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 105
                self.match(BasicParser.T__1)
                self.state = 106
                self.identifier()
                self.state = 111
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Goto_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GOTO_K(self):
            return self.getToken(BasicParser.GOTO_K, 0)

        def identifier(self):
            return self.getTypedRuleContext(BasicParser.IdentifierContext,0)


        def INTEGER(self):
            return self.getToken(BasicParser.INTEGER, 0)

        def getRuleIndex(self):
            return BasicParser.RULE_goto_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGoto_stmt" ):
                listener.enterGoto_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGoto_stmt" ):
                listener.exitGoto_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGoto_stmt" ):
                return visitor.visitGoto_stmt(self)
            else:
                return visitor.visitChildren(self)




    def goto_stmt(self):

        localctx = BasicParser.Goto_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_goto_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(BasicParser.GOTO_K)
            self.state = 115
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [37]:
                self.state = 113
                self.identifier()
                pass
            elif token in [38]:
                self.state = 114
                self.match(BasicParser.INTEGER)
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


    class Gosub_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GOSUB_K(self):
            return self.getToken(BasicParser.GOSUB_K, 0)

        def identifier(self):
            return self.getTypedRuleContext(BasicParser.IdentifierContext,0)


        def INTEGER(self):
            return self.getToken(BasicParser.INTEGER, 0)

        def getRuleIndex(self):
            return BasicParser.RULE_gosub_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGosub_stmt" ):
                listener.enterGosub_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGosub_stmt" ):
                listener.exitGosub_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGosub_stmt" ):
                return visitor.visitGosub_stmt(self)
            else:
                return visitor.visitChildren(self)




    def gosub_stmt(self):

        localctx = BasicParser.Gosub_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_gosub_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.match(BasicParser.GOSUB_K)
            self.state = 120
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [37]:
                self.state = 118
                self.identifier()
                pass
            elif token in [38]:
                self.state = 119
                self.match(BasicParser.INTEGER)
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


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN_K(self):
            return self.getToken(BasicParser.RETURN_K, 0)

        def getRuleIndex(self):
            return BasicParser.RULE_return_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn_stmt" ):
                listener.enterReturn_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn_stmt" ):
                listener.exitReturn_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = BasicParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_return_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.match(BasicParser.RETURN_K)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF_K(self):
            return self.getToken(BasicParser.IF_K, 0)

        def expression(self):
            return self.getTypedRuleContext(BasicParser.ExpressionContext,0)


        def THEN_K(self):
            return self.getToken(BasicParser.THEN_K, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicParser.StatementContext)
            else:
                return self.getTypedRuleContext(BasicParser.StatementContext,i)


        def INTEGER(self, i:int=None):
            if i is None:
                return self.getTokens(BasicParser.INTEGER)
            else:
                return self.getToken(BasicParser.INTEGER, i)

        def ELSE_K(self):
            return self.getToken(BasicParser.ELSE_K, 0)

        def getRuleIndex(self):
            return BasicParser.RULE_if_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_stmt" ):
                listener.enterIf_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_stmt" ):
                listener.exitIf_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = BasicParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.match(BasicParser.IF_K)
            self.state = 125
            self.expression(0)
            self.state = 126
            self.match(BasicParser.THEN_K)
            self.state = 129
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20, 21, 22, 23, 24, 25, 26, 29, 32, 33, 34, 35, 36, 37]:
                self.state = 127
                self.statement()
                pass
            elif token in [38]:
                self.state = 128
                self.match(BasicParser.INTEGER)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 136
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 131
                self.match(BasicParser.ELSE_K)
                self.state = 134
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [20, 21, 22, 23, 24, 25, 26, 29, 32, 33, 34, 35, 36, 37]:
                    self.state = 132
                    self.statement()
                    pass
                elif token in [38]:
                    self.state = 133
                    self.match(BasicParser.INTEGER)
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


    class For_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR_K(self):
            return self.getToken(BasicParser.FOR_K, 0)

        def identifier(self):
            return self.getTypedRuleContext(BasicParser.IdentifierContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BasicParser.ExpressionContext,i)


        def TO_K(self):
            return self.getToken(BasicParser.TO_K, 0)

        def STEP_K(self):
            return self.getToken(BasicParser.STEP_K, 0)

        def getRuleIndex(self):
            return BasicParser.RULE_for_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_stmt" ):
                listener.enterFor_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_stmt" ):
                listener.exitFor_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = BasicParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_for_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.match(BasicParser.FOR_K)
            self.state = 139
            self.identifier()
            self.state = 140
            self.match(BasicParser.T__0)
            self.state = 141
            self.expression(0)
            self.state = 142
            self.match(BasicParser.TO_K)
            self.state = 143
            self.expression(0)
            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==31:
                self.state = 144
                self.match(BasicParser.STEP_K)
                self.state = 145
                self.expression(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Next_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEXT_K(self):
            return self.getToken(BasicParser.NEXT_K, 0)

        def identifier(self):
            return self.getTypedRuleContext(BasicParser.IdentifierContext,0)


        def getRuleIndex(self):
            return BasicParser.RULE_next_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNext_stmt" ):
                listener.enterNext_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNext_stmt" ):
                listener.exitNext_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNext_stmt" ):
                return visitor.visitNext_stmt(self)
            else:
                return visitor.visitChildren(self)




    def next_stmt(self):

        localctx = BasicParser.Next_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_next_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(BasicParser.NEXT_K)
            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==37:
                self.state = 149
                self.identifier()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE_K(self):
            return self.getToken(BasicParser.WHILE_K, 0)

        def expression(self):
            return self.getTypedRuleContext(BasicParser.ExpressionContext,0)


        def getRuleIndex(self):
            return BasicParser.RULE_while_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_stmt" ):
                listener.enterWhile_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_stmt" ):
                listener.exitWhile_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_stmt" ):
                return visitor.visitWhile_stmt(self)
            else:
                return visitor.visitChildren(self)




    def while_stmt(self):

        localctx = BasicParser.While_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.match(BasicParser.WHILE_K)
            self.state = 153
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Wend_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WEND_K(self):
            return self.getToken(BasicParser.WEND_K, 0)

        def getRuleIndex(self):
            return BasicParser.RULE_wend_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWend_stmt" ):
                listener.enterWend_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWend_stmt" ):
                listener.exitWend_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWend_stmt" ):
                return visitor.visitWend_stmt(self)
            else:
                return visitor.visitChildren(self)




    def wend_stmt(self):

        localctx = BasicParser.Wend_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_wend_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.match(BasicParser.WEND_K)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class End_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def END_K(self):
            return self.getToken(BasicParser.END_K, 0)

        def getRuleIndex(self):
            return BasicParser.RULE_end_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnd_stmt" ):
                listener.enterEnd_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnd_stmt" ):
                listener.exitEnd_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnd_stmt" ):
                return visitor.visitEnd_stmt(self)
            else:
                return visitor.visitChildren(self)




    def end_stmt(self):

        localctx = BasicParser.End_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_end_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.match(BasicParser.END_K)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Remark_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REMARK(self):
            return self.getToken(BasicParser.REMARK, 0)

        def getRuleIndex(self):
            return BasicParser.RULE_remark_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRemark_stmt" ):
                listener.enterRemark_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRemark_stmt" ):
                listener.exitRemark_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRemark_stmt" ):
                return visitor.visitRemark_stmt(self)
            else:
                return visitor.visitChildren(self)




    def remark_stmt(self):

        localctx = BasicParser.Remark_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_remark_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(BasicParser.REMARK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(BasicParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return BasicParser.RULE_identifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier" ):
                listener.enterIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier" ):
                listener.exitIdentifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier" ):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def identifier(self):

        localctx = BasicParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(BasicParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(BasicParser.NOT, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BasicParser.ExpressionContext,i)


        def MINUS(self):
            return self.getToken(BasicParser.MINUS, 0)

        def primary(self):
            return self.getTypedRuleContext(BasicParser.PrimaryContext,0)


        def OR(self):
            return self.getToken(BasicParser.OR, 0)

        def AND(self):
            return self.getToken(BasicParser.AND, 0)

        def EQ(self):
            return self.getToken(BasicParser.EQ, 0)

        def NE(self):
            return self.getToken(BasicParser.NE, 0)

        def LT(self):
            return self.getToken(BasicParser.LT, 0)

        def LE(self):
            return self.getToken(BasicParser.LE, 0)

        def GT(self):
            return self.getToken(BasicParser.GT, 0)

        def GE(self):
            return self.getToken(BasicParser.GE, 0)

        def PLUS(self):
            return self.getToken(BasicParser.PLUS, 0)

        def STAR(self):
            return self.getToken(BasicParser.STAR, 0)

        def SLASH(self):
            return self.getToken(BasicParser.SLASH, 0)

        def POWER(self):
            return self.getToken(BasicParser.POWER, 0)

        def getRuleIndex(self):
            return BasicParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BasicParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.state = 164
                self.match(BasicParser.NOT)
                self.state = 165
                self.expression(8)
                pass
            elif token in [16]:
                self.state = 166
                self.match(BasicParser.MINUS)
                self.state = 167
                self.expression(3)
                pass
            elif token in [4]:
                self.state = 168
                self.match(BasicParser.T__3)
                self.state = 169
                self.expression(0)
                self.state = 170
                self.match(BasicParser.T__4)
                pass
            elif token in [37, 38, 39, 40]:
                self.state = 172
                self.primary()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 192
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 190
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                    if la_ == 1:
                        localctx = BasicParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 175
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 176
                        _la = self._input.LA(1)
                        if not(_la==6 or _la==7):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 177
                        self.expression(10)
                        pass

                    elif la_ == 2:
                        localctx = BasicParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 178
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 179
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 32256) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 180
                        self.expression(8)
                        pass

                    elif la_ == 3:
                        localctx = BasicParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 181
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 182
                        _la = self._input.LA(1)
                        if not(_la==15 or _la==16):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 183
                        self.expression(7)
                        pass

                    elif la_ == 4:
                        localctx = BasicParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 184
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 185
                        _la = self._input.LA(1)
                        if not(_la==17 or _la==18):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 186
                        self.expression(6)
                        pass

                    elif la_ == 5:
                        localctx = BasicParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 187
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 188
                        self.match(BasicParser.POWER)
                        self.state = 189
                        self.expression(5)
                        pass

             
                self.state = 194
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class PrimaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(BasicParser.IdentifierContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BasicParser.ExpressionContext,i)


        def literal(self):
            return self.getTypedRuleContext(BasicParser.LiteralContext,0)


        def getRuleIndex(self):
            return BasicParser.RULE_primary

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

        localctx = BasicParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_primary)
        self._la = 0 # Token type
        try:
            self.state = 210
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [37]:
                self.enterOuterAlt(localctx, 1)
                self.state = 195
                self.identifier()
                self.state = 207
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                if la_ == 1:
                    self.state = 196
                    self.match(BasicParser.T__3)
                    self.state = 197
                    self.expression(0)
                    self.state = 202
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==2:
                        self.state = 198
                        self.match(BasicParser.T__1)
                        self.state = 199
                        self.expression(0)
                        self.state = 204
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 205
                    self.match(BasicParser.T__4)


                pass
            elif token in [38, 39, 40]:
                self.enterOuterAlt(localctx, 2)
                self.state = 209
                self.literal()
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


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def integer_literal(self):
            return self.getTypedRuleContext(BasicParser.Integer_literalContext,0)


        def real_literal(self):
            return self.getTypedRuleContext(BasicParser.Real_literalContext,0)


        def string_literal(self):
            return self.getTypedRuleContext(BasicParser.String_literalContext,0)


        def getRuleIndex(self):
            return BasicParser.RULE_literal

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

        localctx = BasicParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_literal)
        try:
            self.state = 215
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [38]:
                self.enterOuterAlt(localctx, 1)
                self.state = 212
                self.integer_literal()
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 2)
                self.state = 213
                self.real_literal()
                pass
            elif token in [40]:
                self.enterOuterAlt(localctx, 3)
                self.state = 214
                self.string_literal()
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


    class Integer_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(BasicParser.INTEGER, 0)

        def getRuleIndex(self):
            return BasicParser.RULE_integer_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInteger_literal" ):
                listener.enterInteger_literal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInteger_literal" ):
                listener.exitInteger_literal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInteger_literal" ):
                return visitor.visitInteger_literal(self)
            else:
                return visitor.visitChildren(self)




    def integer_literal(self):

        localctx = BasicParser.Integer_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_integer_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.match(BasicParser.INTEGER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Real_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REAL(self):
            return self.getToken(BasicParser.REAL, 0)

        def getRuleIndex(self):
            return BasicParser.RULE_real_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReal_literal" ):
                listener.enterReal_literal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReal_literal" ):
                listener.exitReal_literal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReal_literal" ):
                return visitor.visitReal_literal(self)
            else:
                return visitor.visitChildren(self)




    def real_literal(self):

        localctx = BasicParser.Real_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_real_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.match(BasicParser.REAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class String_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(BasicParser.STRING, 0)

        def getRuleIndex(self):
            return BasicParser.RULE_string_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString_literal" ):
                listener.enterString_literal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString_literal" ):
                listener.exitString_literal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString_literal" ):
                return visitor.visitString_literal(self)
            else:
                return visitor.visitChildren(self)




    def string_literal(self):

        localctx = BasicParser.String_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_string_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.match(BasicParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[17] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 4)
         




