# Generated from rosetta/babel/fortran/grammar/Fortran.g4 by ANTLR 4.13.2
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
        4,1,59,613,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,1,0,1,0,1,0,5,0,86,8,0,10,0,12,0,89,9,0,1,0,1,0,1,1,1,
        1,3,1,95,8,1,1,2,3,2,98,8,2,1,2,3,2,101,8,2,1,2,3,2,104,8,2,1,2,
        1,2,1,3,1,3,3,3,110,8,3,1,3,3,3,113,8,3,1,3,1,3,1,4,1,4,3,4,119,
        8,4,1,4,3,4,122,8,4,1,4,1,4,1,5,1,5,1,5,4,5,129,8,5,11,5,12,5,130,
        1,6,1,6,1,6,1,6,1,6,1,6,5,6,139,8,6,10,6,12,6,142,9,6,3,6,144,8,
        6,1,6,3,6,147,8,6,1,6,4,6,150,8,6,11,6,12,6,151,1,7,3,7,155,8,7,
        1,7,1,7,1,7,1,7,1,7,1,7,5,7,163,8,7,10,7,12,7,166,9,7,3,7,168,8,
        7,1,7,1,7,4,7,172,8,7,11,7,12,7,173,1,8,1,8,3,8,178,8,8,1,8,3,8,
        181,8,8,1,8,5,8,184,8,8,10,8,12,8,187,9,8,1,9,4,9,190,8,9,11,9,12,
        9,191,1,10,1,10,4,10,196,8,10,11,10,12,10,197,1,10,1,10,4,10,202,
        8,10,11,10,12,10,203,1,10,1,10,4,10,208,8,10,11,10,12,10,209,1,10,
        1,10,4,10,214,8,10,11,10,12,10,215,3,10,218,8,10,1,11,1,11,3,11,
        222,8,11,1,11,1,11,1,11,5,11,227,8,11,10,11,12,11,230,9,11,1,12,
        1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,3,12,244,
        8,12,1,12,1,12,3,12,248,8,12,1,12,3,12,251,8,12,3,12,253,8,12,1,
        13,1,13,1,13,1,13,1,13,3,13,260,8,13,1,13,1,13,3,13,264,8,13,1,14,
        1,14,1,14,5,14,269,8,14,10,14,12,14,272,9,14,1,15,1,15,1,15,3,15,
        277,8,15,1,15,1,15,3,15,281,8,15,1,16,1,16,1,16,1,17,1,17,1,17,1,
        17,1,17,3,17,291,8,17,1,17,1,17,1,17,5,17,296,8,17,10,17,12,17,299,
        9,17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,5,18,
        312,8,18,10,18,12,18,315,9,18,1,19,4,19,318,8,19,11,19,12,19,319,
        1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,3,20,
        334,8,20,1,20,4,20,337,8,20,11,20,12,20,338,1,21,1,21,1,21,1,21,
        1,21,1,21,1,21,1,21,3,21,349,8,21,1,22,1,22,1,22,1,22,1,22,5,22,
        356,8,22,10,22,12,22,359,9,22,1,22,1,22,3,22,363,8,22,1,22,1,22,
        1,22,1,23,1,23,1,23,1,23,1,23,1,23,4,23,374,8,23,11,23,12,23,375,
        1,23,3,23,379,8,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,4,23,388,8,
        23,11,23,12,23,389,1,23,3,23,393,8,23,5,23,395,8,23,10,23,12,23,
        398,9,23,1,23,1,23,4,23,402,8,23,11,23,12,23,403,1,23,3,23,407,8,
        23,3,23,409,8,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,3,
        23,420,8,23,1,24,1,24,3,24,424,8,24,1,24,1,24,1,24,1,24,1,24,1,24,
        1,24,3,24,433,8,24,3,24,435,8,24,1,24,4,24,438,8,24,11,24,12,24,
        439,1,24,3,24,443,8,24,1,24,1,24,1,24,1,25,1,25,1,25,1,26,1,26,1,
        26,1,26,1,26,1,26,5,26,457,8,26,10,26,12,26,460,9,26,3,26,462,8,
        26,1,26,3,26,465,8,26,1,27,1,27,1,28,1,28,1,28,1,28,3,28,473,8,28,
        1,28,1,28,1,28,1,28,3,28,479,8,28,1,28,1,28,1,28,1,28,5,28,485,8,
        28,10,28,12,28,488,9,28,3,28,490,8,28,1,29,1,29,1,29,1,29,1,29,1,
        29,5,29,498,8,29,10,29,12,29,501,9,29,3,29,503,8,29,1,30,1,30,1,
        30,1,30,1,30,1,30,5,30,511,8,30,10,30,12,30,514,9,30,3,30,516,8,
        30,1,30,1,30,1,31,1,31,1,31,1,31,1,31,1,31,1,31,3,31,527,8,31,1,
        31,1,31,3,31,531,8,31,1,31,1,31,1,31,1,31,5,31,537,8,31,10,31,12,
        31,540,9,31,1,31,1,31,3,31,544,8,31,1,32,1,32,1,33,1,33,1,34,1,34,
        1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,3,34,560,8,34,1,34,1,34,
        1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,
        5,34,577,8,34,10,34,12,34,580,9,34,1,35,1,35,1,35,1,35,1,35,5,35,
        587,8,35,10,35,12,35,590,9,35,1,35,1,35,3,35,594,8,35,1,35,3,35,
        597,8,35,1,36,1,36,1,36,1,36,3,36,603,8,36,1,37,1,37,1,38,1,38,1,
        39,1,39,1,40,1,40,1,40,0,1,68,41,0,2,4,6,8,10,12,14,16,18,20,22,
        24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,
        68,70,72,74,76,78,80,0,6,1,0,24,26,1,0,10,11,1,0,13,18,1,0,19,20,
        1,0,21,22,1,0,8,9,689,0,87,1,0,0,0,2,94,1,0,0,0,4,97,1,0,0,0,6,107,
        1,0,0,0,8,116,1,0,0,0,10,125,1,0,0,0,12,132,1,0,0,0,14,154,1,0,0,
        0,16,175,1,0,0,0,18,189,1,0,0,0,20,217,1,0,0,0,22,219,1,0,0,0,24,
        252,1,0,0,0,26,254,1,0,0,0,28,265,1,0,0,0,30,280,1,0,0,0,32,282,
        1,0,0,0,34,285,1,0,0,0,36,300,1,0,0,0,38,317,1,0,0,0,40,333,1,0,
        0,0,42,348,1,0,0,0,44,350,1,0,0,0,46,419,1,0,0,0,48,421,1,0,0,0,
        50,447,1,0,0,0,52,450,1,0,0,0,54,466,1,0,0,0,56,468,1,0,0,0,58,491,
        1,0,0,0,60,504,1,0,0,0,62,543,1,0,0,0,64,545,1,0,0,0,66,547,1,0,
        0,0,68,559,1,0,0,0,70,596,1,0,0,0,72,602,1,0,0,0,74,604,1,0,0,0,
        76,606,1,0,0,0,78,608,1,0,0,0,80,610,1,0,0,0,82,86,3,2,1,0,83,86,
        3,4,2,0,84,86,5,56,0,0,85,82,1,0,0,0,85,83,1,0,0,0,85,84,1,0,0,0,
        86,89,1,0,0,0,87,85,1,0,0,0,87,88,1,0,0,0,88,90,1,0,0,0,89,87,1,
        0,0,0,90,91,5,0,0,1,91,1,1,0,0,0,92,95,3,6,3,0,93,95,3,8,4,0,94,
        92,1,0,0,0,94,93,1,0,0,0,95,3,1,0,0,0,96,98,3,10,5,0,97,96,1,0,0,
        0,97,98,1,0,0,0,98,100,1,0,0,0,99,101,3,18,9,0,100,99,1,0,0,0,100,
        101,1,0,0,0,101,103,1,0,0,0,102,104,3,38,19,0,103,102,1,0,0,0,103,
        104,1,0,0,0,104,105,1,0,0,0,105,106,3,16,8,0,106,5,1,0,0,0,107,109,
        3,12,6,0,108,110,3,18,9,0,109,108,1,0,0,0,109,110,1,0,0,0,110,112,
        1,0,0,0,111,113,3,38,19,0,112,111,1,0,0,0,112,113,1,0,0,0,113,114,
        1,0,0,0,114,115,3,16,8,0,115,7,1,0,0,0,116,118,3,14,7,0,117,119,
        3,18,9,0,118,117,1,0,0,0,118,119,1,0,0,0,119,121,1,0,0,0,120,122,
        3,38,19,0,121,120,1,0,0,0,121,122,1,0,0,0,122,123,1,0,0,0,123,124,
        3,16,8,0,124,9,1,0,0,0,125,126,5,24,0,0,126,128,3,66,33,0,127,129,
        5,56,0,0,128,127,1,0,0,0,129,130,1,0,0,0,130,128,1,0,0,0,130,131,
        1,0,0,0,131,11,1,0,0,0,132,133,5,25,0,0,133,146,3,66,33,0,134,143,
        5,1,0,0,135,140,3,66,33,0,136,137,5,2,0,0,137,139,3,66,33,0,138,
        136,1,0,0,0,139,142,1,0,0,0,140,138,1,0,0,0,140,141,1,0,0,0,141,
        144,1,0,0,0,142,140,1,0,0,0,143,135,1,0,0,0,143,144,1,0,0,0,144,
        145,1,0,0,0,145,147,5,3,0,0,146,134,1,0,0,0,146,147,1,0,0,0,147,
        149,1,0,0,0,148,150,5,56,0,0,149,148,1,0,0,0,150,151,1,0,0,0,151,
        149,1,0,0,0,151,152,1,0,0,0,152,13,1,0,0,0,153,155,3,24,12,0,154,
        153,1,0,0,0,154,155,1,0,0,0,155,156,1,0,0,0,156,157,5,26,0,0,157,
        158,3,66,33,0,158,167,5,1,0,0,159,164,3,66,33,0,160,161,5,2,0,0,
        161,163,3,66,33,0,162,160,1,0,0,0,163,166,1,0,0,0,164,162,1,0,0,
        0,164,165,1,0,0,0,165,168,1,0,0,0,166,164,1,0,0,0,167,159,1,0,0,
        0,167,168,1,0,0,0,168,169,1,0,0,0,169,171,5,3,0,0,170,172,5,56,0,
        0,171,170,1,0,0,0,172,173,1,0,0,0,173,171,1,0,0,0,173,174,1,0,0,
        0,174,15,1,0,0,0,175,177,5,27,0,0,176,178,7,0,0,0,177,176,1,0,0,
        0,177,178,1,0,0,0,178,180,1,0,0,0,179,181,3,66,33,0,180,179,1,0,
        0,0,180,181,1,0,0,0,181,185,1,0,0,0,182,184,5,56,0,0,183,182,1,0,
        0,0,184,187,1,0,0,0,185,183,1,0,0,0,185,186,1,0,0,0,186,17,1,0,0,
        0,187,185,1,0,0,0,188,190,3,20,10,0,189,188,1,0,0,0,190,191,1,0,
        0,0,191,189,1,0,0,0,191,192,1,0,0,0,192,19,1,0,0,0,193,195,3,22,
        11,0,194,196,5,56,0,0,195,194,1,0,0,0,196,197,1,0,0,0,197,195,1,
        0,0,0,197,198,1,0,0,0,198,218,1,0,0,0,199,201,3,32,16,0,200,202,
        5,56,0,0,201,200,1,0,0,0,202,203,1,0,0,0,203,201,1,0,0,0,203,204,
        1,0,0,0,204,218,1,0,0,0,205,207,3,34,17,0,206,208,5,56,0,0,207,206,
        1,0,0,0,208,209,1,0,0,0,209,207,1,0,0,0,209,210,1,0,0,0,210,218,
        1,0,0,0,211,213,3,36,18,0,212,214,5,56,0,0,213,212,1,0,0,0,214,215,
        1,0,0,0,215,213,1,0,0,0,215,216,1,0,0,0,216,218,1,0,0,0,217,193,
        1,0,0,0,217,199,1,0,0,0,217,205,1,0,0,0,217,211,1,0,0,0,218,21,1,
        0,0,0,219,221,3,24,12,0,220,222,5,4,0,0,221,220,1,0,0,0,221,222,
        1,0,0,0,222,223,1,0,0,0,223,228,3,26,13,0,224,225,5,2,0,0,225,227,
        3,26,13,0,226,224,1,0,0,0,227,230,1,0,0,0,228,226,1,0,0,0,228,229,
        1,0,0,0,229,23,1,0,0,0,230,228,1,0,0,0,231,253,5,28,0,0,232,253,
        5,29,0,0,233,234,5,30,0,0,234,253,5,31,0,0,235,253,5,32,0,0,236,
        253,5,33,0,0,237,250,5,34,0,0,238,239,5,21,0,0,239,251,3,74,37,0,
        240,243,5,1,0,0,241,242,5,35,0,0,242,244,5,5,0,0,243,241,1,0,0,0,
        243,244,1,0,0,0,244,247,1,0,0,0,245,248,3,74,37,0,246,248,5,21,0,
        0,247,245,1,0,0,0,247,246,1,0,0,0,248,249,1,0,0,0,249,251,5,3,0,
        0,250,238,1,0,0,0,250,240,1,0,0,0,250,251,1,0,0,0,251,253,1,0,0,
        0,252,231,1,0,0,0,252,232,1,0,0,0,252,233,1,0,0,0,252,235,1,0,0,
        0,252,236,1,0,0,0,252,237,1,0,0,0,253,25,1,0,0,0,254,259,3,66,33,
        0,255,256,5,1,0,0,256,257,3,28,14,0,257,258,5,3,0,0,258,260,1,0,
        0,0,259,255,1,0,0,0,259,260,1,0,0,0,260,263,1,0,0,0,261,262,5,5,
        0,0,262,264,3,68,34,0,263,261,1,0,0,0,263,264,1,0,0,0,264,27,1,0,
        0,0,265,270,3,30,15,0,266,267,5,2,0,0,267,269,3,30,15,0,268,266,
        1,0,0,0,269,272,1,0,0,0,270,268,1,0,0,0,270,271,1,0,0,0,271,29,1,
        0,0,0,272,270,1,0,0,0,273,274,3,68,34,0,274,275,5,6,0,0,275,277,
        1,0,0,0,276,273,1,0,0,0,276,277,1,0,0,0,277,278,1,0,0,0,278,281,
        3,68,34,0,279,281,5,21,0,0,280,276,1,0,0,0,280,279,1,0,0,0,281,31,
        1,0,0,0,282,283,5,36,0,0,283,284,5,37,0,0,284,33,1,0,0,0,285,290,
        5,38,0,0,286,287,5,22,0,0,287,288,3,66,33,0,288,289,5,22,0,0,289,
        291,1,0,0,0,290,286,1,0,0,0,290,291,1,0,0,0,291,292,1,0,0,0,292,
        297,3,66,33,0,293,294,5,2,0,0,294,296,3,66,33,0,295,293,1,0,0,0,
        296,299,1,0,0,0,297,295,1,0,0,0,297,298,1,0,0,0,298,35,1,0,0,0,299,
        297,1,0,0,0,300,301,5,39,0,0,301,302,3,66,33,0,302,303,5,1,0,0,303,
        304,3,28,14,0,304,313,5,3,0,0,305,306,5,2,0,0,306,307,3,66,33,0,
        307,308,5,1,0,0,308,309,3,28,14,0,309,310,5,3,0,0,310,312,1,0,0,
        0,311,305,1,0,0,0,312,315,1,0,0,0,313,311,1,0,0,0,313,314,1,0,0,
        0,314,37,1,0,0,0,315,313,1,0,0,0,316,318,3,40,20,0,317,316,1,0,0,
        0,318,319,1,0,0,0,319,317,1,0,0,0,319,320,1,0,0,0,320,39,1,0,0,0,
        321,334,3,44,22,0,322,334,3,46,23,0,323,334,3,48,24,0,324,334,3,
        50,25,0,325,334,3,52,26,0,326,334,3,56,28,0,327,334,3,58,29,0,328,
        334,3,60,30,0,329,330,3,64,32,0,330,331,3,42,21,0,331,334,1,0,0,
        0,332,334,3,42,21,0,333,321,1,0,0,0,333,322,1,0,0,0,333,323,1,0,
        0,0,333,324,1,0,0,0,333,325,1,0,0,0,333,326,1,0,0,0,333,327,1,0,
        0,0,333,328,1,0,0,0,333,329,1,0,0,0,333,332,1,0,0,0,334,336,1,0,
        0,0,335,337,5,56,0,0,336,335,1,0,0,0,337,338,1,0,0,0,338,336,1,0,
        0,0,338,339,1,0,0,0,339,41,1,0,0,0,340,349,3,44,22,0,341,349,3,50,
        25,0,342,349,3,52,26,0,343,349,3,56,28,0,344,349,3,58,29,0,345,349,
        3,54,27,0,346,349,5,49,0,0,347,349,5,50,0,0,348,340,1,0,0,0,348,
        341,1,0,0,0,348,342,1,0,0,0,348,343,1,0,0,0,348,344,1,0,0,0,348,
        345,1,0,0,0,348,346,1,0,0,0,348,347,1,0,0,0,349,43,1,0,0,0,350,362,
        3,66,33,0,351,352,5,1,0,0,352,357,3,68,34,0,353,354,5,2,0,0,354,
        356,3,68,34,0,355,353,1,0,0,0,356,359,1,0,0,0,357,355,1,0,0,0,357,
        358,1,0,0,0,358,360,1,0,0,0,359,357,1,0,0,0,360,361,5,3,0,0,361,
        363,1,0,0,0,362,351,1,0,0,0,362,363,1,0,0,0,363,364,1,0,0,0,364,
        365,5,5,0,0,365,366,3,68,34,0,366,45,1,0,0,0,367,368,5,40,0,0,368,
        369,5,1,0,0,369,370,3,68,34,0,370,371,5,3,0,0,371,373,5,41,0,0,372,
        374,5,56,0,0,373,372,1,0,0,0,374,375,1,0,0,0,375,373,1,0,0,0,375,
        376,1,0,0,0,376,378,1,0,0,0,377,379,3,38,19,0,378,377,1,0,0,0,378,
        379,1,0,0,0,379,396,1,0,0,0,380,381,5,42,0,0,381,382,5,40,0,0,382,
        383,5,1,0,0,383,384,3,68,34,0,384,385,5,3,0,0,385,387,5,41,0,0,386,
        388,5,56,0,0,387,386,1,0,0,0,388,389,1,0,0,0,389,387,1,0,0,0,389,
        390,1,0,0,0,390,392,1,0,0,0,391,393,3,38,19,0,392,391,1,0,0,0,392,
        393,1,0,0,0,393,395,1,0,0,0,394,380,1,0,0,0,395,398,1,0,0,0,396,
        394,1,0,0,0,396,397,1,0,0,0,397,408,1,0,0,0,398,396,1,0,0,0,399,
        401,5,42,0,0,400,402,5,56,0,0,401,400,1,0,0,0,402,403,1,0,0,0,403,
        401,1,0,0,0,403,404,1,0,0,0,404,406,1,0,0,0,405,407,3,38,19,0,406,
        405,1,0,0,0,406,407,1,0,0,0,407,409,1,0,0,0,408,399,1,0,0,0,408,
        409,1,0,0,0,409,410,1,0,0,0,410,411,5,27,0,0,411,412,5,40,0,0,412,
        420,1,0,0,0,413,414,5,40,0,0,414,415,5,1,0,0,415,416,3,68,34,0,416,
        417,5,3,0,0,417,418,3,42,21,0,418,420,1,0,0,0,419,367,1,0,0,0,419,
        413,1,0,0,0,420,47,1,0,0,0,421,423,5,43,0,0,422,424,3,64,32,0,423,
        422,1,0,0,0,423,424,1,0,0,0,424,434,1,0,0,0,425,426,3,66,33,0,426,
        427,5,5,0,0,427,428,3,68,34,0,428,429,5,2,0,0,429,432,3,68,34,0,
        430,431,5,2,0,0,431,433,3,68,34,0,432,430,1,0,0,0,432,433,1,0,0,
        0,433,435,1,0,0,0,434,425,1,0,0,0,434,435,1,0,0,0,435,437,1,0,0,
        0,436,438,5,56,0,0,437,436,1,0,0,0,438,439,1,0,0,0,439,437,1,0,0,
        0,439,440,1,0,0,0,440,442,1,0,0,0,441,443,3,38,19,0,442,441,1,0,
        0,0,442,443,1,0,0,0,443,444,1,0,0,0,444,445,5,27,0,0,445,446,5,43,
        0,0,446,49,1,0,0,0,447,448,5,44,0,0,448,449,3,64,32,0,449,51,1,0,
        0,0,450,451,5,45,0,0,451,464,3,66,33,0,452,461,5,1,0,0,453,458,3,
        68,34,0,454,455,5,2,0,0,455,457,3,68,34,0,456,454,1,0,0,0,457,460,
        1,0,0,0,458,456,1,0,0,0,458,459,1,0,0,0,459,462,1,0,0,0,460,458,
        1,0,0,0,461,453,1,0,0,0,461,462,1,0,0,0,462,463,1,0,0,0,463,465,
        5,3,0,0,464,452,1,0,0,0,464,465,1,0,0,0,465,53,1,0,0,0,466,467,5,
        46,0,0,467,55,1,0,0,0,468,469,5,47,0,0,469,472,5,1,0,0,470,473,3,
        66,33,0,471,473,5,21,0,0,472,470,1,0,0,0,472,471,1,0,0,0,473,474,
        1,0,0,0,474,478,5,2,0,0,475,479,3,66,33,0,476,479,3,64,32,0,477,
        479,5,21,0,0,478,475,1,0,0,0,478,476,1,0,0,0,478,477,1,0,0,0,479,
        480,1,0,0,0,480,489,5,3,0,0,481,486,3,68,34,0,482,483,5,2,0,0,483,
        485,3,68,34,0,484,482,1,0,0,0,485,488,1,0,0,0,486,484,1,0,0,0,486,
        487,1,0,0,0,487,490,1,0,0,0,488,486,1,0,0,0,489,481,1,0,0,0,489,
        490,1,0,0,0,490,57,1,0,0,0,491,492,5,48,0,0,492,502,5,21,0,0,493,
        494,5,2,0,0,494,499,3,68,34,0,495,496,5,2,0,0,496,498,3,68,34,0,
        497,495,1,0,0,0,498,501,1,0,0,0,499,497,1,0,0,0,499,500,1,0,0,0,
        500,503,1,0,0,0,501,499,1,0,0,0,502,493,1,0,0,0,502,503,1,0,0,0,
        503,59,1,0,0,0,504,505,3,64,32,0,505,506,5,51,0,0,506,515,5,1,0,
        0,507,512,3,62,31,0,508,509,5,2,0,0,509,511,3,62,31,0,510,508,1,
        0,0,0,511,514,1,0,0,0,512,510,1,0,0,0,512,513,1,0,0,0,513,516,1,
        0,0,0,514,512,1,0,0,0,515,507,1,0,0,0,515,516,1,0,0,0,516,517,1,
        0,0,0,517,518,5,3,0,0,518,61,1,0,0,0,519,544,3,66,33,0,520,544,3,
        78,39,0,521,544,3,74,37,0,522,544,3,76,38,0,523,526,3,66,33,0,524,
        527,3,74,37,0,525,527,3,76,38,0,526,524,1,0,0,0,526,525,1,0,0,0,
        527,530,1,0,0,0,528,529,5,7,0,0,529,531,3,74,37,0,530,528,1,0,0,
        0,530,531,1,0,0,0,531,544,1,0,0,0,532,533,5,1,0,0,533,538,3,62,31,
        0,534,535,5,2,0,0,535,537,3,62,31,0,536,534,1,0,0,0,537,540,1,0,
        0,0,538,536,1,0,0,0,538,539,1,0,0,0,539,541,1,0,0,0,540,538,1,0,
        0,0,541,542,5,3,0,0,542,544,1,0,0,0,543,519,1,0,0,0,543,520,1,0,
        0,0,543,521,1,0,0,0,543,522,1,0,0,0,543,523,1,0,0,0,543,532,1,0,
        0,0,544,63,1,0,0,0,545,546,5,53,0,0,546,65,1,0,0,0,547,548,5,52,
        0,0,548,67,1,0,0,0,549,550,6,34,-1,0,550,551,5,12,0,0,551,560,3,
        68,34,8,552,553,5,20,0,0,553,560,3,68,34,3,554,555,5,1,0,0,555,556,
        3,68,34,0,556,557,5,3,0,0,557,560,1,0,0,0,558,560,3,70,35,0,559,
        549,1,0,0,0,559,552,1,0,0,0,559,554,1,0,0,0,559,558,1,0,0,0,560,
        578,1,0,0,0,561,562,10,9,0,0,562,563,7,1,0,0,563,577,3,68,34,10,
        564,565,10,7,0,0,565,566,7,2,0,0,566,577,3,68,34,8,567,568,10,6,
        0,0,568,569,7,3,0,0,569,577,3,68,34,7,570,571,10,5,0,0,571,572,7,
        4,0,0,572,577,3,68,34,6,573,574,10,4,0,0,574,575,5,23,0,0,575,577,
        3,68,34,5,576,561,1,0,0,0,576,564,1,0,0,0,576,567,1,0,0,0,576,570,
        1,0,0,0,576,573,1,0,0,0,577,580,1,0,0,0,578,576,1,0,0,0,578,579,
        1,0,0,0,579,69,1,0,0,0,580,578,1,0,0,0,581,593,3,66,33,0,582,583,
        5,1,0,0,583,588,3,68,34,0,584,585,5,2,0,0,585,587,3,68,34,0,586,
        584,1,0,0,0,587,590,1,0,0,0,588,586,1,0,0,0,588,589,1,0,0,0,589,
        591,1,0,0,0,590,588,1,0,0,0,591,592,5,3,0,0,592,594,1,0,0,0,593,
        582,1,0,0,0,593,594,1,0,0,0,594,597,1,0,0,0,595,597,3,72,36,0,596,
        581,1,0,0,0,596,595,1,0,0,0,597,71,1,0,0,0,598,603,3,74,37,0,599,
        603,3,76,38,0,600,603,3,78,39,0,601,603,3,80,40,0,602,598,1,0,0,
        0,602,599,1,0,0,0,602,600,1,0,0,0,602,601,1,0,0,0,603,73,1,0,0,0,
        604,605,5,53,0,0,605,75,1,0,0,0,606,607,5,54,0,0,607,77,1,0,0,0,
        608,609,5,55,0,0,609,79,1,0,0,0,610,611,7,5,0,0,611,81,1,0,0,0,84,
        85,87,94,97,100,103,109,112,118,121,130,140,143,146,151,154,164,
        167,173,177,180,185,191,197,203,209,215,217,221,228,243,247,250,
        252,259,263,270,276,280,290,297,313,319,333,338,348,357,362,375,
        378,389,392,396,403,406,408,419,423,432,434,439,442,458,461,464,
        472,478,486,489,499,502,512,515,526,530,538,543,559,576,578,588,
        593,596,602
    ]

class FortranParser ( Parser ):

    grammarFileName = "Fortran.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "','", "')'", "'::'", "'='", "':'", 
                     "'.'", "'.TRUE.'", "'.FALSE.'", "'.OR.'", "'.AND.'", 
                     "'.NOT.'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'+'", "'-'", "'*'", "'/'", 
                     "'**'", "'PROGRAM'", "'SUBROUTINE'", "'FUNCTION'", 
                     "'END'", "'INTEGER'", "'REAL'", "'DOUBLE'", "'PRECISION'", 
                     "'COMPLEX'", "'LOGICAL'", "'CHARACTER'", "'LEN'", "'IMPLICIT'", 
                     "'NONE'", "'COMMON'", "'DIMENSION'", "'IF'", "'THEN'", 
                     "'ELSE'", "'DO'", "'GOTO'", "'CALL'", "'RETURN'", "'WRITE'", 
                     "'PRINT'", "'CONTINUE'", "'STOP'", "'FORMAT'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "OR", "AND", "NOT", "EQ", 
                      "NE", "LT", "LE", "GT", "GE", "PLUS", "MINUS", "STAR", 
                      "SLASH", "POWER", "PROGRAM_K", "SUBROUTINE_K", "FUNCTION_K", 
                      "END_K", "INTEGER_K", "REAL_K", "DOUBLE_K", "PRECISION_K", 
                      "COMPLEX_K", "LOGICAL_K", "CHARACTER_K", "LEN_K", 
                      "IMPLICIT_K", "NONE_K", "COMMON_K", "DIMENSION_K", 
                      "IF_K", "THEN_K", "ELSE_K", "DO_K", "GOTO_K", "CALL_K", 
                      "RETURN_K", "WRITE_K", "PRINT_K", "CONTINUE_K", "STOP_K", 
                      "FORMAT_K", "IDENTIFIER", "INTEGER", "REAL", "STRING", 
                      "NEWLINE", "WS", "COMMENT", "LINE_COMMENT" ]

    RULE_program = 0
    RULE_executable_unit = 1
    RULE_main_program = 2
    RULE_subroutine_def = 3
    RULE_function_def = 4
    RULE_program_stmt = 5
    RULE_subroutine_stmt = 6
    RULE_function_stmt = 7
    RULE_end_stmt = 8
    RULE_specification_part = 9
    RULE_specification_stmt = 10
    RULE_type_declaration_stmt = 11
    RULE_type_spec = 12
    RULE_entity_decl = 13
    RULE_array_spec = 14
    RULE_dimension = 15
    RULE_implicit_none_stmt = 16
    RULE_common_stmt = 17
    RULE_dimension_stmt = 18
    RULE_execution_part = 19
    RULE_executable_stmt = 20
    RULE_action_stmt = 21
    RULE_assignment_stmt = 22
    RULE_if_stmt = 23
    RULE_do_stmt = 24
    RULE_goto_stmt = 25
    RULE_call_stmt = 26
    RULE_return_stmt = 27
    RULE_write_stmt = 28
    RULE_print_stmt = 29
    RULE_format_stmt = 30
    RULE_format_item = 31
    RULE_label = 32
    RULE_identifier = 33
    RULE_expression = 34
    RULE_primary = 35
    RULE_literal = 36
    RULE_integer_literal = 37
    RULE_real_literal = 38
    RULE_string_literal = 39
    RULE_logical_literal = 40

    ruleNames =  [ "program", "executable_unit", "main_program", "subroutine_def", 
                   "function_def", "program_stmt", "subroutine_stmt", "function_stmt", 
                   "end_stmt", "specification_part", "specification_stmt", 
                   "type_declaration_stmt", "type_spec", "entity_decl", 
                   "array_spec", "dimension", "implicit_none_stmt", "common_stmt", 
                   "dimension_stmt", "execution_part", "executable_stmt", 
                   "action_stmt", "assignment_stmt", "if_stmt", "do_stmt", 
                   "goto_stmt", "call_stmt", "return_stmt", "write_stmt", 
                   "print_stmt", "format_stmt", "format_item", "label", 
                   "identifier", "expression", "primary", "literal", "integer_literal", 
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
    OR=10
    AND=11
    NOT=12
    EQ=13
    NE=14
    LT=15
    LE=16
    GT=17
    GE=18
    PLUS=19
    MINUS=20
    STAR=21
    SLASH=22
    POWER=23
    PROGRAM_K=24
    SUBROUTINE_K=25
    FUNCTION_K=26
    END_K=27
    INTEGER_K=28
    REAL_K=29
    DOUBLE_K=30
    PRECISION_K=31
    COMPLEX_K=32
    LOGICAL_K=33
    CHARACTER_K=34
    LEN_K=35
    IMPLICIT_K=36
    NONE_K=37
    COMMON_K=38
    DIMENSION_K=39
    IF_K=40
    THEN_K=41
    ELSE_K=42
    DO_K=43
    GOTO_K=44
    CALL_K=45
    RETURN_K=46
    WRITE_K=47
    PRINT_K=48
    CONTINUE_K=49
    STOP_K=50
    FORMAT_K=51
    IDENTIFIER=52
    INTEGER=53
    REAL=54
    STRING=55
    NEWLINE=56
    WS=57
    COMMENT=58
    LINE_COMMENT=59

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
            return self.getToken(FortranParser.EOF, 0)

        def executable_unit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FortranParser.Executable_unitContext)
            else:
                return self.getTypedRuleContext(FortranParser.Executable_unitContext,i)


        def main_program(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FortranParser.Main_programContext)
            else:
                return self.getTypedRuleContext(FortranParser.Main_programContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(FortranParser.NEWLINE)
            else:
                return self.getToken(FortranParser.NEWLINE, i)

        def getRuleIndex(self):
            return FortranParser.RULE_program

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

        localctx = FortranParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 87813421701005312) != 0):
                self.state = 85
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 82
                    self.executable_unit()
                    pass

                elif la_ == 2:
                    self.state = 83
                    self.main_program()
                    pass

                elif la_ == 3:
                    self.state = 84
                    self.match(FortranParser.NEWLINE)
                    pass


                self.state = 89
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 90
            self.match(FortranParser.EOF)
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

        def subroutine_def(self):
            return self.getTypedRuleContext(FortranParser.Subroutine_defContext,0)


        def function_def(self):
            return self.getTypedRuleContext(FortranParser.Function_defContext,0)


        def getRuleIndex(self):
            return FortranParser.RULE_executable_unit

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

        localctx = FortranParser.Executable_unitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_executable_unit)
        try:
            self.state = 94
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25]:
                self.enterOuterAlt(localctx, 1)
                self.state = 92
                self.subroutine_def()
                pass
            elif token in [26, 28, 29, 30, 32, 33, 34]:
                self.enterOuterAlt(localctx, 2)
                self.state = 93
                self.function_def()
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


    class Main_programContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def end_stmt(self):
            return self.getTypedRuleContext(FortranParser.End_stmtContext,0)


        def program_stmt(self):
            return self.getTypedRuleContext(FortranParser.Program_stmtContext,0)


        def specification_part(self):
            return self.getTypedRuleContext(FortranParser.Specification_partContext,0)


        def execution_part(self):
            return self.getTypedRuleContext(FortranParser.Execution_partContext,0)


        def getRuleIndex(self):
            return FortranParser.RULE_main_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMain_program" ):
                listener.enterMain_program(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMain_program" ):
                listener.exitMain_program(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMain_program" ):
                return visitor.visitMain_program(self)
            else:
                return visitor.visitChildren(self)




    def main_program(self):

        localctx = FortranParser.Main_programContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_main_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==24:
                self.state = 96
                self.program_stmt()


            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 925297016832) != 0):
                self.state = 99
                self.specification_part()


            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 15754902114402304) != 0):
                self.state = 102
                self.execution_part()


            self.state = 105
            self.end_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Subroutine_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def subroutine_stmt(self):
            return self.getTypedRuleContext(FortranParser.Subroutine_stmtContext,0)


        def end_stmt(self):
            return self.getTypedRuleContext(FortranParser.End_stmtContext,0)


        def specification_part(self):
            return self.getTypedRuleContext(FortranParser.Specification_partContext,0)


        def execution_part(self):
            return self.getTypedRuleContext(FortranParser.Execution_partContext,0)


        def getRuleIndex(self):
            return FortranParser.RULE_subroutine_def

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubroutine_def" ):
                listener.enterSubroutine_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubroutine_def" ):
                listener.exitSubroutine_def(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubroutine_def" ):
                return visitor.visitSubroutine_def(self)
            else:
                return visitor.visitChildren(self)




    def subroutine_def(self):

        localctx = FortranParser.Subroutine_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_subroutine_def)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.subroutine_stmt()
            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 925297016832) != 0):
                self.state = 108
                self.specification_part()


            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 15754902114402304) != 0):
                self.state = 111
                self.execution_part()


            self.state = 114
            self.end_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_stmt(self):
            return self.getTypedRuleContext(FortranParser.Function_stmtContext,0)


        def end_stmt(self):
            return self.getTypedRuleContext(FortranParser.End_stmtContext,0)


        def specification_part(self):
            return self.getTypedRuleContext(FortranParser.Specification_partContext,0)


        def execution_part(self):
            return self.getTypedRuleContext(FortranParser.Execution_partContext,0)


        def getRuleIndex(self):
            return FortranParser.RULE_function_def

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_def" ):
                listener.enterFunction_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_def" ):
                listener.exitFunction_def(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_def" ):
                return visitor.visitFunction_def(self)
            else:
                return visitor.visitChildren(self)




    def function_def(self):

        localctx = FortranParser.Function_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_function_def)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.function_stmt()
            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 925297016832) != 0):
                self.state = 117
                self.specification_part()


            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 15754902114402304) != 0):
                self.state = 120
                self.execution_part()


            self.state = 123
            self.end_stmt()
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
            return self.getToken(FortranParser.PROGRAM_K, 0)

        def identifier(self):
            return self.getTypedRuleContext(FortranParser.IdentifierContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(FortranParser.NEWLINE)
            else:
                return self.getToken(FortranParser.NEWLINE, i)

        def getRuleIndex(self):
            return FortranParser.RULE_program_stmt

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

        localctx = FortranParser.Program_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_program_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.match(FortranParser.PROGRAM_K)
            self.state = 126
            self.identifier()
            self.state = 128 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 127
                self.match(FortranParser.NEWLINE)
                self.state = 130 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==56):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Subroutine_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUBROUTINE_K(self):
            return self.getToken(FortranParser.SUBROUTINE_K, 0)

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FortranParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(FortranParser.IdentifierContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(FortranParser.NEWLINE)
            else:
                return self.getToken(FortranParser.NEWLINE, i)

        def getRuleIndex(self):
            return FortranParser.RULE_subroutine_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubroutine_stmt" ):
                listener.enterSubroutine_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubroutine_stmt" ):
                listener.exitSubroutine_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubroutine_stmt" ):
                return visitor.visitSubroutine_stmt(self)
            else:
                return visitor.visitChildren(self)




    def subroutine_stmt(self):

        localctx = FortranParser.Subroutine_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_subroutine_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.match(FortranParser.SUBROUTINE_K)
            self.state = 133
            self.identifier()
            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 134
                self.match(FortranParser.T__0)
                self.state = 143
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==52:
                    self.state = 135
                    self.identifier()
                    self.state = 140
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==2:
                        self.state = 136
                        self.match(FortranParser.T__1)
                        self.state = 137
                        self.identifier()
                        self.state = 142
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 145
                self.match(FortranParser.T__2)


            self.state = 149 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 148
                self.match(FortranParser.NEWLINE)
                self.state = 151 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==56):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION_K(self):
            return self.getToken(FortranParser.FUNCTION_K, 0)

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FortranParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(FortranParser.IdentifierContext,i)


        def type_spec(self):
            return self.getTypedRuleContext(FortranParser.Type_specContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(FortranParser.NEWLINE)
            else:
                return self.getToken(FortranParser.NEWLINE, i)

        def getRuleIndex(self):
            return FortranParser.RULE_function_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_stmt" ):
                listener.enterFunction_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_stmt" ):
                listener.exitFunction_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_stmt" ):
                return visitor.visitFunction_stmt(self)
            else:
                return visitor.visitChildren(self)




    def function_stmt(self):

        localctx = FortranParser.Function_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_function_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 31943819264) != 0):
                self.state = 153
                self.type_spec()


            self.state = 156
            self.match(FortranParser.FUNCTION_K)
            self.state = 157
            self.identifier()
            self.state = 158
            self.match(FortranParser.T__0)
            self.state = 167
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==52:
                self.state = 159
                self.identifier()
                self.state = 164
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 160
                    self.match(FortranParser.T__1)
                    self.state = 161
                    self.identifier()
                    self.state = 166
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 169
            self.match(FortranParser.T__2)
            self.state = 171 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 170
                self.match(FortranParser.NEWLINE)
                self.state = 173 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==56):
                    break

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
            return self.getToken(FortranParser.END_K, 0)

        def identifier(self):
            return self.getTypedRuleContext(FortranParser.IdentifierContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(FortranParser.NEWLINE)
            else:
                return self.getToken(FortranParser.NEWLINE, i)

        def PROGRAM_K(self):
            return self.getToken(FortranParser.PROGRAM_K, 0)

        def SUBROUTINE_K(self):
            return self.getToken(FortranParser.SUBROUTINE_K, 0)

        def FUNCTION_K(self):
            return self.getToken(FortranParser.FUNCTION_K, 0)

        def getRuleIndex(self):
            return FortranParser.RULE_end_stmt

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

        localctx = FortranParser.End_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_end_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.match(FortranParser.END_K)
            self.state = 177
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 176
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 117440512) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 180
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 179
                self.identifier()


            self.state = 185
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 182
                    self.match(FortranParser.NEWLINE) 
                self.state = 187
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Specification_partContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def specification_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FortranParser.Specification_stmtContext)
            else:
                return self.getTypedRuleContext(FortranParser.Specification_stmtContext,i)


        def getRuleIndex(self):
            return FortranParser.RULE_specification_part

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpecification_part" ):
                listener.enterSpecification_part(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpecification_part" ):
                listener.exitSpecification_part(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSpecification_part" ):
                return visitor.visitSpecification_part(self)
            else:
                return visitor.visitChildren(self)




    def specification_part(self):

        localctx = FortranParser.Specification_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_specification_part)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 188
                self.specification_stmt()
                self.state = 191 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 925297016832) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Specification_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_declaration_stmt(self):
            return self.getTypedRuleContext(FortranParser.Type_declaration_stmtContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(FortranParser.NEWLINE)
            else:
                return self.getToken(FortranParser.NEWLINE, i)

        def implicit_none_stmt(self):
            return self.getTypedRuleContext(FortranParser.Implicit_none_stmtContext,0)


        def common_stmt(self):
            return self.getTypedRuleContext(FortranParser.Common_stmtContext,0)


        def dimension_stmt(self):
            return self.getTypedRuleContext(FortranParser.Dimension_stmtContext,0)


        def getRuleIndex(self):
            return FortranParser.RULE_specification_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpecification_stmt" ):
                listener.enterSpecification_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpecification_stmt" ):
                listener.exitSpecification_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSpecification_stmt" ):
                return visitor.visitSpecification_stmt(self)
            else:
                return visitor.visitChildren(self)




    def specification_stmt(self):

        localctx = FortranParser.Specification_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_specification_stmt)
        self._la = 0 # Token type
        try:
            self.state = 217
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28, 29, 30, 32, 33, 34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 193
                self.type_declaration_stmt()
                self.state = 195 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 194
                    self.match(FortranParser.NEWLINE)
                    self.state = 197 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==56):
                        break

                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 2)
                self.state = 199
                self.implicit_none_stmt()
                self.state = 201 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 200
                    self.match(FortranParser.NEWLINE)
                    self.state = 203 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==56):
                        break

                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 3)
                self.state = 205
                self.common_stmt()
                self.state = 207 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 206
                    self.match(FortranParser.NEWLINE)
                    self.state = 209 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==56):
                        break

                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 4)
                self.state = 211
                self.dimension_stmt()
                self.state = 213 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 212
                    self.match(FortranParser.NEWLINE)
                    self.state = 215 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==56):
                        break

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


    class Type_declaration_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_spec(self):
            return self.getTypedRuleContext(FortranParser.Type_specContext,0)


        def entity_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FortranParser.Entity_declContext)
            else:
                return self.getTypedRuleContext(FortranParser.Entity_declContext,i)


        def getRuleIndex(self):
            return FortranParser.RULE_type_declaration_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_declaration_stmt" ):
                listener.enterType_declaration_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_declaration_stmt" ):
                listener.exitType_declaration_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_declaration_stmt" ):
                return visitor.visitType_declaration_stmt(self)
            else:
                return visitor.visitChildren(self)




    def type_declaration_stmt(self):

        localctx = FortranParser.Type_declaration_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_type_declaration_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.type_spec()
            self.state = 221
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 220
                self.match(FortranParser.T__3)


            self.state = 223
            self.entity_decl()
            self.state = 228
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 224
                self.match(FortranParser.T__1)
                self.state = 225
                self.entity_decl()
                self.state = 230
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def INTEGER_K(self):
            return self.getToken(FortranParser.INTEGER_K, 0)

        def REAL_K(self):
            return self.getToken(FortranParser.REAL_K, 0)

        def DOUBLE_K(self):
            return self.getToken(FortranParser.DOUBLE_K, 0)

        def PRECISION_K(self):
            return self.getToken(FortranParser.PRECISION_K, 0)

        def COMPLEX_K(self):
            return self.getToken(FortranParser.COMPLEX_K, 0)

        def LOGICAL_K(self):
            return self.getToken(FortranParser.LOGICAL_K, 0)

        def CHARACTER_K(self):
            return self.getToken(FortranParser.CHARACTER_K, 0)

        def STAR(self):
            return self.getToken(FortranParser.STAR, 0)

        def integer_literal(self):
            return self.getTypedRuleContext(FortranParser.Integer_literalContext,0)


        def LEN_K(self):
            return self.getToken(FortranParser.LEN_K, 0)

        def getRuleIndex(self):
            return FortranParser.RULE_type_spec

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

        localctx = FortranParser.Type_specContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_type_spec)
        self._la = 0 # Token type
        try:
            self.state = 252
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28]:
                self.enterOuterAlt(localctx, 1)
                self.state = 231
                self.match(FortranParser.INTEGER_K)
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 2)
                self.state = 232
                self.match(FortranParser.REAL_K)
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 3)
                self.state = 233
                self.match(FortranParser.DOUBLE_K)
                self.state = 234
                self.match(FortranParser.PRECISION_K)
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 4)
                self.state = 235
                self.match(FortranParser.COMPLEX_K)
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 5)
                self.state = 236
                self.match(FortranParser.LOGICAL_K)
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 6)
                self.state = 237
                self.match(FortranParser.CHARACTER_K)
                self.state = 250
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [21]:
                    self.state = 238
                    self.match(FortranParser.STAR)
                    self.state = 239
                    self.integer_literal()
                    pass
                elif token in [1]:
                    self.state = 240
                    self.match(FortranParser.T__0)
                    self.state = 243
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==35:
                        self.state = 241
                        self.match(FortranParser.LEN_K)
                        self.state = 242
                        self.match(FortranParser.T__4)


                    self.state = 247
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [53]:
                        self.state = 245
                        self.integer_literal()
                        pass
                    elif token in [21]:
                        self.state = 246
                        self.match(FortranParser.STAR)
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 249
                    self.match(FortranParser.T__2)
                    pass
                elif token in [4, 26, 52]:
                    pass
                else:
                    pass
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


    class Entity_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(FortranParser.IdentifierContext,0)


        def array_spec(self):
            return self.getTypedRuleContext(FortranParser.Array_specContext,0)


        def expression(self):
            return self.getTypedRuleContext(FortranParser.ExpressionContext,0)


        def getRuleIndex(self):
            return FortranParser.RULE_entity_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntity_decl" ):
                listener.enterEntity_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntity_decl" ):
                listener.exitEntity_decl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEntity_decl" ):
                return visitor.visitEntity_decl(self)
            else:
                return visitor.visitChildren(self)




    def entity_decl(self):

        localctx = FortranParser.Entity_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_entity_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.identifier()
            self.state = 259
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 255
                self.match(FortranParser.T__0)
                self.state = 256
                self.array_spec()
                self.state = 257
                self.match(FortranParser.T__2)


            self.state = 263
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 261
                self.match(FortranParser.T__4)
                self.state = 262
                self.expression(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_specContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dimension(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FortranParser.DimensionContext)
            else:
                return self.getTypedRuleContext(FortranParser.DimensionContext,i)


        def getRuleIndex(self):
            return FortranParser.RULE_array_spec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray_spec" ):
                listener.enterArray_spec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray_spec" ):
                listener.exitArray_spec(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_spec" ):
                return visitor.visitArray_spec(self)
            else:
                return visitor.visitChildren(self)




    def array_spec(self):

        localctx = FortranParser.Array_specContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_array_spec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.dimension()
            self.state = 270
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 266
                self.match(FortranParser.T__1)
                self.state = 267
                self.dimension()
                self.state = 272
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DimensionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FortranParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(FortranParser.ExpressionContext,i)


        def STAR(self):
            return self.getToken(FortranParser.STAR, 0)

        def getRuleIndex(self):
            return FortranParser.RULE_dimension

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDimension" ):
                listener.enterDimension(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDimension" ):
                listener.exitDimension(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimension" ):
                return visitor.visitDimension(self)
            else:
                return visitor.visitChildren(self)




    def dimension(self):

        localctx = FortranParser.DimensionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_dimension)
        try:
            self.state = 280
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 8, 9, 12, 20, 52, 53, 54, 55]:
                self.enterOuterAlt(localctx, 1)
                self.state = 276
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
                if la_ == 1:
                    self.state = 273
                    self.expression(0)
                    self.state = 274
                    self.match(FortranParser.T__5)


                self.state = 278
                self.expression(0)
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 279
                self.match(FortranParser.STAR)
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


    class Implicit_none_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IMPLICIT_K(self):
            return self.getToken(FortranParser.IMPLICIT_K, 0)

        def NONE_K(self):
            return self.getToken(FortranParser.NONE_K, 0)

        def getRuleIndex(self):
            return FortranParser.RULE_implicit_none_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImplicit_none_stmt" ):
                listener.enterImplicit_none_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImplicit_none_stmt" ):
                listener.exitImplicit_none_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImplicit_none_stmt" ):
                return visitor.visitImplicit_none_stmt(self)
            else:
                return visitor.visitChildren(self)




    def implicit_none_stmt(self):

        localctx = FortranParser.Implicit_none_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_implicit_none_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            self.match(FortranParser.IMPLICIT_K)
            self.state = 283
            self.match(FortranParser.NONE_K)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Common_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMON_K(self):
            return self.getToken(FortranParser.COMMON_K, 0)

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FortranParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(FortranParser.IdentifierContext,i)


        def SLASH(self, i:int=None):
            if i is None:
                return self.getTokens(FortranParser.SLASH)
            else:
                return self.getToken(FortranParser.SLASH, i)

        def getRuleIndex(self):
            return FortranParser.RULE_common_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommon_stmt" ):
                listener.enterCommon_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommon_stmt" ):
                listener.exitCommon_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommon_stmt" ):
                return visitor.visitCommon_stmt(self)
            else:
                return visitor.visitChildren(self)




    def common_stmt(self):

        localctx = FortranParser.Common_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_common_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            self.match(FortranParser.COMMON_K)
            self.state = 290
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==22:
                self.state = 286
                self.match(FortranParser.SLASH)
                self.state = 287
                self.identifier()
                self.state = 288
                self.match(FortranParser.SLASH)


            self.state = 292
            self.identifier()
            self.state = 297
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 293
                self.match(FortranParser.T__1)
                self.state = 294
                self.identifier()
                self.state = 299
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dimension_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIMENSION_K(self):
            return self.getToken(FortranParser.DIMENSION_K, 0)

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FortranParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(FortranParser.IdentifierContext,i)


        def array_spec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FortranParser.Array_specContext)
            else:
                return self.getTypedRuleContext(FortranParser.Array_specContext,i)


        def getRuleIndex(self):
            return FortranParser.RULE_dimension_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDimension_stmt" ):
                listener.enterDimension_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDimension_stmt" ):
                listener.exitDimension_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimension_stmt" ):
                return visitor.visitDimension_stmt(self)
            else:
                return visitor.visitChildren(self)




    def dimension_stmt(self):

        localctx = FortranParser.Dimension_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_dimension_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.match(FortranParser.DIMENSION_K)
            self.state = 301
            self.identifier()
            self.state = 302
            self.match(FortranParser.T__0)
            self.state = 303
            self.array_spec()
            self.state = 304
            self.match(FortranParser.T__2)
            self.state = 313
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 305
                self.match(FortranParser.T__1)
                self.state = 306
                self.identifier()
                self.state = 307
                self.match(FortranParser.T__0)
                self.state = 308
                self.array_spec()
                self.state = 309
                self.match(FortranParser.T__2)
                self.state = 315
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Execution_partContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def executable_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FortranParser.Executable_stmtContext)
            else:
                return self.getTypedRuleContext(FortranParser.Executable_stmtContext,i)


        def getRuleIndex(self):
            return FortranParser.RULE_execution_part

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExecution_part" ):
                listener.enterExecution_part(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExecution_part" ):
                listener.exitExecution_part(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExecution_part" ):
                return visitor.visitExecution_part(self)
            else:
                return visitor.visitChildren(self)




    def execution_part(self):

        localctx = FortranParser.Execution_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_execution_part)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 317 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 316
                self.executable_stmt()
                self.state = 319 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 15754902114402304) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Executable_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment_stmt(self):
            return self.getTypedRuleContext(FortranParser.Assignment_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(FortranParser.If_stmtContext,0)


        def do_stmt(self):
            return self.getTypedRuleContext(FortranParser.Do_stmtContext,0)


        def goto_stmt(self):
            return self.getTypedRuleContext(FortranParser.Goto_stmtContext,0)


        def call_stmt(self):
            return self.getTypedRuleContext(FortranParser.Call_stmtContext,0)


        def write_stmt(self):
            return self.getTypedRuleContext(FortranParser.Write_stmtContext,0)


        def print_stmt(self):
            return self.getTypedRuleContext(FortranParser.Print_stmtContext,0)


        def format_stmt(self):
            return self.getTypedRuleContext(FortranParser.Format_stmtContext,0)


        def label(self):
            return self.getTypedRuleContext(FortranParser.LabelContext,0)


        def action_stmt(self):
            return self.getTypedRuleContext(FortranParser.Action_stmtContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(FortranParser.NEWLINE)
            else:
                return self.getToken(FortranParser.NEWLINE, i)

        def getRuleIndex(self):
            return FortranParser.RULE_executable_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExecutable_stmt" ):
                listener.enterExecutable_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExecutable_stmt" ):
                listener.exitExecutable_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExecutable_stmt" ):
                return visitor.visitExecutable_stmt(self)
            else:
                return visitor.visitChildren(self)




    def executable_stmt(self):

        localctx = FortranParser.Executable_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_executable_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 333
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.state = 321
                self.assignment_stmt()
                pass

            elif la_ == 2:
                self.state = 322
                self.if_stmt()
                pass

            elif la_ == 3:
                self.state = 323
                self.do_stmt()
                pass

            elif la_ == 4:
                self.state = 324
                self.goto_stmt()
                pass

            elif la_ == 5:
                self.state = 325
                self.call_stmt()
                pass

            elif la_ == 6:
                self.state = 326
                self.write_stmt()
                pass

            elif la_ == 7:
                self.state = 327
                self.print_stmt()
                pass

            elif la_ == 8:
                self.state = 328
                self.format_stmt()
                pass

            elif la_ == 9:
                self.state = 329
                self.label()
                self.state = 330
                self.action_stmt()
                pass

            elif la_ == 10:
                self.state = 332
                self.action_stmt()
                pass


            self.state = 336 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 335
                self.match(FortranParser.NEWLINE)
                self.state = 338 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==56):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Action_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment_stmt(self):
            return self.getTypedRuleContext(FortranParser.Assignment_stmtContext,0)


        def goto_stmt(self):
            return self.getTypedRuleContext(FortranParser.Goto_stmtContext,0)


        def call_stmt(self):
            return self.getTypedRuleContext(FortranParser.Call_stmtContext,0)


        def write_stmt(self):
            return self.getTypedRuleContext(FortranParser.Write_stmtContext,0)


        def print_stmt(self):
            return self.getTypedRuleContext(FortranParser.Print_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(FortranParser.Return_stmtContext,0)


        def CONTINUE_K(self):
            return self.getToken(FortranParser.CONTINUE_K, 0)

        def STOP_K(self):
            return self.getToken(FortranParser.STOP_K, 0)

        def getRuleIndex(self):
            return FortranParser.RULE_action_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAction_stmt" ):
                listener.enterAction_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAction_stmt" ):
                listener.exitAction_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAction_stmt" ):
                return visitor.visitAction_stmt(self)
            else:
                return visitor.visitChildren(self)




    def action_stmt(self):

        localctx = FortranParser.Action_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_action_stmt)
        try:
            self.state = 348
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [52]:
                self.enterOuterAlt(localctx, 1)
                self.state = 340
                self.assignment_stmt()
                pass
            elif token in [44]:
                self.enterOuterAlt(localctx, 2)
                self.state = 341
                self.goto_stmt()
                pass
            elif token in [45]:
                self.enterOuterAlt(localctx, 3)
                self.state = 342
                self.call_stmt()
                pass
            elif token in [47]:
                self.enterOuterAlt(localctx, 4)
                self.state = 343
                self.write_stmt()
                pass
            elif token in [48]:
                self.enterOuterAlt(localctx, 5)
                self.state = 344
                self.print_stmt()
                pass
            elif token in [46]:
                self.enterOuterAlt(localctx, 6)
                self.state = 345
                self.return_stmt()
                pass
            elif token in [49]:
                self.enterOuterAlt(localctx, 7)
                self.state = 346
                self.match(FortranParser.CONTINUE_K)
                pass
            elif token in [50]:
                self.enterOuterAlt(localctx, 8)
                self.state = 347
                self.match(FortranParser.STOP_K)
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


    class Assignment_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(FortranParser.IdentifierContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FortranParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(FortranParser.ExpressionContext,i)


        def getRuleIndex(self):
            return FortranParser.RULE_assignment_stmt

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

        localctx = FortranParser.Assignment_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_assignment_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 350
            self.identifier()
            self.state = 362
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 351
                self.match(FortranParser.T__0)
                self.state = 352
                self.expression(0)
                self.state = 357
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 353
                    self.match(FortranParser.T__1)
                    self.state = 354
                    self.expression(0)
                    self.state = 359
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 360
                self.match(FortranParser.T__2)


            self.state = 364
            self.match(FortranParser.T__4)
            self.state = 365
            self.expression(0)
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

        def IF_K(self, i:int=None):
            if i is None:
                return self.getTokens(FortranParser.IF_K)
            else:
                return self.getToken(FortranParser.IF_K, i)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FortranParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(FortranParser.ExpressionContext,i)


        def THEN_K(self, i:int=None):
            if i is None:
                return self.getTokens(FortranParser.THEN_K)
            else:
                return self.getToken(FortranParser.THEN_K, i)

        def END_K(self):
            return self.getToken(FortranParser.END_K, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(FortranParser.NEWLINE)
            else:
                return self.getToken(FortranParser.NEWLINE, i)

        def execution_part(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FortranParser.Execution_partContext)
            else:
                return self.getTypedRuleContext(FortranParser.Execution_partContext,i)


        def ELSE_K(self, i:int=None):
            if i is None:
                return self.getTokens(FortranParser.ELSE_K)
            else:
                return self.getToken(FortranParser.ELSE_K, i)

        def action_stmt(self):
            return self.getTypedRuleContext(FortranParser.Action_stmtContext,0)


        def getRuleIndex(self):
            return FortranParser.RULE_if_stmt

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

        localctx = FortranParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.state = 419
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,56,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 367
                self.match(FortranParser.IF_K)
                self.state = 368
                self.match(FortranParser.T__0)
                self.state = 369
                self.expression(0)
                self.state = 370
                self.match(FortranParser.T__2)
                self.state = 371
                self.match(FortranParser.THEN_K)
                self.state = 373 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 372
                    self.match(FortranParser.NEWLINE)
                    self.state = 375 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==56):
                        break

                self.state = 378
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 15754902114402304) != 0):
                    self.state = 377
                    self.execution_part()


                self.state = 396
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,52,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 380
                        self.match(FortranParser.ELSE_K)
                        self.state = 381
                        self.match(FortranParser.IF_K)
                        self.state = 382
                        self.match(FortranParser.T__0)
                        self.state = 383
                        self.expression(0)
                        self.state = 384
                        self.match(FortranParser.T__2)
                        self.state = 385
                        self.match(FortranParser.THEN_K)
                        self.state = 387 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while True:
                            self.state = 386
                            self.match(FortranParser.NEWLINE)
                            self.state = 389 
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            if not (_la==56):
                                break

                        self.state = 392
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & 15754902114402304) != 0):
                            self.state = 391
                            self.execution_part()

                 
                    self.state = 398
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,52,self._ctx)

                self.state = 408
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==42:
                    self.state = 399
                    self.match(FortranParser.ELSE_K)
                    self.state = 401 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 400
                        self.match(FortranParser.NEWLINE)
                        self.state = 403 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==56):
                            break

                    self.state = 406
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & 15754902114402304) != 0):
                        self.state = 405
                        self.execution_part()




                self.state = 410
                self.match(FortranParser.END_K)
                self.state = 411
                self.match(FortranParser.IF_K)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 413
                self.match(FortranParser.IF_K)
                self.state = 414
                self.match(FortranParser.T__0)
                self.state = 415
                self.expression(0)
                self.state = 416
                self.match(FortranParser.T__2)
                self.state = 417
                self.action_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Do_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO_K(self, i:int=None):
            if i is None:
                return self.getTokens(FortranParser.DO_K)
            else:
                return self.getToken(FortranParser.DO_K, i)

        def END_K(self):
            return self.getToken(FortranParser.END_K, 0)

        def label(self):
            return self.getTypedRuleContext(FortranParser.LabelContext,0)


        def identifier(self):
            return self.getTypedRuleContext(FortranParser.IdentifierContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FortranParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(FortranParser.ExpressionContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(FortranParser.NEWLINE)
            else:
                return self.getToken(FortranParser.NEWLINE, i)

        def execution_part(self):
            return self.getTypedRuleContext(FortranParser.Execution_partContext,0)


        def getRuleIndex(self):
            return FortranParser.RULE_do_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDo_stmt" ):
                listener.enterDo_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDo_stmt" ):
                listener.exitDo_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDo_stmt" ):
                return visitor.visitDo_stmt(self)
            else:
                return visitor.visitChildren(self)




    def do_stmt(self):

        localctx = FortranParser.Do_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_do_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 421
            self.match(FortranParser.DO_K)
            self.state = 423
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==53:
                self.state = 422
                self.label()


            self.state = 434
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==52:
                self.state = 425
                self.identifier()
                self.state = 426
                self.match(FortranParser.T__4)
                self.state = 427
                self.expression(0)
                self.state = 428
                self.match(FortranParser.T__1)
                self.state = 429
                self.expression(0)
                self.state = 432
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==2:
                    self.state = 430
                    self.match(FortranParser.T__1)
                    self.state = 431
                    self.expression(0)




            self.state = 437 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 436
                self.match(FortranParser.NEWLINE)
                self.state = 439 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==56):
                    break

            self.state = 442
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 15754902114402304) != 0):
                self.state = 441
                self.execution_part()


            self.state = 444
            self.match(FortranParser.END_K)
            self.state = 445
            self.match(FortranParser.DO_K)
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
            return self.getToken(FortranParser.GOTO_K, 0)

        def label(self):
            return self.getTypedRuleContext(FortranParser.LabelContext,0)


        def getRuleIndex(self):
            return FortranParser.RULE_goto_stmt

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

        localctx = FortranParser.Goto_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_goto_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 447
            self.match(FortranParser.GOTO_K)
            self.state = 448
            self.label()
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
            return self.getToken(FortranParser.CALL_K, 0)

        def identifier(self):
            return self.getTypedRuleContext(FortranParser.IdentifierContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FortranParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(FortranParser.ExpressionContext,i)


        def getRuleIndex(self):
            return FortranParser.RULE_call_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCall_stmt" ):
                listener.enterCall_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCall_stmt" ):
                listener.exitCall_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_stmt" ):
                return visitor.visitCall_stmt(self)
            else:
                return visitor.visitChildren(self)




    def call_stmt(self):

        localctx = FortranParser.Call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_call_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 450
            self.match(FortranParser.CALL_K)
            self.state = 451
            self.identifier()
            self.state = 464
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 452
                self.match(FortranParser.T__0)
                self.state = 461
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 67553994411610882) != 0):
                    self.state = 453
                    self.expression(0)
                    self.state = 458
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==2:
                        self.state = 454
                        self.match(FortranParser.T__1)
                        self.state = 455
                        self.expression(0)
                        self.state = 460
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 463
                self.match(FortranParser.T__2)


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
            return self.getToken(FortranParser.RETURN_K, 0)

        def getRuleIndex(self):
            return FortranParser.RULE_return_stmt

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

        localctx = FortranParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_return_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 466
            self.match(FortranParser.RETURN_K)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Write_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WRITE_K(self):
            return self.getToken(FortranParser.WRITE_K, 0)

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FortranParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(FortranParser.IdentifierContext,i)


        def STAR(self, i:int=None):
            if i is None:
                return self.getTokens(FortranParser.STAR)
            else:
                return self.getToken(FortranParser.STAR, i)

        def label(self):
            return self.getTypedRuleContext(FortranParser.LabelContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FortranParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(FortranParser.ExpressionContext,i)


        def getRuleIndex(self):
            return FortranParser.RULE_write_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWrite_stmt" ):
                listener.enterWrite_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWrite_stmt" ):
                listener.exitWrite_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWrite_stmt" ):
                return visitor.visitWrite_stmt(self)
            else:
                return visitor.visitChildren(self)




    def write_stmt(self):

        localctx = FortranParser.Write_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_write_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 468
            self.match(FortranParser.WRITE_K)
            self.state = 469
            self.match(FortranParser.T__0)
            self.state = 472
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [52]:
                self.state = 470
                self.identifier()
                pass
            elif token in [21]:
                self.state = 471
                self.match(FortranParser.STAR)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 474
            self.match(FortranParser.T__1)
            self.state = 478
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [52]:
                self.state = 475
                self.identifier()
                pass
            elif token in [53]:
                self.state = 476
                self.label()
                pass
            elif token in [21]:
                self.state = 477
                self.match(FortranParser.STAR)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 480
            self.match(FortranParser.T__2)
            self.state = 489
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 67553994411610882) != 0):
                self.state = 481
                self.expression(0)
                self.state = 486
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 482
                    self.match(FortranParser.T__1)
                    self.state = 483
                    self.expression(0)
                    self.state = 488
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



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
            return self.getToken(FortranParser.PRINT_K, 0)

        def STAR(self):
            return self.getToken(FortranParser.STAR, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FortranParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(FortranParser.ExpressionContext,i)


        def getRuleIndex(self):
            return FortranParser.RULE_print_stmt

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

        localctx = FortranParser.Print_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_print_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 491
            self.match(FortranParser.PRINT_K)
            self.state = 492
            self.match(FortranParser.STAR)
            self.state = 502
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 493
                self.match(FortranParser.T__1)
                self.state = 494
                self.expression(0)
                self.state = 499
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 495
                    self.match(FortranParser.T__1)
                    self.state = 496
                    self.expression(0)
                    self.state = 501
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Format_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def label(self):
            return self.getTypedRuleContext(FortranParser.LabelContext,0)


        def FORMAT_K(self):
            return self.getToken(FortranParser.FORMAT_K, 0)

        def format_item(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FortranParser.Format_itemContext)
            else:
                return self.getTypedRuleContext(FortranParser.Format_itemContext,i)


        def getRuleIndex(self):
            return FortranParser.RULE_format_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormat_stmt" ):
                listener.enterFormat_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormat_stmt" ):
                listener.exitFormat_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFormat_stmt" ):
                return visitor.visitFormat_stmt(self)
            else:
                return visitor.visitChildren(self)




    def format_stmt(self):

        localctx = FortranParser.Format_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_format_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 504
            self.label()
            self.state = 505
            self.match(FortranParser.FORMAT_K)
            self.state = 506
            self.match(FortranParser.T__0)
            self.state = 515
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 67553994410557442) != 0):
                self.state = 507
                self.format_item()
                self.state = 512
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 508
                    self.match(FortranParser.T__1)
                    self.state = 509
                    self.format_item()
                    self.state = 514
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 517
            self.match(FortranParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Format_itemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(FortranParser.IdentifierContext,0)


        def string_literal(self):
            return self.getTypedRuleContext(FortranParser.String_literalContext,0)


        def integer_literal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FortranParser.Integer_literalContext)
            else:
                return self.getTypedRuleContext(FortranParser.Integer_literalContext,i)


        def real_literal(self):
            return self.getTypedRuleContext(FortranParser.Real_literalContext,0)


        def format_item(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FortranParser.Format_itemContext)
            else:
                return self.getTypedRuleContext(FortranParser.Format_itemContext,i)


        def getRuleIndex(self):
            return FortranParser.RULE_format_item

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormat_item" ):
                listener.enterFormat_item(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormat_item" ):
                listener.exitFormat_item(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFormat_item" ):
                return visitor.visitFormat_item(self)
            else:
                return visitor.visitChildren(self)




    def format_item(self):

        localctx = FortranParser.Format_itemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_format_item)
        self._la = 0 # Token type
        try:
            self.state = 543
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,76,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 519
                self.identifier()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 520
                self.string_literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 521
                self.integer_literal()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 522
                self.real_literal()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 523
                self.identifier()
                self.state = 526
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [53]:
                    self.state = 524
                    self.integer_literal()
                    pass
                elif token in [54]:
                    self.state = 525
                    self.real_literal()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 530
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==7:
                    self.state = 528
                    self.match(FortranParser.T__6)
                    self.state = 529
                    self.integer_literal()


                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 532
                self.match(FortranParser.T__0)
                self.state = 533
                self.format_item()
                self.state = 538
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 534
                    self.match(FortranParser.T__1)
                    self.state = 535
                    self.format_item()
                    self.state = 540
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 541
                self.match(FortranParser.T__2)
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

        def INTEGER(self):
            return self.getToken(FortranParser.INTEGER, 0)

        def getRuleIndex(self):
            return FortranParser.RULE_label

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabel" ):
                listener.enterLabel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabel" ):
                listener.exitLabel(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLabel" ):
                return visitor.visitLabel(self)
            else:
                return visitor.visitChildren(self)




    def label(self):

        localctx = FortranParser.LabelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_label)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 545
            self.match(FortranParser.INTEGER)
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
            return self.getToken(FortranParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return FortranParser.RULE_identifier

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

        localctx = FortranParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 547
            self.match(FortranParser.IDENTIFIER)
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
            return self.getToken(FortranParser.NOT, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FortranParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(FortranParser.ExpressionContext,i)


        def MINUS(self):
            return self.getToken(FortranParser.MINUS, 0)

        def primary(self):
            return self.getTypedRuleContext(FortranParser.PrimaryContext,0)


        def OR(self):
            return self.getToken(FortranParser.OR, 0)

        def AND(self):
            return self.getToken(FortranParser.AND, 0)

        def EQ(self):
            return self.getToken(FortranParser.EQ, 0)

        def NE(self):
            return self.getToken(FortranParser.NE, 0)

        def LT(self):
            return self.getToken(FortranParser.LT, 0)

        def LE(self):
            return self.getToken(FortranParser.LE, 0)

        def GT(self):
            return self.getToken(FortranParser.GT, 0)

        def GE(self):
            return self.getToken(FortranParser.GE, 0)

        def PLUS(self):
            return self.getToken(FortranParser.PLUS, 0)

        def STAR(self):
            return self.getToken(FortranParser.STAR, 0)

        def SLASH(self):
            return self.getToken(FortranParser.SLASH, 0)

        def POWER(self):
            return self.getToken(FortranParser.POWER, 0)

        def getRuleIndex(self):
            return FortranParser.RULE_expression

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
        localctx = FortranParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 559
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.state = 550
                self.match(FortranParser.NOT)
                self.state = 551
                self.expression(8)
                pass
            elif token in [20]:
                self.state = 552
                self.match(FortranParser.MINUS)
                self.state = 553
                self.expression(3)
                pass
            elif token in [1]:
                self.state = 554
                self.match(FortranParser.T__0)
                self.state = 555
                self.expression(0)
                self.state = 556
                self.match(FortranParser.T__2)
                pass
            elif token in [8, 9, 52, 53, 54, 55]:
                self.state = 558
                self.primary()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 578
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,79,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 576
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,78,self._ctx)
                    if la_ == 1:
                        localctx = FortranParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 561
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 562
                        _la = self._input.LA(1)
                        if not(_la==10 or _la==11):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 563
                        self.expression(10)
                        pass

                    elif la_ == 2:
                        localctx = FortranParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 564
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 565
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 516096) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 566
                        self.expression(8)
                        pass

                    elif la_ == 3:
                        localctx = FortranParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 567
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 568
                        _la = self._input.LA(1)
                        if not(_la==19 or _la==20):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 569
                        self.expression(7)
                        pass

                    elif la_ == 4:
                        localctx = FortranParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 570
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 571
                        _la = self._input.LA(1)
                        if not(_la==21 or _la==22):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 572
                        self.expression(6)
                        pass

                    elif la_ == 5:
                        localctx = FortranParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 573
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 574
                        self.match(FortranParser.POWER)
                        self.state = 575
                        self.expression(5)
                        pass

             
                self.state = 580
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,79,self._ctx)

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
            return self.getTypedRuleContext(FortranParser.IdentifierContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FortranParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(FortranParser.ExpressionContext,i)


        def literal(self):
            return self.getTypedRuleContext(FortranParser.LiteralContext,0)


        def getRuleIndex(self):
            return FortranParser.RULE_primary

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

        localctx = FortranParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_primary)
        self._la = 0 # Token type
        try:
            self.state = 596
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [52]:
                self.enterOuterAlt(localctx, 1)
                self.state = 581
                self.identifier()
                self.state = 593
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,81,self._ctx)
                if la_ == 1:
                    self.state = 582
                    self.match(FortranParser.T__0)
                    self.state = 583
                    self.expression(0)
                    self.state = 588
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==2:
                        self.state = 584
                        self.match(FortranParser.T__1)
                        self.state = 585
                        self.expression(0)
                        self.state = 590
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 591
                    self.match(FortranParser.T__2)


                pass
            elif token in [8, 9, 53, 54, 55]:
                self.enterOuterAlt(localctx, 2)
                self.state = 595
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
            return self.getTypedRuleContext(FortranParser.Integer_literalContext,0)


        def real_literal(self):
            return self.getTypedRuleContext(FortranParser.Real_literalContext,0)


        def string_literal(self):
            return self.getTypedRuleContext(FortranParser.String_literalContext,0)


        def logical_literal(self):
            return self.getTypedRuleContext(FortranParser.Logical_literalContext,0)


        def getRuleIndex(self):
            return FortranParser.RULE_literal

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

        localctx = FortranParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_literal)
        try:
            self.state = 602
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [53]:
                self.enterOuterAlt(localctx, 1)
                self.state = 598
                self.integer_literal()
                pass
            elif token in [54]:
                self.enterOuterAlt(localctx, 2)
                self.state = 599
                self.real_literal()
                pass
            elif token in [55]:
                self.enterOuterAlt(localctx, 3)
                self.state = 600
                self.string_literal()
                pass
            elif token in [8, 9]:
                self.enterOuterAlt(localctx, 4)
                self.state = 601
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


    class Integer_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(FortranParser.INTEGER, 0)

        def getRuleIndex(self):
            return FortranParser.RULE_integer_literal

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

        localctx = FortranParser.Integer_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_integer_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 604
            self.match(FortranParser.INTEGER)
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
            return self.getToken(FortranParser.REAL, 0)

        def getRuleIndex(self):
            return FortranParser.RULE_real_literal

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

        localctx = FortranParser.Real_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_real_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 606
            self.match(FortranParser.REAL)
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
            return self.getToken(FortranParser.STRING, 0)

        def getRuleIndex(self):
            return FortranParser.RULE_string_literal

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

        localctx = FortranParser.String_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_string_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 608
            self.match(FortranParser.STRING)
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


        def getRuleIndex(self):
            return FortranParser.RULE_logical_literal

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

        localctx = FortranParser.Logical_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_logical_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 610
            _la = self._input.LA(1)
            if not(_la==8 or _la==9):
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
        self._predicates[34] = self.expression_sempred
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
         




