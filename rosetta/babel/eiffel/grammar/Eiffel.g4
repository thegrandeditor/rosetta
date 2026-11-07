grammar Eiffel;

program: class_declaration* EOF;

class_declaration: CLASS_K ID (inheritance)? (create_clause)? (feature_block)* (invariant_clause)? END_K ;

inheritance: INHERIT_K ID (rename_clause)? (redefine_clause)? ;

rename_clause: RENAME_K ID AS_K ID (',' ID AS_K ID)* ;

redefine_clause: REDEFINE_K ID (',' ID)* ;

create_clause: CREATE_K ID (',' ID)* ;

feature_block: FEATURE_K (ID (',' ID)*)? feature_declaration* ;

feature_declaration: ID (formal_params)? (':' type_)? (attribute_init | routine_body) ;

formal_params: '(' param_list ')' ;

param_list: param_group (';' param_list)* ;

param_group: id_list ':' type_ ;

id_list: ID (',' ID)* ;

type_: ID | generic_type ;

generic_type: ID '[' type_ (',' type_)* ']' ;

attribute_init: (DO_K block END_K)? ;

routine_body: (REQUIRE_K assertion_list)? (LOCAL_K declaration_list)? (DO_K block)? (ENSURE_K assertion_list)? (RESCUE_K block)? END_K ;

assertion_list: assertion ((';' | NEWLINE)? assertion)* ;

assertion: (ID ':')? expression ;

declaration_list: declaration ((';' | NEWLINE)? declaration)* ;

declaration: id_list ':' type_ ;

block: (statement (';' | NEWLINE)?)* ;

NEWLINE: '\r'? '\n';

statement
    : assignment
    | call_statement
    | if_statement
    | loop_statement
    | retry_statement
    | check_statement
    ;

assignment: ID ':=' expression ;

call_statement: expression ;

if_statement: IF_K expression THEN_K block (ELSEIF_K expression THEN_K block)* (ELSE_K block)? END_K ;

loop_statement: FROM_K block UNTIL_K expression LOOP_K block END_K ;

retry_statement: RETRY_K ;

check_statement: CHECK_K assertion_list END_K ;

invariant_clause: INVARIANT_K assertion_list ;

expression: logical_expr ;

logical_expr: rel_expr ( (AND_K | OR_K | XOR_K | IMPLIES_K) rel_expr )* ;

rel_expr: add_expr ( ('=' | '/=' | '<' | '<=' | '>' | '>=') add_expr )? ;

add_expr: mul_expr ( ('+' | '-') mul_expr )* ;

mul_expr: unary_expr ( ('*' | '/' | '//' | '\\\\') unary_expr )* ;

unary_expr: (NOT_K | '+' | '-')? primary ;

primary: ID | NUMBER | STRING | '(' expression ')' | call_expr | OLD_K expression ;

call_expr: (ID '.')? ID ('(' actual_params? ')')? ;

actual_params: expression (',' expression)* ;

// Keywords
CLASS_K: 'class';
FEATURE_K: 'feature';
INHERIT_K: 'inherit';
RENAME_K: 'rename';
AS_K: 'as';
REDEFINE_K: 'redefine';
CREATE_K: 'create';
REQUIRE_K: 'require';
ENSURE_K: 'ensure';
INVARIANT_K: 'invariant';
LOCAL_K: 'local';
DO_K: 'do';
END_K: 'end';
IF_K: 'if';
THEN_K: 'then';
ELSEIF_K: 'elseif';
ELSE_K: 'else';
FROM_K: 'from';
UNTIL_K: 'until';
LOOP_K: 'loop';
RETRY_K: 'retry';
RESCUE_K: 'rescue';
CHECK_K: 'check';
OLD_K: 'old';
AND_K: 'and';
OR_K: 'or';
XOR_K: 'xor';
IMPLIES_K: 'implies';
NOT_K: 'not';

ID: [A-Za-z][A-Za-z0-9_]*;
NUMBER: [0-9]+ ('.' [0-9]*)?;
STRING: '"' (~["] | '""')* '"' | '\'' (~['] | '\'\'')* '\'';
WS: [ \t]+ -> skip;
COMMENT: '--' ~[\r\n]* -> skip;
