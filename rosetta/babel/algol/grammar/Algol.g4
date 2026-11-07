grammar Algol;

program : block EOF;

block : BEGIN_K declaration_list? statement_list? END_K ;

declaration_list : (declaration ';')+ ;

declaration
    : type_declaration
    | procedure_declaration
    | own_declaration
    ;

type_declaration : type_hint identifier (',' identifier)* ;

own_declaration : OWN_K type_declaration ;

procedure_declaration : PROCEDURE_K identifier (formal_parameter_list)? ';' statement ;

formal_parameter_list : '(' identifier (',' identifier)* ')' ;

statement_list : (statement (';' statement)*)? ;

statement
    : assignment_statement
    | procedure_call
    | if_statement
    | for_statement
    | while_statement
    | block
    |
    ;

assignment_statement : identifier ':=' expression ;

procedure_call : identifier ( '(' expression (',' expression)* ')' )? ;

if_statement : IF_K expression THEN_K statement (ELSE_K statement)? ;

for_statement : FOR_K identifier ':=' expression STEP_K expression UNTIL_K expression DO_K statement ;

while_statement : WHILE_K expression DO_K statement ;

expression
    : expression (OR_K | AND_K) expression
    | NOT_K expression
    | expression (EQ | NE | LT | LE | GT | GE) expression
    | expression (PLUS | MINUS) expression
    | expression (STAR | SLASH) expression
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
    | logical_literal
    ;

type_hint : INTEGER_K | REAL_K | BOOLEAN_K ;

identifier : IDENTIFIER ;
integer_literal : INTEGER ;
real_literal : REAL ;
string_literal : STRING ;
logical_literal : TRUE_K | FALSE_K ;

EQ : '=' ;
NE : '!=' | '<>' ;
LT : '<' ;
LE : '<=' ;
GT : '>' ;
GE : '>=' ;
PLUS : '+' ;
MINUS : '-' ;
STAR : '*' ;
SLASH : '/' ;

BEGIN_K : 'BEGIN' ;
END_K : 'END' ;
OWN_K : 'OWN' ;
PROCEDURE_K : 'PROCEDURE' ;
IF_K : 'IF' ;
THEN_K : 'THEN' ;
ELSE_K : 'ELSE' ;
FOR_K : 'FOR' ;
STEP_K : 'STEP' ;
UNTIL_K : 'UNTIL' ;
DO_K : 'DO' ;
WHILE_K : 'WHILE' ;
INTEGER_K : 'INTEGER' ;
REAL_K : 'REAL' ;
BOOLEAN_K : 'BOOLEAN' ;
TRUE_K : 'TRUE' ;
FALSE_K : 'FALSE' ;
OR_K : 'OR' ;
AND_K : 'AND' ;
NOT_K : 'NOT' ;

IDENTIFIER : [a-zA-Z][a-zA-Z0-9_]* ;
INTEGER : [0-9]+ ;
REAL : [0-9]+ '.' [0-9]* ([eE] [+-]? [0-9]+)? | '.' [0-9]+ ([eE] [+-]? [0-9]+)? ;
STRING : '"' (~["\r\n])* '"' ;

NEWLINE : [\r\n]+ -> skip ;
WS : [ \t]+ -> skip ;
COMMENT : 'COMMENT' ~';'* ';' -> skip ;
