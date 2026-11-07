grammar Pascal;

program : program_stmt? block '.' EOF;

program_stmt : PROGRAM_K identifier ( '(' identifier ( ',' identifier )* ')' )? ';' ;

block : declaration_part? statement_part ;

declaration_part : (var_decl_part | type_decl_part | procedure_decl | function_decl)+ ;

var_decl_part : VAR_K (var_decl ';')+ ;

var_decl : identifier ( ',' identifier )* ':' type_spec ;

type_decl_part : TYPE_K (type_decl ';')+ ;

type_decl : identifier '=' type_spec ;

type_spec
    : identifier
    | ARRAY_K '[' range ( ',' range )* ']' OF_K type_spec
    | RECORD_K field_list END_K
    ;

range : expression '..' expression ;

field_list : (var_decl ( ';' var_decl )*)? ( ';' )? ;

procedure_decl : PROCEDURE_K identifier ( formal_parameter_list )? ';' block ';' ;

function_decl : FUNCTION_K identifier ( formal_parameter_list )? ':' identifier ';' block ';' ;

formal_parameter_list : '(' formal_parameter ( ';' formal_parameter )* ')' ;

formal_parameter : (VAR_K)? identifier ( ',' identifier )* ':' identifier ;

statement_part : BEGIN_K statement ( ';' statement )* END_K ;

statement
    : assignment_stmt
    | procedure_call
    | if_stmt
    | for_stmt
    | while_stmt
    | repeat_stmt
    | with_stmt
    | statement_part
    |
    ;

assignment_stmt : identifier ':=' expression ;

procedure_call : identifier ( '(' expression ( ',' expression )* ')' )? ;

if_stmt : IF_K expression THEN_K statement ( ELSE_K statement )? ;

for_stmt : FOR_K identifier ':=' expression ( TO_K | DOWNTO_K ) expression DO_K statement ;

while_stmt : WHILE_K expression DO_K statement ;

repeat_stmt : REPEAT_K statement ( ';' statement )* UNTIL_K expression ;

with_stmt : WITH_K identifier ( ',' identifier )* DO_K statement ;

expression
    : expression (OR | AND) expression
    | NOT expression
    | expression (EQ | NE | LT | LE | GT | GE) expression
    | expression (PLUS | MINUS) expression
    | expression (STAR | SLASH | DIV | MOD) expression
    | MINUS expression
    | '(' expression ')'
    | primary
    ;

primary
    : identifier ('(' expression (',' expression)* ')')?
    | identifier '^'
    | identifier '.' identifier
    | literal
    ;

literal
    : integer_literal
    | real_literal
    | string_literal
    | logical_literal
    ;

identifier : IDENTIFIER ;
integer_literal : INTEGER ;
real_literal : REAL ;
string_literal : STRING ;
logical_literal : TRUE_K | FALSE_K ;

OR : 'OR' ;
AND : 'AND' ;
NOT : 'NOT' ;
EQ : '=' ;
NE : '<>' ;
LT : '<' ;
LE : '<=' ;
GT : '>' ;
GE : '>=' ;
PLUS : '+' ;
MINUS : '-' ;
STAR : '*' ;
SLASH : '/' ;
DIV : 'DIV' ;
MOD : 'MOD' ;

PROGRAM_K : 'PROGRAM' ;
BEGIN_K : 'BEGIN' ;
END_K : 'END' ;
VAR_K : 'VAR' ;
TYPE_K : 'TYPE' ;
ARRAY_K : 'ARRAY' ;
OF_K : 'OF' ;
RECORD_K : 'RECORD' ;
PROCEDURE_K : 'PROCEDURE' ;
FUNCTION_K : 'FUNCTION' ;
IF_K : 'IF' ;
THEN_K : 'THEN' ;
ELSE_K : 'ELSE' ;
FOR_K : 'FOR' ;
TO_K : 'TO' ;
DOWNTO_K : 'DOWNTO' ;
DO_K : 'DO' ;
WHILE_K : 'WHILE' ;
REPEAT_K : 'REPEAT' ;
UNTIL_K : 'UNTIL' ;
WITH_K : 'WITH' ;
TRUE_K : 'TRUE' ;
FALSE_K : 'FALSE' ;

IDENTIFIER : [a-zA-Z][a-zA-Z0-9_]* ;
INTEGER : [0-9]+ ;
REAL : [0-9]+ '.' [0-9]* ([eE] [+-]? [0-9]+)? | '.' [0-9]+ ([eE] [+-]? [0-9]+)? ;
STRING : '\'' (~['\r\n])* '\'' ;

NEWLINE : [\r\n]+ -> skip ;
WS : [ \t]+ -> skip ;
COMMENT : '{' ~'}'* '}' -> skip ;
COMMENT2 : '(*' .*? '*)' -> skip ;
