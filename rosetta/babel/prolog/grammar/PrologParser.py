# Generated from rosetta/babel/prolog/grammar/Prolog.g4 by ANTLR 4.13.2
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
        4,1,16,87,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,5,0,24,8,0,10,0,12,0,27,
        9,0,1,0,1,0,1,1,1,1,1,1,3,1,34,8,1,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,
        3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,5,5,51,8,5,10,5,12,5,54,9,5,1,6,1,
        6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,64,8,6,1,7,1,7,1,7,1,7,1,7,1,8,1,8,
        1,8,1,8,1,8,1,8,3,8,77,8,8,1,8,1,8,3,8,81,8,8,1,9,1,9,1,10,1,10,
        1,10,0,0,11,0,2,4,6,8,10,12,14,16,18,20,0,0,85,0,25,1,0,0,0,2,33,
        1,0,0,0,4,35,1,0,0,0,6,38,1,0,0,0,8,43,1,0,0,0,10,47,1,0,0,0,12,
        63,1,0,0,0,14,65,1,0,0,0,16,80,1,0,0,0,18,82,1,0,0,0,20,84,1,0,0,
        0,22,24,3,2,1,0,23,22,1,0,0,0,24,27,1,0,0,0,25,23,1,0,0,0,25,26,
        1,0,0,0,26,28,1,0,0,0,27,25,1,0,0,0,28,29,5,0,0,1,29,1,1,0,0,0,30,
        34,3,4,2,0,31,34,3,6,3,0,32,34,3,8,4,0,33,30,1,0,0,0,33,31,1,0,0,
        0,33,32,1,0,0,0,34,3,1,0,0,0,35,36,3,12,6,0,36,37,5,1,0,0,37,5,1,
        0,0,0,38,39,3,12,6,0,39,40,5,2,0,0,40,41,3,10,5,0,41,42,5,1,0,0,
        42,7,1,0,0,0,43,44,5,3,0,0,44,45,3,10,5,0,45,46,5,1,0,0,46,9,1,0,
        0,0,47,52,3,12,6,0,48,49,5,4,0,0,49,51,3,12,6,0,50,48,1,0,0,0,51,
        54,1,0,0,0,52,50,1,0,0,0,52,53,1,0,0,0,53,11,1,0,0,0,54,52,1,0,0,
        0,55,64,3,18,9,0,56,64,3,20,10,0,57,64,3,16,8,0,58,64,3,14,7,0,59,
        60,5,5,0,0,60,61,3,12,6,0,61,62,5,6,0,0,62,64,1,0,0,0,63,55,1,0,
        0,0,63,56,1,0,0,0,63,57,1,0,0,0,63,58,1,0,0,0,63,59,1,0,0,0,64,13,
        1,0,0,0,65,66,3,18,9,0,66,67,5,5,0,0,67,68,3,10,5,0,68,69,5,6,0,
        0,69,15,1,0,0,0,70,71,5,7,0,0,71,81,5,8,0,0,72,73,5,7,0,0,73,76,
        3,10,5,0,74,75,5,9,0,0,75,77,3,12,6,0,76,74,1,0,0,0,76,77,1,0,0,
        0,77,78,1,0,0,0,78,79,5,8,0,0,79,81,1,0,0,0,80,70,1,0,0,0,80,72,
        1,0,0,0,81,17,1,0,0,0,82,83,5,10,0,0,83,19,1,0,0,0,84,85,5,11,0,
        0,85,21,1,0,0,0,6,25,33,52,63,76,80
    ]

class PrologParser ( Parser ):

    grammarFileName = "Prolog.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'.'", "':-'", "'?-'", "','", "'('", "')'", 
                     "'['", "']'", "'|'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "ATOM", "VARIABLE", "NUMBER", 
                      "NEWLINE", "WS", "COMMENT", "COMMENT2" ]

    RULE_program = 0
    RULE_clause = 1
    RULE_fact = 2
    RULE_rule = 3
    RULE_query = 4
    RULE_term_list = 5
    RULE_term = 6
    RULE_structure = 7
    RULE_list = 8
    RULE_atom = 9
    RULE_variable = 10

    ruleNames =  [ "program", "clause", "fact", "rule", "query", "term_list", 
                   "term", "structure", "list", "atom", "variable" ]

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
    ATOM=10
    VARIABLE=11
    NUMBER=12
    NEWLINE=13
    WS=14
    COMMENT=15
    COMMENT2=16

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
            return self.getToken(PrologParser.EOF, 0)

        def clause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PrologParser.ClauseContext)
            else:
                return self.getTypedRuleContext(PrologParser.ClauseContext,i)


        def getRuleIndex(self):
            return PrologParser.RULE_program

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

        localctx = PrologParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3240) != 0):
                self.state = 22
                self.clause()
                self.state = 27
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 28
            self.match(PrologParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fact(self):
            return self.getTypedRuleContext(PrologParser.FactContext,0)


        def rule_(self):
            return self.getTypedRuleContext(PrologParser.RuleContext,0)


        def query(self):
            return self.getTypedRuleContext(PrologParser.QueryContext,0)


        def getRuleIndex(self):
            return PrologParser.RULE_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClause" ):
                listener.enterClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClause" ):
                listener.exitClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClause" ):
                return visitor.visitClause(self)
            else:
                return visitor.visitChildren(self)




    def clause(self):

        localctx = PrologParser.ClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_clause)
        try:
            self.state = 33
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 30
                self.fact()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 31
                self.rule_()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 32
                self.query()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(PrologParser.TermContext,0)


        def getRuleIndex(self):
            return PrologParser.RULE_fact

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFact" ):
                listener.enterFact(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFact" ):
                listener.exitFact(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFact" ):
                return visitor.visitFact(self)
            else:
                return visitor.visitChildren(self)




    def fact(self):

        localctx = PrologParser.FactContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_fact)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.term()
            self.state = 36
            self.match(PrologParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RuleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(PrologParser.TermContext,0)


        def term_list(self):
            return self.getTypedRuleContext(PrologParser.Term_listContext,0)


        def getRuleIndex(self):
            return PrologParser.RULE_rule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRule" ):
                listener.enterRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRule" ):
                listener.exitRule(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRule" ):
                return visitor.visitRule(self)
            else:
                return visitor.visitChildren(self)




    def rule_(self):

        localctx = PrologParser.RuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_rule)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.term()
            self.state = 39
            self.match(PrologParser.T__1)
            self.state = 40
            self.term_list()
            self.state = 41
            self.match(PrologParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QueryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term_list(self):
            return self.getTypedRuleContext(PrologParser.Term_listContext,0)


        def getRuleIndex(self):
            return PrologParser.RULE_query

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuery" ):
                listener.enterQuery(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuery" ):
                listener.exitQuery(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuery" ):
                return visitor.visitQuery(self)
            else:
                return visitor.visitChildren(self)




    def query(self):

        localctx = PrologParser.QueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_query)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(PrologParser.T__2)
            self.state = 44
            self.term_list()
            self.state = 45
            self.match(PrologParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Term_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PrologParser.TermContext)
            else:
                return self.getTypedRuleContext(PrologParser.TermContext,i)


        def getRuleIndex(self):
            return PrologParser.RULE_term_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm_list" ):
                listener.enterTerm_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm_list" ):
                listener.exitTerm_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm_list" ):
                return visitor.visitTerm_list(self)
            else:
                return visitor.visitChildren(self)




    def term_list(self):

        localctx = PrologParser.Term_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_term_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.term()
            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 48
                self.match(PrologParser.T__3)
                self.state = 49
                self.term()
                self.state = 54
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self):
            return self.getTypedRuleContext(PrologParser.AtomContext,0)


        def variable(self):
            return self.getTypedRuleContext(PrologParser.VariableContext,0)


        def list_(self):
            return self.getTypedRuleContext(PrologParser.ListContext,0)


        def structure(self):
            return self.getTypedRuleContext(PrologParser.StructureContext,0)


        def term(self):
            return self.getTypedRuleContext(PrologParser.TermContext,0)


        def getRuleIndex(self):
            return PrologParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = PrologParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_term)
        try:
            self.state = 63
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 55
                self.atom()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 56
                self.variable()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 57
                self.list_()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 58
                self.structure()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 59
                self.match(PrologParser.T__4)
                self.state = 60
                self.term()
                self.state = 61
                self.match(PrologParser.T__5)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructureContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self):
            return self.getTypedRuleContext(PrologParser.AtomContext,0)


        def term_list(self):
            return self.getTypedRuleContext(PrologParser.Term_listContext,0)


        def getRuleIndex(self):
            return PrologParser.RULE_structure

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStructure" ):
                listener.enterStructure(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStructure" ):
                listener.exitStructure(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructure" ):
                return visitor.visitStructure(self)
            else:
                return visitor.visitChildren(self)




    def structure(self):

        localctx = PrologParser.StructureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_structure)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.atom()
            self.state = 66
            self.match(PrologParser.T__4)
            self.state = 67
            self.term_list()
            self.state = 68
            self.match(PrologParser.T__5)
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

        def term_list(self):
            return self.getTypedRuleContext(PrologParser.Term_listContext,0)


        def term(self):
            return self.getTypedRuleContext(PrologParser.TermContext,0)


        def getRuleIndex(self):
            return PrologParser.RULE_list

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

        localctx = PrologParser.ListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_list)
        self._la = 0 # Token type
        try:
            self.state = 80
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 70
                self.match(PrologParser.T__6)
                self.state = 71
                self.match(PrologParser.T__7)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 72
                self.match(PrologParser.T__6)
                self.state = 73
                self.term_list()
                self.state = 76
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==9:
                    self.state = 74
                    self.match(PrologParser.T__8)
                    self.state = 75
                    self.term()


                self.state = 78
                self.match(PrologParser.T__7)
                pass


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

        def ATOM(self):
            return self.getToken(PrologParser.ATOM, 0)

        def getRuleIndex(self):
            return PrologParser.RULE_atom

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

        localctx = PrologParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_atom)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(PrologParser.ATOM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(PrologParser.VARIABLE, 0)

        def getRuleIndex(self):
            return PrologParser.RULE_variable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)




    def variable(self):

        localctx = PrologParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(PrologParser.VARIABLE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





