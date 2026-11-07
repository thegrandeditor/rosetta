grammar Modula2;

program: compilation_unit* EOF;

compilation_unit
    : main_module
    | definition_module
    | implementation_module
    ;

main_module: MODULE_K ID ';' import_list* export_list* block ID '.' ;

definition_module: DEFINITION_K MODULE_K ID ';' import_list* export_list* declaration* END_K ID '.' ;

implementation_module: IMPLEMENTATION_K MODULE_K ID ';' import_list* block ID '.' ;

import_list: (FROM_K ID)? IMPORT_K id_list ';' ;

export_list: (QUALIFIED_K)? EXPORT_K id_list ';' ;

id_list: ID (',' ID)* ;

block: (declaration)* (BEGIN_K statement_sequence)? END_K ;

declaration
    : CONST_K (ID '=' expression ';')*
    | TYPE_K (ID '=' type_ ';')*
    | VAR_K (id_list ':' type_ ';')*
    | procedure_declaration
    ;

procedure_declaration: PROCEDURE_K ID ('(' formal_params? ')')? (':' ID)? ';' block ID ';' ;

formal_params: fp_section (';' fp_section)* ;

fp_section: (VAR_K)? id_list ':' type_ ;

type_: ID | array_type | pointer_type | record_type ;

array_type: ARRAY_K expression OF_K type_ ;

pointer_type: POINTER_K TO_K type_ ;

record_type: RECORD_K (id_list ':' type_ ';')* END_K ;

statement_sequence: statement (';' statement)* ;

statement
    : assignment
    | procedure_call
    | if_statement
    | case_statement
    | while_statement
    | repeat_statement
    | loop_statement
    | for_statement
    | return_statement
    | exit_statement
    | // empty
    ;

assignment: designator ':=' expression ;

procedure_call: designator ('(' actual_params? ')')? ;

actual_params: expression (',' expression)* ;

if_statement: IF_K expression THEN_K statement_sequence (ELSIF_K expression THEN_K statement_sequence)* (ELSE_K statement_sequence)? END_K ;

case_statement: CASE_K expression OF_K (case_item ('|' case_item)*)? (ELSE_K statement_sequence)? END_K ;

case_item: id_list ':' statement_sequence ;

while_statement: WHILE_K expression DO_K statement_sequence END_K ;

repeat_statement: REPEAT_K statement_sequence UNTIL_K expression ;

loop_statement: LOOP_K statement_sequence END_K ;

for_statement: FOR_K ID ':=' expression TO_K expression (BY_K expression)? DO_K statement_sequence END_K ;

return_statement: RETURN_K (expression)? ;

exit_statement: EXIT_K ;

designator: ID ('.' ID | '[' expression (',' expression)* ']' | '^')* ;

expression: simple_expression (rel_op simple_expression)? ;

rel_op: '=' | '#' | '<' | '<=' | '>' | '>=' | IN_K ;

simple_expression: (PLUS | MINUS)? term (add_op term)* ;

add_op: PLUS | MINUS | OR_K ;

term: factor (mul_op factor)* ;

mul_op: TIMES | DIV_K | MOD_K | AND_K | '&' ;

factor: NUMBER | STRING | designator ('(' actual_params? ')')? | '(' expression ')' | NOT_K factor | '{' (element (',' element)*)? '}' ;

element: expression (RANGE_K expression)? ;

// Keywords
MODULE_K: 'MODULE';
IMPORT_K: 'IMPORT';
EXPORT_K: 'EXPORT';
FROM_K: 'FROM';
QUALIFIED_K: 'QUALIFIED';
DEFINITION_K: 'DEFINITION';
IMPLEMENTATION_K: 'IMPLEMENTATION';
BEGIN_K: 'BEGIN';
END_K: 'END';
CONST_K: 'CONST';
TYPE_K: 'TYPE';
VAR_K: 'VAR';
PROCEDURE_K: 'PROCEDURE';
ARRAY_K: 'ARRAY';
OF_K: 'OF';
RECORD_K: 'RECORD';
POINTER_K: 'POINTER';
TO_K: 'TO';
IF_K: 'IF';
THEN_K: 'THEN';
ELSIF_K: 'ELSIF';
ELSE_K: 'ELSE';
CASE_K: 'CASE';
WHILE_K: 'WHILE';
DO_K: 'DO';
REPEAT_K: 'REPEAT';
UNTIL_K: 'UNTIL';
LOOP_K: 'LOOP';
FOR_K: 'FOR';
BY_K: 'BY';
RETURN_K: 'RETURN';
EXIT_K: 'EXIT';
IN_K: 'IN';
OR_K: 'OR';
DIV_K: 'DIV';
MOD_K: 'MOD';
AND_K: 'AND';
NOT_K: 'NOT';

PLUS: '+';
MINUS: '-';
TIMES: '*';
DIV: '/';
RANGE_K: '..';

ID: [A-Za-z][A-Za-z0-9]*;
NUMBER: [0-9]+ ('.' [0-9]*)?;
STRING: '"' (~["] | '""')* '"' | '\'' (~['] | '\'\'')* '\'';
WS: [ \t\r\n]+ -> skip;
COMMENT: '(*' .*? '*)' -> skip;
