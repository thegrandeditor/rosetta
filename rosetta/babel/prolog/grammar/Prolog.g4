grammar Prolog;

program : (clause)* EOF;

clause : fact | rule | query ;

fact : term '.' ;

rule : term ':-' term_list '.' ;

query : '?-' term_list '.' ;

term_list : term (',' term)* ;

term
    : atom
    | variable
    | list
    | structure
    | '(' term ')'
    ;

structure : atom '(' term_list ')' ;

list
    : '[' ']'
    | '[' term_list ('|' term)? ']'
    ;

atom : ATOM ;
variable : VARIABLE ;

ATOM : [a-z][a-zA-Z0-9_]* | '\'' (~['\r\n])* '\'' | [+\-*/=<>!]+ ;
VARIABLE : [A-Z_][a-zA-Z0-9_]* ;
NUMBER : [0-9]+ ('.' [0-9]+)? ;

NEWLINE : [\r\n]+ -> skip ;
WS : [ \t]+ -> skip ;
COMMENT : '%' ~[\r\n]* -> skip ;
COMMENT2 : '/*' .*? '*/' -> skip ;
