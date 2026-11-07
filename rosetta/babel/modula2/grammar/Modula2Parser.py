# Generated from rosetta/babel/modula2/grammar/Modula2.g4 by ANTLR 4.13.2
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
        4,1,68,492,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        1,0,5,0,82,8,0,10,0,12,0,85,9,0,1,0,1,0,1,1,1,1,1,1,3,1,92,8,1,1,
        2,1,2,1,2,1,2,5,2,98,8,2,10,2,12,2,101,9,2,1,2,5,2,104,8,2,10,2,
        12,2,107,9,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,5,3,118,8,3,10,
        3,12,3,121,9,3,1,3,5,3,124,8,3,10,3,12,3,127,9,3,1,3,5,3,130,8,3,
        10,3,12,3,133,9,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,5,4,144,8,
        4,10,4,12,4,147,9,4,1,4,1,4,1,4,1,4,1,5,1,5,3,5,155,8,5,1,5,1,5,
        1,5,1,5,1,6,3,6,162,8,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,5,7,171,8,7,
        10,7,12,7,174,9,7,1,8,5,8,177,8,8,10,8,12,8,180,9,8,1,8,1,8,3,8,
        184,8,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,5,9,194,8,9,10,9,12,9,197,
        9,9,1,9,1,9,1,9,1,9,1,9,1,9,5,9,205,8,9,10,9,12,9,208,9,9,1,9,1,
        9,1,9,1,9,1,9,1,9,5,9,216,8,9,10,9,12,9,219,9,9,1,9,3,9,222,8,9,
        1,10,1,10,1,10,1,10,3,10,228,8,10,1,10,3,10,231,8,10,1,10,1,10,3,
        10,235,8,10,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,5,11,245,8,11,
        10,11,12,11,248,9,11,1,12,3,12,251,8,12,1,12,1,12,1,12,1,12,1,13,
        1,13,1,13,1,13,3,13,261,8,13,1,14,1,14,1,14,1,14,1,14,1,15,1,15,
        1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,16,5,16,278,8,16,10,16,12,16,
        281,9,16,1,16,1,16,1,17,1,17,1,17,5,17,288,8,17,10,17,12,17,291,
        9,17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,3,18,
        304,8,18,1,19,1,19,1,19,1,19,1,20,1,20,1,20,3,20,313,8,20,1,20,3,
        20,316,8,20,1,21,1,21,1,21,5,21,321,8,21,10,21,12,21,324,9,21,1,
        22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,5,22,335,8,22,10,22,12,
        22,338,9,22,1,22,1,22,3,22,342,8,22,1,22,1,22,1,23,1,23,1,23,1,23,
        1,23,1,23,5,23,352,8,23,10,23,12,23,355,9,23,3,23,357,8,23,1,23,
        1,23,3,23,361,8,23,1,23,1,23,1,24,1,24,1,24,1,24,1,25,1,25,1,25,
        1,25,1,25,1,25,1,26,1,26,1,26,1,26,1,26,1,27,1,27,1,27,1,27,1,28,
        1,28,1,28,1,28,1,28,1,28,1,28,1,28,3,28,392,8,28,1,28,1,28,1,28,
        1,28,1,29,1,29,3,29,400,8,29,1,30,1,30,1,31,1,31,1,31,1,31,1,31,
        1,31,1,31,5,31,411,8,31,10,31,12,31,414,9,31,1,31,1,31,1,31,5,31,
        419,8,31,10,31,12,31,422,9,31,1,32,1,32,1,32,1,32,3,32,428,8,32,
        1,33,1,33,1,34,3,34,433,8,34,1,34,1,34,1,34,1,34,5,34,439,8,34,10,
        34,12,34,442,9,34,1,35,1,35,1,36,1,36,1,36,1,36,5,36,450,8,36,10,
        36,12,36,453,9,36,1,37,1,37,1,38,1,38,1,38,1,38,1,38,3,38,462,8,
        38,1,38,3,38,465,8,38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,
        38,1,38,5,38,477,8,38,10,38,12,38,480,9,38,3,38,482,8,38,1,38,3,
        38,485,8,38,1,39,1,39,1,39,3,39,490,8,39,1,39,0,0,40,0,2,4,6,8,10,
        12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,
        56,58,60,62,64,66,68,70,72,74,76,78,0,4,3,0,4,4,13,17,53,53,1,0,
        59,60,2,0,54,54,59,60,3,0,18,18,55,57,61,61,519,0,83,1,0,0,0,2,91,
        1,0,0,0,4,93,1,0,0,0,6,112,1,0,0,0,8,138,1,0,0,0,10,154,1,0,0,0,
        12,161,1,0,0,0,14,167,1,0,0,0,16,178,1,0,0,0,18,221,1,0,0,0,20,223,
        1,0,0,0,22,241,1,0,0,0,24,250,1,0,0,0,26,260,1,0,0,0,28,262,1,0,
        0,0,30,267,1,0,0,0,32,271,1,0,0,0,34,284,1,0,0,0,36,303,1,0,0,0,
        38,305,1,0,0,0,40,309,1,0,0,0,42,317,1,0,0,0,44,325,1,0,0,0,46,345,
        1,0,0,0,48,364,1,0,0,0,50,368,1,0,0,0,52,374,1,0,0,0,54,379,1,0,
        0,0,56,383,1,0,0,0,58,397,1,0,0,0,60,401,1,0,0,0,62,403,1,0,0,0,
        64,423,1,0,0,0,66,429,1,0,0,0,68,432,1,0,0,0,70,443,1,0,0,0,72,445,
        1,0,0,0,74,454,1,0,0,0,76,484,1,0,0,0,78,486,1,0,0,0,80,82,3,2,1,
        0,81,80,1,0,0,0,82,85,1,0,0,0,83,81,1,0,0,0,83,84,1,0,0,0,84,86,
        1,0,0,0,85,83,1,0,0,0,86,87,5,0,0,1,87,1,1,0,0,0,88,92,3,4,2,0,89,
        92,3,6,3,0,90,92,3,8,4,0,91,88,1,0,0,0,91,89,1,0,0,0,91,90,1,0,0,
        0,92,3,1,0,0,0,93,94,5,21,0,0,94,95,5,64,0,0,95,99,5,1,0,0,96,98,
        3,10,5,0,97,96,1,0,0,0,98,101,1,0,0,0,99,97,1,0,0,0,99,100,1,0,0,
        0,100,105,1,0,0,0,101,99,1,0,0,0,102,104,3,12,6,0,103,102,1,0,0,
        0,104,107,1,0,0,0,105,103,1,0,0,0,105,106,1,0,0,0,106,108,1,0,0,
        0,107,105,1,0,0,0,108,109,3,16,8,0,109,110,5,64,0,0,110,111,5,2,
        0,0,111,5,1,0,0,0,112,113,5,26,0,0,113,114,5,21,0,0,114,115,5,64,
        0,0,115,119,5,1,0,0,116,118,3,10,5,0,117,116,1,0,0,0,118,121,1,0,
        0,0,119,117,1,0,0,0,119,120,1,0,0,0,120,125,1,0,0,0,121,119,1,0,
        0,0,122,124,3,12,6,0,123,122,1,0,0,0,124,127,1,0,0,0,125,123,1,0,
        0,0,125,126,1,0,0,0,126,131,1,0,0,0,127,125,1,0,0,0,128,130,3,18,
        9,0,129,128,1,0,0,0,130,133,1,0,0,0,131,129,1,0,0,0,131,132,1,0,
        0,0,132,134,1,0,0,0,133,131,1,0,0,0,134,135,5,29,0,0,135,136,5,64,
        0,0,136,137,5,2,0,0,137,7,1,0,0,0,138,139,5,27,0,0,139,140,5,21,
        0,0,140,141,5,64,0,0,141,145,5,1,0,0,142,144,3,10,5,0,143,142,1,
        0,0,0,144,147,1,0,0,0,145,143,1,0,0,0,145,146,1,0,0,0,146,148,1,
        0,0,0,147,145,1,0,0,0,148,149,3,16,8,0,149,150,5,64,0,0,150,151,
        5,2,0,0,151,9,1,0,0,0,152,153,5,24,0,0,153,155,5,64,0,0,154,152,
        1,0,0,0,154,155,1,0,0,0,155,156,1,0,0,0,156,157,5,22,0,0,157,158,
        3,14,7,0,158,159,5,1,0,0,159,11,1,0,0,0,160,162,5,25,0,0,161,160,
        1,0,0,0,161,162,1,0,0,0,162,163,1,0,0,0,163,164,5,23,0,0,164,165,
        3,14,7,0,165,166,5,1,0,0,166,13,1,0,0,0,167,172,5,64,0,0,168,169,
        5,3,0,0,169,171,5,64,0,0,170,168,1,0,0,0,171,174,1,0,0,0,172,170,
        1,0,0,0,172,173,1,0,0,0,173,15,1,0,0,0,174,172,1,0,0,0,175,177,3,
        18,9,0,176,175,1,0,0,0,177,180,1,0,0,0,178,176,1,0,0,0,178,179,1,
        0,0,0,179,183,1,0,0,0,180,178,1,0,0,0,181,182,5,28,0,0,182,184,3,
        34,17,0,183,181,1,0,0,0,183,184,1,0,0,0,184,185,1,0,0,0,185,186,
        5,29,0,0,186,17,1,0,0,0,187,195,5,30,0,0,188,189,5,64,0,0,189,190,
        5,4,0,0,190,191,3,64,32,0,191,192,5,1,0,0,192,194,1,0,0,0,193,188,
        1,0,0,0,194,197,1,0,0,0,195,193,1,0,0,0,195,196,1,0,0,0,196,222,
        1,0,0,0,197,195,1,0,0,0,198,206,5,31,0,0,199,200,5,64,0,0,200,201,
        5,4,0,0,201,202,3,26,13,0,202,203,5,1,0,0,203,205,1,0,0,0,204,199,
        1,0,0,0,205,208,1,0,0,0,206,204,1,0,0,0,206,207,1,0,0,0,207,222,
        1,0,0,0,208,206,1,0,0,0,209,217,5,32,0,0,210,211,3,14,7,0,211,212,
        5,5,0,0,212,213,3,26,13,0,213,214,5,1,0,0,214,216,1,0,0,0,215,210,
        1,0,0,0,216,219,1,0,0,0,217,215,1,0,0,0,217,218,1,0,0,0,218,222,
        1,0,0,0,219,217,1,0,0,0,220,222,3,20,10,0,221,187,1,0,0,0,221,198,
        1,0,0,0,221,209,1,0,0,0,221,220,1,0,0,0,222,19,1,0,0,0,223,224,5,
        33,0,0,224,230,5,64,0,0,225,227,5,6,0,0,226,228,3,22,11,0,227,226,
        1,0,0,0,227,228,1,0,0,0,228,229,1,0,0,0,229,231,5,7,0,0,230,225,
        1,0,0,0,230,231,1,0,0,0,231,234,1,0,0,0,232,233,5,5,0,0,233,235,
        5,64,0,0,234,232,1,0,0,0,234,235,1,0,0,0,235,236,1,0,0,0,236,237,
        5,1,0,0,237,238,3,16,8,0,238,239,5,64,0,0,239,240,5,1,0,0,240,21,
        1,0,0,0,241,246,3,24,12,0,242,243,5,1,0,0,243,245,3,24,12,0,244,
        242,1,0,0,0,245,248,1,0,0,0,246,244,1,0,0,0,246,247,1,0,0,0,247,
        23,1,0,0,0,248,246,1,0,0,0,249,251,5,32,0,0,250,249,1,0,0,0,250,
        251,1,0,0,0,251,252,1,0,0,0,252,253,3,14,7,0,253,254,5,5,0,0,254,
        255,3,26,13,0,255,25,1,0,0,0,256,261,5,64,0,0,257,261,3,28,14,0,
        258,261,3,30,15,0,259,261,3,32,16,0,260,256,1,0,0,0,260,257,1,0,
        0,0,260,258,1,0,0,0,260,259,1,0,0,0,261,27,1,0,0,0,262,263,5,34,
        0,0,263,264,3,64,32,0,264,265,5,35,0,0,265,266,3,26,13,0,266,29,
        1,0,0,0,267,268,5,37,0,0,268,269,5,38,0,0,269,270,3,26,13,0,270,
        31,1,0,0,0,271,279,5,36,0,0,272,273,3,14,7,0,273,274,5,5,0,0,274,
        275,3,26,13,0,275,276,5,1,0,0,276,278,1,0,0,0,277,272,1,0,0,0,278,
        281,1,0,0,0,279,277,1,0,0,0,279,280,1,0,0,0,280,282,1,0,0,0,281,
        279,1,0,0,0,282,283,5,29,0,0,283,33,1,0,0,0,284,289,3,36,18,0,285,
        286,5,1,0,0,286,288,3,36,18,0,287,285,1,0,0,0,288,291,1,0,0,0,289,
        287,1,0,0,0,289,290,1,0,0,0,290,35,1,0,0,0,291,289,1,0,0,0,292,304,
        3,38,19,0,293,304,3,40,20,0,294,304,3,44,22,0,295,304,3,46,23,0,
        296,304,3,50,25,0,297,304,3,52,26,0,298,304,3,54,27,0,299,304,3,
        56,28,0,300,304,3,58,29,0,301,304,3,60,30,0,302,304,1,0,0,0,303,
        292,1,0,0,0,303,293,1,0,0,0,303,294,1,0,0,0,303,295,1,0,0,0,303,
        296,1,0,0,0,303,297,1,0,0,0,303,298,1,0,0,0,303,299,1,0,0,0,303,
        300,1,0,0,0,303,301,1,0,0,0,303,302,1,0,0,0,304,37,1,0,0,0,305,306,
        3,62,31,0,306,307,5,8,0,0,307,308,3,64,32,0,308,39,1,0,0,0,309,315,
        3,62,31,0,310,312,5,6,0,0,311,313,3,42,21,0,312,311,1,0,0,0,312,
        313,1,0,0,0,313,314,1,0,0,0,314,316,5,7,0,0,315,310,1,0,0,0,315,
        316,1,0,0,0,316,41,1,0,0,0,317,322,3,64,32,0,318,319,5,3,0,0,319,
        321,3,64,32,0,320,318,1,0,0,0,321,324,1,0,0,0,322,320,1,0,0,0,322,
        323,1,0,0,0,323,43,1,0,0,0,324,322,1,0,0,0,325,326,5,39,0,0,326,
        327,3,64,32,0,327,328,5,40,0,0,328,336,3,34,17,0,329,330,5,41,0,
        0,330,331,3,64,32,0,331,332,5,40,0,0,332,333,3,34,17,0,333,335,1,
        0,0,0,334,329,1,0,0,0,335,338,1,0,0,0,336,334,1,0,0,0,336,337,1,
        0,0,0,337,341,1,0,0,0,338,336,1,0,0,0,339,340,5,42,0,0,340,342,3,
        34,17,0,341,339,1,0,0,0,341,342,1,0,0,0,342,343,1,0,0,0,343,344,
        5,29,0,0,344,45,1,0,0,0,345,346,5,43,0,0,346,347,3,64,32,0,347,356,
        5,35,0,0,348,353,3,48,24,0,349,350,5,9,0,0,350,352,3,48,24,0,351,
        349,1,0,0,0,352,355,1,0,0,0,353,351,1,0,0,0,353,354,1,0,0,0,354,
        357,1,0,0,0,355,353,1,0,0,0,356,348,1,0,0,0,356,357,1,0,0,0,357,
        360,1,0,0,0,358,359,5,42,0,0,359,361,3,34,17,0,360,358,1,0,0,0,360,
        361,1,0,0,0,361,362,1,0,0,0,362,363,5,29,0,0,363,47,1,0,0,0,364,
        365,3,14,7,0,365,366,5,5,0,0,366,367,3,34,17,0,367,49,1,0,0,0,368,
        369,5,44,0,0,369,370,3,64,32,0,370,371,5,45,0,0,371,372,3,34,17,
        0,372,373,5,29,0,0,373,51,1,0,0,0,374,375,5,46,0,0,375,376,3,34,
        17,0,376,377,5,47,0,0,377,378,3,64,32,0,378,53,1,0,0,0,379,380,5,
        48,0,0,380,381,3,34,17,0,381,382,5,29,0,0,382,55,1,0,0,0,383,384,
        5,49,0,0,384,385,5,64,0,0,385,386,5,8,0,0,386,387,3,64,32,0,387,
        388,5,38,0,0,388,391,3,64,32,0,389,390,5,50,0,0,390,392,3,64,32,
        0,391,389,1,0,0,0,391,392,1,0,0,0,392,393,1,0,0,0,393,394,5,45,0,
        0,394,395,3,34,17,0,395,396,5,29,0,0,396,57,1,0,0,0,397,399,5,51,
        0,0,398,400,3,64,32,0,399,398,1,0,0,0,399,400,1,0,0,0,400,59,1,0,
        0,0,401,402,5,52,0,0,402,61,1,0,0,0,403,420,5,64,0,0,404,405,5,2,
        0,0,405,419,5,64,0,0,406,407,5,10,0,0,407,412,3,64,32,0,408,409,
        5,3,0,0,409,411,3,64,32,0,410,408,1,0,0,0,411,414,1,0,0,0,412,410,
        1,0,0,0,412,413,1,0,0,0,413,415,1,0,0,0,414,412,1,0,0,0,415,416,
        5,11,0,0,416,419,1,0,0,0,417,419,5,12,0,0,418,404,1,0,0,0,418,406,
        1,0,0,0,418,417,1,0,0,0,419,422,1,0,0,0,420,418,1,0,0,0,420,421,
        1,0,0,0,421,63,1,0,0,0,422,420,1,0,0,0,423,427,3,68,34,0,424,425,
        3,66,33,0,425,426,3,68,34,0,426,428,1,0,0,0,427,424,1,0,0,0,427,
        428,1,0,0,0,428,65,1,0,0,0,429,430,7,0,0,0,430,67,1,0,0,0,431,433,
        7,1,0,0,432,431,1,0,0,0,432,433,1,0,0,0,433,434,1,0,0,0,434,440,
        3,72,36,0,435,436,3,70,35,0,436,437,3,72,36,0,437,439,1,0,0,0,438,
        435,1,0,0,0,439,442,1,0,0,0,440,438,1,0,0,0,440,441,1,0,0,0,441,
        69,1,0,0,0,442,440,1,0,0,0,443,444,7,2,0,0,444,71,1,0,0,0,445,451,
        3,76,38,0,446,447,3,74,37,0,447,448,3,76,38,0,448,450,1,0,0,0,449,
        446,1,0,0,0,450,453,1,0,0,0,451,449,1,0,0,0,451,452,1,0,0,0,452,
        73,1,0,0,0,453,451,1,0,0,0,454,455,7,3,0,0,455,75,1,0,0,0,456,485,
        5,65,0,0,457,485,5,66,0,0,458,464,3,62,31,0,459,461,5,6,0,0,460,
        462,3,42,21,0,461,460,1,0,0,0,461,462,1,0,0,0,462,463,1,0,0,0,463,
        465,5,7,0,0,464,459,1,0,0,0,464,465,1,0,0,0,465,485,1,0,0,0,466,
        467,5,6,0,0,467,468,3,64,32,0,468,469,5,7,0,0,469,485,1,0,0,0,470,
        471,5,58,0,0,471,485,3,76,38,0,472,481,5,19,0,0,473,478,3,78,39,
        0,474,475,5,3,0,0,475,477,3,78,39,0,476,474,1,0,0,0,477,480,1,0,
        0,0,478,476,1,0,0,0,478,479,1,0,0,0,479,482,1,0,0,0,480,478,1,0,
        0,0,481,473,1,0,0,0,481,482,1,0,0,0,482,483,1,0,0,0,483,485,5,20,
        0,0,484,456,1,0,0,0,484,457,1,0,0,0,484,458,1,0,0,0,484,466,1,0,
        0,0,484,470,1,0,0,0,484,472,1,0,0,0,485,77,1,0,0,0,486,489,3,64,
        32,0,487,488,5,63,0,0,488,490,3,64,32,0,489,487,1,0,0,0,489,490,
        1,0,0,0,490,79,1,0,0,0,49,83,91,99,105,119,125,131,145,154,161,172,
        178,183,195,206,217,221,227,230,234,246,250,260,279,289,303,312,
        315,322,336,341,353,356,360,391,399,412,418,420,427,432,440,451,
        461,464,478,481,484,489
    ]

class Modula2Parser ( Parser ):

    grammarFileName = "Modula2.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'.'", "','", "'='", "':'", "'('", 
                     "')'", "':='", "'|'", "'['", "']'", "'^'", "'#'", "'<'", 
                     "'<='", "'>'", "'>='", "'&'", "'{'", "'}'", "'MODULE'", 
                     "'IMPORT'", "'EXPORT'", "'FROM'", "'QUALIFIED'", "'DEFINITION'", 
                     "'IMPLEMENTATION'", "'BEGIN'", "'END'", "'CONST'", 
                     "'TYPE'", "'VAR'", "'PROCEDURE'", "'ARRAY'", "'OF'", 
                     "'RECORD'", "'POINTER'", "'TO'", "'IF'", "'THEN'", 
                     "'ELSIF'", "'ELSE'", "'CASE'", "'WHILE'", "'DO'", "'REPEAT'", 
                     "'UNTIL'", "'LOOP'", "'FOR'", "'BY'", "'RETURN'", "'EXIT'", 
                     "'IN'", "'OR'", "'DIV'", "'MOD'", "'AND'", "'NOT'", 
                     "'+'", "'-'", "'*'", "'/'", "'..'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "MODULE_K", "IMPORT_K", "EXPORT_K", "FROM_K", 
                      "QUALIFIED_K", "DEFINITION_K", "IMPLEMENTATION_K", 
                      "BEGIN_K", "END_K", "CONST_K", "TYPE_K", "VAR_K", 
                      "PROCEDURE_K", "ARRAY_K", "OF_K", "RECORD_K", "POINTER_K", 
                      "TO_K", "IF_K", "THEN_K", "ELSIF_K", "ELSE_K", "CASE_K", 
                      "WHILE_K", "DO_K", "REPEAT_K", "UNTIL_K", "LOOP_K", 
                      "FOR_K", "BY_K", "RETURN_K", "EXIT_K", "IN_K", "OR_K", 
                      "DIV_K", "MOD_K", "AND_K", "NOT_K", "PLUS", "MINUS", 
                      "TIMES", "DIV", "RANGE_K", "ID", "NUMBER", "STRING", 
                      "WS", "COMMENT" ]

    RULE_program = 0
    RULE_compilation_unit = 1
    RULE_main_module = 2
    RULE_definition_module = 3
    RULE_implementation_module = 4
    RULE_import_list = 5
    RULE_export_list = 6
    RULE_id_list = 7
    RULE_block = 8
    RULE_declaration = 9
    RULE_procedure_declaration = 10
    RULE_formal_params = 11
    RULE_fp_section = 12
    RULE_type_ = 13
    RULE_array_type = 14
    RULE_pointer_type = 15
    RULE_record_type = 16
    RULE_statement_sequence = 17
    RULE_statement = 18
    RULE_assignment = 19
    RULE_procedure_call = 20
    RULE_actual_params = 21
    RULE_if_statement = 22
    RULE_case_statement = 23
    RULE_case_item = 24
    RULE_while_statement = 25
    RULE_repeat_statement = 26
    RULE_loop_statement = 27
    RULE_for_statement = 28
    RULE_return_statement = 29
    RULE_exit_statement = 30
    RULE_designator = 31
    RULE_expression = 32
    RULE_rel_op = 33
    RULE_simple_expression = 34
    RULE_add_op = 35
    RULE_term = 36
    RULE_mul_op = 37
    RULE_factor = 38
    RULE_element = 39

    ruleNames =  [ "program", "compilation_unit", "main_module", "definition_module", 
                   "implementation_module", "import_list", "export_list", 
                   "id_list", "block", "declaration", "procedure_declaration", 
                   "formal_params", "fp_section", "type_", "array_type", 
                   "pointer_type", "record_type", "statement_sequence", 
                   "statement", "assignment", "procedure_call", "actual_params", 
                   "if_statement", "case_statement", "case_item", "while_statement", 
                   "repeat_statement", "loop_statement", "for_statement", 
                   "return_statement", "exit_statement", "designator", "expression", 
                   "rel_op", "simple_expression", "add_op", "term", "mul_op", 
                   "factor", "element" ]

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
    T__18=19
    T__19=20
    MODULE_K=21
    IMPORT_K=22
    EXPORT_K=23
    FROM_K=24
    QUALIFIED_K=25
    DEFINITION_K=26
    IMPLEMENTATION_K=27
    BEGIN_K=28
    END_K=29
    CONST_K=30
    TYPE_K=31
    VAR_K=32
    PROCEDURE_K=33
    ARRAY_K=34
    OF_K=35
    RECORD_K=36
    POINTER_K=37
    TO_K=38
    IF_K=39
    THEN_K=40
    ELSIF_K=41
    ELSE_K=42
    CASE_K=43
    WHILE_K=44
    DO_K=45
    REPEAT_K=46
    UNTIL_K=47
    LOOP_K=48
    FOR_K=49
    BY_K=50
    RETURN_K=51
    EXIT_K=52
    IN_K=53
    OR_K=54
    DIV_K=55
    MOD_K=56
    AND_K=57
    NOT_K=58
    PLUS=59
    MINUS=60
    TIMES=61
    DIV=62
    RANGE_K=63
    ID=64
    NUMBER=65
    STRING=66
    WS=67
    COMMENT=68

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
            return self.getToken(Modula2Parser.EOF, 0)

        def compilation_unit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Modula2Parser.Compilation_unitContext)
            else:
                return self.getTypedRuleContext(Modula2Parser.Compilation_unitContext,i)


        def getRuleIndex(self):
            return Modula2Parser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = Modula2Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 203423744) != 0):
                self.state = 80
                self.compilation_unit()
                self.state = 85
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 86
            self.match(Modula2Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Compilation_unitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def main_module(self):
            return self.getTypedRuleContext(Modula2Parser.Main_moduleContext,0)


        def definition_module(self):
            return self.getTypedRuleContext(Modula2Parser.Definition_moduleContext,0)


        def implementation_module(self):
            return self.getTypedRuleContext(Modula2Parser.Implementation_moduleContext,0)


        def getRuleIndex(self):
            return Modula2Parser.RULE_compilation_unit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompilation_unit" ):
                return visitor.visitCompilation_unit(self)
            else:
                return visitor.visitChildren(self)




    def compilation_unit(self):

        localctx = Modula2Parser.Compilation_unitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_compilation_unit)
        try:
            self.state = 91
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                self.enterOuterAlt(localctx, 1)
                self.state = 88
                self.main_module()
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 2)
                self.state = 89
                self.definition_module()
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 3)
                self.state = 90
                self.implementation_module()
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


    class Main_moduleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MODULE_K(self):
            return self.getToken(Modula2Parser.MODULE_K, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(Modula2Parser.ID)
            else:
                return self.getToken(Modula2Parser.ID, i)

        def block(self):
            return self.getTypedRuleContext(Modula2Parser.BlockContext,0)


        def import_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Modula2Parser.Import_listContext)
            else:
                return self.getTypedRuleContext(Modula2Parser.Import_listContext,i)


        def export_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Modula2Parser.Export_listContext)
            else:
                return self.getTypedRuleContext(Modula2Parser.Export_listContext,i)


        def getRuleIndex(self):
            return Modula2Parser.RULE_main_module

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMain_module" ):
                return visitor.visitMain_module(self)
            else:
                return visitor.visitChildren(self)




    def main_module(self):

        localctx = Modula2Parser.Main_moduleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_main_module)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(Modula2Parser.MODULE_K)
            self.state = 94
            self.match(Modula2Parser.ID)
            self.state = 95
            self.match(Modula2Parser.T__0)
            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==22 or _la==24:
                self.state = 96
                self.import_list()
                self.state = 101
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==23 or _la==25:
                self.state = 102
                self.export_list()
                self.state = 107
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 108
            self.block()
            self.state = 109
            self.match(Modula2Parser.ID)
            self.state = 110
            self.match(Modula2Parser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Definition_moduleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEFINITION_K(self):
            return self.getToken(Modula2Parser.DEFINITION_K, 0)

        def MODULE_K(self):
            return self.getToken(Modula2Parser.MODULE_K, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(Modula2Parser.ID)
            else:
                return self.getToken(Modula2Parser.ID, i)

        def END_K(self):
            return self.getToken(Modula2Parser.END_K, 0)

        def import_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Modula2Parser.Import_listContext)
            else:
                return self.getTypedRuleContext(Modula2Parser.Import_listContext,i)


        def export_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Modula2Parser.Export_listContext)
            else:
                return self.getTypedRuleContext(Modula2Parser.Export_listContext,i)


        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Modula2Parser.DeclarationContext)
            else:
                return self.getTypedRuleContext(Modula2Parser.DeclarationContext,i)


        def getRuleIndex(self):
            return Modula2Parser.RULE_definition_module

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefinition_module" ):
                return visitor.visitDefinition_module(self)
            else:
                return visitor.visitChildren(self)




    def definition_module(self):

        localctx = Modula2Parser.Definition_moduleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_definition_module)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(Modula2Parser.DEFINITION_K)
            self.state = 113
            self.match(Modula2Parser.MODULE_K)
            self.state = 114
            self.match(Modula2Parser.ID)
            self.state = 115
            self.match(Modula2Parser.T__0)
            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==22 or _la==24:
                self.state = 116
                self.import_list()
                self.state = 121
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==23 or _la==25:
                self.state = 122
                self.export_list()
                self.state = 127
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 16106127360) != 0):
                self.state = 128
                self.declaration()
                self.state = 133
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 134
            self.match(Modula2Parser.END_K)
            self.state = 135
            self.match(Modula2Parser.ID)
            self.state = 136
            self.match(Modula2Parser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Implementation_moduleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IMPLEMENTATION_K(self):
            return self.getToken(Modula2Parser.IMPLEMENTATION_K, 0)

        def MODULE_K(self):
            return self.getToken(Modula2Parser.MODULE_K, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(Modula2Parser.ID)
            else:
                return self.getToken(Modula2Parser.ID, i)

        def block(self):
            return self.getTypedRuleContext(Modula2Parser.BlockContext,0)


        def import_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Modula2Parser.Import_listContext)
            else:
                return self.getTypedRuleContext(Modula2Parser.Import_listContext,i)


        def getRuleIndex(self):
            return Modula2Parser.RULE_implementation_module

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImplementation_module" ):
                return visitor.visitImplementation_module(self)
            else:
                return visitor.visitChildren(self)




    def implementation_module(self):

        localctx = Modula2Parser.Implementation_moduleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_implementation_module)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.match(Modula2Parser.IMPLEMENTATION_K)
            self.state = 139
            self.match(Modula2Parser.MODULE_K)
            self.state = 140
            self.match(Modula2Parser.ID)
            self.state = 141
            self.match(Modula2Parser.T__0)
            self.state = 145
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==22 or _la==24:
                self.state = 142
                self.import_list()
                self.state = 147
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 148
            self.block()
            self.state = 149
            self.match(Modula2Parser.ID)
            self.state = 150
            self.match(Modula2Parser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Import_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IMPORT_K(self):
            return self.getToken(Modula2Parser.IMPORT_K, 0)

        def id_list(self):
            return self.getTypedRuleContext(Modula2Parser.Id_listContext,0)


        def FROM_K(self):
            return self.getToken(Modula2Parser.FROM_K, 0)

        def ID(self):
            return self.getToken(Modula2Parser.ID, 0)

        def getRuleIndex(self):
            return Modula2Parser.RULE_import_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImport_list" ):
                return visitor.visitImport_list(self)
            else:
                return visitor.visitChildren(self)




    def import_list(self):

        localctx = Modula2Parser.Import_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_import_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==24:
                self.state = 152
                self.match(Modula2Parser.FROM_K)
                self.state = 153
                self.match(Modula2Parser.ID)


            self.state = 156
            self.match(Modula2Parser.IMPORT_K)
            self.state = 157
            self.id_list()
            self.state = 158
            self.match(Modula2Parser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Export_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXPORT_K(self):
            return self.getToken(Modula2Parser.EXPORT_K, 0)

        def id_list(self):
            return self.getTypedRuleContext(Modula2Parser.Id_listContext,0)


        def QUALIFIED_K(self):
            return self.getToken(Modula2Parser.QUALIFIED_K, 0)

        def getRuleIndex(self):
            return Modula2Parser.RULE_export_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExport_list" ):
                return visitor.visitExport_list(self)
            else:
                return visitor.visitChildren(self)




    def export_list(self):

        localctx = Modula2Parser.Export_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_export_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25:
                self.state = 160
                self.match(Modula2Parser.QUALIFIED_K)


            self.state = 163
            self.match(Modula2Parser.EXPORT_K)
            self.state = 164
            self.id_list()
            self.state = 165
            self.match(Modula2Parser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Id_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(Modula2Parser.ID)
            else:
                return self.getToken(Modula2Parser.ID, i)

        def getRuleIndex(self):
            return Modula2Parser.RULE_id_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId_list" ):
                return visitor.visitId_list(self)
            else:
                return visitor.visitChildren(self)




    def id_list(self):

        localctx = Modula2Parser.Id_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_id_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.match(Modula2Parser.ID)
            self.state = 172
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 168
                self.match(Modula2Parser.T__2)
                self.state = 169
                self.match(Modula2Parser.ID)
                self.state = 174
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def END_K(self):
            return self.getToken(Modula2Parser.END_K, 0)

        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Modula2Parser.DeclarationContext)
            else:
                return self.getTypedRuleContext(Modula2Parser.DeclarationContext,i)


        def BEGIN_K(self):
            return self.getToken(Modula2Parser.BEGIN_K, 0)

        def statement_sequence(self):
            return self.getTypedRuleContext(Modula2Parser.Statement_sequenceContext,0)


        def getRuleIndex(self):
            return Modula2Parser.RULE_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = Modula2Parser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 16106127360) != 0):
                self.state = 175
                self.declaration()
                self.state = 180
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 183
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 181
                self.match(Modula2Parser.BEGIN_K)
                self.state = 182
                self.statement_sequence()


            self.state = 185
            self.match(Modula2Parser.END_K)
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

        def CONST_K(self):
            return self.getToken(Modula2Parser.CONST_K, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(Modula2Parser.ID)
            else:
                return self.getToken(Modula2Parser.ID, i)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Modula2Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(Modula2Parser.ExpressionContext,i)


        def TYPE_K(self):
            return self.getToken(Modula2Parser.TYPE_K, 0)

        def type_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Modula2Parser.Type_Context)
            else:
                return self.getTypedRuleContext(Modula2Parser.Type_Context,i)


        def VAR_K(self):
            return self.getToken(Modula2Parser.VAR_K, 0)

        def id_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Modula2Parser.Id_listContext)
            else:
                return self.getTypedRuleContext(Modula2Parser.Id_listContext,i)


        def procedure_declaration(self):
            return self.getTypedRuleContext(Modula2Parser.Procedure_declarationContext,0)


        def getRuleIndex(self):
            return Modula2Parser.RULE_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = Modula2Parser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_declaration)
        self._la = 0 # Token type
        try:
            self.state = 221
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [30]:
                self.enterOuterAlt(localctx, 1)
                self.state = 187
                self.match(Modula2Parser.CONST_K)
                self.state = 195
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==64:
                    self.state = 188
                    self.match(Modula2Parser.ID)
                    self.state = 189
                    self.match(Modula2Parser.T__3)
                    self.state = 190
                    self.expression()
                    self.state = 191
                    self.match(Modula2Parser.T__0)
                    self.state = 197
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 2)
                self.state = 198
                self.match(Modula2Parser.TYPE_K)
                self.state = 206
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==64:
                    self.state = 199
                    self.match(Modula2Parser.ID)
                    self.state = 200
                    self.match(Modula2Parser.T__3)
                    self.state = 201
                    self.type_()
                    self.state = 202
                    self.match(Modula2Parser.T__0)
                    self.state = 208
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 3)
                self.state = 209
                self.match(Modula2Parser.VAR_K)
                self.state = 217
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==64:
                    self.state = 210
                    self.id_list()
                    self.state = 211
                    self.match(Modula2Parser.T__4)
                    self.state = 212
                    self.type_()
                    self.state = 213
                    self.match(Modula2Parser.T__0)
                    self.state = 219
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 4)
                self.state = 220
                self.procedure_declaration()
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


    class Procedure_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROCEDURE_K(self):
            return self.getToken(Modula2Parser.PROCEDURE_K, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(Modula2Parser.ID)
            else:
                return self.getToken(Modula2Parser.ID, i)

        def block(self):
            return self.getTypedRuleContext(Modula2Parser.BlockContext,0)


        def formal_params(self):
            return self.getTypedRuleContext(Modula2Parser.Formal_paramsContext,0)


        def getRuleIndex(self):
            return Modula2Parser.RULE_procedure_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProcedure_declaration" ):
                return visitor.visitProcedure_declaration(self)
            else:
                return visitor.visitChildren(self)




    def procedure_declaration(self):

        localctx = Modula2Parser.Procedure_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_procedure_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self.match(Modula2Parser.PROCEDURE_K)
            self.state = 224
            self.match(Modula2Parser.ID)
            self.state = 230
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 225
                self.match(Modula2Parser.T__5)
                self.state = 227
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==32 or _la==64:
                    self.state = 226
                    self.formal_params()


                self.state = 229
                self.match(Modula2Parser.T__6)


            self.state = 234
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 232
                self.match(Modula2Parser.T__4)
                self.state = 233
                self.match(Modula2Parser.ID)


            self.state = 236
            self.match(Modula2Parser.T__0)
            self.state = 237
            self.block()
            self.state = 238
            self.match(Modula2Parser.ID)
            self.state = 239
            self.match(Modula2Parser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Formal_paramsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fp_section(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Modula2Parser.Fp_sectionContext)
            else:
                return self.getTypedRuleContext(Modula2Parser.Fp_sectionContext,i)


        def getRuleIndex(self):
            return Modula2Parser.RULE_formal_params

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFormal_params" ):
                return visitor.visitFormal_params(self)
            else:
                return visitor.visitChildren(self)




    def formal_params(self):

        localctx = Modula2Parser.Formal_paramsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_formal_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.fp_section()
            self.state = 246
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 242
                self.match(Modula2Parser.T__0)
                self.state = 243
                self.fp_section()
                self.state = 248
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Fp_sectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_list(self):
            return self.getTypedRuleContext(Modula2Parser.Id_listContext,0)


        def type_(self):
            return self.getTypedRuleContext(Modula2Parser.Type_Context,0)


        def VAR_K(self):
            return self.getToken(Modula2Parser.VAR_K, 0)

        def getRuleIndex(self):
            return Modula2Parser.RULE_fp_section

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFp_section" ):
                return visitor.visitFp_section(self)
            else:
                return visitor.visitChildren(self)




    def fp_section(self):

        localctx = Modula2Parser.Fp_sectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_fp_section)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==32:
                self.state = 249
                self.match(Modula2Parser.VAR_K)


            self.state = 252
            self.id_list()
            self.state = 253
            self.match(Modula2Parser.T__4)
            self.state = 254
            self.type_()
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

        def ID(self):
            return self.getToken(Modula2Parser.ID, 0)

        def array_type(self):
            return self.getTypedRuleContext(Modula2Parser.Array_typeContext,0)


        def pointer_type(self):
            return self.getTypedRuleContext(Modula2Parser.Pointer_typeContext,0)


        def record_type(self):
            return self.getTypedRuleContext(Modula2Parser.Record_typeContext,0)


        def getRuleIndex(self):
            return Modula2Parser.RULE_type_

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_" ):
                return visitor.visitType_(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = Modula2Parser.Type_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_type_)
        try:
            self.state = 260
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [64]:
                self.enterOuterAlt(localctx, 1)
                self.state = 256
                self.match(Modula2Parser.ID)
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 2)
                self.state = 257
                self.array_type()
                pass
            elif token in [37]:
                self.enterOuterAlt(localctx, 3)
                self.state = 258
                self.pointer_type()
                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 4)
                self.state = 259
                self.record_type()
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


    class Array_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY_K(self):
            return self.getToken(Modula2Parser.ARRAY_K, 0)

        def expression(self):
            return self.getTypedRuleContext(Modula2Parser.ExpressionContext,0)


        def OF_K(self):
            return self.getToken(Modula2Parser.OF_K, 0)

        def type_(self):
            return self.getTypedRuleContext(Modula2Parser.Type_Context,0)


        def getRuleIndex(self):
            return Modula2Parser.RULE_array_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




    def array_type(self):

        localctx = Modula2Parser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self.match(Modula2Parser.ARRAY_K)
            self.state = 263
            self.expression()
            self.state = 264
            self.match(Modula2Parser.OF_K)
            self.state = 265
            self.type_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Pointer_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def POINTER_K(self):
            return self.getToken(Modula2Parser.POINTER_K, 0)

        def TO_K(self):
            return self.getToken(Modula2Parser.TO_K, 0)

        def type_(self):
            return self.getTypedRuleContext(Modula2Parser.Type_Context,0)


        def getRuleIndex(self):
            return Modula2Parser.RULE_pointer_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPointer_type" ):
                return visitor.visitPointer_type(self)
            else:
                return visitor.visitChildren(self)




    def pointer_type(self):

        localctx = Modula2Parser.Pointer_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_pointer_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            self.match(Modula2Parser.POINTER_K)
            self.state = 268
            self.match(Modula2Parser.TO_K)
            self.state = 269
            self.type_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Record_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RECORD_K(self):
            return self.getToken(Modula2Parser.RECORD_K, 0)

        def END_K(self):
            return self.getToken(Modula2Parser.END_K, 0)

        def id_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Modula2Parser.Id_listContext)
            else:
                return self.getTypedRuleContext(Modula2Parser.Id_listContext,i)


        def type_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Modula2Parser.Type_Context)
            else:
                return self.getTypedRuleContext(Modula2Parser.Type_Context,i)


        def getRuleIndex(self):
            return Modula2Parser.RULE_record_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRecord_type" ):
                return visitor.visitRecord_type(self)
            else:
                return visitor.visitChildren(self)




    def record_type(self):

        localctx = Modula2Parser.Record_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_record_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            self.match(Modula2Parser.RECORD_K)
            self.state = 279
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==64:
                self.state = 272
                self.id_list()
                self.state = 273
                self.match(Modula2Parser.T__4)
                self.state = 274
                self.type_()
                self.state = 275
                self.match(Modula2Parser.T__0)
                self.state = 281
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 282
            self.match(Modula2Parser.END_K)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Statement_sequenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Modula2Parser.StatementContext)
            else:
                return self.getTypedRuleContext(Modula2Parser.StatementContext,i)


        def getRuleIndex(self):
            return Modula2Parser.RULE_statement_sequence

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement_sequence" ):
                return visitor.visitStatement_sequence(self)
            else:
                return visitor.visitChildren(self)




    def statement_sequence(self):

        localctx = Modula2Parser.Statement_sequenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_statement_sequence)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self.statement()
            self.state = 289
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 285
                self.match(Modula2Parser.T__0)
                self.state = 286
                self.statement()
                self.state = 291
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

        def assignment(self):
            return self.getTypedRuleContext(Modula2Parser.AssignmentContext,0)


        def procedure_call(self):
            return self.getTypedRuleContext(Modula2Parser.Procedure_callContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(Modula2Parser.If_statementContext,0)


        def case_statement(self):
            return self.getTypedRuleContext(Modula2Parser.Case_statementContext,0)


        def while_statement(self):
            return self.getTypedRuleContext(Modula2Parser.While_statementContext,0)


        def repeat_statement(self):
            return self.getTypedRuleContext(Modula2Parser.Repeat_statementContext,0)


        def loop_statement(self):
            return self.getTypedRuleContext(Modula2Parser.Loop_statementContext,0)


        def for_statement(self):
            return self.getTypedRuleContext(Modula2Parser.For_statementContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(Modula2Parser.Return_statementContext,0)


        def exit_statement(self):
            return self.getTypedRuleContext(Modula2Parser.Exit_statementContext,0)


        def getRuleIndex(self):
            return Modula2Parser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = Modula2Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_statement)
        try:
            self.state = 303
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 292
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 293
                self.procedure_call()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 294
                self.if_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 295
                self.case_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 296
                self.while_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 297
                self.repeat_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 298
                self.loop_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 299
                self.for_statement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 300
                self.return_statement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 301
                self.exit_statement()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)

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

        def designator(self):
            return self.getTypedRuleContext(Modula2Parser.DesignatorContext,0)


        def expression(self):
            return self.getTypedRuleContext(Modula2Parser.ExpressionContext,0)


        def getRuleIndex(self):
            return Modula2Parser.RULE_assignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = Modula2Parser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self.designator()
            self.state = 306
            self.match(Modula2Parser.T__7)
            self.state = 307
            self.expression()
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

        def designator(self):
            return self.getTypedRuleContext(Modula2Parser.DesignatorContext,0)


        def actual_params(self):
            return self.getTypedRuleContext(Modula2Parser.Actual_paramsContext,0)


        def getRuleIndex(self):
            return Modula2Parser.RULE_procedure_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProcedure_call" ):
                return visitor.visitProcedure_call(self)
            else:
                return visitor.visitChildren(self)




    def procedure_call(self):

        localctx = Modula2Parser.Procedure_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_procedure_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            self.designator()
            self.state = 315
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 310
                self.match(Modula2Parser.T__5)
                self.state = 312
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 6)) & ~0x3f) == 0 and ((1 << (_la - 6)) & 2049137830453583873) != 0):
                    self.state = 311
                    self.actual_params()


                self.state = 314
                self.match(Modula2Parser.T__6)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Actual_paramsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Modula2Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(Modula2Parser.ExpressionContext,i)


        def getRuleIndex(self):
            return Modula2Parser.RULE_actual_params

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitActual_params" ):
                return visitor.visitActual_params(self)
            else:
                return visitor.visitChildren(self)




    def actual_params(self):

        localctx = Modula2Parser.Actual_paramsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_actual_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 317
            self.expression()
            self.state = 322
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 318
                self.match(Modula2Parser.T__2)
                self.state = 319
                self.expression()
                self.state = 324
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
            return self.getToken(Modula2Parser.IF_K, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Modula2Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(Modula2Parser.ExpressionContext,i)


        def THEN_K(self, i:int=None):
            if i is None:
                return self.getTokens(Modula2Parser.THEN_K)
            else:
                return self.getToken(Modula2Parser.THEN_K, i)

        def statement_sequence(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Modula2Parser.Statement_sequenceContext)
            else:
                return self.getTypedRuleContext(Modula2Parser.Statement_sequenceContext,i)


        def END_K(self):
            return self.getToken(Modula2Parser.END_K, 0)

        def ELSIF_K(self, i:int=None):
            if i is None:
                return self.getTokens(Modula2Parser.ELSIF_K)
            else:
                return self.getToken(Modula2Parser.ELSIF_K, i)

        def ELSE_K(self):
            return self.getToken(Modula2Parser.ELSE_K, 0)

        def getRuleIndex(self):
            return Modula2Parser.RULE_if_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = Modula2Parser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_if_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 325
            self.match(Modula2Parser.IF_K)
            self.state = 326
            self.expression()
            self.state = 327
            self.match(Modula2Parser.THEN_K)
            self.state = 328
            self.statement_sequence()
            self.state = 336
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==41:
                self.state = 329
                self.match(Modula2Parser.ELSIF_K)
                self.state = 330
                self.expression()
                self.state = 331
                self.match(Modula2Parser.THEN_K)
                self.state = 332
                self.statement_sequence()
                self.state = 338
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 341
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==42:
                self.state = 339
                self.match(Modula2Parser.ELSE_K)
                self.state = 340
                self.statement_sequence()


            self.state = 343
            self.match(Modula2Parser.END_K)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Case_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CASE_K(self):
            return self.getToken(Modula2Parser.CASE_K, 0)

        def expression(self):
            return self.getTypedRuleContext(Modula2Parser.ExpressionContext,0)


        def OF_K(self):
            return self.getToken(Modula2Parser.OF_K, 0)

        def END_K(self):
            return self.getToken(Modula2Parser.END_K, 0)

        def case_item(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Modula2Parser.Case_itemContext)
            else:
                return self.getTypedRuleContext(Modula2Parser.Case_itemContext,i)


        def ELSE_K(self):
            return self.getToken(Modula2Parser.ELSE_K, 0)

        def statement_sequence(self):
            return self.getTypedRuleContext(Modula2Parser.Statement_sequenceContext,0)


        def getRuleIndex(self):
            return Modula2Parser.RULE_case_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCase_statement" ):
                return visitor.visitCase_statement(self)
            else:
                return visitor.visitChildren(self)




    def case_statement(self):

        localctx = Modula2Parser.Case_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_case_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 345
            self.match(Modula2Parser.CASE_K)
            self.state = 346
            self.expression()
            self.state = 347
            self.match(Modula2Parser.OF_K)
            self.state = 356
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==64:
                self.state = 348
                self.case_item()
                self.state = 353
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==9:
                    self.state = 349
                    self.match(Modula2Parser.T__8)
                    self.state = 350
                    self.case_item()
                    self.state = 355
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 360
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==42:
                self.state = 358
                self.match(Modula2Parser.ELSE_K)
                self.state = 359
                self.statement_sequence()


            self.state = 362
            self.match(Modula2Parser.END_K)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Case_itemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_list(self):
            return self.getTypedRuleContext(Modula2Parser.Id_listContext,0)


        def statement_sequence(self):
            return self.getTypedRuleContext(Modula2Parser.Statement_sequenceContext,0)


        def getRuleIndex(self):
            return Modula2Parser.RULE_case_item

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCase_item" ):
                return visitor.visitCase_item(self)
            else:
                return visitor.visitChildren(self)




    def case_item(self):

        localctx = Modula2Parser.Case_itemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_case_item)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 364
            self.id_list()
            self.state = 365
            self.match(Modula2Parser.T__4)
            self.state = 366
            self.statement_sequence()
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
            return self.getToken(Modula2Parser.WHILE_K, 0)

        def expression(self):
            return self.getTypedRuleContext(Modula2Parser.ExpressionContext,0)


        def DO_K(self):
            return self.getToken(Modula2Parser.DO_K, 0)

        def statement_sequence(self):
            return self.getTypedRuleContext(Modula2Parser.Statement_sequenceContext,0)


        def END_K(self):
            return self.getToken(Modula2Parser.END_K, 0)

        def getRuleIndex(self):
            return Modula2Parser.RULE_while_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_statement" ):
                return visitor.visitWhile_statement(self)
            else:
                return visitor.visitChildren(self)




    def while_statement(self):

        localctx = Modula2Parser.While_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_while_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 368
            self.match(Modula2Parser.WHILE_K)
            self.state = 369
            self.expression()
            self.state = 370
            self.match(Modula2Parser.DO_K)
            self.state = 371
            self.statement_sequence()
            self.state = 372
            self.match(Modula2Parser.END_K)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Repeat_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REPEAT_K(self):
            return self.getToken(Modula2Parser.REPEAT_K, 0)

        def statement_sequence(self):
            return self.getTypedRuleContext(Modula2Parser.Statement_sequenceContext,0)


        def UNTIL_K(self):
            return self.getToken(Modula2Parser.UNTIL_K, 0)

        def expression(self):
            return self.getTypedRuleContext(Modula2Parser.ExpressionContext,0)


        def getRuleIndex(self):
            return Modula2Parser.RULE_repeat_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRepeat_statement" ):
                return visitor.visitRepeat_statement(self)
            else:
                return visitor.visitChildren(self)




    def repeat_statement(self):

        localctx = Modula2Parser.Repeat_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_repeat_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 374
            self.match(Modula2Parser.REPEAT_K)
            self.state = 375
            self.statement_sequence()
            self.state = 376
            self.match(Modula2Parser.UNTIL_K)
            self.state = 377
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Loop_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LOOP_K(self):
            return self.getToken(Modula2Parser.LOOP_K, 0)

        def statement_sequence(self):
            return self.getTypedRuleContext(Modula2Parser.Statement_sequenceContext,0)


        def END_K(self):
            return self.getToken(Modula2Parser.END_K, 0)

        def getRuleIndex(self):
            return Modula2Parser.RULE_loop_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoop_statement" ):
                return visitor.visitLoop_statement(self)
            else:
                return visitor.visitChildren(self)




    def loop_statement(self):

        localctx = Modula2Parser.Loop_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_loop_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 379
            self.match(Modula2Parser.LOOP_K)
            self.state = 380
            self.statement_sequence()
            self.state = 381
            self.match(Modula2Parser.END_K)
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
            return self.getToken(Modula2Parser.FOR_K, 0)

        def ID(self):
            return self.getToken(Modula2Parser.ID, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Modula2Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(Modula2Parser.ExpressionContext,i)


        def TO_K(self):
            return self.getToken(Modula2Parser.TO_K, 0)

        def DO_K(self):
            return self.getToken(Modula2Parser.DO_K, 0)

        def statement_sequence(self):
            return self.getTypedRuleContext(Modula2Parser.Statement_sequenceContext,0)


        def END_K(self):
            return self.getToken(Modula2Parser.END_K, 0)

        def BY_K(self):
            return self.getToken(Modula2Parser.BY_K, 0)

        def getRuleIndex(self):
            return Modula2Parser.RULE_for_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_statement" ):
                return visitor.visitFor_statement(self)
            else:
                return visitor.visitChildren(self)




    def for_statement(self):

        localctx = Modula2Parser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_for_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 383
            self.match(Modula2Parser.FOR_K)
            self.state = 384
            self.match(Modula2Parser.ID)
            self.state = 385
            self.match(Modula2Parser.T__7)
            self.state = 386
            self.expression()
            self.state = 387
            self.match(Modula2Parser.TO_K)
            self.state = 388
            self.expression()
            self.state = 391
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==50:
                self.state = 389
                self.match(Modula2Parser.BY_K)
                self.state = 390
                self.expression()


            self.state = 393
            self.match(Modula2Parser.DO_K)
            self.state = 394
            self.statement_sequence()
            self.state = 395
            self.match(Modula2Parser.END_K)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN_K(self):
            return self.getToken(Modula2Parser.RETURN_K, 0)

        def expression(self):
            return self.getTypedRuleContext(Modula2Parser.ExpressionContext,0)


        def getRuleIndex(self):
            return Modula2Parser.RULE_return_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = Modula2Parser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_return_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 397
            self.match(Modula2Parser.RETURN_K)
            self.state = 399
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 6)) & ~0x3f) == 0 and ((1 << (_la - 6)) & 2049137830453583873) != 0):
                self.state = 398
                self.expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exit_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXIT_K(self):
            return self.getToken(Modula2Parser.EXIT_K, 0)

        def getRuleIndex(self):
            return Modula2Parser.RULE_exit_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExit_statement" ):
                return visitor.visitExit_statement(self)
            else:
                return visitor.visitChildren(self)




    def exit_statement(self):

        localctx = Modula2Parser.Exit_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_exit_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 401
            self.match(Modula2Parser.EXIT_K)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DesignatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(Modula2Parser.ID)
            else:
                return self.getToken(Modula2Parser.ID, i)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Modula2Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(Modula2Parser.ExpressionContext,i)


        def getRuleIndex(self):
            return Modula2Parser.RULE_designator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDesignator" ):
                return visitor.visitDesignator(self)
            else:
                return visitor.visitChildren(self)




    def designator(self):

        localctx = Modula2Parser.DesignatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_designator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 403
            self.match(Modula2Parser.ID)
            self.state = 420
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 5124) != 0):
                self.state = 418
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [2]:
                    self.state = 404
                    self.match(Modula2Parser.T__1)
                    self.state = 405
                    self.match(Modula2Parser.ID)
                    pass
                elif token in [10]:
                    self.state = 406
                    self.match(Modula2Parser.T__9)
                    self.state = 407
                    self.expression()
                    self.state = 412
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==3:
                        self.state = 408
                        self.match(Modula2Parser.T__2)
                        self.state = 409
                        self.expression()
                        self.state = 414
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 415
                    self.match(Modula2Parser.T__10)
                    pass
                elif token in [12]:
                    self.state = 417
                    self.match(Modula2Parser.T__11)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 422
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def simple_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Modula2Parser.Simple_expressionContext)
            else:
                return self.getTypedRuleContext(Modula2Parser.Simple_expressionContext,i)


        def rel_op(self):
            return self.getTypedRuleContext(Modula2Parser.Rel_opContext,0)


        def getRuleIndex(self):
            return Modula2Parser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = Modula2Parser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 423
            self.simple_expression()
            self.state = 427
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 9007199254994960) != 0):
                self.state = 424
                self.rel_op()
                self.state = 425
                self.simple_expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Rel_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IN_K(self):
            return self.getToken(Modula2Parser.IN_K, 0)

        def getRuleIndex(self):
            return Modula2Parser.RULE_rel_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRel_op" ):
                return visitor.visitRel_op(self)
            else:
                return visitor.visitChildren(self)




    def rel_op(self):

        localctx = Modula2Parser.Rel_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_rel_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 429
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 9007199254994960) != 0)):
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


    class Simple_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Modula2Parser.TermContext)
            else:
                return self.getTypedRuleContext(Modula2Parser.TermContext,i)


        def add_op(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Modula2Parser.Add_opContext)
            else:
                return self.getTypedRuleContext(Modula2Parser.Add_opContext,i)


        def PLUS(self):
            return self.getToken(Modula2Parser.PLUS, 0)

        def MINUS(self):
            return self.getToken(Modula2Parser.MINUS, 0)

        def getRuleIndex(self):
            return Modula2Parser.RULE_simple_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimple_expression" ):
                return visitor.visitSimple_expression(self)
            else:
                return visitor.visitChildren(self)




    def simple_expression(self):

        localctx = Modula2Parser.Simple_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_simple_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 432
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==59 or _la==60:
                self.state = 431
                _la = self._input.LA(1)
                if not(_la==59 or _la==60):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 434
            self.term()
            self.state = 440
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1747396655419752448) != 0):
                self.state = 435
                self.add_op()
                self.state = 436
                self.term()
                self.state = 442
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Add_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(Modula2Parser.PLUS, 0)

        def MINUS(self):
            return self.getToken(Modula2Parser.MINUS, 0)

        def OR_K(self):
            return self.getToken(Modula2Parser.OR_K, 0)

        def getRuleIndex(self):
            return Modula2Parser.RULE_add_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd_op" ):
                return visitor.visitAdd_op(self)
            else:
                return visitor.visitChildren(self)




    def add_op(self):

        localctx = Modula2Parser.Add_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_add_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 443
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1747396655419752448) != 0)):
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


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Modula2Parser.FactorContext)
            else:
                return self.getTypedRuleContext(Modula2Parser.FactorContext,i)


        def mul_op(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Modula2Parser.Mul_opContext)
            else:
                return self.getTypedRuleContext(Modula2Parser.Mul_opContext,i)


        def getRuleIndex(self):
            return Modula2Parser.RULE_term

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = Modula2Parser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 445
            self.factor()
            self.state = 451
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2558044588346703872) != 0):
                self.state = 446
                self.mul_op()
                self.state = 447
                self.factor()
                self.state = 453
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Mul_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TIMES(self):
            return self.getToken(Modula2Parser.TIMES, 0)

        def DIV_K(self):
            return self.getToken(Modula2Parser.DIV_K, 0)

        def MOD_K(self):
            return self.getToken(Modula2Parser.MOD_K, 0)

        def AND_K(self):
            return self.getToken(Modula2Parser.AND_K, 0)

        def getRuleIndex(self):
            return Modula2Parser.RULE_mul_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMul_op" ):
                return visitor.visitMul_op(self)
            else:
                return visitor.visitChildren(self)




    def mul_op(self):

        localctx = Modula2Parser.Mul_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_mul_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 454
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2558044588346703872) != 0)):
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


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(Modula2Parser.NUMBER, 0)

        def STRING(self):
            return self.getToken(Modula2Parser.STRING, 0)

        def designator(self):
            return self.getTypedRuleContext(Modula2Parser.DesignatorContext,0)


        def actual_params(self):
            return self.getTypedRuleContext(Modula2Parser.Actual_paramsContext,0)


        def expression(self):
            return self.getTypedRuleContext(Modula2Parser.ExpressionContext,0)


        def NOT_K(self):
            return self.getToken(Modula2Parser.NOT_K, 0)

        def factor(self):
            return self.getTypedRuleContext(Modula2Parser.FactorContext,0)


        def element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Modula2Parser.ElementContext)
            else:
                return self.getTypedRuleContext(Modula2Parser.ElementContext,i)


        def getRuleIndex(self):
            return Modula2Parser.RULE_factor

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = Modula2Parser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.state = 484
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [65]:
                self.enterOuterAlt(localctx, 1)
                self.state = 456
                self.match(Modula2Parser.NUMBER)
                pass
            elif token in [66]:
                self.enterOuterAlt(localctx, 2)
                self.state = 457
                self.match(Modula2Parser.STRING)
                pass
            elif token in [64]:
                self.enterOuterAlt(localctx, 3)
                self.state = 458
                self.designator()
                self.state = 464
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==6:
                    self.state = 459
                    self.match(Modula2Parser.T__5)
                    self.state = 461
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if ((((_la - 6)) & ~0x3f) == 0 and ((1 << (_la - 6)) & 2049137830453583873) != 0):
                        self.state = 460
                        self.actual_params()


                    self.state = 463
                    self.match(Modula2Parser.T__6)


                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 4)
                self.state = 466
                self.match(Modula2Parser.T__5)
                self.state = 467
                self.expression()
                self.state = 468
                self.match(Modula2Parser.T__6)
                pass
            elif token in [58]:
                self.enterOuterAlt(localctx, 5)
                self.state = 470
                self.match(Modula2Parser.NOT_K)
                self.state = 471
                self.factor()
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 6)
                self.state = 472
                self.match(Modula2Parser.T__18)
                self.state = 481
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 6)) & ~0x3f) == 0 and ((1 << (_la - 6)) & 2049137830453583873) != 0):
                    self.state = 473
                    self.element()
                    self.state = 478
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==3:
                        self.state = 474
                        self.match(Modula2Parser.T__2)
                        self.state = 475
                        self.element()
                        self.state = 480
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 483
                self.match(Modula2Parser.T__19)
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


    class ElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Modula2Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(Modula2Parser.ExpressionContext,i)


        def RANGE_K(self):
            return self.getToken(Modula2Parser.RANGE_K, 0)

        def getRuleIndex(self):
            return Modula2Parser.RULE_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement" ):
                return visitor.visitElement(self)
            else:
                return visitor.visitChildren(self)




    def element(self):

        localctx = Modula2Parser.ElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_element)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 486
            self.expression()
            self.state = 489
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==63:
                self.state = 487
                self.match(Modula2Parser.RANGE_K)
                self.state = 488
                self.expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





