# Generated from rosetta/babel/pli/grammar/PLI.g4 by ANTLR 4.13.2
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
        4,1,64,346,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        1,0,5,0,56,8,0,10,0,12,0,59,9,0,1,0,5,0,62,8,0,10,0,12,0,65,9,0,
        1,0,1,0,1,1,1,1,1,1,1,1,1,2,1,2,1,2,3,2,76,8,2,1,2,1,2,1,2,1,2,3,
        2,82,8,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,90,8,2,1,2,1,2,1,2,1,2,1,2,
        1,2,3,2,98,8,2,1,2,3,2,101,8,2,1,3,1,3,1,4,1,4,1,4,1,4,3,4,109,8,
        4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,118,8,5,1,6,1,6,1,6,3,6,123,8,
        6,1,6,3,6,126,8,6,1,6,1,6,1,6,1,6,1,6,5,6,133,8,6,10,6,12,6,136,
        9,6,1,6,3,6,139,8,6,1,6,1,6,1,6,1,6,1,6,3,6,146,8,6,1,6,1,6,5,6,
        150,8,6,10,6,12,6,153,9,6,1,6,1,6,3,6,157,8,6,1,6,1,6,1,7,1,7,1,
        7,3,7,164,8,7,1,7,3,7,167,8,7,1,7,1,7,1,7,1,7,1,7,3,7,174,8,7,1,
        8,1,8,1,8,5,8,179,8,8,10,8,12,8,182,9,8,1,9,1,9,1,9,1,9,5,9,188,
        8,9,10,9,12,9,191,9,9,1,10,1,10,5,10,195,8,10,10,10,12,10,198,9,
        10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,5,11,210,8,
        11,10,11,12,11,213,9,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,
        222,8,11,1,12,1,12,1,13,1,13,1,13,1,13,1,14,1,14,1,14,3,14,233,8,
        14,1,14,1,14,1,14,1,14,3,14,239,8,14,1,15,1,15,1,15,1,16,1,16,3,
        16,246,8,16,1,16,1,16,5,16,250,8,16,10,16,12,16,253,9,16,1,16,1,
        16,3,16,257,8,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,17,1,17,3,
        17,268,8,17,3,17,270,8,17,1,18,1,18,1,18,1,18,1,18,1,18,3,18,278,
        8,18,1,19,1,19,1,19,1,19,3,19,284,8,19,1,19,3,19,287,8,19,1,20,1,
        20,1,20,5,20,292,8,20,10,20,12,20,295,9,20,1,21,1,21,1,21,1,21,1,
        22,1,22,1,22,1,22,1,22,3,22,306,8,22,1,23,1,23,3,23,310,8,23,1,23,
        1,23,3,23,314,8,23,1,23,3,23,317,8,23,1,24,1,24,1,24,1,24,5,24,323,
        8,24,10,24,12,24,326,9,24,1,25,1,25,1,25,3,25,331,8,25,1,25,3,25,
        334,8,25,1,25,1,25,1,25,1,25,1,25,1,25,3,25,342,8,25,1,26,1,26,1,
        26,0,0,27,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,
        40,42,44,46,48,50,52,0,6,1,0,19,20,1,0,24,25,1,0,48,57,1,0,37,38,
        1,0,39,42,2,0,1,1,7,18,377,0,57,1,0,0,0,2,68,1,0,0,0,4,100,1,0,0,
        0,6,102,1,0,0,0,8,108,1,0,0,0,10,117,1,0,0,0,12,119,1,0,0,0,14,160,
        1,0,0,0,16,175,1,0,0,0,18,183,1,0,0,0,20,192,1,0,0,0,22,221,1,0,
        0,0,24,223,1,0,0,0,26,225,1,0,0,0,28,229,1,0,0,0,30,240,1,0,0,0,
        32,243,1,0,0,0,34,260,1,0,0,0,36,271,1,0,0,0,38,279,1,0,0,0,40,288,
        1,0,0,0,42,296,1,0,0,0,44,300,1,0,0,0,46,307,1,0,0,0,48,318,1,0,
        0,0,50,341,1,0,0,0,52,343,1,0,0,0,54,56,3,2,1,0,55,54,1,0,0,0,56,
        59,1,0,0,0,57,55,1,0,0,0,57,58,1,0,0,0,58,63,1,0,0,0,59,57,1,0,0,
        0,60,62,3,4,2,0,61,60,1,0,0,0,62,65,1,0,0,0,63,61,1,0,0,0,63,64,
        1,0,0,0,64,66,1,0,0,0,65,63,1,0,0,0,66,67,5,0,0,1,67,1,1,0,0,0,68,
        69,5,1,0,0,69,70,5,60,0,0,70,71,5,2,0,0,71,3,1,0,0,0,72,73,3,6,3,
        0,73,74,5,3,0,0,74,76,1,0,0,0,75,72,1,0,0,0,75,76,1,0,0,0,76,77,
        1,0,0,0,77,101,3,8,4,0,78,79,3,6,3,0,79,80,5,3,0,0,80,82,1,0,0,0,
        81,78,1,0,0,0,81,82,1,0,0,0,82,83,1,0,0,0,83,84,3,10,5,0,84,85,5,
        2,0,0,85,101,1,0,0,0,86,87,3,6,3,0,87,88,5,3,0,0,88,90,1,0,0,0,89,
        86,1,0,0,0,89,90,1,0,0,0,90,91,1,0,0,0,91,92,3,14,7,0,92,93,5,2,
        0,0,93,101,1,0,0,0,94,95,3,6,3,0,95,96,5,3,0,0,96,98,1,0,0,0,97,
        94,1,0,0,0,97,98,1,0,0,0,98,99,1,0,0,0,99,101,5,2,0,0,100,75,1,0,
        0,0,100,81,1,0,0,0,100,89,1,0,0,0,100,97,1,0,0,0,101,5,1,0,0,0,102,
        103,5,60,0,0,103,7,1,0,0,0,104,109,3,12,6,0,105,109,3,32,16,0,106,
        109,3,36,18,0,107,109,3,26,13,0,108,104,1,0,0,0,108,105,1,0,0,0,
        108,106,1,0,0,0,108,107,1,0,0,0,109,9,1,0,0,0,110,118,3,18,9,0,111,
        118,3,28,14,0,112,118,3,30,15,0,113,118,3,38,19,0,114,118,3,42,21,
        0,115,118,3,44,22,0,116,118,3,46,23,0,117,110,1,0,0,0,117,111,1,
        0,0,0,117,112,1,0,0,0,117,113,1,0,0,0,117,114,1,0,0,0,117,115,1,
        0,0,0,117,116,1,0,0,0,118,11,1,0,0,0,119,125,7,0,0,0,120,122,5,4,
        0,0,121,123,3,16,8,0,122,121,1,0,0,0,122,123,1,0,0,0,123,124,1,0,
        0,0,124,126,5,5,0,0,125,120,1,0,0,0,125,126,1,0,0,0,126,138,1,0,
        0,0,127,128,5,43,0,0,128,129,5,4,0,0,129,134,5,60,0,0,130,131,5,
        6,0,0,131,133,5,60,0,0,132,130,1,0,0,0,133,136,1,0,0,0,134,132,1,
        0,0,0,134,135,1,0,0,0,135,137,1,0,0,0,136,134,1,0,0,0,137,139,5,
        5,0,0,138,127,1,0,0,0,138,139,1,0,0,0,139,145,1,0,0,0,140,141,5,
        22,0,0,141,142,5,4,0,0,142,143,3,24,12,0,143,144,5,5,0,0,144,146,
        1,0,0,0,145,140,1,0,0,0,145,146,1,0,0,0,146,147,1,0,0,0,147,151,
        5,2,0,0,148,150,3,4,2,0,149,148,1,0,0,0,150,153,1,0,0,0,151,149,
        1,0,0,0,151,152,1,0,0,0,152,154,1,0,0,0,153,151,1,0,0,0,154,156,
        5,23,0,0,155,157,5,60,0,0,156,155,1,0,0,0,156,157,1,0,0,0,157,158,
        1,0,0,0,158,159,5,2,0,0,159,13,1,0,0,0,160,166,5,21,0,0,161,163,
        5,4,0,0,162,164,3,16,8,0,163,162,1,0,0,0,163,164,1,0,0,0,164,165,
        1,0,0,0,165,167,5,5,0,0,166,161,1,0,0,0,166,167,1,0,0,0,167,173,
        1,0,0,0,168,169,5,22,0,0,169,170,5,4,0,0,170,171,3,24,12,0,171,172,
        5,5,0,0,172,174,1,0,0,0,173,168,1,0,0,0,173,174,1,0,0,0,174,15,1,
        0,0,0,175,180,5,60,0,0,176,177,5,6,0,0,177,179,5,60,0,0,178,176,
        1,0,0,0,179,182,1,0,0,0,180,178,1,0,0,0,180,181,1,0,0,0,181,17,1,
        0,0,0,182,180,1,0,0,0,183,184,7,1,0,0,184,189,3,20,10,0,185,186,
        5,6,0,0,186,188,3,20,10,0,187,185,1,0,0,0,188,191,1,0,0,0,189,187,
        1,0,0,0,189,190,1,0,0,0,190,19,1,0,0,0,191,189,1,0,0,0,192,196,5,
        60,0,0,193,195,3,22,11,0,194,193,1,0,0,0,195,198,1,0,0,0,196,194,
        1,0,0,0,196,197,1,0,0,0,197,21,1,0,0,0,198,196,1,0,0,0,199,222,3,
        24,12,0,200,201,5,44,0,0,201,222,5,61,0,0,202,222,5,45,0,0,203,222,
        5,46,0,0,204,222,5,47,0,0,205,206,5,4,0,0,206,211,3,48,24,0,207,
        208,5,6,0,0,208,210,3,48,24,0,209,207,1,0,0,0,210,213,1,0,0,0,211,
        209,1,0,0,0,211,212,1,0,0,0,212,214,1,0,0,0,213,211,1,0,0,0,214,
        215,5,5,0,0,215,222,1,0,0,0,216,217,5,58,0,0,217,218,5,4,0,0,218,
        219,3,48,24,0,219,220,5,5,0,0,220,222,1,0,0,0,221,199,1,0,0,0,221,
        200,1,0,0,0,221,202,1,0,0,0,221,203,1,0,0,0,221,204,1,0,0,0,221,
        205,1,0,0,0,221,216,1,0,0,0,222,23,1,0,0,0,223,224,7,2,0,0,224,25,
        1,0,0,0,225,226,5,26,0,0,226,227,5,60,0,0,227,228,3,4,2,0,228,27,
        1,0,0,0,229,232,5,27,0,0,230,233,5,60,0,0,231,233,3,24,12,0,232,
        230,1,0,0,0,232,231,1,0,0,0,233,238,1,0,0,0,234,235,5,59,0,0,235,
        236,5,4,0,0,236,237,5,60,0,0,237,239,5,5,0,0,238,234,1,0,0,0,238,
        239,1,0,0,0,239,29,1,0,0,0,240,241,5,28,0,0,241,242,5,60,0,0,242,
        31,1,0,0,0,243,245,5,29,0,0,244,246,3,34,17,0,245,244,1,0,0,0,245,
        246,1,0,0,0,246,247,1,0,0,0,247,251,5,2,0,0,248,250,3,4,2,0,249,
        248,1,0,0,0,250,253,1,0,0,0,251,249,1,0,0,0,251,252,1,0,0,0,252,
        254,1,0,0,0,253,251,1,0,0,0,254,256,5,23,0,0,255,257,5,60,0,0,256,
        255,1,0,0,0,256,257,1,0,0,0,257,258,1,0,0,0,258,259,5,2,0,0,259,
        33,1,0,0,0,260,261,5,60,0,0,261,262,5,7,0,0,262,269,3,48,24,0,263,
        264,5,33,0,0,264,267,3,48,24,0,265,266,5,34,0,0,266,268,3,48,24,
        0,267,265,1,0,0,0,267,268,1,0,0,0,268,270,1,0,0,0,269,263,1,0,0,
        0,269,270,1,0,0,0,270,35,1,0,0,0,271,272,5,30,0,0,272,273,3,48,24,
        0,273,274,5,31,0,0,274,277,3,4,2,0,275,276,5,32,0,0,276,278,3,4,
        2,0,277,275,1,0,0,0,277,278,1,0,0,0,278,37,1,0,0,0,279,280,5,35,
        0,0,280,286,5,60,0,0,281,283,5,4,0,0,282,284,3,40,20,0,283,282,1,
        0,0,0,283,284,1,0,0,0,284,285,1,0,0,0,285,287,5,5,0,0,286,281,1,
        0,0,0,286,287,1,0,0,0,287,39,1,0,0,0,288,293,3,48,24,0,289,290,5,
        6,0,0,290,292,3,48,24,0,291,289,1,0,0,0,292,295,1,0,0,0,293,291,
        1,0,0,0,293,294,1,0,0,0,294,41,1,0,0,0,295,293,1,0,0,0,296,297,3,
        50,25,0,297,298,5,7,0,0,298,299,3,48,24,0,299,43,1,0,0,0,300,305,
        5,36,0,0,301,302,5,4,0,0,302,303,3,48,24,0,303,304,5,5,0,0,304,306,
        1,0,0,0,305,301,1,0,0,0,305,306,1,0,0,0,306,45,1,0,0,0,307,309,7,
        3,0,0,308,310,7,4,0,0,309,308,1,0,0,0,309,310,1,0,0,0,310,316,1,
        0,0,0,311,313,5,4,0,0,312,314,3,40,20,0,313,312,1,0,0,0,313,314,
        1,0,0,0,314,315,1,0,0,0,315,317,5,5,0,0,316,311,1,0,0,0,316,317,
        1,0,0,0,317,47,1,0,0,0,318,324,3,50,25,0,319,320,3,52,26,0,320,321,
        3,50,25,0,321,323,1,0,0,0,322,319,1,0,0,0,323,326,1,0,0,0,324,322,
        1,0,0,0,324,325,1,0,0,0,325,49,1,0,0,0,326,324,1,0,0,0,327,333,5,
        60,0,0,328,330,5,4,0,0,329,331,3,40,20,0,330,329,1,0,0,0,330,331,
        1,0,0,0,331,332,1,0,0,0,332,334,5,5,0,0,333,328,1,0,0,0,333,334,
        1,0,0,0,334,342,1,0,0,0,335,342,5,61,0,0,336,342,5,62,0,0,337,338,
        5,4,0,0,338,339,3,48,24,0,339,340,5,5,0,0,340,342,1,0,0,0,341,327,
        1,0,0,0,341,335,1,0,0,0,341,336,1,0,0,0,341,337,1,0,0,0,342,51,1,
        0,0,0,343,344,7,5,0,0,344,53,1,0,0,0,43,57,63,75,81,89,97,100,108,
        117,122,125,134,138,145,151,156,163,166,173,180,189,196,211,221,
        232,238,245,251,256,267,269,277,283,286,293,305,309,313,316,324,
        330,333,341
    ]

class PLIParser ( Parser ):

    grammarFileName = "PLI.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'*'", "';'", "':'", "'('", "')'", "','", 
                     "'='", "'+'", "'-'", "'/'", "'||'", "'=='", "'<'", 
                     "'>'", "'<='", "'>='", "'&'", "'|'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "PROCEDURE_K", 
                      "PROC_K", "ENTRY_K", "RETURNS_K", "END_K", "DECLARE_K", 
                      "DCL_K", "ON_K", "ALLOCATE_K", "FREE_K", "DO_K", "IF_K", 
                      "THEN_K", "ELSE_K", "TO_K", "BY_K", "CALL_K", "RETURN_K", 
                      "PUT_K", "GET_K", "LIST_K", "EDIT_K", "SKIP_K", "DATA_K", 
                      "OPTIONS_K", "PICTURE_K", "TASK_K", "VARYING_K", "ALIGNED_K", 
                      "FIXED_K", "FLOAT_K", "CHARACTER_K", "CHAR_K", "BINARY_K", 
                      "BIN_K", "DECIMAL_K", "DEC_K", "POINTER_K", "BIT_K", 
                      "INIT_K", "SET_K", "ID", "STRING", "NUMBER", "WS", 
                      "COMMENT" ]

    RULE_program = 0
    RULE_directive = 1
    RULE_statement = 2
    RULE_label = 3
    RULE_content_no_semi = 4
    RULE_content_semi = 5
    RULE_procedure_def = 6
    RULE_entry_stmt = 7
    RULE_params = 8
    RULE_declare_stmt = 9
    RULE_declaration = 10
    RULE_attribute = 11
    RULE_type_ = 12
    RULE_on_stmt = 13
    RULE_allocate_stmt = 14
    RULE_free_stmt = 15
    RULE_do_block = 16
    RULE_do_spec = 17
    RULE_if_stmt = 18
    RULE_call_stmt = 19
    RULE_args = 20
    RULE_assignment = 21
    RULE_return_stmt = 22
    RULE_action = 23
    RULE_expression = 24
    RULE_primary = 25
    RULE_operator = 26

    ruleNames =  [ "program", "directive", "statement", "label", "content_no_semi", 
                   "content_semi", "procedure_def", "entry_stmt", "params", 
                   "declare_stmt", "declaration", "attribute", "type_", 
                   "on_stmt", "allocate_stmt", "free_stmt", "do_block", 
                   "do_spec", "if_stmt", "call_stmt", "args", "assignment", 
                   "return_stmt", "action", "expression", "primary", "operator" ]

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
    PROCEDURE_K=19
    PROC_K=20
    ENTRY_K=21
    RETURNS_K=22
    END_K=23
    DECLARE_K=24
    DCL_K=25
    ON_K=26
    ALLOCATE_K=27
    FREE_K=28
    DO_K=29
    IF_K=30
    THEN_K=31
    ELSE_K=32
    TO_K=33
    BY_K=34
    CALL_K=35
    RETURN_K=36
    PUT_K=37
    GET_K=38
    LIST_K=39
    EDIT_K=40
    SKIP_K=41
    DATA_K=42
    OPTIONS_K=43
    PICTURE_K=44
    TASK_K=45
    VARYING_K=46
    ALIGNED_K=47
    FIXED_K=48
    FLOAT_K=49
    CHARACTER_K=50
    CHAR_K=51
    BINARY_K=52
    BIN_K=53
    DECIMAL_K=54
    DEC_K=55
    POINTER_K=56
    BIT_K=57
    INIT_K=58
    SET_K=59
    ID=60
    STRING=61
    NUMBER=62
    WS=63
    COMMENT=64

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
            return self.getToken(PLIParser.EOF, 0)

        def directive(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLIParser.DirectiveContext)
            else:
                return self.getTypedRuleContext(PLIParser.DirectiveContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLIParser.StatementContext)
            else:
                return self.getTypedRuleContext(PLIParser.StatementContext,i)


        def getRuleIndex(self):
            return PLIParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = PLIParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 54
                self.directive()
                self.state = 59
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8070451049778380820) != 0):
                self.state = 60
                self.statement()
                self.state = 65
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 66
            self.match(PLIParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DirectiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PLIParser.ID, 0)

        def getRuleIndex(self):
            return PLIParser.RULE_directive

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDirective" ):
                return visitor.visitDirective(self)
            else:
                return visitor.visitChildren(self)




    def directive(self):

        localctx = PLIParser.DirectiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_directive)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(PLIParser.T__0)
            self.state = 69
            self.match(PLIParser.ID)
            self.state = 70
            self.match(PLIParser.T__1)
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

        def content_no_semi(self):
            return self.getTypedRuleContext(PLIParser.Content_no_semiContext,0)


        def label(self):
            return self.getTypedRuleContext(PLIParser.LabelContext,0)


        def content_semi(self):
            return self.getTypedRuleContext(PLIParser.Content_semiContext,0)


        def entry_stmt(self):
            return self.getTypedRuleContext(PLIParser.Entry_stmtContext,0)


        def getRuleIndex(self):
            return PLIParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = PLIParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 100
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 75
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==60:
                    self.state = 72
                    self.label()
                    self.state = 73
                    self.match(PLIParser.T__2)


                self.state = 77
                self.content_no_semi()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 81
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                if la_ == 1:
                    self.state = 78
                    self.label()
                    self.state = 79
                    self.match(PLIParser.T__2)


                self.state = 83
                self.content_semi()
                self.state = 84
                self.match(PLIParser.T__1)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 89
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==60:
                    self.state = 86
                    self.label()
                    self.state = 87
                    self.match(PLIParser.T__2)


                self.state = 91
                self.entry_stmt()
                self.state = 92
                self.match(PLIParser.T__1)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 97
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==60:
                    self.state = 94
                    self.label()
                    self.state = 95
                    self.match(PLIParser.T__2)


                self.state = 99
                self.match(PLIParser.T__1)
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
            return self.getToken(PLIParser.ID, 0)

        def getRuleIndex(self):
            return PLIParser.RULE_label

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLabel" ):
                return visitor.visitLabel(self)
            else:
                return visitor.visitChildren(self)




    def label(self):

        localctx = PLIParser.LabelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_label)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(PLIParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Content_no_semiContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def procedure_def(self):
            return self.getTypedRuleContext(PLIParser.Procedure_defContext,0)


        def do_block(self):
            return self.getTypedRuleContext(PLIParser.Do_blockContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(PLIParser.If_stmtContext,0)


        def on_stmt(self):
            return self.getTypedRuleContext(PLIParser.On_stmtContext,0)


        def getRuleIndex(self):
            return PLIParser.RULE_content_no_semi

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContent_no_semi" ):
                return visitor.visitContent_no_semi(self)
            else:
                return visitor.visitChildren(self)




    def content_no_semi(self):

        localctx = PLIParser.Content_no_semiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_content_no_semi)
        try:
            self.state = 108
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19, 20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 104
                self.procedure_def()
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 2)
                self.state = 105
                self.do_block()
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 3)
                self.state = 106
                self.if_stmt()
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 4)
                self.state = 107
                self.on_stmt()
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


    class Content_semiContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declare_stmt(self):
            return self.getTypedRuleContext(PLIParser.Declare_stmtContext,0)


        def allocate_stmt(self):
            return self.getTypedRuleContext(PLIParser.Allocate_stmtContext,0)


        def free_stmt(self):
            return self.getTypedRuleContext(PLIParser.Free_stmtContext,0)


        def call_stmt(self):
            return self.getTypedRuleContext(PLIParser.Call_stmtContext,0)


        def assignment(self):
            return self.getTypedRuleContext(PLIParser.AssignmentContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(PLIParser.Return_stmtContext,0)


        def action(self):
            return self.getTypedRuleContext(PLIParser.ActionContext,0)


        def getRuleIndex(self):
            return PLIParser.RULE_content_semi

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContent_semi" ):
                return visitor.visitContent_semi(self)
            else:
                return visitor.visitChildren(self)




    def content_semi(self):

        localctx = PLIParser.Content_semiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_content_semi)
        try:
            self.state = 117
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24, 25]:
                self.enterOuterAlt(localctx, 1)
                self.state = 110
                self.declare_stmt()
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 2)
                self.state = 111
                self.allocate_stmt()
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 3)
                self.state = 112
                self.free_stmt()
                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 4)
                self.state = 113
                self.call_stmt()
                pass
            elif token in [4, 60, 61, 62]:
                self.enterOuterAlt(localctx, 5)
                self.state = 114
                self.assignment()
                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 6)
                self.state = 115
                self.return_stmt()
                pass
            elif token in [37, 38]:
                self.enterOuterAlt(localctx, 7)
                self.state = 116
                self.action()
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


    class Procedure_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def END_K(self):
            return self.getToken(PLIParser.END_K, 0)

        def PROCEDURE_K(self):
            return self.getToken(PLIParser.PROCEDURE_K, 0)

        def PROC_K(self):
            return self.getToken(PLIParser.PROC_K, 0)

        def OPTIONS_K(self):
            return self.getToken(PLIParser.OPTIONS_K, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(PLIParser.ID)
            else:
                return self.getToken(PLIParser.ID, i)

        def RETURNS_K(self):
            return self.getToken(PLIParser.RETURNS_K, 0)

        def type_(self):
            return self.getTypedRuleContext(PLIParser.Type_Context,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLIParser.StatementContext)
            else:
                return self.getTypedRuleContext(PLIParser.StatementContext,i)


        def params(self):
            return self.getTypedRuleContext(PLIParser.ParamsContext,0)


        def getRuleIndex(self):
            return PLIParser.RULE_procedure_def

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProcedure_def" ):
                return visitor.visitProcedure_def(self)
            else:
                return visitor.visitChildren(self)




    def procedure_def(self):

        localctx = PLIParser.Procedure_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_procedure_def)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            _la = self._input.LA(1)
            if not(_la==19 or _la==20):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 120
                self.match(PLIParser.T__3)
                self.state = 122
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==60:
                    self.state = 121
                    self.params()


                self.state = 124
                self.match(PLIParser.T__4)


            self.state = 138
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==43:
                self.state = 127
                self.match(PLIParser.OPTIONS_K)
                self.state = 128
                self.match(PLIParser.T__3)
                self.state = 129
                self.match(PLIParser.ID)
                self.state = 134
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==6:
                    self.state = 130
                    self.match(PLIParser.T__5)
                    self.state = 131
                    self.match(PLIParser.ID)
                    self.state = 136
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 137
                self.match(PLIParser.T__4)


            self.state = 145
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==22:
                self.state = 140
                self.match(PLIParser.RETURNS_K)
                self.state = 141
                self.match(PLIParser.T__3)
                self.state = 142
                self.type_()
                self.state = 143
                self.match(PLIParser.T__4)


            self.state = 147
            self.match(PLIParser.T__1)
            self.state = 151
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8070451049778380820) != 0):
                self.state = 148
                self.statement()
                self.state = 153
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 154
            self.match(PLIParser.END_K)
            self.state = 156
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==60:
                self.state = 155
                self.match(PLIParser.ID)


            self.state = 158
            self.match(PLIParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Entry_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ENTRY_K(self):
            return self.getToken(PLIParser.ENTRY_K, 0)

        def RETURNS_K(self):
            return self.getToken(PLIParser.RETURNS_K, 0)

        def type_(self):
            return self.getTypedRuleContext(PLIParser.Type_Context,0)


        def params(self):
            return self.getTypedRuleContext(PLIParser.ParamsContext,0)


        def getRuleIndex(self):
            return PLIParser.RULE_entry_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEntry_stmt" ):
                return visitor.visitEntry_stmt(self)
            else:
                return visitor.visitChildren(self)




    def entry_stmt(self):

        localctx = PLIParser.Entry_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_entry_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.match(PLIParser.ENTRY_K)
            self.state = 166
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 161
                self.match(PLIParser.T__3)
                self.state = 163
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==60:
                    self.state = 162
                    self.params()


                self.state = 165
                self.match(PLIParser.T__4)


            self.state = 173
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==22:
                self.state = 168
                self.match(PLIParser.RETURNS_K)
                self.state = 169
                self.match(PLIParser.T__3)
                self.state = 170
                self.type_()
                self.state = 171
                self.match(PLIParser.T__4)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(PLIParser.ID)
            else:
                return self.getToken(PLIParser.ID, i)

        def getRuleIndex(self):
            return PLIParser.RULE_params

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams" ):
                return visitor.visitParams(self)
            else:
                return visitor.visitChildren(self)




    def params(self):

        localctx = PLIParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.match(PLIParser.ID)
            self.state = 180
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 176
                self.match(PLIParser.T__5)
                self.state = 177
                self.match(PLIParser.ID)
                self.state = 182
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declare_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLIParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(PLIParser.DeclarationContext,i)


        def DECLARE_K(self):
            return self.getToken(PLIParser.DECLARE_K, 0)

        def DCL_K(self):
            return self.getToken(PLIParser.DCL_K, 0)

        def getRuleIndex(self):
            return PLIParser.RULE_declare_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclare_stmt" ):
                return visitor.visitDeclare_stmt(self)
            else:
                return visitor.visitChildren(self)




    def declare_stmt(self):

        localctx = PLIParser.Declare_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_declare_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            _la = self._input.LA(1)
            if not(_la==24 or _la==25):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 184
            self.declaration()
            self.state = 189
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 185
                self.match(PLIParser.T__5)
                self.state = 186
                self.declaration()
                self.state = 191
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def ID(self):
            return self.getToken(PLIParser.ID, 0)

        def attribute(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLIParser.AttributeContext)
            else:
                return self.getTypedRuleContext(PLIParser.AttributeContext,i)


        def getRuleIndex(self):
            return PLIParser.RULE_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = PLIParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.match(PLIParser.ID)
            self.state = 196
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 576443160117379088) != 0):
                self.state = 193
                self.attribute()
                self.state = 198
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(PLIParser.Type_Context,0)


        def PICTURE_K(self):
            return self.getToken(PLIParser.PICTURE_K, 0)

        def STRING(self):
            return self.getToken(PLIParser.STRING, 0)

        def TASK_K(self):
            return self.getToken(PLIParser.TASK_K, 0)

        def VARYING_K(self):
            return self.getToken(PLIParser.VARYING_K, 0)

        def ALIGNED_K(self):
            return self.getToken(PLIParser.ALIGNED_K, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLIParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PLIParser.ExpressionContext,i)


        def INIT_K(self):
            return self.getToken(PLIParser.INIT_K, 0)

        def getRuleIndex(self):
            return PLIParser.RULE_attribute

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute" ):
                return visitor.visitAttribute(self)
            else:
                return visitor.visitChildren(self)




    def attribute(self):

        localctx = PLIParser.AttributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_attribute)
        self._la = 0 # Token type
        try:
            self.state = 221
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [48, 49, 50, 51, 52, 53, 54, 55, 56, 57]:
                self.enterOuterAlt(localctx, 1)
                self.state = 199
                self.type_()
                pass
            elif token in [44]:
                self.enterOuterAlt(localctx, 2)
                self.state = 200
                self.match(PLIParser.PICTURE_K)
                self.state = 201
                self.match(PLIParser.STRING)
                pass
            elif token in [45]:
                self.enterOuterAlt(localctx, 3)
                self.state = 202
                self.match(PLIParser.TASK_K)
                pass
            elif token in [46]:
                self.enterOuterAlt(localctx, 4)
                self.state = 203
                self.match(PLIParser.VARYING_K)
                pass
            elif token in [47]:
                self.enterOuterAlt(localctx, 5)
                self.state = 204
                self.match(PLIParser.ALIGNED_K)
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 6)
                self.state = 205
                self.match(PLIParser.T__3)
                self.state = 206
                self.expression()
                self.state = 211
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==6:
                    self.state = 207
                    self.match(PLIParser.T__5)
                    self.state = 208
                    self.expression()
                    self.state = 213
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 214
                self.match(PLIParser.T__4)
                pass
            elif token in [58]:
                self.enterOuterAlt(localctx, 7)
                self.state = 216
                self.match(PLIParser.INIT_K)
                self.state = 217
                self.match(PLIParser.T__3)
                self.state = 218
                self.expression()
                self.state = 219
                self.match(PLIParser.T__4)
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


    class Type_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FIXED_K(self):
            return self.getToken(PLIParser.FIXED_K, 0)

        def FLOAT_K(self):
            return self.getToken(PLIParser.FLOAT_K, 0)

        def CHARACTER_K(self):
            return self.getToken(PLIParser.CHARACTER_K, 0)

        def CHAR_K(self):
            return self.getToken(PLIParser.CHAR_K, 0)

        def BINARY_K(self):
            return self.getToken(PLIParser.BINARY_K, 0)

        def BIN_K(self):
            return self.getToken(PLIParser.BIN_K, 0)

        def DECIMAL_K(self):
            return self.getToken(PLIParser.DECIMAL_K, 0)

        def DEC_K(self):
            return self.getToken(PLIParser.DEC_K, 0)

        def POINTER_K(self):
            return self.getToken(PLIParser.POINTER_K, 0)

        def BIT_K(self):
            return self.getToken(PLIParser.BIT_K, 0)

        def getRuleIndex(self):
            return PLIParser.RULE_type_

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_" ):
                return visitor.visitType_(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = PLIParser.Type_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_type_)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 287948901175001088) != 0)):
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


    class On_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ON_K(self):
            return self.getToken(PLIParser.ON_K, 0)

        def ID(self):
            return self.getToken(PLIParser.ID, 0)

        def statement(self):
            return self.getTypedRuleContext(PLIParser.StatementContext,0)


        def getRuleIndex(self):
            return PLIParser.RULE_on_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOn_stmt" ):
                return visitor.visitOn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def on_stmt(self):

        localctx = PLIParser.On_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_on_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.match(PLIParser.ON_K)
            self.state = 226
            self.match(PLIParser.ID)
            self.state = 227
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Allocate_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ALLOCATE_K(self):
            return self.getToken(PLIParser.ALLOCATE_K, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(PLIParser.ID)
            else:
                return self.getToken(PLIParser.ID, i)

        def type_(self):
            return self.getTypedRuleContext(PLIParser.Type_Context,0)


        def SET_K(self):
            return self.getToken(PLIParser.SET_K, 0)

        def getRuleIndex(self):
            return PLIParser.RULE_allocate_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAllocate_stmt" ):
                return visitor.visitAllocate_stmt(self)
            else:
                return visitor.visitChildren(self)




    def allocate_stmt(self):

        localctx = PLIParser.Allocate_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_allocate_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.match(PLIParser.ALLOCATE_K)
            self.state = 232
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [60]:
                self.state = 230
                self.match(PLIParser.ID)
                pass
            elif token in [48, 49, 50, 51, 52, 53, 54, 55, 56, 57]:
                self.state = 231
                self.type_()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 238
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==59:
                self.state = 234
                self.match(PLIParser.SET_K)
                self.state = 235
                self.match(PLIParser.T__3)
                self.state = 236
                self.match(PLIParser.ID)
                self.state = 237
                self.match(PLIParser.T__4)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Free_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FREE_K(self):
            return self.getToken(PLIParser.FREE_K, 0)

        def ID(self):
            return self.getToken(PLIParser.ID, 0)

        def getRuleIndex(self):
            return PLIParser.RULE_free_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFree_stmt" ):
                return visitor.visitFree_stmt(self)
            else:
                return visitor.visitChildren(self)




    def free_stmt(self):

        localctx = PLIParser.Free_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_free_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self.match(PLIParser.FREE_K)
            self.state = 241
            self.match(PLIParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Do_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO_K(self):
            return self.getToken(PLIParser.DO_K, 0)

        def END_K(self):
            return self.getToken(PLIParser.END_K, 0)

        def do_spec(self):
            return self.getTypedRuleContext(PLIParser.Do_specContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLIParser.StatementContext)
            else:
                return self.getTypedRuleContext(PLIParser.StatementContext,i)


        def ID(self):
            return self.getToken(PLIParser.ID, 0)

        def getRuleIndex(self):
            return PLIParser.RULE_do_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDo_block" ):
                return visitor.visitDo_block(self)
            else:
                return visitor.visitChildren(self)




    def do_block(self):

        localctx = PLIParser.Do_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_do_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.match(PLIParser.DO_K)
            self.state = 245
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==60:
                self.state = 244
                self.do_spec()


            self.state = 247
            self.match(PLIParser.T__1)
            self.state = 251
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8070451049778380820) != 0):
                self.state = 248
                self.statement()
                self.state = 253
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 254
            self.match(PLIParser.END_K)
            self.state = 256
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==60:
                self.state = 255
                self.match(PLIParser.ID)


            self.state = 258
            self.match(PLIParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Do_specContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PLIParser.ID, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLIParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PLIParser.ExpressionContext,i)


        def TO_K(self):
            return self.getToken(PLIParser.TO_K, 0)

        def BY_K(self):
            return self.getToken(PLIParser.BY_K, 0)

        def getRuleIndex(self):
            return PLIParser.RULE_do_spec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDo_spec" ):
                return visitor.visitDo_spec(self)
            else:
                return visitor.visitChildren(self)




    def do_spec(self):

        localctx = PLIParser.Do_specContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_do_spec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.match(PLIParser.ID)
            self.state = 261
            self.match(PLIParser.T__6)
            self.state = 262
            self.expression()
            self.state = 269
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 263
                self.match(PLIParser.TO_K)
                self.state = 264
                self.expression()
                self.state = 267
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==34:
                    self.state = 265
                    self.match(PLIParser.BY_K)
                    self.state = 266
                    self.expression()




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
            return self.getToken(PLIParser.IF_K, 0)

        def expression(self):
            return self.getTypedRuleContext(PLIParser.ExpressionContext,0)


        def THEN_K(self):
            return self.getToken(PLIParser.THEN_K, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLIParser.StatementContext)
            else:
                return self.getTypedRuleContext(PLIParser.StatementContext,i)


        def ELSE_K(self):
            return self.getToken(PLIParser.ELSE_K, 0)

        def getRuleIndex(self):
            return PLIParser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = PLIParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            self.match(PLIParser.IF_K)
            self.state = 272
            self.expression()
            self.state = 273
            self.match(PLIParser.THEN_K)
            self.state = 274
            self.statement()
            self.state = 277
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 275
                self.match(PLIParser.ELSE_K)
                self.state = 276
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CALL_K(self):
            return self.getToken(PLIParser.CALL_K, 0)

        def ID(self):
            return self.getToken(PLIParser.ID, 0)

        def args(self):
            return self.getTypedRuleContext(PLIParser.ArgsContext,0)


        def getRuleIndex(self):
            return PLIParser.RULE_call_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_stmt" ):
                return visitor.visitCall_stmt(self)
            else:
                return visitor.visitChildren(self)




    def call_stmt(self):

        localctx = PLIParser.Call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_call_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self.match(PLIParser.CALL_K)
            self.state = 280
            self.match(PLIParser.ID)
            self.state = 286
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 281
                self.match(PLIParser.T__3)
                self.state = 283
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8070450532247928848) != 0):
                    self.state = 282
                    self.args()


                self.state = 285
                self.match(PLIParser.T__4)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLIParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PLIParser.ExpressionContext,i)


        def getRuleIndex(self):
            return PLIParser.RULE_args

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgs" ):
                return visitor.visitArgs(self)
            else:
                return visitor.visitChildren(self)




    def args(self):

        localctx = PLIParser.ArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
            self.expression()
            self.state = 293
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 289
                self.match(PLIParser.T__5)
                self.state = 290
                self.expression()
                self.state = 295
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def primary(self):
            return self.getTypedRuleContext(PLIParser.PrimaryContext,0)


        def expression(self):
            return self.getTypedRuleContext(PLIParser.ExpressionContext,0)


        def getRuleIndex(self):
            return PLIParser.RULE_assignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = PLIParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
            self.primary()
            self.state = 297
            self.match(PLIParser.T__6)
            self.state = 298
            self.expression()
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
            return self.getToken(PLIParser.RETURN_K, 0)

        def expression(self):
            return self.getTypedRuleContext(PLIParser.ExpressionContext,0)


        def getRuleIndex(self):
            return PLIParser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = PLIParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.match(PLIParser.RETURN_K)
            self.state = 305
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 301
                self.match(PLIParser.T__3)
                self.state = 302
                self.expression()
                self.state = 303
                self.match(PLIParser.T__4)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ActionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PUT_K(self):
            return self.getToken(PLIParser.PUT_K, 0)

        def GET_K(self):
            return self.getToken(PLIParser.GET_K, 0)

        def LIST_K(self):
            return self.getToken(PLIParser.LIST_K, 0)

        def EDIT_K(self):
            return self.getToken(PLIParser.EDIT_K, 0)

        def SKIP_K(self):
            return self.getToken(PLIParser.SKIP_K, 0)

        def DATA_K(self):
            return self.getToken(PLIParser.DATA_K, 0)

        def args(self):
            return self.getTypedRuleContext(PLIParser.ArgsContext,0)


        def getRuleIndex(self):
            return PLIParser.RULE_action

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAction" ):
                return visitor.visitAction(self)
            else:
                return visitor.visitChildren(self)




    def action(self):

        localctx = PLIParser.ActionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_action)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
            _la = self._input.LA(1)
            if not(_la==37 or _la==38):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 309
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8246337208320) != 0):
                self.state = 308
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8246337208320) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 316
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 311
                self.match(PLIParser.T__3)
                self.state = 313
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8070450532247928848) != 0):
                    self.state = 312
                    self.args()


                self.state = 315
                self.match(PLIParser.T__4)


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

        def primary(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLIParser.PrimaryContext)
            else:
                return self.getTypedRuleContext(PLIParser.PrimaryContext,i)


        def operator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLIParser.OperatorContext)
            else:
                return self.getTypedRuleContext(PLIParser.OperatorContext,i)


        def getRuleIndex(self):
            return PLIParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = PLIParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
            self.primary()
            self.state = 324
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 524162) != 0):
                self.state = 319
                self.operator()
                self.state = 320
                self.primary()
                self.state = 326
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
            return self.getToken(PLIParser.ID, 0)

        def args(self):
            return self.getTypedRuleContext(PLIParser.ArgsContext,0)


        def STRING(self):
            return self.getToken(PLIParser.STRING, 0)

        def NUMBER(self):
            return self.getToken(PLIParser.NUMBER, 0)

        def expression(self):
            return self.getTypedRuleContext(PLIParser.ExpressionContext,0)


        def getRuleIndex(self):
            return PLIParser.RULE_primary

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimary" ):
                return visitor.visitPrimary(self)
            else:
                return visitor.visitChildren(self)




    def primary(self):

        localctx = PLIParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_primary)
        self._la = 0 # Token type
        try:
            self.state = 341
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [60]:
                self.enterOuterAlt(localctx, 1)
                self.state = 327
                self.match(PLIParser.ID)
                self.state = 333
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==4:
                    self.state = 328
                    self.match(PLIParser.T__3)
                    self.state = 330
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8070450532247928848) != 0):
                        self.state = 329
                        self.args()


                    self.state = 332
                    self.match(PLIParser.T__4)


                pass
            elif token in [61]:
                self.enterOuterAlt(localctx, 2)
                self.state = 335
                self.match(PLIParser.STRING)
                pass
            elif token in [62]:
                self.enterOuterAlt(localctx, 3)
                self.state = 336
                self.match(PLIParser.NUMBER)
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 4)
                self.state = 337
                self.match(PLIParser.T__3)
                self.state = 338
                self.expression()
                self.state = 339
                self.match(PLIParser.T__4)
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


    class OperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PLIParser.RULE_operator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperator" ):
                return visitor.visitOperator(self)
            else:
                return visitor.visitChildren(self)




    def operator(self):

        localctx = PLIParser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 524162) != 0)):
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





