# Generated from Forth.g4 by ANTLR 4.13.2
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
        4,1,13,88,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,5,0,20,8,0,10,0,12,0,23,9,0,1,0,1,0,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,3,1,34,8,1,1,2,1,2,1,2,5,2,39,8,2,10,2,12,
        2,42,9,2,1,2,1,2,1,3,1,3,5,3,48,8,3,10,3,12,3,51,9,3,1,3,1,3,5,3,
        55,8,3,10,3,12,3,58,9,3,3,3,60,8,3,1,3,1,3,1,4,1,4,5,4,66,8,4,10,
        4,12,4,69,9,4,1,4,1,4,1,5,1,5,5,5,75,8,5,10,5,12,5,78,9,5,1,5,1,
        5,1,6,1,6,1,7,1,7,1,8,1,8,1,8,0,0,9,0,2,4,6,8,10,12,14,16,0,0,91,
        0,21,1,0,0,0,2,33,1,0,0,0,4,35,1,0,0,0,6,45,1,0,0,0,8,63,1,0,0,0,
        10,72,1,0,0,0,12,81,1,0,0,0,14,83,1,0,0,0,16,85,1,0,0,0,18,20,3,
        2,1,0,19,18,1,0,0,0,20,23,1,0,0,0,21,19,1,0,0,0,21,22,1,0,0,0,22,
        24,1,0,0,0,23,21,1,0,0,0,24,25,5,0,0,1,25,1,1,0,0,0,26,34,3,4,2,
        0,27,34,3,6,3,0,28,34,3,8,4,0,29,34,3,10,5,0,30,34,3,12,6,0,31,34,
        3,14,7,0,32,34,3,16,8,0,33,26,1,0,0,0,33,27,1,0,0,0,33,28,1,0,0,
        0,33,29,1,0,0,0,33,30,1,0,0,0,33,31,1,0,0,0,33,32,1,0,0,0,34,3,1,
        0,0,0,35,36,5,1,0,0,36,40,5,11,0,0,37,39,3,2,1,0,38,37,1,0,0,0,39,
        42,1,0,0,0,40,38,1,0,0,0,40,41,1,0,0,0,41,43,1,0,0,0,42,40,1,0,0,
        0,43,44,5,2,0,0,44,5,1,0,0,0,45,49,5,3,0,0,46,48,3,2,1,0,47,46,1,
        0,0,0,48,51,1,0,0,0,49,47,1,0,0,0,49,50,1,0,0,0,50,59,1,0,0,0,51,
        49,1,0,0,0,52,56,5,4,0,0,53,55,3,2,1,0,54,53,1,0,0,0,55,58,1,0,0,
        0,56,54,1,0,0,0,56,57,1,0,0,0,57,60,1,0,0,0,58,56,1,0,0,0,59,52,
        1,0,0,0,59,60,1,0,0,0,60,61,1,0,0,0,61,62,5,5,0,0,62,7,1,0,0,0,63,
        67,5,6,0,0,64,66,3,2,1,0,65,64,1,0,0,0,66,69,1,0,0,0,67,65,1,0,0,
        0,67,68,1,0,0,0,68,70,1,0,0,0,69,67,1,0,0,0,70,71,5,7,0,0,71,9,1,
        0,0,0,72,76,5,8,0,0,73,75,3,2,1,0,74,73,1,0,0,0,75,78,1,0,0,0,76,
        74,1,0,0,0,76,77,1,0,0,0,77,79,1,0,0,0,78,76,1,0,0,0,79,80,5,9,0,
        0,80,11,1,0,0,0,81,82,5,10,0,0,82,13,1,0,0,0,83,84,5,12,0,0,84,15,
        1,0,0,0,85,86,5,11,0,0,86,17,1,0,0,0,8,21,33,40,49,56,59,67,76
    ]

class ForthParser ( Parser ):

    grammarFileName = "Forth.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':'", "';'", "'IF'", "'ELSE'", "'THEN'", 
                     "'DO'", "'LOOP'", "'BEGIN'", "'UNTIL'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "STACK_CMD", "ID", "NUMBER", 
                      "WS" ]

    RULE_program = 0
    RULE_element = 1
    RULE_definition = 2
    RULE_if_stmt = 3
    RULE_do_loop = 4
    RULE_begin_until = 5
    RULE_stack_op = 6
    RULE_literal = 7
    RULE_call = 8

    ruleNames =  [ "program", "element", "definition", "if_stmt", "do_loop", 
                   "begin_until", "stack_op", "literal", "call" ]

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
    STACK_CMD=10
    ID=11
    NUMBER=12
    WS=13

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
            return self.getToken(ForthParser.EOF, 0)

        def element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ForthParser.ElementContext)
            else:
                return self.getTypedRuleContext(ForthParser.ElementContext,i)


        def getRuleIndex(self):
            return ForthParser.RULE_program

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

        localctx = ForthParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 7498) != 0):
                self.state = 18
                self.element()
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 24
            self.match(ForthParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def definition(self):
            return self.getTypedRuleContext(ForthParser.DefinitionContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(ForthParser.If_stmtContext,0)


        def do_loop(self):
            return self.getTypedRuleContext(ForthParser.Do_loopContext,0)


        def begin_until(self):
            return self.getTypedRuleContext(ForthParser.Begin_untilContext,0)


        def stack_op(self):
            return self.getTypedRuleContext(ForthParser.Stack_opContext,0)


        def literal(self):
            return self.getTypedRuleContext(ForthParser.LiteralContext,0)


        def call(self):
            return self.getTypedRuleContext(ForthParser.CallContext,0)


        def getRuleIndex(self):
            return ForthParser.RULE_element

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElement" ):
                listener.enterElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElement" ):
                listener.exitElement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement" ):
                return visitor.visitElement(self)
            else:
                return visitor.visitChildren(self)




    def element(self):

        localctx = ForthParser.ElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_element)
        try:
            self.state = 33
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.definition()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 27
                self.if_stmt()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 28
                self.do_loop()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 4)
                self.state = 29
                self.begin_until()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 5)
                self.state = 30
                self.stack_op()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 6)
                self.state = 31
                self.literal()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 7)
                self.state = 32
                self.call()
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


    class DefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Token
            self._element = None # ElementContext
            self.body = list() # of ElementContexts

        def ID(self):
            return self.getToken(ForthParser.ID, 0)

        def element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ForthParser.ElementContext)
            else:
                return self.getTypedRuleContext(ForthParser.ElementContext,i)


        def getRuleIndex(self):
            return ForthParser.RULE_definition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefinition" ):
                listener.enterDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefinition" ):
                listener.exitDefinition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefinition" ):
                return visitor.visitDefinition(self)
            else:
                return visitor.visitChildren(self)




    def definition(self):

        localctx = ForthParser.DefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_definition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(ForthParser.T__0)
            self.state = 36
            localctx.name = self.match(ForthParser.ID)
            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 7498) != 0):
                self.state = 37
                localctx._element = self.element()
                localctx.body.append(localctx._element)
                self.state = 42
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 43
            self.match(ForthParser.T__1)
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
            self._element = None # ElementContext
            self.consequent = list() # of ElementContexts
            self.alternate = list() # of ElementContexts

        def element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ForthParser.ElementContext)
            else:
                return self.getTypedRuleContext(ForthParser.ElementContext,i)


        def getRuleIndex(self):
            return ForthParser.RULE_if_stmt

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

        localctx = ForthParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(ForthParser.T__2)
            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 7498) != 0):
                self.state = 46
                localctx._element = self.element()
                localctx.consequent.append(localctx._element)
                self.state = 51
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 52
                self.match(ForthParser.T__3)
                self.state = 56
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 7498) != 0):
                    self.state = 53
                    localctx._element = self.element()
                    localctx.alternate.append(localctx._element)
                    self.state = 58
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 61
            self.match(ForthParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Do_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._element = None # ElementContext
            self.body = list() # of ElementContexts

        def element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ForthParser.ElementContext)
            else:
                return self.getTypedRuleContext(ForthParser.ElementContext,i)


        def getRuleIndex(self):
            return ForthParser.RULE_do_loop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDo_loop" ):
                listener.enterDo_loop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDo_loop" ):
                listener.exitDo_loop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDo_loop" ):
                return visitor.visitDo_loop(self)
            else:
                return visitor.visitChildren(self)




    def do_loop(self):

        localctx = ForthParser.Do_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_do_loop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(ForthParser.T__5)
            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 7498) != 0):
                self.state = 64
                localctx._element = self.element()
                localctx.body.append(localctx._element)
                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 70
            self.match(ForthParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Begin_untilContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._element = None # ElementContext
            self.body = list() # of ElementContexts

        def element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ForthParser.ElementContext)
            else:
                return self.getTypedRuleContext(ForthParser.ElementContext,i)


        def getRuleIndex(self):
            return ForthParser.RULE_begin_until

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBegin_until" ):
                listener.enterBegin_until(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBegin_until" ):
                listener.exitBegin_until(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBegin_until" ):
                return visitor.visitBegin_until(self)
            else:
                return visitor.visitChildren(self)




    def begin_until(self):

        localctx = ForthParser.Begin_untilContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_begin_until)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(ForthParser.T__7)
            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 7498) != 0):
                self.state = 73
                localctx._element = self.element()
                localctx.body.append(localctx._element)
                self.state = 78
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 79
            self.match(ForthParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stack_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def STACK_CMD(self):
            return self.getToken(ForthParser.STACK_CMD, 0)

        def getRuleIndex(self):
            return ForthParser.RULE_stack_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStack_op" ):
                listener.enterStack_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStack_op" ):
                listener.exitStack_op(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStack_op" ):
                return visitor.visitStack_op(self)
            else:
                return visitor.visitChildren(self)




    def stack_op(self):

        localctx = ForthParser.Stack_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_stack_op)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            localctx.op = self.match(ForthParser.STACK_CMD)
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
            self.val = None # Token

        def NUMBER(self):
            return self.getToken(ForthParser.NUMBER, 0)

        def getRuleIndex(self):
            return ForthParser.RULE_literal

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

        localctx = ForthParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            localctx.val = self.match(ForthParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Token

        def ID(self):
            return self.getToken(ForthParser.ID, 0)

        def getRuleIndex(self):
            return ForthParser.RULE_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCall" ):
                listener.enterCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCall" ):
                listener.exitCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall" ):
                return visitor.visitCall(self)
            else:
                return visitor.visitChildren(self)




    def call(self):

        localctx = ForthParser.CallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            localctx.name = self.match(ForthParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





