grammar Fortran;

program : (executable_unit | main_program | NEWLINE)* EOF;

executable_unit
    : subroutine_def
    | function_def
    ;

main_program
    : program_stmt?
      specification_part?
      execution_part?
      end_stmt
    ;

subroutine_def
    : subroutine_stmt
      specification_part?
      execution_part?
      end_stmt
    ;

function_def
    : function_stmt
      specification_part?
      execution_part?
      end_stmt
    ;

program_stmt : PROGRAM_K identifier NEWLINE+ ;

subroutine_stmt : SUBROUTINE_K identifier ('(' (identifier (',' identifier)*)? ')')? NEWLINE+ ;

function_stmt : type_spec? FUNCTION_K identifier '(' (identifier (',' identifier)*)? ')' NEWLINE+ ;

end_stmt : END_K (PROGRAM_K | SUBROUTINE_K | FUNCTION_K)? identifier? NEWLINE* ;

specification_part : specification_stmt+ ;

specification_stmt
    : type_declaration_stmt NEWLINE+
    | implicit_none_stmt NEWLINE+
    | common_stmt NEWLINE+
    | dimension_stmt NEWLINE+
    ;

type_declaration_stmt : type_spec ('::')? entity_decl (',' entity_decl)* ;

type_spec
    : INTEGER_K
    | REAL_K
    | DOUBLE_K PRECISION_K
    | COMPLEX_K
    | LOGICAL_K
    | CHARACTER_K (('*' integer_literal) | ('(' (LEN_K '=')? (integer_literal | '*') ')'))?
    ;

entity_decl : identifier ('(' array_spec ')')? ('=' expression)? ;

array_spec : dimension (',' dimension)* ;

dimension : (expression ':')? expression | '*' ;

implicit_none_stmt : IMPLICIT_K NONE_K ;

common_stmt : COMMON_K ('/' identifier '/')? identifier (',' identifier)* ;

dimension_stmt : DIMENSION_K identifier '(' array_spec ')' (',' identifier '(' array_spec ')')* ;

execution_part : executable_stmt+ ;

executable_stmt
    : (assignment_stmt
    | if_stmt
    | do_stmt
    | goto_stmt
    | call_stmt
    | write_stmt
    | print_stmt
    | format_stmt
    | label action_stmt
    | action_stmt) NEWLINE+
    ;

action_stmt
    : assignment_stmt
    | goto_stmt
    | call_stmt
    | write_stmt
    | print_stmt
    | return_stmt
    | CONTINUE_K
    | STOP_K
    ;

assignment_stmt : identifier ('(' expression (',' expression)* ')')? '=' expression ;

if_stmt
    : IF_K '(' expression ')' THEN_K NEWLINE+
      execution_part?
      ( ELSE_K IF_K '(' expression ')' THEN_K NEWLINE+ execution_part? )*
      ( ELSE_K NEWLINE+ execution_part? )?
      END_K IF_K
    | IF_K '(' expression ')' action_stmt
    ;

do_stmt
    : DO_K label? (identifier '=' expression ',' expression (',' expression)?)? NEWLINE+
      execution_part?
      END_K DO_K
    ;

goto_stmt : GOTO_K label ;

call_stmt : CALL_K identifier ('(' (expression (',' expression)*)? ')')? ;

return_stmt : RETURN_K ;

write_stmt : WRITE_K '(' (identifier | '*') ',' (identifier | label | '*') ')' (expression (',' expression)*)? ;

print_stmt : PRINT_K '*' (',' expression (',' expression)*)? ;

format_stmt : label FORMAT_K '(' (format_item (',' format_item)*)? ')' ;

format_item
    : identifier
    | string_literal
    | integer_literal
    | real_literal
    | identifier (integer_literal | real_literal) ('.' integer_literal)?
    | '(' format_item (',' format_item)* ')'
    ;

label : INTEGER ;

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
    | logical_literal
    ;

integer_literal : INTEGER ;
real_literal : REAL ;
string_literal : STRING ;
logical_literal : '.TRUE.' | '.FALSE.' ;

OR : '.OR.' ;
AND : '.AND.' ;
NOT : '.NOT.' ;
EQ : '==' | '.EQ.' ;
NE : '/=' | '.NE.' ;
LT : '<' | '.LT.' ;
LE : '<=' | '.LE.' ;
GT : '>' | '.GT.' ;
GE : '>=' | '.GE.' ;
PLUS : '+' ;
MINUS : '-' ;
STAR : '*' ;
SLASH : '/' ;
POWER : '**' ;

PROGRAM_K : 'PROGRAM' ;
SUBROUTINE_K : 'SUBROUTINE' ;
FUNCTION_K : 'FUNCTION' ;
END_K : 'END' ;
INTEGER_K : 'INTEGER' ;
REAL_K : 'REAL' ;
DOUBLE_K : 'DOUBLE' ;
PRECISION_K : 'PRECISION' ;
COMPLEX_K : 'COMPLEX' ;
LOGICAL_K : 'LOGICAL' ;
CHARACTER_K : 'CHARACTER' ;
LEN_K : 'LEN' ;
IMPLICIT_K : 'IMPLICIT' ;
NONE_K : 'NONE' ;
COMMON_K : 'COMMON' ;
DIMENSION_K : 'DIMENSION' ;
IF_K : 'IF' ;
THEN_K : 'THEN' ;
ELSE_K : 'ELSE' ;
DO_K : 'DO' ;
GOTO_K : 'GOTO' ;
CALL_K : 'CALL' ;
RETURN_K : 'RETURN' ;
WRITE_K : 'WRITE' ;
PRINT_K : 'PRINT' ;
CONTINUE_K : 'CONTINUE' ;
STOP_K : 'STOP' ;
FORMAT_K : 'FORMAT' ;

IDENTIFIER : [a-zA-Z][a-zA-Z0-9_]* ;
INTEGER : [0-9]+ ;
REAL : [0-9]+ '.' [0-9]* ([eE] [+-]? [0-9]+)? | '.' [0-9]+ ([eE] [+-]? [0-9]+)? ;
STRING : '"' (~["\r\n])* '"' | '\'' (~['\r\n])* '\'' ;

NEWLINE : [\r\n]+ ;
WS : [ \t]+ -> skip ;
COMMENT : '!' ~[\r\n]* -> skip ;
LINE_COMMENT : [\r\n] 'C' ~[\r\n]* -> skip ;
