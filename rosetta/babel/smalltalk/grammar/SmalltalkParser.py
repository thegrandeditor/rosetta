# Generated from rosetta/babel/smalltalk/grammar/Smalltalk.g4 by ANTLR 4.13.2
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
        4,1,21,188,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,1,0,5,0,48,8,0,10,0,12,0,51,9,0,1,0,1,0,
        1,1,1,1,1,1,1,1,3,1,59,8,1,1,2,1,2,1,2,1,2,3,2,65,8,2,1,2,1,2,1,
        2,5,2,70,8,2,10,2,12,2,73,9,2,1,3,1,3,3,3,77,8,3,1,3,1,3,1,3,3,3,
        82,8,3,1,3,1,3,1,4,1,4,1,4,3,4,89,8,4,1,5,1,5,1,5,1,5,1,6,1,6,1,
        6,4,6,98,8,6,11,6,12,6,99,1,7,1,7,5,7,104,8,7,10,7,12,7,107,9,7,
        1,8,1,8,1,8,3,8,112,8,8,1,9,1,9,4,9,116,8,9,11,9,12,9,117,1,10,1,
        10,1,10,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,3,12,132,8,
        12,1,13,1,13,1,13,5,13,137,8,13,10,13,12,13,140,9,13,1,13,3,13,143,
        8,13,1,13,1,13,1,13,5,13,148,8,13,10,13,12,13,151,9,13,1,13,1,13,
        1,14,1,14,1,14,1,14,3,14,159,8,14,1,15,1,15,1,16,1,16,1,17,1,17,
        1,17,1,17,3,17,169,8,17,1,18,1,18,5,18,173,8,18,10,18,12,18,176,
        9,18,1,18,1,18,1,19,1,19,1,20,1,20,1,21,1,21,1,22,1,22,1,22,0,0,
        23,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,
        44,0,0,190,0,49,1,0,0,0,2,58,1,0,0,0,4,60,1,0,0,0,6,76,1,0,0,0,8,
        88,1,0,0,0,10,90,1,0,0,0,12,94,1,0,0,0,14,101,1,0,0,0,16,111,1,0,
        0,0,18,115,1,0,0,0,20,119,1,0,0,0,22,122,1,0,0,0,24,131,1,0,0,0,
        26,133,1,0,0,0,28,158,1,0,0,0,30,160,1,0,0,0,32,162,1,0,0,0,34,164,
        1,0,0,0,36,170,1,0,0,0,38,179,1,0,0,0,40,181,1,0,0,0,42,183,1,0,
        0,0,44,185,1,0,0,0,46,48,3,2,1,0,47,46,1,0,0,0,48,51,1,0,0,0,49,
        47,1,0,0,0,49,50,1,0,0,0,50,52,1,0,0,0,51,49,1,0,0,0,52,53,5,0,0,
        1,53,1,1,0,0,0,54,59,3,4,2,0,55,56,3,8,4,0,56,57,5,1,0,0,57,59,1,
        0,0,0,58,54,1,0,0,0,58,55,1,0,0,0,59,3,1,0,0,0,60,61,3,38,19,0,61,
        64,5,12,0,0,62,65,3,34,17,0,63,65,3,38,19,0,64,62,1,0,0,0,64,63,
        1,0,0,0,65,66,1,0,0,0,66,67,5,13,0,0,67,71,3,32,16,0,68,70,3,6,3,
        0,69,68,1,0,0,0,70,73,1,0,0,0,71,69,1,0,0,0,71,72,1,0,0,0,72,5,1,
        0,0,0,73,71,1,0,0,0,74,77,3,34,17,0,75,77,3,38,19,0,76,74,1,0,0,
        0,76,75,1,0,0,0,77,81,1,0,0,0,78,82,3,40,20,0,79,82,3,42,21,0,80,
        82,3,44,22,0,81,78,1,0,0,0,81,79,1,0,0,0,81,80,1,0,0,0,82,83,1,0,
        0,0,83,84,3,26,13,0,84,7,1,0,0,0,85,89,3,10,5,0,86,89,3,12,6,0,87,
        89,3,14,7,0,88,85,1,0,0,0,88,86,1,0,0,0,88,87,1,0,0,0,89,9,1,0,0,
        0,90,91,3,38,19,0,91,92,5,2,0,0,92,93,3,8,4,0,93,11,1,0,0,0,94,97,
        3,14,7,0,95,96,5,3,0,0,96,98,3,16,8,0,97,95,1,0,0,0,98,99,1,0,0,
        0,99,97,1,0,0,0,99,100,1,0,0,0,100,13,1,0,0,0,101,105,3,24,12,0,
        102,104,3,16,8,0,103,102,1,0,0,0,104,107,1,0,0,0,105,103,1,0,0,0,
        105,106,1,0,0,0,106,15,1,0,0,0,107,105,1,0,0,0,108,112,3,18,9,0,
        109,112,3,20,10,0,110,112,3,22,11,0,111,108,1,0,0,0,111,109,1,0,
        0,0,111,110,1,0,0,0,112,17,1,0,0,0,113,114,5,15,0,0,114,116,3,8,
        4,0,115,113,1,0,0,0,116,117,1,0,0,0,117,115,1,0,0,0,117,118,1,0,
        0,0,118,19,1,0,0,0,119,120,5,16,0,0,120,121,3,24,12,0,121,21,1,0,
        0,0,122,123,3,38,19,0,123,23,1,0,0,0,124,132,3,38,19,0,125,132,3,
        28,14,0,126,132,3,26,13,0,127,128,5,4,0,0,128,129,3,8,4,0,129,130,
        5,5,0,0,130,132,1,0,0,0,131,124,1,0,0,0,131,125,1,0,0,0,131,126,
        1,0,0,0,131,127,1,0,0,0,132,25,1,0,0,0,133,138,5,6,0,0,134,135,5,
        7,0,0,135,137,3,38,19,0,136,134,1,0,0,0,137,140,1,0,0,0,138,136,
        1,0,0,0,138,139,1,0,0,0,139,142,1,0,0,0,140,138,1,0,0,0,141,143,
        5,8,0,0,142,141,1,0,0,0,142,143,1,0,0,0,143,149,1,0,0,0,144,145,
        3,8,4,0,145,146,5,1,0,0,146,148,1,0,0,0,147,144,1,0,0,0,148,151,
        1,0,0,0,149,147,1,0,0,0,149,150,1,0,0,0,150,152,1,0,0,0,151,149,
        1,0,0,0,152,153,5,9,0,0,153,27,1,0,0,0,154,159,3,30,15,0,155,159,
        3,32,16,0,156,159,3,34,17,0,157,159,3,36,18,0,158,154,1,0,0,0,158,
        155,1,0,0,0,158,156,1,0,0,0,158,157,1,0,0,0,159,29,1,0,0,0,160,161,
        5,17,0,0,161,31,1,0,0,0,162,163,5,18,0,0,163,33,1,0,0,0,164,168,
        5,10,0,0,165,169,3,38,19,0,166,169,5,15,0,0,167,169,5,16,0,0,168,
        165,1,0,0,0,168,166,1,0,0,0,168,167,1,0,0,0,169,35,1,0,0,0,170,174,
        5,11,0,0,171,173,3,28,14,0,172,171,1,0,0,0,173,176,1,0,0,0,174,172,
        1,0,0,0,174,175,1,0,0,0,175,177,1,0,0,0,176,174,1,0,0,0,177,178,
        5,5,0,0,178,37,1,0,0,0,179,180,5,14,0,0,180,39,1,0,0,0,181,182,5,
        15,0,0,182,41,1,0,0,0,183,184,5,16,0,0,184,43,1,0,0,0,185,186,3,
        38,19,0,186,45,1,0,0,0,18,49,58,64,71,76,81,88,99,105,111,117,131,
        138,142,149,158,168,174
    ]

class SmalltalkParser ( Parser ):

    grammarFileName = "Smalltalk.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'.'", "':='", "';'", "'('", "')'", "'['", 
                     "':'", "'|'", "']'", "'#'", "'#('", "'subclass:'", 
                     "'instanceVariableNames:'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "SUBCLASS_K", "INSTANCE_VARIABLE_NAMES_K", "IDENTIFIER", 
                      "KEYWORD", "BINARY_SELECTOR", "NUMBER", "STRING", 
                      "NEWLINE", "WS", "COMMENT" ]

    RULE_program = 0
    RULE_executable_unit = 1
    RULE_class_definition = 2
    RULE_method_definition = 3
    RULE_expression = 4
    RULE_assignment = 5
    RULE_cascade = 6
    RULE_message_expression = 7
    RULE_messages = 8
    RULE_keyword_message = 9
    RULE_binary_message = 10
    RULE_unary_message = 11
    RULE_primary = 12
    RULE_block = 13
    RULE_literal = 14
    RULE_number = 15
    RULE_string_literal = 16
    RULE_symbol = 17
    RULE_array_literal = 18
    RULE_identifier = 19
    RULE_keyword_selector = 20
    RULE_binary_selector = 21
    RULE_unary_selector = 22

    ruleNames =  [ "program", "executable_unit", "class_definition", "method_definition", 
                   "expression", "assignment", "cascade", "message_expression", 
                   "messages", "keyword_message", "binary_message", "unary_message", 
                   "primary", "block", "literal", "number", "string_literal", 
                   "symbol", "array_literal", "identifier", "keyword_selector", 
                   "binary_selector", "unary_selector" ]

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
    SUBCLASS_K=12
    INSTANCE_VARIABLE_NAMES_K=13
    IDENTIFIER=14
    KEYWORD=15
    BINARY_SELECTOR=16
    NUMBER=17
    STRING=18
    NEWLINE=19
    WS=20
    COMMENT=21

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
            return self.getToken(SmalltalkParser.EOF, 0)

        def executable_unit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SmalltalkParser.Executable_unitContext)
            else:
                return self.getTypedRuleContext(SmalltalkParser.Executable_unitContext,i)


        def getRuleIndex(self):
            return SmalltalkParser.RULE_program

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

        localctx = SmalltalkParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 412752) != 0):
                self.state = 46
                self.executable_unit()
                self.state = 51
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 52
            self.match(SmalltalkParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Executable_unitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_definition(self):
            return self.getTypedRuleContext(SmalltalkParser.Class_definitionContext,0)


        def expression(self):
            return self.getTypedRuleContext(SmalltalkParser.ExpressionContext,0)


        def getRuleIndex(self):
            return SmalltalkParser.RULE_executable_unit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExecutable_unit" ):
                listener.enterExecutable_unit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExecutable_unit" ):
                listener.exitExecutable_unit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExecutable_unit" ):
                return visitor.visitExecutable_unit(self)
            else:
                return visitor.visitChildren(self)




    def executable_unit(self):

        localctx = SmalltalkParser.Executable_unitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_executable_unit)
        try:
            self.state = 58
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 54
                self.class_definition()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 55
                self.expression()
                self.state = 56
                self.match(SmalltalkParser.T__0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_definitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SmalltalkParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(SmalltalkParser.IdentifierContext,i)


        def SUBCLASS_K(self):
            return self.getToken(SmalltalkParser.SUBCLASS_K, 0)

        def INSTANCE_VARIABLE_NAMES_K(self):
            return self.getToken(SmalltalkParser.INSTANCE_VARIABLE_NAMES_K, 0)

        def string_literal(self):
            return self.getTypedRuleContext(SmalltalkParser.String_literalContext,0)


        def symbol(self):
            return self.getTypedRuleContext(SmalltalkParser.SymbolContext,0)


        def method_definition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SmalltalkParser.Method_definitionContext)
            else:
                return self.getTypedRuleContext(SmalltalkParser.Method_definitionContext,i)


        def getRuleIndex(self):
            return SmalltalkParser.RULE_class_definition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClass_definition" ):
                listener.enterClass_definition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClass_definition" ):
                listener.exitClass_definition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_definition" ):
                return visitor.visitClass_definition(self)
            else:
                return visitor.visitChildren(self)




    def class_definition(self):

        localctx = SmalltalkParser.Class_definitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_class_definition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.identifier()
            self.state = 61
            self.match(SmalltalkParser.SUBCLASS_K)
            self.state = 64
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.state = 62
                self.symbol()
                pass
            elif token in [14]:
                self.state = 63
                self.identifier()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 66
            self.match(SmalltalkParser.INSTANCE_VARIABLE_NAMES_K)
            self.state = 67
            self.string_literal()
            self.state = 71
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 68
                    self.method_definition() 
                self.state = 73
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_definitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(SmalltalkParser.BlockContext,0)


        def symbol(self):
            return self.getTypedRuleContext(SmalltalkParser.SymbolContext,0)


        def identifier(self):
            return self.getTypedRuleContext(SmalltalkParser.IdentifierContext,0)


        def keyword_selector(self):
            return self.getTypedRuleContext(SmalltalkParser.Keyword_selectorContext,0)


        def binary_selector(self):
            return self.getTypedRuleContext(SmalltalkParser.Binary_selectorContext,0)


        def unary_selector(self):
            return self.getTypedRuleContext(SmalltalkParser.Unary_selectorContext,0)


        def getRuleIndex(self):
            return SmalltalkParser.RULE_method_definition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethod_definition" ):
                listener.enterMethod_definition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethod_definition" ):
                listener.exitMethod_definition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_definition" ):
                return visitor.visitMethod_definition(self)
            else:
                return visitor.visitChildren(self)




    def method_definition(self):

        localctx = SmalltalkParser.Method_definitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_method_definition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.state = 74
                self.symbol()
                pass
            elif token in [14]:
                self.state = 75
                self.identifier()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 81
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.state = 78
                self.keyword_selector()
                pass
            elif token in [16]:
                self.state = 79
                self.binary_selector()
                pass
            elif token in [14]:
                self.state = 80
                self.unary_selector()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 83
            self.block()
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

        def assignment(self):
            return self.getTypedRuleContext(SmalltalkParser.AssignmentContext,0)


        def cascade(self):
            return self.getTypedRuleContext(SmalltalkParser.CascadeContext,0)


        def message_expression(self):
            return self.getTypedRuleContext(SmalltalkParser.Message_expressionContext,0)


        def getRuleIndex(self):
            return SmalltalkParser.RULE_expression

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

        localctx = SmalltalkParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_expression)
        try:
            self.state = 88
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 85
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 86
                self.cascade()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 87
                self.message_expression()
                pass


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

        def identifier(self):
            return self.getTypedRuleContext(SmalltalkParser.IdentifierContext,0)


        def expression(self):
            return self.getTypedRuleContext(SmalltalkParser.ExpressionContext,0)


        def getRuleIndex(self):
            return SmalltalkParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = SmalltalkParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.identifier()
            self.state = 91
            self.match(SmalltalkParser.T__1)
            self.state = 92
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CascadeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def message_expression(self):
            return self.getTypedRuleContext(SmalltalkParser.Message_expressionContext,0)


        def messages(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SmalltalkParser.MessagesContext)
            else:
                return self.getTypedRuleContext(SmalltalkParser.MessagesContext,i)


        def getRuleIndex(self):
            return SmalltalkParser.RULE_cascade

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCascade" ):
                listener.enterCascade(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCascade" ):
                listener.exitCascade(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCascade" ):
                return visitor.visitCascade(self)
            else:
                return visitor.visitChildren(self)




    def cascade(self):

        localctx = SmalltalkParser.CascadeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_cascade)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.message_expression()
            self.state = 97 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 95
                    self.match(SmalltalkParser.T__2)
                    self.state = 96
                    self.messages()

                else:
                    raise NoViableAltException(self)
                self.state = 99 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Message_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primary(self):
            return self.getTypedRuleContext(SmalltalkParser.PrimaryContext,0)


        def messages(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SmalltalkParser.MessagesContext)
            else:
                return self.getTypedRuleContext(SmalltalkParser.MessagesContext,i)


        def getRuleIndex(self):
            return SmalltalkParser.RULE_message_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMessage_expression" ):
                listener.enterMessage_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMessage_expression" ):
                listener.exitMessage_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMessage_expression" ):
                return visitor.visitMessage_expression(self)
            else:
                return visitor.visitChildren(self)




    def message_expression(self):

        localctx = SmalltalkParser.Message_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_message_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.primary()
            self.state = 105
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 102
                    self.messages() 
                self.state = 107
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MessagesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def keyword_message(self):
            return self.getTypedRuleContext(SmalltalkParser.Keyword_messageContext,0)


        def binary_message(self):
            return self.getTypedRuleContext(SmalltalkParser.Binary_messageContext,0)


        def unary_message(self):
            return self.getTypedRuleContext(SmalltalkParser.Unary_messageContext,0)


        def getRuleIndex(self):
            return SmalltalkParser.RULE_messages

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMessages" ):
                listener.enterMessages(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMessages" ):
                listener.exitMessages(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMessages" ):
                return visitor.visitMessages(self)
            else:
                return visitor.visitChildren(self)




    def messages(self):

        localctx = SmalltalkParser.MessagesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_messages)
        try:
            self.state = 111
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 108
                self.keyword_message()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 109
                self.binary_message()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 3)
                self.state = 110
                self.unary_message()
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


    class Keyword_messageContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEYWORD(self, i:int=None):
            if i is None:
                return self.getTokens(SmalltalkParser.KEYWORD)
            else:
                return self.getToken(SmalltalkParser.KEYWORD, i)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SmalltalkParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SmalltalkParser.ExpressionContext,i)


        def getRuleIndex(self):
            return SmalltalkParser.RULE_keyword_message

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKeyword_message" ):
                listener.enterKeyword_message(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKeyword_message" ):
                listener.exitKeyword_message(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKeyword_message" ):
                return visitor.visitKeyword_message(self)
            else:
                return visitor.visitChildren(self)




    def keyword_message(self):

        localctx = SmalltalkParser.Keyword_messageContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_keyword_message)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 113
                    self.match(SmalltalkParser.KEYWORD)
                    self.state = 114
                    self.expression()

                else:
                    raise NoViableAltException(self)
                self.state = 117 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Binary_messageContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BINARY_SELECTOR(self):
            return self.getToken(SmalltalkParser.BINARY_SELECTOR, 0)

        def primary(self):
            return self.getTypedRuleContext(SmalltalkParser.PrimaryContext,0)


        def getRuleIndex(self):
            return SmalltalkParser.RULE_binary_message

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinary_message" ):
                listener.enterBinary_message(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinary_message" ):
                listener.exitBinary_message(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinary_message" ):
                return visitor.visitBinary_message(self)
            else:
                return visitor.visitChildren(self)




    def binary_message(self):

        localctx = SmalltalkParser.Binary_messageContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_binary_message)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.match(SmalltalkParser.BINARY_SELECTOR)
            self.state = 120
            self.primary()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Unary_messageContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(SmalltalkParser.IdentifierContext,0)


        def getRuleIndex(self):
            return SmalltalkParser.RULE_unary_message

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnary_message" ):
                listener.enterUnary_message(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnary_message" ):
                listener.exitUnary_message(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnary_message" ):
                return visitor.visitUnary_message(self)
            else:
                return visitor.visitChildren(self)




    def unary_message(self):

        localctx = SmalltalkParser.Unary_messageContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_unary_message)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.identifier()
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

        def identifier(self):
            return self.getTypedRuleContext(SmalltalkParser.IdentifierContext,0)


        def literal(self):
            return self.getTypedRuleContext(SmalltalkParser.LiteralContext,0)


        def block(self):
            return self.getTypedRuleContext(SmalltalkParser.BlockContext,0)


        def expression(self):
            return self.getTypedRuleContext(SmalltalkParser.ExpressionContext,0)


        def getRuleIndex(self):
            return SmalltalkParser.RULE_primary

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

        localctx = SmalltalkParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_primary)
        try:
            self.state = 131
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                self.identifier()
                pass
            elif token in [10, 11, 17, 18]:
                self.enterOuterAlt(localctx, 2)
                self.state = 125
                self.literal()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 126
                self.block()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 4)
                self.state = 127
                self.match(SmalltalkParser.T__3)
                self.state = 128
                self.expression()
                self.state = 129
                self.match(SmalltalkParser.T__4)
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


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SmalltalkParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(SmalltalkParser.IdentifierContext,i)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SmalltalkParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SmalltalkParser.ExpressionContext,i)


        def getRuleIndex(self):
            return SmalltalkParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = SmalltalkParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.match(SmalltalkParser.T__5)
            self.state = 138
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 134
                self.match(SmalltalkParser.T__6)
                self.state = 135
                self.identifier()
                self.state = 140
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 141
                self.match(SmalltalkParser.T__7)


            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 412752) != 0):
                self.state = 144
                self.expression()
                self.state = 145
                self.match(SmalltalkParser.T__0)
                self.state = 151
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 152
            self.match(SmalltalkParser.T__8)
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

        def number(self):
            return self.getTypedRuleContext(SmalltalkParser.NumberContext,0)


        def string_literal(self):
            return self.getTypedRuleContext(SmalltalkParser.String_literalContext,0)


        def symbol(self):
            return self.getTypedRuleContext(SmalltalkParser.SymbolContext,0)


        def array_literal(self):
            return self.getTypedRuleContext(SmalltalkParser.Array_literalContext,0)


        def getRuleIndex(self):
            return SmalltalkParser.RULE_literal

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

        localctx = SmalltalkParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_literal)
        try:
            self.state = 158
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                self.enterOuterAlt(localctx, 1)
                self.state = 154
                self.number()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 2)
                self.state = 155
                self.string_literal()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 3)
                self.state = 156
                self.symbol()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 4)
                self.state = 157
                self.array_literal()
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


    class NumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(SmalltalkParser.NUMBER, 0)

        def getRuleIndex(self):
            return SmalltalkParser.RULE_number

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

        localctx = SmalltalkParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.match(SmalltalkParser.NUMBER)
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
            return self.getToken(SmalltalkParser.STRING, 0)

        def getRuleIndex(self):
            return SmalltalkParser.RULE_string_literal

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

        localctx = SmalltalkParser.String_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_string_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.match(SmalltalkParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SymbolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(SmalltalkParser.IdentifierContext,0)


        def KEYWORD(self):
            return self.getToken(SmalltalkParser.KEYWORD, 0)

        def BINARY_SELECTOR(self):
            return self.getToken(SmalltalkParser.BINARY_SELECTOR, 0)

        def getRuleIndex(self):
            return SmalltalkParser.RULE_symbol

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSymbol" ):
                listener.enterSymbol(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSymbol" ):
                listener.exitSymbol(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSymbol" ):
                return visitor.visitSymbol(self)
            else:
                return visitor.visitChildren(self)




    def symbol(self):

        localctx = SmalltalkParser.SymbolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_symbol)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.match(SmalltalkParser.T__9)
            self.state = 168
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.state = 165
                self.identifier()
                pass
            elif token in [15]:
                self.state = 166
                self.match(SmalltalkParser.KEYWORD)
                pass
            elif token in [16]:
                self.state = 167
                self.match(SmalltalkParser.BINARY_SELECTOR)
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


    class Array_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SmalltalkParser.LiteralContext)
            else:
                return self.getTypedRuleContext(SmalltalkParser.LiteralContext,i)


        def getRuleIndex(self):
            return SmalltalkParser.RULE_array_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray_literal" ):
                listener.enterArray_literal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray_literal" ):
                listener.exitArray_literal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_literal" ):
                return visitor.visitArray_literal(self)
            else:
                return visitor.visitChildren(self)




    def array_literal(self):

        localctx = SmalltalkParser.Array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_array_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.match(SmalltalkParser.T__10)
            self.state = 174
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 396288) != 0):
                self.state = 171
                self.literal()
                self.state = 176
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 177
            self.match(SmalltalkParser.T__4)
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
            return self.getToken(SmalltalkParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return SmalltalkParser.RULE_identifier

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

        localctx = SmalltalkParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.match(SmalltalkParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Keyword_selectorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEYWORD(self):
            return self.getToken(SmalltalkParser.KEYWORD, 0)

        def getRuleIndex(self):
            return SmalltalkParser.RULE_keyword_selector

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKeyword_selector" ):
                listener.enterKeyword_selector(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKeyword_selector" ):
                listener.exitKeyword_selector(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKeyword_selector" ):
                return visitor.visitKeyword_selector(self)
            else:
                return visitor.visitChildren(self)




    def keyword_selector(self):

        localctx = SmalltalkParser.Keyword_selectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_keyword_selector)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.match(SmalltalkParser.KEYWORD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Binary_selectorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BINARY_SELECTOR(self):
            return self.getToken(SmalltalkParser.BINARY_SELECTOR, 0)

        def getRuleIndex(self):
            return SmalltalkParser.RULE_binary_selector

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinary_selector" ):
                listener.enterBinary_selector(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinary_selector" ):
                listener.exitBinary_selector(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinary_selector" ):
                return visitor.visitBinary_selector(self)
            else:
                return visitor.visitChildren(self)




    def binary_selector(self):

        localctx = SmalltalkParser.Binary_selectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_binary_selector)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.match(SmalltalkParser.BINARY_SELECTOR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Unary_selectorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(SmalltalkParser.IdentifierContext,0)


        def getRuleIndex(self):
            return SmalltalkParser.RULE_unary_selector

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnary_selector" ):
                listener.enterUnary_selector(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnary_selector" ):
                listener.exitUnary_selector(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnary_selector" ):
                return visitor.visitUnary_selector(self)
            else:
                return visitor.visitChildren(self)




    def unary_selector(self):

        localctx = SmalltalkParser.Unary_selectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_unary_selector)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





