grammar Basic;

program : (line | NEWLINE)* EOF;

line : (INTEGER)? statement NEWLINE+ ;

statement
    : let_stmt
    | print_stmt
    | input_stmt
    | goto_stmt
    | gosub_stmt
    | return_stmt
    | if_stmt
    | for_stmt
    | next_stmt
    | while_stmt
    | wend_stmt
    | end_stmt
    | remark_stmt
    ;

let_stmt : (LET_K)? identifier '=' expression ;

print_stmt : PRINT_K (expression (',' expression)*)? ;

input_stmt : INPUT_K string_literal? (';')? identifier (',' identifier)* ;

goto_stmt : GOTO_K (identifier | INTEGER) ;

gosub_stmt : GOSUB_K (identifier | INTEGER) ;

return_stmt : RETURN_K ;

if_stmt : IF_K expression THEN_K (statement | INTEGER) (ELSE_K (statement | INTEGER))? ;

for_stmt : FOR_K identifier '=' expression TO_K expression (STEP_K expression)? ;

next_stmt : NEXT_K identifier? ;

while_stmt : WHILE_K expression ;

wend_stmt : WEND_K ;

end_stmt : END_K ;

remark_stmt : REMARK ;

identifier : IDENTIFIER ;

expression
    : expression (OR | AND) expression
    | NOT expression
    | expression (EQ | NE | LT | LE | GT | GE) expression
    | expression (PLUS | MINUS) expression
    | expression (STAR | SLASH) expression
    | expression POWER expression
    | MINUS expression
    | '(' expression ')'
    | primary
    ;

primary
    : identifier ('(' expression (',' expression)* ')')?
    | literal
    ;

literal
    : integer_literal
    | real_literal
    | string_literal
    ;

integer_literal : INTEGER ;
real_literal : REAL ;
string_literal : STRING ;

OR : 'OR' ;
AND : 'AND' ;
NOT : 'NOT' ;
EQ : '=' | '==' ;
NE : '<>' | '!=' ;
LT : '<' ;
LE : '<=' ;
GT : '>' ;
GE : '>=' ;
PLUS : '+' ;
MINUS : '-' ;
STAR : '*' ;
SLASH : '/' ;
POWER : '^' | '**' ;

LET_K : 'LET' ;
PRINT_K : 'PRINT' | '?' ;
INPUT_K : 'INPUT' ;
GOTO_K : 'GOTO' ;
GOSUB_K : 'GOSUB' ;
RETURN_K : 'RETURN' ;
IF_K : 'IF' ;
THEN_K : 'THEN' ;
ELSE_K : 'ELSE' ;
FOR_K : 'FOR' ;
TO_K : 'TO' ;
STEP_K : 'STEP' ;
NEXT_K : 'NEXT' ;
WHILE_K : 'WHILE' ;
WEND_K : 'WEND' ;
END_K : 'END' ;
REMARK : ('REM' | '\'') ~[\r\n]* ;

IDENTIFIER : [a-zA-Z][a-zA-Z0-9_$%#]* ;
INTEGER : [0-9]+ ;
REAL : [0-9]+ '.' [0-9]* ([eE] [+-]? [0-9]+)? | '.' [0-9]+ ([eE] [+-]? [0-9]+)? ;
STRING : '"' ~["\r\n]* '"' ;

NEWLINE : [\r\n]+ ;
WS : [ \t]+ -> skip ;
