# Generated from rosetta/babel/lisp/grammar/Lisp.g4 by ANTLR 4.13.2
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
        4,1,10,53,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,5,0,18,8,0,10,0,12,0,21,9,0,1,0,1,0,1,1,1,1,1,1,3,
        1,28,8,1,1,2,1,2,1,2,3,2,33,8,2,1,3,1,3,5,3,37,8,3,10,3,12,3,40,
        9,3,1,3,1,3,1,4,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,7,0,0,8,0,2,4,
        6,8,10,12,14,0,1,1,0,4,5,50,0,19,1,0,0,0,2,27,1,0,0,0,4,32,1,0,0,
        0,6,34,1,0,0,0,8,43,1,0,0,0,10,46,1,0,0,0,12,48,1,0,0,0,14,50,1,
        0,0,0,16,18,3,2,1,0,17,16,1,0,0,0,18,21,1,0,0,0,19,17,1,0,0,0,19,
        20,1,0,0,0,20,22,1,0,0,0,21,19,1,0,0,0,22,23,5,0,0,1,23,1,1,0,0,
        0,24,28,3,4,2,0,25,28,3,6,3,0,26,28,3,8,4,0,27,24,1,0,0,0,27,25,
        1,0,0,0,27,26,1,0,0,0,28,3,1,0,0,0,29,33,3,10,5,0,30,33,3,12,6,0,
        31,33,3,14,7,0,32,29,1,0,0,0,32,30,1,0,0,0,32,31,1,0,0,0,33,5,1,
        0,0,0,34,38,5,1,0,0,35,37,3,2,1,0,36,35,1,0,0,0,37,40,1,0,0,0,38,
        36,1,0,0,0,38,39,1,0,0,0,39,41,1,0,0,0,40,38,1,0,0,0,41,42,5,2,0,
        0,42,7,1,0,0,0,43,44,5,3,0,0,44,45,3,2,1,0,45,9,1,0,0,0,46,47,7,
        0,0,0,47,11,1,0,0,0,48,49,5,6,0,0,49,13,1,0,0,0,50,51,5,7,0,0,51,
        15,1,0,0,0,4,19,27,32,38
    ]

class LispParser ( Parser ):

    grammarFileName = "Lisp.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'''" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "IDENTIFIER", "SYMBOL_OPERATOR", "NUMBER", "STRING", 
                      "NEWLINE", "WS", "COMMENT" ]

    RULE_program = 0
    RULE_expression = 1
    RULE_atom = 2
    RULE_list = 3
    RULE_quote = 4
    RULE_identifier = 5
    RULE_number = 6
    RULE_string = 7

    ruleNames =  [ "program", "expression", "atom", "list", "quote", "identifier", 
                   "number", "string" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    IDENTIFIER=4
    SYMBOL_OPERATOR=5
    NUMBER=6
    STRING=7
    NEWLINE=8
    WS=9
    COMMENT=10

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
            return self.getToken(LispParser.EOF, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LispParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LispParser.ExpressionContext,i)


        def getRuleIndex(self):
            return LispParser.RULE_program

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

        localctx = LispParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 250) != 0):
                self.state = 16
                self.expression()
                self.state = 21
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 22
            self.match(LispParser.EOF)
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

        def atom(self):
            return self.getTypedRuleContext(LispParser.AtomContext,0)


        def list_(self):
            return self.getTypedRuleContext(LispParser.ListContext,0)


        def quote(self):
            return self.getTypedRuleContext(LispParser.QuoteContext,0)


        def getRuleIndex(self):
            return LispParser.RULE_expression

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




    def expression(self):

        localctx = LispParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expression)
        try:
            self.state = 27
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 5, 6, 7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 24
                self.atom()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 25
                self.list_()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 26
                self.quote()
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


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(LispParser.IdentifierContext,0)


        def number(self):
            return self.getTypedRuleContext(LispParser.NumberContext,0)


        def string(self):
            return self.getTypedRuleContext(LispParser.StringContext,0)


        def getRuleIndex(self):
            return LispParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = LispParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_atom)
        try:
            self.state = 32
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 29
                self.identifier()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 30
                self.number()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 31
                self.string()
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


    class ListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LispParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LispParser.ExpressionContext,i)


        def getRuleIndex(self):
            return LispParser.RULE_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList" ):
                listener.enterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList" ):
                listener.exitList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList" ):
                return visitor.visitList(self)
            else:
                return visitor.visitChildren(self)




    def list_(self):

        localctx = LispParser.ListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(LispParser.T__0)
            self.state = 38
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 250) != 0):
                self.state = 35
                self.expression()
                self.state = 40
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 41
            self.match(LispParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QuoteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(LispParser.ExpressionContext,0)


        def getRuleIndex(self):
            return LispParser.RULE_quote

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuote" ):
                listener.enterQuote(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuote" ):
                listener.exitQuote(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuote" ):
                return visitor.visitQuote(self)
            else:
                return visitor.visitChildren(self)




    def quote(self):

        localctx = LispParser.QuoteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_quote)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(LispParser.T__2)
            self.state = 44
            self.expression()
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
            return self.getToken(LispParser.IDENTIFIER, 0)

        def SYMBOL_OPERATOR(self):
            return self.getToken(LispParser.SYMBOL_OPERATOR, 0)

        def getRuleIndex(self):
            return LispParser.RULE_identifier

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

        localctx = LispParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            _la = self._input.LA(1)
            if not(_la==4 or _la==5):
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


    class NumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(LispParser.NUMBER, 0)

        def getRuleIndex(self):
            return LispParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber" ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)




    def number(self):

        localctx = LispParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(LispParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(LispParser.STRING, 0)

        def getRuleIndex(self):
            return LispParser.RULE_string

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString" ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)




    def string(self):

        localctx = LispParser.StringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_string)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(LispParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





