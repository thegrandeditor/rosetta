# Generated from rosetta/babel/algol/grammar/Algol.g4 by ANTLR 4.13.2
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
        4,1,42,229,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,1,0,1,0,1,0,1,1,1,1,3,1,54,8,
        1,1,1,3,1,57,8,1,1,1,1,1,1,2,1,2,1,2,4,2,64,8,2,11,2,12,2,65,1,3,
        1,3,1,3,3,3,71,8,3,1,4,1,4,1,4,1,4,5,4,77,8,4,10,4,12,4,80,9,4,1,
        5,1,5,1,5,1,6,1,6,1,6,3,6,88,8,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,5,7,
        97,8,7,10,7,12,7,100,9,7,1,7,1,7,1,8,1,8,1,8,5,8,107,8,8,10,8,12,
        8,110,9,8,3,8,112,8,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,121,8,9,1,
        10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,5,11,132,8,11,10,11,12,
        11,135,9,11,1,11,1,11,3,11,139,8,11,1,12,1,12,1,12,1,12,1,12,1,12,
        3,12,147,8,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,1,14,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,
        1,15,1,15,1,15,3,15,175,8,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,
        1,15,1,15,1,15,1,15,1,15,5,15,189,8,15,10,15,12,15,192,9,15,1,16,
        1,16,1,16,1,16,1,16,5,16,199,8,16,10,16,12,16,202,9,16,1,16,1,16,
        3,16,206,8,16,1,16,3,16,209,8,16,1,17,1,17,1,17,1,17,3,17,215,8,
        17,1,18,1,18,1,19,1,19,1,20,1,20,1,21,1,21,1,22,1,22,1,23,1,23,1,
        23,0,1,30,24,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,
        38,40,42,44,46,0,6,1,0,33,34,1,0,6,11,1,0,12,13,1,0,14,15,1,0,28,
        30,1,0,31,32,236,0,48,1,0,0,0,2,51,1,0,0,0,4,63,1,0,0,0,6,70,1,0,
        0,0,8,72,1,0,0,0,10,81,1,0,0,0,12,84,1,0,0,0,14,92,1,0,0,0,16,111,
        1,0,0,0,18,120,1,0,0,0,20,122,1,0,0,0,22,126,1,0,0,0,24,140,1,0,
        0,0,26,148,1,0,0,0,28,159,1,0,0,0,30,174,1,0,0,0,32,208,1,0,0,0,
        34,214,1,0,0,0,36,216,1,0,0,0,38,218,1,0,0,0,40,220,1,0,0,0,42,222,
        1,0,0,0,44,224,1,0,0,0,46,226,1,0,0,0,48,49,3,2,1,0,49,50,5,0,0,
        1,50,1,1,0,0,0,51,53,5,16,0,0,52,54,3,4,2,0,53,52,1,0,0,0,53,54,
        1,0,0,0,54,56,1,0,0,0,55,57,3,16,8,0,56,55,1,0,0,0,56,57,1,0,0,0,
        57,58,1,0,0,0,58,59,5,17,0,0,59,3,1,0,0,0,60,61,3,6,3,0,61,62,5,
        1,0,0,62,64,1,0,0,0,63,60,1,0,0,0,64,65,1,0,0,0,65,63,1,0,0,0,65,
        66,1,0,0,0,66,5,1,0,0,0,67,71,3,8,4,0,68,71,3,12,6,0,69,71,3,10,
        5,0,70,67,1,0,0,0,70,68,1,0,0,0,70,69,1,0,0,0,71,7,1,0,0,0,72,73,
        3,36,18,0,73,78,3,38,19,0,74,75,5,2,0,0,75,77,3,38,19,0,76,74,1,
        0,0,0,77,80,1,0,0,0,78,76,1,0,0,0,78,79,1,0,0,0,79,9,1,0,0,0,80,
        78,1,0,0,0,81,82,5,18,0,0,82,83,3,8,4,0,83,11,1,0,0,0,84,85,5,19,
        0,0,85,87,3,38,19,0,86,88,3,14,7,0,87,86,1,0,0,0,87,88,1,0,0,0,88,
        89,1,0,0,0,89,90,5,1,0,0,90,91,3,18,9,0,91,13,1,0,0,0,92,93,5,3,
        0,0,93,98,3,38,19,0,94,95,5,2,0,0,95,97,3,38,19,0,96,94,1,0,0,0,
        97,100,1,0,0,0,98,96,1,0,0,0,98,99,1,0,0,0,99,101,1,0,0,0,100,98,
        1,0,0,0,101,102,5,4,0,0,102,15,1,0,0,0,103,108,3,18,9,0,104,105,
        5,1,0,0,105,107,3,18,9,0,106,104,1,0,0,0,107,110,1,0,0,0,108,106,
        1,0,0,0,108,109,1,0,0,0,109,112,1,0,0,0,110,108,1,0,0,0,111,103,
        1,0,0,0,111,112,1,0,0,0,112,17,1,0,0,0,113,121,3,20,10,0,114,121,
        3,22,11,0,115,121,3,24,12,0,116,121,3,26,13,0,117,121,3,28,14,0,
        118,121,3,2,1,0,119,121,1,0,0,0,120,113,1,0,0,0,120,114,1,0,0,0,
        120,115,1,0,0,0,120,116,1,0,0,0,120,117,1,0,0,0,120,118,1,0,0,0,
        120,119,1,0,0,0,121,19,1,0,0,0,122,123,3,38,19,0,123,124,5,5,0,0,
        124,125,3,30,15,0,125,21,1,0,0,0,126,138,3,38,19,0,127,128,5,3,0,
        0,128,133,3,30,15,0,129,130,5,2,0,0,130,132,3,30,15,0,131,129,1,
        0,0,0,132,135,1,0,0,0,133,131,1,0,0,0,133,134,1,0,0,0,134,136,1,
        0,0,0,135,133,1,0,0,0,136,137,5,4,0,0,137,139,1,0,0,0,138,127,1,
        0,0,0,138,139,1,0,0,0,139,23,1,0,0,0,140,141,5,20,0,0,141,142,3,
        30,15,0,142,143,5,21,0,0,143,146,3,18,9,0,144,145,5,22,0,0,145,147,
        3,18,9,0,146,144,1,0,0,0,146,147,1,0,0,0,147,25,1,0,0,0,148,149,
        5,23,0,0,149,150,3,38,19,0,150,151,5,5,0,0,151,152,3,30,15,0,152,
        153,5,24,0,0,153,154,3,30,15,0,154,155,5,25,0,0,155,156,3,30,15,
        0,156,157,5,26,0,0,157,158,3,18,9,0,158,27,1,0,0,0,159,160,5,27,
        0,0,160,161,3,30,15,0,161,162,5,26,0,0,162,163,3,18,9,0,163,29,1,
        0,0,0,164,165,6,15,-1,0,165,166,5,35,0,0,166,175,3,30,15,7,167,168,
        5,13,0,0,168,175,3,30,15,3,169,170,5,3,0,0,170,171,3,30,15,0,171,
        172,5,4,0,0,172,175,1,0,0,0,173,175,3,32,16,0,174,164,1,0,0,0,174,
        167,1,0,0,0,174,169,1,0,0,0,174,173,1,0,0,0,175,190,1,0,0,0,176,
        177,10,8,0,0,177,178,7,0,0,0,178,189,3,30,15,9,179,180,10,6,0,0,
        180,181,7,1,0,0,181,189,3,30,15,7,182,183,10,5,0,0,183,184,7,2,0,
        0,184,189,3,30,15,6,185,186,10,4,0,0,186,187,7,3,0,0,187,189,3,30,
        15,5,188,176,1,0,0,0,188,179,1,0,0,0,188,182,1,0,0,0,188,185,1,0,
        0,0,189,192,1,0,0,0,190,188,1,0,0,0,190,191,1,0,0,0,191,31,1,0,0,
        0,192,190,1,0,0,0,193,205,3,38,19,0,194,195,5,3,0,0,195,200,3,30,
        15,0,196,197,5,2,0,0,197,199,3,30,15,0,198,196,1,0,0,0,199,202,1,
        0,0,0,200,198,1,0,0,0,200,201,1,0,0,0,201,203,1,0,0,0,202,200,1,
        0,0,0,203,204,5,4,0,0,204,206,1,0,0,0,205,194,1,0,0,0,205,206,1,
        0,0,0,206,209,1,0,0,0,207,209,3,34,17,0,208,193,1,0,0,0,208,207,
        1,0,0,0,209,33,1,0,0,0,210,215,3,40,20,0,211,215,3,42,21,0,212,215,
        3,44,22,0,213,215,3,46,23,0,214,210,1,0,0,0,214,211,1,0,0,0,214,
        212,1,0,0,0,214,213,1,0,0,0,215,35,1,0,0,0,216,217,7,4,0,0,217,37,
        1,0,0,0,218,219,5,36,0,0,219,39,1,0,0,0,220,221,5,37,0,0,221,41,
        1,0,0,0,222,223,5,38,0,0,223,43,1,0,0,0,224,225,5,39,0,0,225,45,
        1,0,0,0,226,227,7,5,0,0,227,47,1,0,0,0,20,53,56,65,70,78,87,98,108,
        111,120,133,138,146,174,188,190,200,205,208,214
    ]

class AlgolParser ( Parser ):

    grammarFileName = "Algol.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "','", "'('", "')'", "':='", "'='", 
                     "<INVALID>", "'<'", "'<='", "'>'", "'>='", "'+'", "'-'", 
                     "'*'", "'/'", "'BEGIN'", "'END'", "'OWN'", "'PROCEDURE'", 
                     "'IF'", "'THEN'", "'ELSE'", "'FOR'", "'STEP'", "'UNTIL'", 
                     "'DO'", "'WHILE'", "'INTEGER'", "'REAL'", "'BOOLEAN'", 
                     "'TRUE'", "'FALSE'", "'OR'", "'AND'", "'NOT'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "EQ", "NE", "LT", "LE", 
                      "GT", "GE", "PLUS", "MINUS", "STAR", "SLASH", "BEGIN_K", 
                      "END_K", "OWN_K", "PROCEDURE_K", "IF_K", "THEN_K", 
                      "ELSE_K", "FOR_K", "STEP_K", "UNTIL_K", "DO_K", "WHILE_K", 
                      "INTEGER_K", "REAL_K", "BOOLEAN_K", "TRUE_K", "FALSE_K", 
                      "OR_K", "AND_K", "NOT_K", "IDENTIFIER", "INTEGER", 
                      "REAL", "STRING", "NEWLINE", "WS", "COMMENT" ]

    RULE_program = 0
    RULE_block = 1
    RULE_declaration_list = 2
    RULE_declaration = 3
    RULE_type_declaration = 4
    RULE_own_declaration = 5
    RULE_procedure_declaration = 6
    RULE_formal_parameter_list = 7
    RULE_statement_list = 8
    RULE_statement = 9
    RULE_assignment_statement = 10
    RULE_procedure_call = 11
    RULE_if_statement = 12
    RULE_for_statement = 13
    RULE_while_statement = 14
    RULE_expression = 15
    RULE_primary = 16
    RULE_literal = 17
    RULE_type_hint = 18
    RULE_identifier = 19
    RULE_integer_literal = 20
    RULE_real_literal = 21
    RULE_string_literal = 22
    RULE_logical_literal = 23

    ruleNames =  [ "program", "block", "declaration_list", "declaration", 
                   "type_declaration", "own_declaration", "procedure_declaration", 
                   "formal_parameter_list", "statement_list", "statement", 
                   "assignment_statement", "procedure_call", "if_statement", 
                   "for_statement", "while_statement", "expression", "primary", 
                   "literal", "type_hint", "identifier", "integer_literal", 
                   "real_literal", "string_literal", "logical_literal" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    EQ=6
    NE=7
    LT=8
    LE=9
    GT=10
    GE=11
    PLUS=12
    MINUS=13
    STAR=14
    SLASH=15
    BEGIN_K=16
    END_K=17
    OWN_K=18
    PROCEDURE_K=19
    IF_K=20
    THEN_K=21
    ELSE_K=22
    FOR_K=23
    STEP_K=24
    UNTIL_K=25
    DO_K=26
    WHILE_K=27
    INTEGER_K=28
    REAL_K=29
    BOOLEAN_K=30
    TRUE_K=31
    FALSE_K=32
    OR_K=33
    AND_K=34
    NOT_K=35
    IDENTIFIER=36
    INTEGER=37
    REAL=38
    STRING=39
    NEWLINE=40
    WS=41
    COMMENT=42

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

        def block(self):
            return self.getTypedRuleContext(AlgolParser.BlockContext,0)


        def EOF(self):
            return self.getToken(AlgolParser.EOF, 0)

        def getRuleIndex(self):
            return AlgolParser.RULE_program

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

        localctx = AlgolParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.block()
            self.state = 49
            self.match(AlgolParser.EOF)
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

        def BEGIN_K(self):
            return self.getToken(AlgolParser.BEGIN_K, 0)

        def END_K(self):
            return self.getToken(AlgolParser.END_K, 0)

        def declaration_list(self):
            return self.getTypedRuleContext(AlgolParser.Declaration_listContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(AlgolParser.Statement_listContext,0)


        def getRuleIndex(self):
            return AlgolParser.RULE_block

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

        localctx = AlgolParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(AlgolParser.BEGIN_K)
            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1879834624) != 0):
                self.state = 52
                self.declaration_list()


            self.state = 56
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 55
                self.statement_list()


            self.state = 58
            self.match(AlgolParser.END_K)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declaration_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AlgolParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(AlgolParser.DeclarationContext,i)


        def getRuleIndex(self):
            return AlgolParser.RULE_declaration_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration_list" ):
                listener.enterDeclaration_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration_list" ):
                listener.exitDeclaration_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration_list" ):
                return visitor.visitDeclaration_list(self)
            else:
                return visitor.visitChildren(self)




    def declaration_list(self):

        localctx = AlgolParser.Declaration_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaration_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 60
                self.declaration()
                self.state = 61
                self.match(AlgolParser.T__0)
                self.state = 65 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1879834624) != 0)):
                    break

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

        def type_declaration(self):
            return self.getTypedRuleContext(AlgolParser.Type_declarationContext,0)


        def procedure_declaration(self):
            return self.getTypedRuleContext(AlgolParser.Procedure_declarationContext,0)


        def own_declaration(self):
            return self.getTypedRuleContext(AlgolParser.Own_declarationContext,0)


        def getRuleIndex(self):
            return AlgolParser.RULE_declaration

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

        localctx = AlgolParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_declaration)
        try:
            self.state = 70
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28, 29, 30]:
                self.enterOuterAlt(localctx, 1)
                self.state = 67
                self.type_declaration()
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 2)
                self.state = 68
                self.procedure_declaration()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 3)
                self.state = 69
                self.own_declaration()
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


    class Type_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_hint(self):
            return self.getTypedRuleContext(AlgolParser.Type_hintContext,0)


        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AlgolParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(AlgolParser.IdentifierContext,i)


        def getRuleIndex(self):
            return AlgolParser.RULE_type_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_declaration" ):
                listener.enterType_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_declaration" ):
                listener.exitType_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_declaration" ):
                return visitor.visitType_declaration(self)
            else:
                return visitor.visitChildren(self)




    def type_declaration(self):

        localctx = AlgolParser.Type_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_type_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.type_hint()
            self.state = 73
            self.identifier()
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 74
                self.match(AlgolParser.T__1)
                self.state = 75
                self.identifier()
                self.state = 80
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Own_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OWN_K(self):
            return self.getToken(AlgolParser.OWN_K, 0)

        def type_declaration(self):
            return self.getTypedRuleContext(AlgolParser.Type_declarationContext,0)


        def getRuleIndex(self):
            return AlgolParser.RULE_own_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOwn_declaration" ):
                listener.enterOwn_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOwn_declaration" ):
                listener.exitOwn_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOwn_declaration" ):
                return visitor.visitOwn_declaration(self)
            else:
                return visitor.visitChildren(self)




    def own_declaration(self):

        localctx = AlgolParser.Own_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_own_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(AlgolParser.OWN_K)
            self.state = 82
            self.type_declaration()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Procedure_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROCEDURE_K(self):
            return self.getToken(AlgolParser.PROCEDURE_K, 0)

        def identifier(self):
            return self.getTypedRuleContext(AlgolParser.IdentifierContext,0)


        def statement(self):
            return self.getTypedRuleContext(AlgolParser.StatementContext,0)


        def formal_parameter_list(self):
            return self.getTypedRuleContext(AlgolParser.Formal_parameter_listContext,0)


        def getRuleIndex(self):
            return AlgolParser.RULE_procedure_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProcedure_declaration" ):
                listener.enterProcedure_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProcedure_declaration" ):
                listener.exitProcedure_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProcedure_declaration" ):
                return visitor.visitProcedure_declaration(self)
            else:
                return visitor.visitChildren(self)




    def procedure_declaration(self):

        localctx = AlgolParser.Procedure_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_procedure_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(AlgolParser.PROCEDURE_K)
            self.state = 85
            self.identifier()
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 86
                self.formal_parameter_list()


            self.state = 89
            self.match(AlgolParser.T__0)
            self.state = 90
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Formal_parameter_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AlgolParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(AlgolParser.IdentifierContext,i)


        def getRuleIndex(self):
            return AlgolParser.RULE_formal_parameter_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormal_parameter_list" ):
                listener.enterFormal_parameter_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormal_parameter_list" ):
                listener.exitFormal_parameter_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFormal_parameter_list" ):
                return visitor.visitFormal_parameter_list(self)
            else:
                return visitor.visitChildren(self)




    def formal_parameter_list(self):

        localctx = AlgolParser.Formal_parameter_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_formal_parameter_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(AlgolParser.T__2)
            self.state = 93
            self.identifier()
            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 94
                self.match(AlgolParser.T__1)
                self.state = 95
                self.identifier()
                self.state = 100
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 101
            self.match(AlgolParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Statement_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AlgolParser.StatementContext)
            else:
                return self.getTypedRuleContext(AlgolParser.StatementContext,i)


        def getRuleIndex(self):
            return AlgolParser.RULE_statement_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement_list" ):
                listener.enterStatement_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement_list" ):
                listener.exitStatement_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement_list" ):
                return visitor.visitStatement_list(self)
            else:
                return visitor.visitChildren(self)




    def statement_list(self):

        localctx = AlgolParser.Statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_statement_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 103
                self.statement()
                self.state = 108
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==1:
                    self.state = 104
                    self.match(AlgolParser.T__0)
                    self.state = 105
                    self.statement()
                    self.state = 110
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



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

        def assignment_statement(self):
            return self.getTypedRuleContext(AlgolParser.Assignment_statementContext,0)


        def procedure_call(self):
            return self.getTypedRuleContext(AlgolParser.Procedure_callContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(AlgolParser.If_statementContext,0)


        def for_statement(self):
            return self.getTypedRuleContext(AlgolParser.For_statementContext,0)


        def while_statement(self):
            return self.getTypedRuleContext(AlgolParser.While_statementContext,0)


        def block(self):
            return self.getTypedRuleContext(AlgolParser.BlockContext,0)


        def getRuleIndex(self):
            return AlgolParser.RULE_statement

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

        localctx = AlgolParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_statement)
        try:
            self.state = 120
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 113
                self.assignment_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 114
                self.procedure_call()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 115
                self.if_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 116
                self.for_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 117
                self.while_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 118
                self.block()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(AlgolParser.IdentifierContext,0)


        def expression(self):
            return self.getTypedRuleContext(AlgolParser.ExpressionContext,0)


        def getRuleIndex(self):
            return AlgolParser.RULE_assignment_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment_statement" ):
                listener.enterAssignment_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment_statement" ):
                listener.exitAssignment_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_statement" ):
                return visitor.visitAssignment_statement(self)
            else:
                return visitor.visitChildren(self)




    def assignment_statement(self):

        localctx = AlgolParser.Assignment_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_assignment_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.identifier()
            self.state = 123
            self.match(AlgolParser.T__4)
            self.state = 124
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Procedure_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(AlgolParser.IdentifierContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AlgolParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(AlgolParser.ExpressionContext,i)


        def getRuleIndex(self):
            return AlgolParser.RULE_procedure_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProcedure_call" ):
                listener.enterProcedure_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProcedure_call" ):
                listener.exitProcedure_call(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProcedure_call" ):
                return visitor.visitProcedure_call(self)
            else:
                return visitor.visitChildren(self)




    def procedure_call(self):

        localctx = AlgolParser.Procedure_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_procedure_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.identifier()
            self.state = 138
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 127
                self.match(AlgolParser.T__2)
                self.state = 128
                self.expression(0)
                self.state = 133
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 129
                    self.match(AlgolParser.T__1)
                    self.state = 130
                    self.expression(0)
                    self.state = 135
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 136
                self.match(AlgolParser.T__3)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF_K(self):
            return self.getToken(AlgolParser.IF_K, 0)

        def expression(self):
            return self.getTypedRuleContext(AlgolParser.ExpressionContext,0)


        def THEN_K(self):
            return self.getToken(AlgolParser.THEN_K, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AlgolParser.StatementContext)
            else:
                return self.getTypedRuleContext(AlgolParser.StatementContext,i)


        def ELSE_K(self):
            return self.getToken(AlgolParser.ELSE_K, 0)

        def getRuleIndex(self):
            return AlgolParser.RULE_if_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_statement" ):
                listener.enterIf_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_statement" ):
                listener.exitIf_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = AlgolParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(AlgolParser.IF_K)
            self.state = 141
            self.expression(0)
            self.state = 142
            self.match(AlgolParser.THEN_K)
            self.state = 143
            self.statement()
            self.state = 146
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 144
                self.match(AlgolParser.ELSE_K)
                self.state = 145
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR_K(self):
            return self.getToken(AlgolParser.FOR_K, 0)

        def identifier(self):
            return self.getTypedRuleContext(AlgolParser.IdentifierContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AlgolParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(AlgolParser.ExpressionContext,i)


        def STEP_K(self):
            return self.getToken(AlgolParser.STEP_K, 0)

        def UNTIL_K(self):
            return self.getToken(AlgolParser.UNTIL_K, 0)

        def DO_K(self):
            return self.getToken(AlgolParser.DO_K, 0)

        def statement(self):
            return self.getTypedRuleContext(AlgolParser.StatementContext,0)


        def getRuleIndex(self):
            return AlgolParser.RULE_for_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_statement" ):
                listener.enterFor_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_statement" ):
                listener.exitFor_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_statement" ):
                return visitor.visitFor_statement(self)
            else:
                return visitor.visitChildren(self)




    def for_statement(self):

        localctx = AlgolParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_for_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(AlgolParser.FOR_K)
            self.state = 149
            self.identifier()
            self.state = 150
            self.match(AlgolParser.T__4)
            self.state = 151
            self.expression(0)
            self.state = 152
            self.match(AlgolParser.STEP_K)
            self.state = 153
            self.expression(0)
            self.state = 154
            self.match(AlgolParser.UNTIL_K)
            self.state = 155
            self.expression(0)
            self.state = 156
            self.match(AlgolParser.DO_K)
            self.state = 157
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE_K(self):
            return self.getToken(AlgolParser.WHILE_K, 0)

        def expression(self):
            return self.getTypedRuleContext(AlgolParser.ExpressionContext,0)


        def DO_K(self):
            return self.getToken(AlgolParser.DO_K, 0)

        def statement(self):
            return self.getTypedRuleContext(AlgolParser.StatementContext,0)


        def getRuleIndex(self):
            return AlgolParser.RULE_while_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_statement" ):
                listener.enterWhile_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_statement" ):
                listener.exitWhile_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_statement" ):
                return visitor.visitWhile_statement(self)
            else:
                return visitor.visitChildren(self)




    def while_statement(self):

        localctx = AlgolParser.While_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_while_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(AlgolParser.WHILE_K)
            self.state = 160
            self.expression(0)
            self.state = 161
            self.match(AlgolParser.DO_K)
            self.state = 162
            self.statement()
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

        def NOT_K(self):
            return self.getToken(AlgolParser.NOT_K, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AlgolParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(AlgolParser.ExpressionContext,i)


        def MINUS(self):
            return self.getToken(AlgolParser.MINUS, 0)

        def primary(self):
            return self.getTypedRuleContext(AlgolParser.PrimaryContext,0)


        def OR_K(self):
            return self.getToken(AlgolParser.OR_K, 0)

        def AND_K(self):
            return self.getToken(AlgolParser.AND_K, 0)

        def EQ(self):
            return self.getToken(AlgolParser.EQ, 0)

        def NE(self):
            return self.getToken(AlgolParser.NE, 0)

        def LT(self):
            return self.getToken(AlgolParser.LT, 0)

        def LE(self):
            return self.getToken(AlgolParser.LE, 0)

        def GT(self):
            return self.getToken(AlgolParser.GT, 0)

        def GE(self):
            return self.getToken(AlgolParser.GE, 0)

        def PLUS(self):
            return self.getToken(AlgolParser.PLUS, 0)

        def STAR(self):
            return self.getToken(AlgolParser.STAR, 0)

        def SLASH(self):
            return self.getToken(AlgolParser.SLASH, 0)

        def getRuleIndex(self):
            return AlgolParser.RULE_expression

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
        localctx = AlgolParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [35]:
                self.state = 165
                self.match(AlgolParser.NOT_K)
                self.state = 166
                self.expression(7)
                pass
            elif token in [13]:
                self.state = 167
                self.match(AlgolParser.MINUS)
                self.state = 168
                self.expression(3)
                pass
            elif token in [3]:
                self.state = 169
                self.match(AlgolParser.T__2)
                self.state = 170
                self.expression(0)
                self.state = 171
                self.match(AlgolParser.T__3)
                pass
            elif token in [31, 32, 36, 37, 38, 39]:
                self.state = 173
                self.primary()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 190
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 188
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                    if la_ == 1:
                        localctx = AlgolParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 176
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 177
                        _la = self._input.LA(1)
                        if not(_la==33 or _la==34):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 178
                        self.expression(9)
                        pass

                    elif la_ == 2:
                        localctx = AlgolParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 179
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 180
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4032) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 181
                        self.expression(7)
                        pass

                    elif la_ == 3:
                        localctx = AlgolParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 182
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 183
                        _la = self._input.LA(1)
                        if not(_la==12 or _la==13):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 184
                        self.expression(6)
                        pass

                    elif la_ == 4:
                        localctx = AlgolParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 185
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 186
                        _la = self._input.LA(1)
                        if not(_la==14 or _la==15):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 187
                        self.expression(5)
                        pass

             
                self.state = 192
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

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
            return self.getTypedRuleContext(AlgolParser.IdentifierContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AlgolParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(AlgolParser.ExpressionContext,i)


        def literal(self):
            return self.getTypedRuleContext(AlgolParser.LiteralContext,0)


        def getRuleIndex(self):
            return AlgolParser.RULE_primary

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

        localctx = AlgolParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_primary)
        self._la = 0 # Token type
        try:
            self.state = 208
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [36]:
                self.enterOuterAlt(localctx, 1)
                self.state = 193
                self.identifier()
                self.state = 205
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                if la_ == 1:
                    self.state = 194
                    self.match(AlgolParser.T__2)
                    self.state = 195
                    self.expression(0)
                    self.state = 200
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==2:
                        self.state = 196
                        self.match(AlgolParser.T__1)
                        self.state = 197
                        self.expression(0)
                        self.state = 202
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 203
                    self.match(AlgolParser.T__3)


                pass
            elif token in [31, 32, 37, 38, 39]:
                self.enterOuterAlt(localctx, 2)
                self.state = 207
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
            return self.getTypedRuleContext(AlgolParser.Integer_literalContext,0)


        def real_literal(self):
            return self.getTypedRuleContext(AlgolParser.Real_literalContext,0)


        def string_literal(self):
            return self.getTypedRuleContext(AlgolParser.String_literalContext,0)


        def logical_literal(self):
            return self.getTypedRuleContext(AlgolParser.Logical_literalContext,0)


        def getRuleIndex(self):
            return AlgolParser.RULE_literal

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

        localctx = AlgolParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_literal)
        try:
            self.state = 214
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [37]:
                self.enterOuterAlt(localctx, 1)
                self.state = 210
                self.integer_literal()
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 2)
                self.state = 211
                self.real_literal()
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 3)
                self.state = 212
                self.string_literal()
                pass
            elif token in [31, 32]:
                self.enterOuterAlt(localctx, 4)
                self.state = 213
                self.logical_literal()
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


    class Type_hintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER_K(self):
            return self.getToken(AlgolParser.INTEGER_K, 0)

        def REAL_K(self):
            return self.getToken(AlgolParser.REAL_K, 0)

        def BOOLEAN_K(self):
            return self.getToken(AlgolParser.BOOLEAN_K, 0)

        def getRuleIndex(self):
            return AlgolParser.RULE_type_hint

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_hint" ):
                listener.enterType_hint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_hint" ):
                listener.exitType_hint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_hint" ):
                return visitor.visitType_hint(self)
            else:
                return visitor.visitChildren(self)




    def type_hint(self):

        localctx = AlgolParser.Type_hintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_type_hint)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1879048192) != 0)):
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


    class IdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(AlgolParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return AlgolParser.RULE_identifier

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

        localctx = AlgolParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self.match(AlgolParser.IDENTIFIER)
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
            return self.getToken(AlgolParser.INTEGER, 0)

        def getRuleIndex(self):
            return AlgolParser.RULE_integer_literal

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

        localctx = AlgolParser.Integer_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_integer_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.match(AlgolParser.INTEGER)
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
            return self.getToken(AlgolParser.REAL, 0)

        def getRuleIndex(self):
            return AlgolParser.RULE_real_literal

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

        localctx = AlgolParser.Real_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_real_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.match(AlgolParser.REAL)
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
            return self.getToken(AlgolParser.STRING, 0)

        def getRuleIndex(self):
            return AlgolParser.RULE_string_literal

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

        localctx = AlgolParser.String_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_string_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.match(AlgolParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Logical_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE_K(self):
            return self.getToken(AlgolParser.TRUE_K, 0)

        def FALSE_K(self):
            return self.getToken(AlgolParser.FALSE_K, 0)

        def getRuleIndex(self):
            return AlgolParser.RULE_logical_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogical_literal" ):
                listener.enterLogical_literal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogical_literal" ):
                listener.exitLogical_literal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogical_literal" ):
                return visitor.visitLogical_literal(self)
            else:
                return visitor.visitChildren(self)




    def logical_literal(self):

        localctx = AlgolParser.Logical_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_logical_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            _la = self._input.LA(1)
            if not(_la==31 or _la==32):
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[15] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         




