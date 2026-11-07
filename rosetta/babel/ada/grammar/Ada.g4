grammar Ada;

program : (context_item | compilation_unit)* EOF;

context_item
    : WITH_K qualified_name (',' qualified_name)* ';'
    | USE_K (TYPE_K)? qualified_name (',' qualified_name)* ';'
    ;

qualified_name : identifier ('.' identifier)* ;

compilation_unit
    : generic_declaration
    | package_declaration
    | package_body
    | subprogram_declaration
    | subprogram_body
    ;

generic_declaration : 'GENERIC' (generic_formal_part)? (package_declaration | subprogram_declaration) ;

generic_formal_part : (parameter_specification | type_declaration | subprogram_declaration)* ;

package_declaration : PACKAGE_K identifier IS_K (package_item)* (PRIVATE_K (package_item)*)? END_K (identifier)? ';' ;

package_body : PACKAGE_K BODY_K identifier IS_K (package_item)* (BEGIN_K (statement)*)? END_K (identifier)? ';' ;

package_item
    : subprogram_declaration
    | subprogram_body
    | type_declaration
    | variable_declaration
    | task_declaration
    ;

subprogram_declaration : subprogram_specification ';' ;

subprogram_body : subprogram_specification IS_K (declaration)* BEGIN_K (statement)* (EXCEPTION_K (exception_handler)*)? END_K (identifier)? ';' ;

subprogram_specification
    : PROCEDURE_K identifier (formal_part)?
    | FUNCTION_K identifier (formal_part)? RETURN_K type_mark
    ;

formal_part : '(' parameter_specification (';' parameter_specification)* ')' ;

parameter_specification : identifier (',' identifier)* ':' (IN_K)? (OUT_K)? type_mark (':=' expression)? ;

type_declaration : TYPE_K identifier IS_K type_definition ';' ;

type_definition
    : RECORD_K (component_list) END_K RECORD_K
    | ARRAY_K '(' index_constraint ')' OF_K type_mark
    | access_definition
    | private_type_definition
    ;

component_list : (variable_declaration)+ ;

variable_declaration : identifier (',' identifier)* ':' type_mark (':=' expression)? ';' ;

task_declaration : TASK_K (BODY_K)? identifier (IS_K (declaration)* BEGIN_K (statement)* END_K (identifier)?)? ';' ;

declaration
    : variable_declaration
    | type_declaration
    | subprogram_declaration
    | subprogram_body
    ;

statement
    : assignment_statement
    | procedure_call_statement
    | if_statement
    | case_statement
    | loop_statement
    | return_statement
    | exit_statement
    | entry_call_statement
    | delay_statement
    | select_statement
    | accept_statement
    ;

assignment_statement : identifier ':=' expression ';' ;

procedure_call_statement : qualified_name ('(' expression (',' expression)* ')')? ';' ;

if_statement : IF_K expression THEN_K (statement)* (ELSIF_K expression THEN_K (statement)*)* (ELSE_K (statement)*)? END_K IF_K ';' ;

case_statement : CASE_K expression IS_K (WHEN_K choice_list '=>' (statement)*)+ END_K CASE_K ';' ;

loop_statement : (iteration_scheme)? LOOP_K (statement)* END_K LOOP_K ';' ;

iteration_scheme
    : WHILE_K expression
    | FOR_K identifier IN_K (REVERSE_K)? range_spec
    ;

return_statement : RETURN_K (expression)? ';' ;

exit_statement : EXIT_K (identifier)? (WHEN_K expression)? ';' ;

exception_handler : WHEN_K (identifier '|')? choice_list '=>' (statement)* ;

choice_list : identifier ( '|' identifier )* | OTHERS_K ;

range_spec : expression '..' expression ;

type_mark : qualified_name ;

access_definition : ACCESS_K identifier ;

private_type_definition : PRIVATE_K ;

index_constraint : range_spec (',' range_spec)* ;

entry_call_statement : identifier '.' identifier ('(' expression (',' expression)* ')')? ';' ;

delay_statement : DELAY_K expression ';' ;

select_statement : SELECT_K (select_alternative (OR_K select_alternative)*)? (ELSE_K (statement)*)? END_K SELECT_K ';' ;

select_alternative : (WHEN_K expression '=>')? (statement)* ;

accept_statement : ACCEPT_K identifier (formal_part)? (DO_K (statement)* END_K (identifier)?)? ';' ;

expression
    : expression (OR_K | AND_K | XOR_K) expression
    | NOT_K expression
    | expression (EQ | NE | LT | LE | GT | GE) expression
    | expression (PLUS | MINUS | AMP) expression
    | expression (STAR | SLASH | REM_K | MOD_K) expression
    | expression POWER expression
    | ABS_K expression
    | '(' expression ')'
    | primary
    ;

primary
    : identifier ('(' expression (',' expression)* ')')?
    | identifier '\'' identifier ('(' expression (',' expression)* ')')?
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

EQ : '=' ;
NE : '/=' ;
LT : '<' ;
LE : '<=' ;
GT : '>' ;
GE : '>=' ;
PLUS : '+' ;
MINUS : '-' ;
STAR : '*' ;
SLASH : '/' ;
AMP : '&' ;
POWER : '**' ;

PACKAGE_K : 'PACKAGE' ;
BODY_K : 'BODY' ;
IS_K : 'IS' ;
END_K : 'END' ;
PRIVATE_K : 'PRIVATE' ;
PROCEDURE_K : 'PROCEDURE' ;
FUNCTION_K : 'FUNCTION' ;
RETURN_K : 'RETURN' ;
TYPE_K : 'TYPE' ;
RECORD_K : 'RECORD' ;
ARRAY_K : 'ARRAY' ;
OF_K : 'OF' ;
ACCESS_K : 'ACCESS' ;
TASK_K : 'TASK' ;
BEGIN_K : 'BEGIN' ;
IF_K : 'IF' ;
THEN_K : 'THEN' ;
ELSIF_K : 'ELSIF' ;
ELSE_K : 'ELSE' ;
CASE_K : 'CASE' ;
WHEN_K : 'WHEN' ;
LOOP_K : 'LOOP' ;
WHILE_K : 'WHILE' ;
FOR_K : 'FOR' ;
IN_K : 'IN' ;
REVERSE_K : 'REVERSE' ;
EXIT_K : 'EXIT' ;
EXCEPTION_K : 'EXCEPTION' ;
OTHERS_K : 'OTHERS' ;
SELECT_K : 'SELECT' ;
OR_K : 'OR' ;
AND_K : 'AND' ;
XOR_K : 'XOR' ;
NOT_K : 'NOT' ;
DELAY_K : 'DELAY' ;
ACCEPT_K : 'ACCEPT' ;
DO_K : 'DO' ;
ABS_K : 'ABS' ;
REM_K : 'REM' ;
MOD_K : 'MOD' ;
OUT_K : 'OUT' ;
WITH_K : 'WITH' ;
USE_K : 'USE' ;
TRUE_K : 'TRUE' ;
FALSE_K : 'FALSE' ;

IDENTIFIER : [a-zA-Z][a-zA-Z0-9_]* ;
INTEGER : [0-9]+ ;
REAL : [0-9]+ '.' [0-9]* ([eE] [+-]? [0-9]+)? | '.' [0-9]+ ([eE] [+-]? [0-9]+)? ;
STRING : '"' (~["\r\n])* '"' ;

NEWLINE : [\r\n]+ -> skip ;
WS : [ \t]+ -> skip ;
COMMENT : '--' ~[\r\n]* -> skip ;
