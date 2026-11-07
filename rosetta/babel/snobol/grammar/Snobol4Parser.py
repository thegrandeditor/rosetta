# Generated from rosetta/babel/snobol/grammar/Snobol4.g4 by ANTLR 4.13.2
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
        4,1,24,260,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,1,0,1,0,5,
        0,55,8,0,10,0,12,0,58,9,0,1,0,1,0,1,1,1,1,3,1,64,8,1,1,1,1,1,1,2,
        3,2,69,8,2,1,2,1,2,1,2,1,2,3,2,75,8,2,1,2,3,2,78,8,2,1,2,1,2,1,2,
        3,2,83,8,2,1,3,1,3,1,3,3,3,88,8,3,1,4,1,4,1,5,1,5,3,5,94,8,5,1,5,
        1,5,3,5,98,8,5,1,5,1,5,1,6,1,6,1,6,1,6,3,6,106,8,6,1,6,1,6,3,6,110,
        8,6,1,6,3,6,113,8,6,1,7,1,7,1,8,1,8,1,9,1,9,1,10,1,10,3,10,123,8,
        10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,3,11,133,8,11,1,12,1,
        12,1,13,1,13,4,13,139,8,13,11,13,12,13,140,1,14,1,14,1,14,1,14,1,
        14,1,15,1,15,1,15,1,15,1,15,1,16,1,16,1,17,1,17,3,17,157,8,17,1,
        17,1,17,3,17,161,8,17,1,17,5,17,164,8,17,10,17,12,17,167,9,17,1,
        18,1,18,1,18,5,18,172,8,18,10,18,12,18,175,9,18,1,19,1,19,3,19,179,
        8,19,1,19,1,19,3,19,183,8,19,1,19,5,19,186,8,19,10,19,12,19,189,
        9,19,1,20,1,20,3,20,193,8,20,1,20,1,20,3,20,197,8,20,1,20,5,20,200,
        8,20,10,20,12,20,203,9,20,1,21,1,21,3,21,207,8,21,1,21,1,21,3,21,
        211,8,21,1,21,5,21,214,8,21,10,21,12,21,217,9,21,1,22,1,22,1,22,
        1,22,1,22,1,22,1,22,1,22,1,22,1,22,3,22,229,8,22,1,23,1,23,1,23,
        1,23,1,23,5,23,236,8,23,10,23,12,23,239,9,23,1,23,1,23,1,24,1,24,
        1,24,1,25,1,25,1,25,1,25,1,25,5,25,251,8,25,10,25,12,25,254,9,25,
        3,25,256,8,25,1,25,1,25,1,25,0,0,26,0,2,4,6,8,10,12,14,16,18,20,
        22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,0,5,1,1,24,24,1,0,8,
        9,1,0,15,16,1,0,17,18,2,0,8,9,13,17,275,0,56,1,0,0,0,2,63,1,0,0,
        0,4,82,1,0,0,0,6,87,1,0,0,0,8,89,1,0,0,0,10,91,1,0,0,0,12,101,1,
        0,0,0,14,114,1,0,0,0,16,116,1,0,0,0,18,118,1,0,0,0,20,120,1,0,0,
        0,22,132,1,0,0,0,24,134,1,0,0,0,26,138,1,0,0,0,28,142,1,0,0,0,30,
        147,1,0,0,0,32,152,1,0,0,0,34,154,1,0,0,0,36,168,1,0,0,0,38,176,
        1,0,0,0,40,190,1,0,0,0,42,204,1,0,0,0,44,228,1,0,0,0,46,230,1,0,
        0,0,48,242,1,0,0,0,50,245,1,0,0,0,52,55,3,2,1,0,53,55,5,24,0,0,54,
        52,1,0,0,0,54,53,1,0,0,0,55,58,1,0,0,0,56,54,1,0,0,0,56,57,1,0,0,
        0,57,59,1,0,0,0,58,56,1,0,0,0,59,60,5,0,0,1,60,1,1,0,0,0,61,64,5,
        22,0,0,62,64,3,4,2,0,63,61,1,0,0,0,63,62,1,0,0,0,64,65,1,0,0,0,65,
        66,7,0,0,0,66,3,1,0,0,0,67,69,3,8,4,0,68,67,1,0,0,0,68,69,1,0,0,
        0,69,70,1,0,0,0,70,71,5,23,0,0,71,74,3,6,3,0,72,73,5,23,0,0,73,75,
        3,20,10,0,74,72,1,0,0,0,74,75,1,0,0,0,75,83,1,0,0,0,76,78,3,8,4,
        0,77,76,1,0,0,0,77,78,1,0,0,0,78,79,1,0,0,0,79,80,5,23,0,0,80,83,
        3,20,10,0,81,83,3,8,4,0,82,68,1,0,0,0,82,77,1,0,0,0,82,81,1,0,0,
        0,83,5,1,0,0,0,84,88,3,12,6,0,85,88,3,10,5,0,86,88,3,32,16,0,87,
        84,1,0,0,0,87,85,1,0,0,0,87,86,1,0,0,0,88,7,1,0,0,0,89,90,5,19,0,
        0,90,9,1,0,0,0,91,93,3,14,7,0,92,94,5,23,0,0,93,92,1,0,0,0,93,94,
        1,0,0,0,94,95,1,0,0,0,95,97,5,1,0,0,96,98,5,23,0,0,97,96,1,0,0,0,
        97,98,1,0,0,0,98,99,1,0,0,0,99,100,3,32,16,0,100,11,1,0,0,0,101,
        102,3,14,7,0,102,103,5,23,0,0,103,112,3,16,8,0,104,106,5,23,0,0,
        105,104,1,0,0,0,105,106,1,0,0,0,106,107,1,0,0,0,107,109,5,1,0,0,
        108,110,5,23,0,0,109,108,1,0,0,0,109,110,1,0,0,0,110,111,1,0,0,0,
        111,113,3,18,9,0,112,105,1,0,0,0,112,113,1,0,0,0,113,13,1,0,0,0,
        114,115,3,32,16,0,115,15,1,0,0,0,116,117,3,32,16,0,117,17,1,0,0,
        0,118,119,3,32,16,0,119,19,1,0,0,0,120,122,5,2,0,0,121,123,5,23,
        0,0,122,121,1,0,0,0,122,123,1,0,0,0,123,124,1,0,0,0,124,125,3,22,
        11,0,125,21,1,0,0,0,126,127,5,3,0,0,127,128,3,24,12,0,128,129,5,
        4,0,0,129,133,1,0,0,0,130,133,3,26,13,0,131,133,3,24,12,0,132,126,
        1,0,0,0,132,130,1,0,0,0,132,131,1,0,0,0,133,23,1,0,0,0,134,135,5,
        19,0,0,135,25,1,0,0,0,136,139,3,28,14,0,137,139,3,30,15,0,138,136,
        1,0,0,0,138,137,1,0,0,0,139,140,1,0,0,0,140,138,1,0,0,0,140,141,
        1,0,0,0,141,27,1,0,0,0,142,143,5,5,0,0,143,144,5,3,0,0,144,145,5,
        19,0,0,145,146,5,4,0,0,146,29,1,0,0,0,147,148,5,6,0,0,148,149,5,
        3,0,0,149,150,5,19,0,0,150,151,5,4,0,0,151,31,1,0,0,0,152,153,3,
        34,17,0,153,33,1,0,0,0,154,165,3,36,18,0,155,157,5,23,0,0,156,155,
        1,0,0,0,156,157,1,0,0,0,157,158,1,0,0,0,158,160,5,7,0,0,159,161,
        5,23,0,0,160,159,1,0,0,0,160,161,1,0,0,0,161,162,1,0,0,0,162,164,
        3,36,18,0,163,156,1,0,0,0,164,167,1,0,0,0,165,163,1,0,0,0,165,166,
        1,0,0,0,166,35,1,0,0,0,167,165,1,0,0,0,168,173,3,38,19,0,169,170,
        5,23,0,0,170,172,3,38,19,0,171,169,1,0,0,0,172,175,1,0,0,0,173,171,
        1,0,0,0,173,174,1,0,0,0,174,37,1,0,0,0,175,173,1,0,0,0,176,187,3,
        40,20,0,177,179,5,23,0,0,178,177,1,0,0,0,178,179,1,0,0,0,179,180,
        1,0,0,0,180,182,7,1,0,0,181,183,5,23,0,0,182,181,1,0,0,0,182,183,
        1,0,0,0,183,184,1,0,0,0,184,186,5,19,0,0,185,178,1,0,0,0,186,189,
        1,0,0,0,187,185,1,0,0,0,187,188,1,0,0,0,188,39,1,0,0,0,189,187,1,
        0,0,0,190,201,3,42,21,0,191,193,5,23,0,0,192,191,1,0,0,0,192,193,
        1,0,0,0,193,194,1,0,0,0,194,196,7,2,0,0,195,197,5,23,0,0,196,195,
        1,0,0,0,196,197,1,0,0,0,197,198,1,0,0,0,198,200,3,42,21,0,199,192,
        1,0,0,0,200,203,1,0,0,0,201,199,1,0,0,0,201,202,1,0,0,0,202,41,1,
        0,0,0,203,201,1,0,0,0,204,215,3,44,22,0,205,207,5,23,0,0,206,205,
        1,0,0,0,206,207,1,0,0,0,207,208,1,0,0,0,208,210,7,3,0,0,209,211,
        5,23,0,0,210,209,1,0,0,0,210,211,1,0,0,0,211,212,1,0,0,0,212,214,
        3,44,22,0,213,206,1,0,0,0,214,217,1,0,0,0,215,213,1,0,0,0,215,216,
        1,0,0,0,216,43,1,0,0,0,217,215,1,0,0,0,218,229,5,19,0,0,219,229,
        5,20,0,0,220,229,5,21,0,0,221,222,5,3,0,0,222,223,3,32,16,0,223,
        224,5,4,0,0,224,229,1,0,0,0,225,229,3,50,25,0,226,229,3,48,24,0,
        227,229,3,46,23,0,228,218,1,0,0,0,228,219,1,0,0,0,228,220,1,0,0,
        0,228,221,1,0,0,0,228,225,1,0,0,0,228,226,1,0,0,0,228,227,1,0,0,
        0,229,45,1,0,0,0,230,231,5,19,0,0,231,232,5,10,0,0,232,237,3,32,
        16,0,233,234,5,11,0,0,234,236,3,32,16,0,235,233,1,0,0,0,236,239,
        1,0,0,0,237,235,1,0,0,0,237,238,1,0,0,0,238,240,1,0,0,0,239,237,
        1,0,0,0,240,241,5,12,0,0,241,47,1,0,0,0,242,243,7,4,0,0,243,244,
        3,44,22,0,244,49,1,0,0,0,245,246,5,19,0,0,246,255,5,3,0,0,247,252,
        3,32,16,0,248,249,5,11,0,0,249,251,3,32,16,0,250,248,1,0,0,0,251,
        254,1,0,0,0,252,250,1,0,0,0,252,253,1,0,0,0,253,256,1,0,0,0,254,
        252,1,0,0,0,255,247,1,0,0,0,255,256,1,0,0,0,256,257,1,0,0,0,257,
        258,5,4,0,0,258,51,1,0,0,0,34,54,56,63,68,74,77,82,87,93,97,105,
        109,112,122,132,138,140,156,160,165,173,178,182,187,192,196,201,
        206,210,215,228,237,252,255
    ]

class Snobol4Parser ( Parser ):

    grammarFileName = "Snobol4.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "':'", "'('", "')'", "'S'", "'F'", 
                     "'|'", "'.'", "'$'", "'<'", "','", "'>'", "'&'", "'@'", 
                     "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "PLUS", "MINUS", 
                      "TIMES", "DIV", "ID", "STRING", "NUMBER", "COMMENT", 
                      "WS", "NEWLINE" ]

    RULE_program = 0
    RULE_line = 1
    RULE_statement = 2
    RULE_content = 3
    RULE_label = 4
    RULE_assignment = 5
    RULE_patternMatch = 6
    RULE_subject = 7
    RULE_pattern = 8
    RULE_replacement = 9
    RULE_transfer = 10
    RULE_transfer_dest = 11
    RULE_direct_goto = 12
    RULE_conditional_gotos = 13
    RULE_success_goto = 14
    RULE_failure_goto = 15
    RULE_expression = 16
    RULE_alternation_expr = 17
    RULE_concatenation_expr = 18
    RULE_capture_expr = 19
    RULE_additive_expr = 20
    RULE_multiplicative_expr = 21
    RULE_primary = 22
    RULE_array_access = 23
    RULE_unary_expr = 24
    RULE_function_call = 25

    ruleNames =  [ "program", "line", "statement", "content", "label", "assignment", 
                   "patternMatch", "subject", "pattern", "replacement", 
                   "transfer", "transfer_dest", "direct_goto", "conditional_gotos", 
                   "success_goto", "failure_goto", "expression", "alternation_expr", 
                   "concatenation_expr", "capture_expr", "additive_expr", 
                   "multiplicative_expr", "primary", "array_access", "unary_expr", 
                   "function_call" ]

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
    PLUS=15
    MINUS=16
    TIMES=17
    DIV=18
    ID=19
    STRING=20
    NUMBER=21
    COMMENT=22
    WS=23
    NEWLINE=24

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
            return self.getToken(Snobol4Parser.EOF, 0)

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Snobol4Parser.LineContext)
            else:
                return self.getTypedRuleContext(Snobol4Parser.LineContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(Snobol4Parser.NEWLINE)
            else:
                return self.getToken(Snobol4Parser.NEWLINE, i)

        def getRuleIndex(self):
            return Snobol4Parser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = Snobol4Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 29884416) != 0):
                self.state = 54
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [19, 22, 23]:
                    self.state = 52
                    self.line()
                    pass
                elif token in [24]:
                    self.state = 53
                    self.match(Snobol4Parser.NEWLINE)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 58
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 59
            self.match(Snobol4Parser.EOF)
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

        def NEWLINE(self):
            return self.getToken(Snobol4Parser.NEWLINE, 0)

        def EOF(self):
            return self.getToken(Snobol4Parser.EOF, 0)

        def COMMENT(self):
            return self.getToken(Snobol4Parser.COMMENT, 0)

        def statement(self):
            return self.getTypedRuleContext(Snobol4Parser.StatementContext,0)


        def getRuleIndex(self):
            return Snobol4Parser.RULE_line

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLine" ):
                return visitor.visitLine(self)
            else:
                return visitor.visitChildren(self)




    def line(self):

        localctx = Snobol4Parser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_line)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                self.state = 61
                self.match(Snobol4Parser.COMMENT)
                pass
            elif token in [19, 23]:
                self.state = 62
                self.statement()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 65
            _la = self._input.LA(1)
            if not(_la==-1 or _la==24):
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


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(Snobol4Parser.WS)
            else:
                return self.getToken(Snobol4Parser.WS, i)

        def content(self):
            return self.getTypedRuleContext(Snobol4Parser.ContentContext,0)


        def label(self):
            return self.getTypedRuleContext(Snobol4Parser.LabelContext,0)


        def transfer(self):
            return self.getTypedRuleContext(Snobol4Parser.TransferContext,0)


        def getRuleIndex(self):
            return Snobol4Parser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = Snobol4Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 82
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 68
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==19:
                    self.state = 67
                    self.label()


                self.state = 70
                self.match(Snobol4Parser.WS)

                self.state = 71
                self.content()
                self.state = 74
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==23:
                    self.state = 72
                    self.match(Snobol4Parser.WS)
                    self.state = 73
                    self.transfer()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 77
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==19:
                    self.state = 76
                    self.label()


                self.state = 79
                self.match(Snobol4Parser.WS)
                self.state = 80
                self.transfer()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 81
                self.label()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def patternMatch(self):
            return self.getTypedRuleContext(Snobol4Parser.PatternMatchContext,0)


        def assignment(self):
            return self.getTypedRuleContext(Snobol4Parser.AssignmentContext,0)


        def expression(self):
            return self.getTypedRuleContext(Snobol4Parser.ExpressionContext,0)


        def getRuleIndex(self):
            return Snobol4Parser.RULE_content

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContent" ):
                return visitor.visitContent(self)
            else:
                return visitor.visitChildren(self)




    def content(self):

        localctx = Snobol4Parser.ContentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_content)
        try:
            self.state = 87
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 84
                self.patternMatch()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 85
                self.assignment()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 86
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LabelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(Snobol4Parser.ID, 0)

        def getRuleIndex(self):
            return Snobol4Parser.RULE_label

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLabel" ):
                return visitor.visitLabel(self)
            else:
                return visitor.visitChildren(self)




    def label(self):

        localctx = Snobol4Parser.LabelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_label)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(Snobol4Parser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def subject(self):
            return self.getTypedRuleContext(Snobol4Parser.SubjectContext,0)


        def expression(self):
            return self.getTypedRuleContext(Snobol4Parser.ExpressionContext,0)


        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(Snobol4Parser.WS)
            else:
                return self.getToken(Snobol4Parser.WS, i)

        def getRuleIndex(self):
            return Snobol4Parser.RULE_assignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = Snobol4Parser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_assignment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.subject()
            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==23:
                self.state = 92
                self.match(Snobol4Parser.WS)


            self.state = 95
            self.match(Snobol4Parser.T__0)
            self.state = 97
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==23:
                self.state = 96
                self.match(Snobol4Parser.WS)


            self.state = 99
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PatternMatchContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def subject(self):
            return self.getTypedRuleContext(Snobol4Parser.SubjectContext,0)


        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(Snobol4Parser.WS)
            else:
                return self.getToken(Snobol4Parser.WS, i)

        def pattern(self):
            return self.getTypedRuleContext(Snobol4Parser.PatternContext,0)


        def replacement(self):
            return self.getTypedRuleContext(Snobol4Parser.ReplacementContext,0)


        def getRuleIndex(self):
            return Snobol4Parser.RULE_patternMatch

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPatternMatch" ):
                return visitor.visitPatternMatch(self)
            else:
                return visitor.visitChildren(self)




    def patternMatch(self):

        localctx = Snobol4Parser.PatternMatchContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_patternMatch)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.subject()
            self.state = 102
            self.match(Snobol4Parser.WS)
            self.state = 103
            self.pattern()
            self.state = 112
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 105
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==23:
                    self.state = 104
                    self.match(Snobol4Parser.WS)


                self.state = 107
                self.match(Snobol4Parser.T__0)
                self.state = 109
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==23:
                    self.state = 108
                    self.match(Snobol4Parser.WS)


                self.state = 111
                self.replacement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubjectContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(Snobol4Parser.ExpressionContext,0)


        def getRuleIndex(self):
            return Snobol4Parser.RULE_subject

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubject" ):
                return visitor.visitSubject(self)
            else:
                return visitor.visitChildren(self)




    def subject(self):

        localctx = Snobol4Parser.SubjectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_subject)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.expression()
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

        def expression(self):
            return self.getTypedRuleContext(Snobol4Parser.ExpressionContext,0)


        def getRuleIndex(self):
            return Snobol4Parser.RULE_pattern

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPattern" ):
                return visitor.visitPattern(self)
            else:
                return visitor.visitChildren(self)




    def pattern(self):

        localctx = Snobol4Parser.PatternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_pattern)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReplacementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(Snobol4Parser.ExpressionContext,0)


        def getRuleIndex(self):
            return Snobol4Parser.RULE_replacement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReplacement" ):
                return visitor.visitReplacement(self)
            else:
                return visitor.visitChildren(self)




    def replacement(self):

        localctx = Snobol4Parser.ReplacementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_replacement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TransferContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def transfer_dest(self):
            return self.getTypedRuleContext(Snobol4Parser.Transfer_destContext,0)


        def WS(self):
            return self.getToken(Snobol4Parser.WS, 0)

        def getRuleIndex(self):
            return Snobol4Parser.RULE_transfer

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTransfer" ):
                return visitor.visitTransfer(self)
            else:
                return visitor.visitChildren(self)




    def transfer(self):

        localctx = Snobol4Parser.TransferContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_transfer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(Snobol4Parser.T__1)
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==23:
                self.state = 121
                self.match(Snobol4Parser.WS)


            self.state = 124
            self.transfer_dest()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Transfer_destContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def direct_goto(self):
            return self.getTypedRuleContext(Snobol4Parser.Direct_gotoContext,0)


        def conditional_gotos(self):
            return self.getTypedRuleContext(Snobol4Parser.Conditional_gotosContext,0)


        def getRuleIndex(self):
            return Snobol4Parser.RULE_transfer_dest

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTransfer_dest" ):
                return visitor.visitTransfer_dest(self)
            else:
                return visitor.visitChildren(self)




    def transfer_dest(self):

        localctx = Snobol4Parser.Transfer_destContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_transfer_dest)
        try:
            self.state = 132
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 126
                self.match(Snobol4Parser.T__2)
                self.state = 127
                self.direct_goto()
                self.state = 128
                self.match(Snobol4Parser.T__3)
                pass
            elif token in [5, 6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 130
                self.conditional_gotos()
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 3)
                self.state = 131
                self.direct_goto()
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


    class Direct_gotoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(Snobol4Parser.ID, 0)

        def getRuleIndex(self):
            return Snobol4Parser.RULE_direct_goto

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDirect_goto" ):
                return visitor.visitDirect_goto(self)
            else:
                return visitor.visitChildren(self)




    def direct_goto(self):

        localctx = Snobol4Parser.Direct_gotoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_direct_goto)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.match(Snobol4Parser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Conditional_gotosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def success_goto(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Snobol4Parser.Success_gotoContext)
            else:
                return self.getTypedRuleContext(Snobol4Parser.Success_gotoContext,i)


        def failure_goto(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Snobol4Parser.Failure_gotoContext)
            else:
                return self.getTypedRuleContext(Snobol4Parser.Failure_gotoContext,i)


        def getRuleIndex(self):
            return Snobol4Parser.RULE_conditional_gotos

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditional_gotos" ):
                return visitor.visitConditional_gotos(self)
            else:
                return visitor.visitChildren(self)




    def conditional_gotos(self):

        localctx = Snobol4Parser.Conditional_gotosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_conditional_gotos)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 138
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [5]:
                    self.state = 136
                    self.success_goto()
                    pass
                elif token in [6]:
                    self.state = 137
                    self.failure_goto()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 140 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==5 or _la==6):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Success_gotoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(Snobol4Parser.ID, 0)

        def getRuleIndex(self):
            return Snobol4Parser.RULE_success_goto

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSuccess_goto" ):
                return visitor.visitSuccess_goto(self)
            else:
                return visitor.visitChildren(self)




    def success_goto(self):

        localctx = Snobol4Parser.Success_gotoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_success_goto)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.match(Snobol4Parser.T__4)
            self.state = 143
            self.match(Snobol4Parser.T__2)
            self.state = 144
            self.match(Snobol4Parser.ID)
            self.state = 145
            self.match(Snobol4Parser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Failure_gotoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(Snobol4Parser.ID, 0)

        def getRuleIndex(self):
            return Snobol4Parser.RULE_failure_goto

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFailure_goto" ):
                return visitor.visitFailure_goto(self)
            else:
                return visitor.visitChildren(self)




    def failure_goto(self):

        localctx = Snobol4Parser.Failure_gotoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_failure_goto)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.match(Snobol4Parser.T__5)
            self.state = 148
            self.match(Snobol4Parser.T__2)
            self.state = 149
            self.match(Snobol4Parser.ID)
            self.state = 150
            self.match(Snobol4Parser.T__3)
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

        def alternation_expr(self):
            return self.getTypedRuleContext(Snobol4Parser.Alternation_exprContext,0)


        def getRuleIndex(self):
            return Snobol4Parser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = Snobol4Parser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.alternation_expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Alternation_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def concatenation_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Snobol4Parser.Concatenation_exprContext)
            else:
                return self.getTypedRuleContext(Snobol4Parser.Concatenation_exprContext,i)


        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(Snobol4Parser.WS)
            else:
                return self.getToken(Snobol4Parser.WS, i)

        def getRuleIndex(self):
            return Snobol4Parser.RULE_alternation_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAlternation_expr" ):
                return visitor.visitAlternation_expr(self)
            else:
                return visitor.visitChildren(self)




    def alternation_expr(self):

        localctx = Snobol4Parser.Alternation_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_alternation_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.concatenation_expr()
            self.state = 165
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 156
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==23:
                        self.state = 155
                        self.match(Snobol4Parser.WS)


                    self.state = 158
                    self.match(Snobol4Parser.T__6)
                    self.state = 160
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==23:
                        self.state = 159
                        self.match(Snobol4Parser.WS)


                    self.state = 162
                    self.concatenation_expr() 
                self.state = 167
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Concatenation_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def capture_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Snobol4Parser.Capture_exprContext)
            else:
                return self.getTypedRuleContext(Snobol4Parser.Capture_exprContext,i)


        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(Snobol4Parser.WS)
            else:
                return self.getToken(Snobol4Parser.WS, i)

        def getRuleIndex(self):
            return Snobol4Parser.RULE_concatenation_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConcatenation_expr" ):
                return visitor.visitConcatenation_expr(self)
            else:
                return visitor.visitChildren(self)




    def concatenation_expr(self):

        localctx = Snobol4Parser.Concatenation_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_concatenation_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.capture_expr()
            self.state = 173
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 169
                    self.match(Snobol4Parser.WS)
                    self.state = 170
                    self.capture_expr() 
                self.state = 175
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Capture_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additive_expr(self):
            return self.getTypedRuleContext(Snobol4Parser.Additive_exprContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(Snobol4Parser.ID)
            else:
                return self.getToken(Snobol4Parser.ID, i)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(Snobol4Parser.WS)
            else:
                return self.getToken(Snobol4Parser.WS, i)

        def getRuleIndex(self):
            return Snobol4Parser.RULE_capture_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCapture_expr" ):
                return visitor.visitCapture_expr(self)
            else:
                return visitor.visitChildren(self)




    def capture_expr(self):

        localctx = Snobol4Parser.Capture_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_capture_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.additive_expr()
            self.state = 187
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 178
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==23:
                        self.state = 177
                        self.match(Snobol4Parser.WS)


                    self.state = 180
                    _la = self._input.LA(1)
                    if not(_la==8 or _la==9):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 182
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==23:
                        self.state = 181
                        self.match(Snobol4Parser.WS)


                    self.state = 184
                    self.match(Snobol4Parser.ID) 
                self.state = 189
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Additive_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicative_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Snobol4Parser.Multiplicative_exprContext)
            else:
                return self.getTypedRuleContext(Snobol4Parser.Multiplicative_exprContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(Snobol4Parser.PLUS)
            else:
                return self.getToken(Snobol4Parser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(Snobol4Parser.MINUS)
            else:
                return self.getToken(Snobol4Parser.MINUS, i)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(Snobol4Parser.WS)
            else:
                return self.getToken(Snobol4Parser.WS, i)

        def getRuleIndex(self):
            return Snobol4Parser.RULE_additive_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditive_expr" ):
                return visitor.visitAdditive_expr(self)
            else:
                return visitor.visitChildren(self)




    def additive_expr(self):

        localctx = Snobol4Parser.Additive_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_additive_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.multiplicative_expr()
            self.state = 201
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 192
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==23:
                        self.state = 191
                        self.match(Snobol4Parser.WS)


                    self.state = 194
                    _la = self._input.LA(1)
                    if not(_la==15 or _la==16):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 196
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==23:
                        self.state = 195
                        self.match(Snobol4Parser.WS)


                    self.state = 198
                    self.multiplicative_expr() 
                self.state = 203
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Multiplicative_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primary(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Snobol4Parser.PrimaryContext)
            else:
                return self.getTypedRuleContext(Snobol4Parser.PrimaryContext,i)


        def TIMES(self, i:int=None):
            if i is None:
                return self.getTokens(Snobol4Parser.TIMES)
            else:
                return self.getToken(Snobol4Parser.TIMES, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(Snobol4Parser.DIV)
            else:
                return self.getToken(Snobol4Parser.DIV, i)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(Snobol4Parser.WS)
            else:
                return self.getToken(Snobol4Parser.WS, i)

        def getRuleIndex(self):
            return Snobol4Parser.RULE_multiplicative_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicative_expr" ):
                return visitor.visitMultiplicative_expr(self)
            else:
                return visitor.visitChildren(self)




    def multiplicative_expr(self):

        localctx = Snobol4Parser.Multiplicative_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_multiplicative_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.primary()
            self.state = 215
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 206
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==23:
                        self.state = 205
                        self.match(Snobol4Parser.WS)


                    self.state = 208
                    _la = self._input.LA(1)
                    if not(_la==17 or _la==18):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 210
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==23:
                        self.state = 209
                        self.match(Snobol4Parser.WS)


                    self.state = 212
                    self.primary() 
                self.state = 217
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

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

        def ID(self):
            return self.getToken(Snobol4Parser.ID, 0)

        def STRING(self):
            return self.getToken(Snobol4Parser.STRING, 0)

        def NUMBER(self):
            return self.getToken(Snobol4Parser.NUMBER, 0)

        def expression(self):
            return self.getTypedRuleContext(Snobol4Parser.ExpressionContext,0)


        def function_call(self):
            return self.getTypedRuleContext(Snobol4Parser.Function_callContext,0)


        def unary_expr(self):
            return self.getTypedRuleContext(Snobol4Parser.Unary_exprContext,0)


        def array_access(self):
            return self.getTypedRuleContext(Snobol4Parser.Array_accessContext,0)


        def getRuleIndex(self):
            return Snobol4Parser.RULE_primary

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimary" ):
                return visitor.visitPrimary(self)
            else:
                return visitor.visitChildren(self)




    def primary(self):

        localctx = Snobol4Parser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_primary)
        try:
            self.state = 228
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 218
                self.match(Snobol4Parser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 219
                self.match(Snobol4Parser.STRING)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 220
                self.match(Snobol4Parser.NUMBER)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 221
                self.match(Snobol4Parser.T__2)
                self.state = 222
                self.expression()
                self.state = 223
                self.match(Snobol4Parser.T__3)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 225
                self.function_call()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 226
                self.unary_expr()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 227
                self.array_access()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(Snobol4Parser.ID, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Snobol4Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(Snobol4Parser.ExpressionContext,i)


        def getRuleIndex(self):
            return Snobol4Parser.RULE_array_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_access" ):
                return visitor.visitArray_access(self)
            else:
                return visitor.visitChildren(self)




    def array_access(self):

        localctx = Snobol4Parser.Array_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_array_access)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.match(Snobol4Parser.ID)
            self.state = 231
            self.match(Snobol4Parser.T__9)
            self.state = 232
            self.expression()
            self.state = 237
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 233
                self.match(Snobol4Parser.T__10)
                self.state = 234
                self.expression()
                self.state = 239
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 240
            self.match(Snobol4Parser.T__11)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Unary_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primary(self):
            return self.getTypedRuleContext(Snobol4Parser.PrimaryContext,0)


        def TIMES(self):
            return self.getToken(Snobol4Parser.TIMES, 0)

        def PLUS(self):
            return self.getToken(Snobol4Parser.PLUS, 0)

        def MINUS(self):
            return self.getToken(Snobol4Parser.MINUS, 0)

        def getRuleIndex(self):
            return Snobol4Parser.RULE_unary_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnary_expr" ):
                return visitor.visitUnary_expr(self)
            else:
                return visitor.visitChildren(self)




    def unary_expr(self):

        localctx = Snobol4Parser.Unary_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_unary_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 254720) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 243
            self.primary()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(Snobol4Parser.ID, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Snobol4Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(Snobol4Parser.ExpressionContext,i)


        def getRuleIndex(self):
            return Snobol4Parser.RULE_function_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call" ):
                return visitor.visitFunction_call(self)
            else:
                return visitor.visitChildren(self)




    def function_call(self):

        localctx = Snobol4Parser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_function_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.match(Snobol4Parser.ID)
            self.state = 246
            self.match(Snobol4Parser.T__2)
            self.state = 255
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 3924744) != 0):
                self.state = 247
                self.expression()
                self.state = 252
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==11:
                    self.state = 248
                    self.match(Snobol4Parser.T__10)
                    self.state = 249
                    self.expression()
                    self.state = 254
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 257
            self.match(Snobol4Parser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





