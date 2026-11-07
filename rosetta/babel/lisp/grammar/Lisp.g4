grammar Lisp;

program : (expression)* EOF;

expression
    : atom
    | list
    | quote
    ;

atom
    : identifier
    | number
    | string
    ;

list : '(' (expression)* ')' ;

quote : '\'' expression ;

identifier : IDENTIFIER | SYMBOL_OPERATOR ;
number : NUMBER ;
string : STRING ;

IDENTIFIER : [a-zA-Z*+/=?<>!][a-zA-Z0-9*+/=?<>!-]* ;
SYMBOL_OPERATOR : [+\-*/=<>!]+ ;
NUMBER : [+-]? [0-9]+ ('.' [0-9]+)? ;
STRING : '"' (~["\r\n])* '"' ;

NEWLINE : [\r\n]+ -> skip ;
WS : [ \t]+ -> skip ;
COMMENT : ';' ~[\r\n]* -> skip ;
