# Generated from rosetta/babel/pascal/grammar/Pascal.g4 by ANTLR 4.13.2
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
        4,1,57,371,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,1,0,3,0,66,8,0,
        1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,5,1,78,8,1,10,1,12,1,81,
        9,1,1,1,1,1,3,1,85,8,1,1,1,1,1,1,2,3,2,90,8,2,1,2,1,2,1,3,1,3,1,
        3,1,3,4,3,98,8,3,11,3,12,3,99,1,4,1,4,1,4,1,4,4,4,106,8,4,11,4,12,
        4,107,1,5,1,5,1,5,5,5,113,8,5,10,5,12,5,116,9,5,1,5,1,5,1,5,1,6,
        1,6,1,6,1,6,4,6,125,8,6,11,6,12,6,126,1,7,1,7,1,7,1,7,1,8,1,8,1,
        8,1,8,1,8,1,8,5,8,139,8,8,10,8,12,8,142,9,8,1,8,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,3,8,152,8,8,1,9,1,9,1,9,1,9,1,10,1,10,1,10,5,10,161,
        8,10,10,10,12,10,164,9,10,3,10,166,8,10,1,10,3,10,169,8,10,1,11,
        1,11,1,11,3,11,174,8,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,3,12,
        183,8,12,1,12,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,5,13,
        195,8,13,10,13,12,13,198,9,13,1,13,1,13,1,14,3,14,203,8,14,1,14,
        1,14,1,14,5,14,208,8,14,10,14,12,14,211,9,14,1,14,1,14,1,14,1,15,
        1,15,1,15,1,15,5,15,220,8,15,10,15,12,15,223,9,15,1,15,1,15,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,3,16,236,8,16,1,17,1,17,
        1,17,1,17,1,18,1,18,1,18,1,18,1,18,5,18,247,8,18,10,18,12,18,250,
        9,18,1,18,1,18,3,18,254,8,18,1,19,1,19,1,19,1,19,1,19,1,19,3,19,
        262,8,19,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,21,1,21,
        1,21,1,21,1,21,1,22,1,22,1,22,1,22,5,22,282,8,22,10,22,12,22,285,
        9,22,1,22,1,22,1,22,1,23,1,23,1,23,1,23,5,23,294,8,23,10,23,12,23,
        297,9,23,1,23,1,23,1,23,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,
        1,24,1,24,3,24,312,8,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,
        1,24,1,24,1,24,1,24,5,24,326,8,24,10,24,12,24,329,9,24,1,25,1,25,
        1,25,1,25,1,25,5,25,336,8,25,10,25,12,25,339,9,25,1,25,1,25,3,25,
        343,8,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,3,25,353,8,25,1,
        26,1,26,1,26,1,26,3,26,359,8,26,1,27,1,27,1,28,1,28,1,29,1,29,1,
        30,1,30,1,31,1,31,1,31,0,1,48,32,0,2,4,6,8,10,12,14,16,18,20,22,
        24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,0,6,
        1,0,41,42,1,0,12,13,1,0,15,20,1,0,21,22,1,0,23,26,1,0,48,49,389,
        0,65,1,0,0,0,2,71,1,0,0,0,4,89,1,0,0,0,6,97,1,0,0,0,8,101,1,0,0,
        0,10,109,1,0,0,0,12,120,1,0,0,0,14,128,1,0,0,0,16,151,1,0,0,0,18,
        153,1,0,0,0,20,165,1,0,0,0,22,170,1,0,0,0,24,179,1,0,0,0,26,190,
        1,0,0,0,28,202,1,0,0,0,30,215,1,0,0,0,32,235,1,0,0,0,34,237,1,0,
        0,0,36,241,1,0,0,0,38,255,1,0,0,0,40,263,1,0,0,0,42,272,1,0,0,0,
        44,277,1,0,0,0,46,289,1,0,0,0,48,311,1,0,0,0,50,352,1,0,0,0,52,358,
        1,0,0,0,54,360,1,0,0,0,56,362,1,0,0,0,58,364,1,0,0,0,60,366,1,0,
        0,0,62,368,1,0,0,0,64,66,3,2,1,0,65,64,1,0,0,0,65,66,1,0,0,0,66,
        67,1,0,0,0,67,68,3,4,2,0,68,69,5,1,0,0,69,70,5,0,0,1,70,1,1,0,0,
        0,71,72,5,27,0,0,72,84,3,54,27,0,73,74,5,2,0,0,74,79,3,54,27,0,75,
        76,5,3,0,0,76,78,3,54,27,0,77,75,1,0,0,0,78,81,1,0,0,0,79,77,1,0,
        0,0,79,80,1,0,0,0,80,82,1,0,0,0,81,79,1,0,0,0,82,83,5,4,0,0,83,85,
        1,0,0,0,84,73,1,0,0,0,84,85,1,0,0,0,85,86,1,0,0,0,86,87,5,5,0,0,
        87,3,1,0,0,0,88,90,3,6,3,0,89,88,1,0,0,0,89,90,1,0,0,0,90,91,1,0,
        0,0,91,92,3,30,15,0,92,5,1,0,0,0,93,98,3,8,4,0,94,98,3,12,6,0,95,
        98,3,22,11,0,96,98,3,24,12,0,97,93,1,0,0,0,97,94,1,0,0,0,97,95,1,
        0,0,0,97,96,1,0,0,0,98,99,1,0,0,0,99,97,1,0,0,0,99,100,1,0,0,0,100,
        7,1,0,0,0,101,105,5,30,0,0,102,103,3,10,5,0,103,104,5,5,0,0,104,
        106,1,0,0,0,105,102,1,0,0,0,106,107,1,0,0,0,107,105,1,0,0,0,107,
        108,1,0,0,0,108,9,1,0,0,0,109,114,3,54,27,0,110,111,5,3,0,0,111,
        113,3,54,27,0,112,110,1,0,0,0,113,116,1,0,0,0,114,112,1,0,0,0,114,
        115,1,0,0,0,115,117,1,0,0,0,116,114,1,0,0,0,117,118,5,6,0,0,118,
        119,3,16,8,0,119,11,1,0,0,0,120,124,5,31,0,0,121,122,3,14,7,0,122,
        123,5,5,0,0,123,125,1,0,0,0,124,121,1,0,0,0,125,126,1,0,0,0,126,
        124,1,0,0,0,126,127,1,0,0,0,127,13,1,0,0,0,128,129,3,54,27,0,129,
        130,5,15,0,0,130,131,3,16,8,0,131,15,1,0,0,0,132,152,3,54,27,0,133,
        134,5,32,0,0,134,135,5,7,0,0,135,140,3,18,9,0,136,137,5,3,0,0,137,
        139,3,18,9,0,138,136,1,0,0,0,139,142,1,0,0,0,140,138,1,0,0,0,140,
        141,1,0,0,0,141,143,1,0,0,0,142,140,1,0,0,0,143,144,5,8,0,0,144,
        145,5,33,0,0,145,146,3,16,8,0,146,152,1,0,0,0,147,148,5,34,0,0,148,
        149,3,20,10,0,149,150,5,29,0,0,150,152,1,0,0,0,151,132,1,0,0,0,151,
        133,1,0,0,0,151,147,1,0,0,0,152,17,1,0,0,0,153,154,3,48,24,0,154,
        155,5,9,0,0,155,156,3,48,24,0,156,19,1,0,0,0,157,162,3,10,5,0,158,
        159,5,5,0,0,159,161,3,10,5,0,160,158,1,0,0,0,161,164,1,0,0,0,162,
        160,1,0,0,0,162,163,1,0,0,0,163,166,1,0,0,0,164,162,1,0,0,0,165,
        157,1,0,0,0,165,166,1,0,0,0,166,168,1,0,0,0,167,169,5,5,0,0,168,
        167,1,0,0,0,168,169,1,0,0,0,169,21,1,0,0,0,170,171,5,35,0,0,171,
        173,3,54,27,0,172,174,3,26,13,0,173,172,1,0,0,0,173,174,1,0,0,0,
        174,175,1,0,0,0,175,176,5,5,0,0,176,177,3,4,2,0,177,178,5,5,0,0,
        178,23,1,0,0,0,179,180,5,36,0,0,180,182,3,54,27,0,181,183,3,26,13,
        0,182,181,1,0,0,0,182,183,1,0,0,0,183,184,1,0,0,0,184,185,5,6,0,
        0,185,186,3,54,27,0,186,187,5,5,0,0,187,188,3,4,2,0,188,189,5,5,
        0,0,189,25,1,0,0,0,190,191,5,2,0,0,191,196,3,28,14,0,192,193,5,5,
        0,0,193,195,3,28,14,0,194,192,1,0,0,0,195,198,1,0,0,0,196,194,1,
        0,0,0,196,197,1,0,0,0,197,199,1,0,0,0,198,196,1,0,0,0,199,200,5,
        4,0,0,200,27,1,0,0,0,201,203,5,30,0,0,202,201,1,0,0,0,202,203,1,
        0,0,0,203,204,1,0,0,0,204,209,3,54,27,0,205,206,5,3,0,0,206,208,
        3,54,27,0,207,205,1,0,0,0,208,211,1,0,0,0,209,207,1,0,0,0,209,210,
        1,0,0,0,210,212,1,0,0,0,211,209,1,0,0,0,212,213,5,6,0,0,213,214,
        3,54,27,0,214,29,1,0,0,0,215,216,5,28,0,0,216,221,3,32,16,0,217,
        218,5,5,0,0,218,220,3,32,16,0,219,217,1,0,0,0,220,223,1,0,0,0,221,
        219,1,0,0,0,221,222,1,0,0,0,222,224,1,0,0,0,223,221,1,0,0,0,224,
        225,5,29,0,0,225,31,1,0,0,0,226,236,3,34,17,0,227,236,3,36,18,0,
        228,236,3,38,19,0,229,236,3,40,20,0,230,236,3,42,21,0,231,236,3,
        44,22,0,232,236,3,46,23,0,233,236,3,30,15,0,234,236,1,0,0,0,235,
        226,1,0,0,0,235,227,1,0,0,0,235,228,1,0,0,0,235,229,1,0,0,0,235,
        230,1,0,0,0,235,231,1,0,0,0,235,232,1,0,0,0,235,233,1,0,0,0,235,
        234,1,0,0,0,236,33,1,0,0,0,237,238,3,54,27,0,238,239,5,10,0,0,239,
        240,3,48,24,0,240,35,1,0,0,0,241,253,3,54,27,0,242,243,5,2,0,0,243,
        248,3,48,24,0,244,245,5,3,0,0,245,247,3,48,24,0,246,244,1,0,0,0,
        247,250,1,0,0,0,248,246,1,0,0,0,248,249,1,0,0,0,249,251,1,0,0,0,
        250,248,1,0,0,0,251,252,5,4,0,0,252,254,1,0,0,0,253,242,1,0,0,0,
        253,254,1,0,0,0,254,37,1,0,0,0,255,256,5,37,0,0,256,257,3,48,24,
        0,257,258,5,38,0,0,258,261,3,32,16,0,259,260,5,39,0,0,260,262,3,
        32,16,0,261,259,1,0,0,0,261,262,1,0,0,0,262,39,1,0,0,0,263,264,5,
        40,0,0,264,265,3,54,27,0,265,266,5,10,0,0,266,267,3,48,24,0,267,
        268,7,0,0,0,268,269,3,48,24,0,269,270,5,43,0,0,270,271,3,32,16,0,
        271,41,1,0,0,0,272,273,5,44,0,0,273,274,3,48,24,0,274,275,5,43,0,
        0,275,276,3,32,16,0,276,43,1,0,0,0,277,278,5,45,0,0,278,283,3,32,
        16,0,279,280,5,5,0,0,280,282,3,32,16,0,281,279,1,0,0,0,282,285,1,
        0,0,0,283,281,1,0,0,0,283,284,1,0,0,0,284,286,1,0,0,0,285,283,1,
        0,0,0,286,287,5,46,0,0,287,288,3,48,24,0,288,45,1,0,0,0,289,290,
        5,47,0,0,290,295,3,54,27,0,291,292,5,3,0,0,292,294,3,54,27,0,293,
        291,1,0,0,0,294,297,1,0,0,0,295,293,1,0,0,0,295,296,1,0,0,0,296,
        298,1,0,0,0,297,295,1,0,0,0,298,299,5,43,0,0,299,300,3,32,16,0,300,
        47,1,0,0,0,301,302,6,24,-1,0,302,303,5,14,0,0,303,312,3,48,24,7,
        304,305,5,22,0,0,305,312,3,48,24,3,306,307,5,2,0,0,307,308,3,48,
        24,0,308,309,5,4,0,0,309,312,1,0,0,0,310,312,3,50,25,0,311,301,1,
        0,0,0,311,304,1,0,0,0,311,306,1,0,0,0,311,310,1,0,0,0,312,327,1,
        0,0,0,313,314,10,8,0,0,314,315,7,1,0,0,315,326,3,48,24,9,316,317,
        10,6,0,0,317,318,7,2,0,0,318,326,3,48,24,7,319,320,10,5,0,0,320,
        321,7,3,0,0,321,326,3,48,24,6,322,323,10,4,0,0,323,324,7,4,0,0,324,
        326,3,48,24,5,325,313,1,0,0,0,325,316,1,0,0,0,325,319,1,0,0,0,325,
        322,1,0,0,0,326,329,1,0,0,0,327,325,1,0,0,0,327,328,1,0,0,0,328,
        49,1,0,0,0,329,327,1,0,0,0,330,342,3,54,27,0,331,332,5,2,0,0,332,
        337,3,48,24,0,333,334,5,3,0,0,334,336,3,48,24,0,335,333,1,0,0,0,
        336,339,1,0,0,0,337,335,1,0,0,0,337,338,1,0,0,0,338,340,1,0,0,0,
        339,337,1,0,0,0,340,341,5,4,0,0,341,343,1,0,0,0,342,331,1,0,0,0,
        342,343,1,0,0,0,343,353,1,0,0,0,344,345,3,54,27,0,345,346,5,11,0,
        0,346,353,1,0,0,0,347,348,3,54,27,0,348,349,5,1,0,0,349,350,3,54,
        27,0,350,353,1,0,0,0,351,353,3,52,26,0,352,330,1,0,0,0,352,344,1,
        0,0,0,352,347,1,0,0,0,352,351,1,0,0,0,353,51,1,0,0,0,354,359,3,56,
        28,0,355,359,3,58,29,0,356,359,3,60,30,0,357,359,3,62,31,0,358,354,
        1,0,0,0,358,355,1,0,0,0,358,356,1,0,0,0,358,357,1,0,0,0,359,53,1,
        0,0,0,360,361,5,50,0,0,361,55,1,0,0,0,362,363,5,51,0,0,363,57,1,
        0,0,0,364,365,5,52,0,0,365,59,1,0,0,0,366,367,5,53,0,0,367,61,1,
        0,0,0,368,369,7,5,0,0,369,63,1,0,0,0,33,65,79,84,89,97,99,107,114,
        126,140,151,162,165,168,173,182,196,202,209,221,235,248,253,261,
        283,295,311,325,327,337,342,352,358
    ]

class PascalParser ( Parser ):

    grammarFileName = "Pascal.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'.'", "'('", "','", "')'", "';'", "':'", 
                     "'['", "']'", "'..'", "':='", "'^'", "'OR'", "'AND'", 
                     "'NOT'", "'='", "'<>'", "'<'", "'<='", "'>'", "'>='", 
                     "'+'", "'-'", "'*'", "'/'", "'DIV'", "'MOD'", "'PROGRAM'", 
                     "'BEGIN'", "'END'", "'VAR'", "'TYPE'", "'ARRAY'", "'OF'", 
                     "'RECORD'", "'PROCEDURE'", "'FUNCTION'", "'IF'", "'THEN'", 
                     "'ELSE'", "'FOR'", "'TO'", "'DOWNTO'", "'DO'", "'WHILE'", 
                     "'REPEAT'", "'UNTIL'", "'WITH'", "'TRUE'", "'FALSE'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "OR", "AND", "NOT", "EQ", "NE", "LT", "LE", "GT", 
                      "GE", "PLUS", "MINUS", "STAR", "SLASH", "DIV", "MOD", 
                      "PROGRAM_K", "BEGIN_K", "END_K", "VAR_K", "TYPE_K", 
                      "ARRAY_K", "OF_K", "RECORD_K", "PROCEDURE_K", "FUNCTION_K", 
                      "IF_K", "THEN_K", "ELSE_K", "FOR_K", "TO_K", "DOWNTO_K", 
                      "DO_K", "WHILE_K", "REPEAT_K", "UNTIL_K", "WITH_K", 
                      "TRUE_K", "FALSE_K", "IDENTIFIER", "INTEGER", "REAL", 
                      "STRING", "NEWLINE", "WS", "COMMENT", "COMMENT2" ]

    RULE_program = 0
    RULE_program_stmt = 1
    RULE_block = 2
    RULE_declaration_part = 3
    RULE_var_decl_part = 4
    RULE_var_decl = 5
    RULE_type_decl_part = 6
    RULE_type_decl = 7
    RULE_type_spec = 8
    RULE_range = 9
    RULE_field_list = 10
    RULE_procedure_decl = 11
    RULE_function_decl = 12
    RULE_formal_parameter_list = 13
    RULE_formal_parameter = 14
    RULE_statement_part = 15
    RULE_statement = 16
    RULE_assignment_stmt = 17
    RULE_procedure_call = 18
    RULE_if_stmt = 19
    RULE_for_stmt = 20
    RULE_while_stmt = 21
    RULE_repeat_stmt = 22
    RULE_with_stmt = 23
    RULE_expression = 24
    RULE_primary = 25
    RULE_literal = 26
    RULE_identifier = 27
    RULE_integer_literal = 28
    RULE_real_literal = 29
    RULE_string_literal = 30
    RULE_logical_literal = 31

    ruleNames =  [ "program", "program_stmt", "block", "declaration_part", 
                   "var_decl_part", "var_decl", "type_decl_part", "type_decl", 
                   "type_spec", "range", "field_list", "procedure_decl", 
                   "function_decl", "formal_parameter_list", "formal_parameter", 
                   "statement_part", "statement", "assignment_stmt", "procedure_call", 
                   "if_stmt", "for_stmt", "while_stmt", "repeat_stmt", "with_stmt", 
                   "expression", "primary", "literal", "identifier", "integer_literal", 
                   "real_literal", "string_literal", "logical_literal" ]

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
    OR=12
    AND=13
    NOT=14
    EQ=15
    NE=16
    LT=17
    LE=18
    GT=19
    GE=20
    PLUS=21
    MINUS=22
    STAR=23
    SLASH=24
    DIV=25
    MOD=26
    PROGRAM_K=27
    BEGIN_K=28
    END_K=29
    VAR_K=30
    TYPE_K=31
    ARRAY_K=32
    OF_K=33
    RECORD_K=34
    PROCEDURE_K=35
    FUNCTION_K=36
    IF_K=37
    THEN_K=38
    ELSE_K=39
    FOR_K=40
    TO_K=41
    DOWNTO_K=42
    DO_K=43
    WHILE_K=44
    REPEAT_K=45
    UNTIL_K=46
    WITH_K=47
    TRUE_K=48
    FALSE_K=49
    IDENTIFIER=50
    INTEGER=51
    REAL=52
    STRING=53
    NEWLINE=54
    WS=55
    COMMENT=56
    COMMENT2=57

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
            return self.getTypedRuleContext(PascalParser.BlockContext,0)


        def EOF(self):
            return self.getToken(PascalParser.EOF, 0)

        def program_stmt(self):
            return self.getTypedRuleContext(PascalParser.Program_stmtContext,0)


        def getRuleIndex(self):
            return PascalParser.RULE_program

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

        localctx = PascalParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27:
                self.state = 64
                self.program_stmt()


            self.state = 67
            self.block()
            self.state = 68
            self.match(PascalParser.T__0)
            self.state = 69
            self.match(PascalParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Program_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROGRAM_K(self):
            return self.getToken(PascalParser.PROGRAM_K, 0)

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PascalParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(PascalParser.IdentifierContext,i)


        def getRuleIndex(self):
            return PascalParser.RULE_program_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram_stmt" ):
                listener.enterProgram_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram_stmt" ):
                listener.exitProgram_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram_stmt" ):
                return visitor.visitProgram_stmt(self)
            else:
                return visitor.visitChildren(self)




    def program_stmt(self):

        localctx = PascalParser.Program_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_program_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(PascalParser.PROGRAM_K)
            self.state = 72
            self.identifier()
            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 73
                self.match(PascalParser.T__1)
                self.state = 74
                self.identifier()
                self.state = 79
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==3:
                    self.state = 75
                    self.match(PascalParser.T__2)
                    self.state = 76
                    self.identifier()
                    self.state = 81
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 82
                self.match(PascalParser.T__3)


            self.state = 86
            self.match(PascalParser.T__4)
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

        def statement_part(self):
            return self.getTypedRuleContext(PascalParser.Statement_partContext,0)


        def declaration_part(self):
            return self.getTypedRuleContext(PascalParser.Declaration_partContext,0)


        def getRuleIndex(self):
            return PascalParser.RULE_block

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

        localctx = PascalParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 106300440576) != 0):
                self.state = 88
                self.declaration_part()


            self.state = 91
            self.statement_part()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declaration_partContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl_part(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PascalParser.Var_decl_partContext)
            else:
                return self.getTypedRuleContext(PascalParser.Var_decl_partContext,i)


        def type_decl_part(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PascalParser.Type_decl_partContext)
            else:
                return self.getTypedRuleContext(PascalParser.Type_decl_partContext,i)


        def procedure_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PascalParser.Procedure_declContext)
            else:
                return self.getTypedRuleContext(PascalParser.Procedure_declContext,i)


        def function_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PascalParser.Function_declContext)
            else:
                return self.getTypedRuleContext(PascalParser.Function_declContext,i)


        def getRuleIndex(self):
            return PascalParser.RULE_declaration_part

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration_part" ):
                listener.enterDeclaration_part(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration_part" ):
                listener.exitDeclaration_part(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration_part" ):
                return visitor.visitDeclaration_part(self)
            else:
                return visitor.visitChildren(self)




    def declaration_part(self):

        localctx = PascalParser.Declaration_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_declaration_part)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 97
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [30]:
                    self.state = 93
                    self.var_decl_part()
                    pass
                elif token in [31]:
                    self.state = 94
                    self.type_decl_part()
                    pass
                elif token in [35]:
                    self.state = 95
                    self.procedure_decl()
                    pass
                elif token in [36]:
                    self.state = 96
                    self.function_decl()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 99 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 106300440576) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_decl_partContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR_K(self):
            return self.getToken(PascalParser.VAR_K, 0)

        def var_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PascalParser.Var_declContext)
            else:
                return self.getTypedRuleContext(PascalParser.Var_declContext,i)


        def getRuleIndex(self):
            return PascalParser.RULE_var_decl_part

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_decl_part" ):
                listener.enterVar_decl_part(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_decl_part" ):
                listener.exitVar_decl_part(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl_part" ):
                return visitor.visitVar_decl_part(self)
            else:
                return visitor.visitChildren(self)




    def var_decl_part(self):

        localctx = PascalParser.Var_decl_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_var_decl_part)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.match(PascalParser.VAR_K)
            self.state = 105 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 102
                self.var_decl()
                self.state = 103
                self.match(PascalParser.T__4)
                self.state = 107 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==50):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PascalParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(PascalParser.IdentifierContext,i)


        def type_spec(self):
            return self.getTypedRuleContext(PascalParser.Type_specContext,0)


        def getRuleIndex(self):
            return PascalParser.RULE_var_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_decl" ):
                listener.enterVar_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_decl" ):
                listener.exitVar_decl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl" ):
                return visitor.visitVar_decl(self)
            else:
                return visitor.visitChildren(self)




    def var_decl(self):

        localctx = PascalParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_var_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.identifier()
            self.state = 114
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 110
                self.match(PascalParser.T__2)
                self.state = 111
                self.identifier()
                self.state = 116
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 117
            self.match(PascalParser.T__5)
            self.state = 118
            self.type_spec()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_decl_partContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE_K(self):
            return self.getToken(PascalParser.TYPE_K, 0)

        def type_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PascalParser.Type_declContext)
            else:
                return self.getTypedRuleContext(PascalParser.Type_declContext,i)


        def getRuleIndex(self):
            return PascalParser.RULE_type_decl_part

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_decl_part" ):
                listener.enterType_decl_part(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_decl_part" ):
                listener.exitType_decl_part(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_decl_part" ):
                return visitor.visitType_decl_part(self)
            else:
                return visitor.visitChildren(self)




    def type_decl_part(self):

        localctx = PascalParser.Type_decl_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_type_decl_part)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(PascalParser.TYPE_K)
            self.state = 124 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 121
                self.type_decl()
                self.state = 122
                self.match(PascalParser.T__4)
                self.state = 126 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==50):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(PascalParser.IdentifierContext,0)


        def EQ(self):
            return self.getToken(PascalParser.EQ, 0)

        def type_spec(self):
            return self.getTypedRuleContext(PascalParser.Type_specContext,0)


        def getRuleIndex(self):
            return PascalParser.RULE_type_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_decl" ):
                listener.enterType_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_decl" ):
                listener.exitType_decl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_decl" ):
                return visitor.visitType_decl(self)
            else:
                return visitor.visitChildren(self)




    def type_decl(self):

        localctx = PascalParser.Type_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_type_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.identifier()
            self.state = 129
            self.match(PascalParser.EQ)
            self.state = 130
            self.type_spec()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_specContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(PascalParser.IdentifierContext,0)


        def ARRAY_K(self):
            return self.getToken(PascalParser.ARRAY_K, 0)

        def range_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PascalParser.RangeContext)
            else:
                return self.getTypedRuleContext(PascalParser.RangeContext,i)


        def OF_K(self):
            return self.getToken(PascalParser.OF_K, 0)

        def type_spec(self):
            return self.getTypedRuleContext(PascalParser.Type_specContext,0)


        def RECORD_K(self):
            return self.getToken(PascalParser.RECORD_K, 0)

        def field_list(self):
            return self.getTypedRuleContext(PascalParser.Field_listContext,0)


        def END_K(self):
            return self.getToken(PascalParser.END_K, 0)

        def getRuleIndex(self):
            return PascalParser.RULE_type_spec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_spec" ):
                listener.enterType_spec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_spec" ):
                listener.exitType_spec(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_spec" ):
                return visitor.visitType_spec(self)
            else:
                return visitor.visitChildren(self)




    def type_spec(self):

        localctx = PascalParser.Type_specContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_type_spec)
        self._la = 0 # Token type
        try:
            self.state = 151
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [50]:
                self.enterOuterAlt(localctx, 1)
                self.state = 132
                self.identifier()
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 2)
                self.state = 133
                self.match(PascalParser.ARRAY_K)
                self.state = 134
                self.match(PascalParser.T__6)
                self.state = 135
                self.range_()
                self.state = 140
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==3:
                    self.state = 136
                    self.match(PascalParser.T__2)
                    self.state = 137
                    self.range_()
                    self.state = 142
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 143
                self.match(PascalParser.T__7)
                self.state = 144
                self.match(PascalParser.OF_K)
                self.state = 145
                self.type_spec()
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 3)
                self.state = 147
                self.match(PascalParser.RECORD_K)
                self.state = 148
                self.field_list()
                self.state = 149
                self.match(PascalParser.END_K)
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


    class RangeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PascalParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PascalParser.ExpressionContext,i)


        def getRuleIndex(self):
            return PascalParser.RULE_range

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRange" ):
                listener.enterRange(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRange" ):
                listener.exitRange(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRange" ):
                return visitor.visitRange(self)
            else:
                return visitor.visitChildren(self)




    def range_(self):

        localctx = PascalParser.RangeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_range)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.expression(0)
            self.state = 154
            self.match(PascalParser.T__8)
            self.state = 155
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PascalParser.Var_declContext)
            else:
                return self.getTypedRuleContext(PascalParser.Var_declContext,i)


        def getRuleIndex(self):
            return PascalParser.RULE_field_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_list" ):
                listener.enterField_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_list" ):
                listener.exitField_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitField_list" ):
                return visitor.visitField_list(self)
            else:
                return visitor.visitChildren(self)




    def field_list(self):

        localctx = PascalParser.Field_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_field_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==50:
                self.state = 157
                self.var_decl()
                self.state = 162
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 158
                        self.match(PascalParser.T__4)
                        self.state = 159
                        self.var_decl() 
                    self.state = 164
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,11,self._ctx)



            self.state = 168
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 167
                self.match(PascalParser.T__4)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Procedure_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROCEDURE_K(self):
            return self.getToken(PascalParser.PROCEDURE_K, 0)

        def identifier(self):
            return self.getTypedRuleContext(PascalParser.IdentifierContext,0)


        def block(self):
            return self.getTypedRuleContext(PascalParser.BlockContext,0)


        def formal_parameter_list(self):
            return self.getTypedRuleContext(PascalParser.Formal_parameter_listContext,0)


        def getRuleIndex(self):
            return PascalParser.RULE_procedure_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProcedure_decl" ):
                listener.enterProcedure_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProcedure_decl" ):
                listener.exitProcedure_decl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProcedure_decl" ):
                return visitor.visitProcedure_decl(self)
            else:
                return visitor.visitChildren(self)




    def procedure_decl(self):

        localctx = PascalParser.Procedure_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_procedure_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.match(PascalParser.PROCEDURE_K)
            self.state = 171
            self.identifier()
            self.state = 173
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 172
                self.formal_parameter_list()


            self.state = 175
            self.match(PascalParser.T__4)
            self.state = 176
            self.block()
            self.state = 177
            self.match(PascalParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION_K(self):
            return self.getToken(PascalParser.FUNCTION_K, 0)

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PascalParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(PascalParser.IdentifierContext,i)


        def block(self):
            return self.getTypedRuleContext(PascalParser.BlockContext,0)


        def formal_parameter_list(self):
            return self.getTypedRuleContext(PascalParser.Formal_parameter_listContext,0)


        def getRuleIndex(self):
            return PascalParser.RULE_function_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_decl" ):
                listener.enterFunction_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_decl" ):
                listener.exitFunction_decl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_decl" ):
                return visitor.visitFunction_decl(self)
            else:
                return visitor.visitChildren(self)




    def function_decl(self):

        localctx = PascalParser.Function_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_function_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.match(PascalParser.FUNCTION_K)
            self.state = 180
            self.identifier()
            self.state = 182
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 181
                self.formal_parameter_list()


            self.state = 184
            self.match(PascalParser.T__5)
            self.state = 185
            self.identifier()
            self.state = 186
            self.match(PascalParser.T__4)
            self.state = 187
            self.block()
            self.state = 188
            self.match(PascalParser.T__4)
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

        def formal_parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PascalParser.Formal_parameterContext)
            else:
                return self.getTypedRuleContext(PascalParser.Formal_parameterContext,i)


        def getRuleIndex(self):
            return PascalParser.RULE_formal_parameter_list

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

        localctx = PascalParser.Formal_parameter_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_formal_parameter_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.match(PascalParser.T__1)
            self.state = 191
            self.formal_parameter()
            self.state = 196
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 192
                self.match(PascalParser.T__4)
                self.state = 193
                self.formal_parameter()
                self.state = 198
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 199
            self.match(PascalParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Formal_parameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PascalParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(PascalParser.IdentifierContext,i)


        def VAR_K(self):
            return self.getToken(PascalParser.VAR_K, 0)

        def getRuleIndex(self):
            return PascalParser.RULE_formal_parameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormal_parameter" ):
                listener.enterFormal_parameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormal_parameter" ):
                listener.exitFormal_parameter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFormal_parameter" ):
                return visitor.visitFormal_parameter(self)
            else:
                return visitor.visitChildren(self)




    def formal_parameter(self):

        localctx = PascalParser.Formal_parameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_formal_parameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 201
                self.match(PascalParser.VAR_K)


            self.state = 204
            self.identifier()
            self.state = 209
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 205
                self.match(PascalParser.T__2)
                self.state = 206
                self.identifier()
                self.state = 211
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 212
            self.match(PascalParser.T__5)
            self.state = 213
            self.identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Statement_partContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN_K(self):
            return self.getToken(PascalParser.BEGIN_K, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PascalParser.StatementContext)
            else:
                return self.getTypedRuleContext(PascalParser.StatementContext,i)


        def END_K(self):
            return self.getToken(PascalParser.END_K, 0)

        def getRuleIndex(self):
            return PascalParser.RULE_statement_part

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement_part" ):
                listener.enterStatement_part(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement_part" ):
                listener.exitStatement_part(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement_part" ):
                return visitor.visitStatement_part(self)
            else:
                return visitor.visitChildren(self)




    def statement_part(self):

        localctx = PascalParser.Statement_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_statement_part)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self.match(PascalParser.BEGIN_K)
            self.state = 216
            self.statement()
            self.state = 221
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 217
                self.match(PascalParser.T__4)
                self.state = 218
                self.statement()
                self.state = 223
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 224
            self.match(PascalParser.END_K)
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

        def assignment_stmt(self):
            return self.getTypedRuleContext(PascalParser.Assignment_stmtContext,0)


        def procedure_call(self):
            return self.getTypedRuleContext(PascalParser.Procedure_callContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(PascalParser.If_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(PascalParser.For_stmtContext,0)


        def while_stmt(self):
            return self.getTypedRuleContext(PascalParser.While_stmtContext,0)


        def repeat_stmt(self):
            return self.getTypedRuleContext(PascalParser.Repeat_stmtContext,0)


        def with_stmt(self):
            return self.getTypedRuleContext(PascalParser.With_stmtContext,0)


        def statement_part(self):
            return self.getTypedRuleContext(PascalParser.Statement_partContext,0)


        def getRuleIndex(self):
            return PascalParser.RULE_statement

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

        localctx = PascalParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_statement)
        try:
            self.state = 235
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 226
                self.assignment_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 227
                self.procedure_call()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 228
                self.if_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 229
                self.for_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 230
                self.while_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 231
                self.repeat_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 232
                self.with_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 233
                self.statement_part()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(PascalParser.IdentifierContext,0)


        def expression(self):
            return self.getTypedRuleContext(PascalParser.ExpressionContext,0)


        def getRuleIndex(self):
            return PascalParser.RULE_assignment_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment_stmt" ):
                listener.enterAssignment_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment_stmt" ):
                listener.exitAssignment_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_stmt" ):
                return visitor.visitAssignment_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assignment_stmt(self):

        localctx = PascalParser.Assignment_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_assignment_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self.identifier()
            self.state = 238
            self.match(PascalParser.T__9)
            self.state = 239
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
            return self.getTypedRuleContext(PascalParser.IdentifierContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PascalParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PascalParser.ExpressionContext,i)


        def getRuleIndex(self):
            return PascalParser.RULE_procedure_call

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

        localctx = PascalParser.Procedure_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_procedure_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.identifier()
            self.state = 253
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 242
                self.match(PascalParser.T__1)
                self.state = 243
                self.expression(0)
                self.state = 248
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==3:
                    self.state = 244
                    self.match(PascalParser.T__2)
                    self.state = 245
                    self.expression(0)
                    self.state = 250
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 251
                self.match(PascalParser.T__3)


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
            return self.getToken(PascalParser.IF_K, 0)

        def expression(self):
            return self.getTypedRuleContext(PascalParser.ExpressionContext,0)


        def THEN_K(self):
            return self.getToken(PascalParser.THEN_K, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PascalParser.StatementContext)
            else:
                return self.getTypedRuleContext(PascalParser.StatementContext,i)


        def ELSE_K(self):
            return self.getToken(PascalParser.ELSE_K, 0)

        def getRuleIndex(self):
            return PascalParser.RULE_if_stmt

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

        localctx = PascalParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self.match(PascalParser.IF_K)
            self.state = 256
            self.expression(0)
            self.state = 257
            self.match(PascalParser.THEN_K)
            self.state = 258
            self.statement()
            self.state = 261
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 259
                self.match(PascalParser.ELSE_K)
                self.state = 260
                self.statement()


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
            return self.getToken(PascalParser.FOR_K, 0)

        def identifier(self):
            return self.getTypedRuleContext(PascalParser.IdentifierContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PascalParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PascalParser.ExpressionContext,i)


        def DO_K(self):
            return self.getToken(PascalParser.DO_K, 0)

        def statement(self):
            return self.getTypedRuleContext(PascalParser.StatementContext,0)


        def TO_K(self):
            return self.getToken(PascalParser.TO_K, 0)

        def DOWNTO_K(self):
            return self.getToken(PascalParser.DOWNTO_K, 0)

        def getRuleIndex(self):
            return PascalParser.RULE_for_stmt

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

        localctx = PascalParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_for_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self.match(PascalParser.FOR_K)
            self.state = 264
            self.identifier()
            self.state = 265
            self.match(PascalParser.T__9)
            self.state = 266
            self.expression(0)
            self.state = 267
            _la = self._input.LA(1)
            if not(_la==41 or _la==42):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 268
            self.expression(0)
            self.state = 269
            self.match(PascalParser.DO_K)
            self.state = 270
            self.statement()
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
            return self.getToken(PascalParser.WHILE_K, 0)

        def expression(self):
            return self.getTypedRuleContext(PascalParser.ExpressionContext,0)


        def DO_K(self):
            return self.getToken(PascalParser.DO_K, 0)

        def statement(self):
            return self.getTypedRuleContext(PascalParser.StatementContext,0)


        def getRuleIndex(self):
            return PascalParser.RULE_while_stmt

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

        localctx = PascalParser.While_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.match(PascalParser.WHILE_K)
            self.state = 273
            self.expression(0)
            self.state = 274
            self.match(PascalParser.DO_K)
            self.state = 275
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Repeat_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REPEAT_K(self):
            return self.getToken(PascalParser.REPEAT_K, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PascalParser.StatementContext)
            else:
                return self.getTypedRuleContext(PascalParser.StatementContext,i)


        def UNTIL_K(self):
            return self.getToken(PascalParser.UNTIL_K, 0)

        def expression(self):
            return self.getTypedRuleContext(PascalParser.ExpressionContext,0)


        def getRuleIndex(self):
            return PascalParser.RULE_repeat_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRepeat_stmt" ):
                listener.enterRepeat_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRepeat_stmt" ):
                listener.exitRepeat_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRepeat_stmt" ):
                return visitor.visitRepeat_stmt(self)
            else:
                return visitor.visitChildren(self)




    def repeat_stmt(self):

        localctx = PascalParser.Repeat_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_repeat_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self.match(PascalParser.REPEAT_K)
            self.state = 278
            self.statement()
            self.state = 283
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 279
                self.match(PascalParser.T__4)
                self.state = 280
                self.statement()
                self.state = 285
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 286
            self.match(PascalParser.UNTIL_K)
            self.state = 287
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class With_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WITH_K(self):
            return self.getToken(PascalParser.WITH_K, 0)

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PascalParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(PascalParser.IdentifierContext,i)


        def DO_K(self):
            return self.getToken(PascalParser.DO_K, 0)

        def statement(self):
            return self.getTypedRuleContext(PascalParser.StatementContext,0)


        def getRuleIndex(self):
            return PascalParser.RULE_with_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWith_stmt" ):
                listener.enterWith_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWith_stmt" ):
                listener.exitWith_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWith_stmt" ):
                return visitor.visitWith_stmt(self)
            else:
                return visitor.visitChildren(self)




    def with_stmt(self):

        localctx = PascalParser.With_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_with_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            self.match(PascalParser.WITH_K)
            self.state = 290
            self.identifier()
            self.state = 295
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 291
                self.match(PascalParser.T__2)
                self.state = 292
                self.identifier()
                self.state = 297
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 298
            self.match(PascalParser.DO_K)
            self.state = 299
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

        def NOT(self):
            return self.getToken(PascalParser.NOT, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PascalParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PascalParser.ExpressionContext,i)


        def MINUS(self):
            return self.getToken(PascalParser.MINUS, 0)

        def primary(self):
            return self.getTypedRuleContext(PascalParser.PrimaryContext,0)


        def OR(self):
            return self.getToken(PascalParser.OR, 0)

        def AND(self):
            return self.getToken(PascalParser.AND, 0)

        def EQ(self):
            return self.getToken(PascalParser.EQ, 0)

        def NE(self):
            return self.getToken(PascalParser.NE, 0)

        def LT(self):
            return self.getToken(PascalParser.LT, 0)

        def LE(self):
            return self.getToken(PascalParser.LE, 0)

        def GT(self):
            return self.getToken(PascalParser.GT, 0)

        def GE(self):
            return self.getToken(PascalParser.GE, 0)

        def PLUS(self):
            return self.getToken(PascalParser.PLUS, 0)

        def STAR(self):
            return self.getToken(PascalParser.STAR, 0)

        def SLASH(self):
            return self.getToken(PascalParser.SLASH, 0)

        def DIV(self):
            return self.getToken(PascalParser.DIV, 0)

        def MOD(self):
            return self.getToken(PascalParser.MOD, 0)

        def getRuleIndex(self):
            return PascalParser.RULE_expression

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
        localctx = PascalParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 48
        self.enterRecursionRule(localctx, 48, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 311
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.state = 302
                self.match(PascalParser.NOT)
                self.state = 303
                self.expression(7)
                pass
            elif token in [22]:
                self.state = 304
                self.match(PascalParser.MINUS)
                self.state = 305
                self.expression(3)
                pass
            elif token in [2]:
                self.state = 306
                self.match(PascalParser.T__1)
                self.state = 307
                self.expression(0)
                self.state = 308
                self.match(PascalParser.T__3)
                pass
            elif token in [48, 49, 50, 51, 52, 53]:
                self.state = 310
                self.primary()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 327
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 325
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
                    if la_ == 1:
                        localctx = PascalParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 313
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 314
                        _la = self._input.LA(1)
                        if not(_la==12 or _la==13):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 315
                        self.expression(9)
                        pass

                    elif la_ == 2:
                        localctx = PascalParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 316
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 317
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2064384) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 318
                        self.expression(7)
                        pass

                    elif la_ == 3:
                        localctx = PascalParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 319
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 320
                        _la = self._input.LA(1)
                        if not(_la==21 or _la==22):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 321
                        self.expression(6)
                        pass

                    elif la_ == 4:
                        localctx = PascalParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 322
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 323
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 125829120) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 324
                        self.expression(5)
                        pass

             
                self.state = 329
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

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

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PascalParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(PascalParser.IdentifierContext,i)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PascalParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PascalParser.ExpressionContext,i)


        def literal(self):
            return self.getTypedRuleContext(PascalParser.LiteralContext,0)


        def getRuleIndex(self):
            return PascalParser.RULE_primary

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

        localctx = PascalParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_primary)
        self._la = 0 # Token type
        try:
            self.state = 352
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 330
                self.identifier()
                self.state = 342
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
                if la_ == 1:
                    self.state = 331
                    self.match(PascalParser.T__1)
                    self.state = 332
                    self.expression(0)
                    self.state = 337
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==3:
                        self.state = 333
                        self.match(PascalParser.T__2)
                        self.state = 334
                        self.expression(0)
                        self.state = 339
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 340
                    self.match(PascalParser.T__3)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 344
                self.identifier()
                self.state = 345
                self.match(PascalParser.T__10)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 347
                self.identifier()
                self.state = 348
                self.match(PascalParser.T__0)
                self.state = 349
                self.identifier()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 351
                self.literal()
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

        def integer_literal(self):
            return self.getTypedRuleContext(PascalParser.Integer_literalContext,0)


        def real_literal(self):
            return self.getTypedRuleContext(PascalParser.Real_literalContext,0)


        def string_literal(self):
            return self.getTypedRuleContext(PascalParser.String_literalContext,0)


        def logical_literal(self):
            return self.getTypedRuleContext(PascalParser.Logical_literalContext,0)


        def getRuleIndex(self):
            return PascalParser.RULE_literal

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

        localctx = PascalParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_literal)
        try:
            self.state = 358
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [51]:
                self.enterOuterAlt(localctx, 1)
                self.state = 354
                self.integer_literal()
                pass
            elif token in [52]:
                self.enterOuterAlt(localctx, 2)
                self.state = 355
                self.real_literal()
                pass
            elif token in [53]:
                self.enterOuterAlt(localctx, 3)
                self.state = 356
                self.string_literal()
                pass
            elif token in [48, 49]:
                self.enterOuterAlt(localctx, 4)
                self.state = 357
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


    class IdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(PascalParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return PascalParser.RULE_identifier

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

        localctx = PascalParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 360
            self.match(PascalParser.IDENTIFIER)
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
            return self.getToken(PascalParser.INTEGER, 0)

        def getRuleIndex(self):
            return PascalParser.RULE_integer_literal

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

        localctx = PascalParser.Integer_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_integer_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 362
            self.match(PascalParser.INTEGER)
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
            return self.getToken(PascalParser.REAL, 0)

        def getRuleIndex(self):
            return PascalParser.RULE_real_literal

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

        localctx = PascalParser.Real_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_real_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 364
            self.match(PascalParser.REAL)
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
            return self.getToken(PascalParser.STRING, 0)

        def getRuleIndex(self):
            return PascalParser.RULE_string_literal

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

        localctx = PascalParser.String_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_string_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 366
            self.match(PascalParser.STRING)
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
            return self.getToken(PascalParser.TRUE_K, 0)

        def FALSE_K(self):
            return self.getToken(PascalParser.FALSE_K, 0)

        def getRuleIndex(self):
            return PascalParser.RULE_logical_literal

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

        localctx = PascalParser.Logical_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_logical_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 368
            _la = self._input.LA(1)
            if not(_la==48 or _la==49):
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
        self._predicates[24] = self.expression_sempred
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
         




