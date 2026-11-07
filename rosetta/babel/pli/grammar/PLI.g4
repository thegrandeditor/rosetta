grammar PLI;

program: directive* statement* EOF;

directive: '*' ID ';';

statement
    : (label ':')? content_no_semi
    | (label ':')? content_semi ';'
    | (label ':')? entry_stmt ';'
    | (label ':')? ';'
    ;

label: ID;

content_no_semi
    : procedure_def
    | do_block
    | if_stmt
    | on_stmt
    ;

content_semi
    : declare_stmt
    | allocate_stmt
    | free_stmt
    | call_stmt
    | assignment
    | return_stmt
    | action
    ;

procedure_def: (PROCEDURE_K | PROC_K) ('(' params? ')')? (OPTIONS_K '(' ID (',' ID)* ')')? (RETURNS_K '(' type_ ')')? ';' statement* END_K (ID)? ';' ;

entry_stmt: ENTRY_K ('(' params? ')')? (RETURNS_K '(' type_ ')')?;

params: ID (',' ID)*;

declare_stmt: (DECLARE_K | DCL_K) declaration (',' declaration)*;

declaration: ID (attribute)*;

attribute
    : type_
    | PICTURE_K STRING
    | TASK_K
    | VARYING_K
    | ALIGNED_K
    | '(' expression (',' expression)* ')' // Dimension
    | INIT_K '(' expression ')'
    ;

type_: FIXED_K | FLOAT_K | CHARACTER_K | CHAR_K | BINARY_K | BIN_K | DECIMAL_K | DEC_K | POINTER_K | BIT_K;

on_stmt: ON_K ID statement;

allocate_stmt: ALLOCATE_K (ID | type_) (SET_K '(' ID ')')?;

free_stmt: FREE_K ID;

do_block: DO_K (do_spec)? ';' statement* END_K (ID)? ';';

do_spec: ID '=' expression (TO_K expression (BY_K expression)?)?;

if_stmt: IF_K expression THEN_K statement (ELSE_K statement)?;

call_stmt: CALL_K ID ('(' args? ')')?;

args: expression (',' expression)*;

assignment: primary '=' expression;

return_stmt: RETURN_K ('(' expression ')')?;

action: (PUT_K | GET_K) (LIST_K | EDIT_K | SKIP_K | DATA_K)? ('(' args? ')')?;

expression: primary (operator primary)*;

primary
    : ID ('(' args? ')')? // Variable or Array Access or Function Call
    | STRING
    | NUMBER
    | '(' expression ')'
    ;

operator: '+' | '-' | '*' | '/' | '||' | '==' | '=' | '<' | '>' | '<=' | '>=' | '&' | '|';

// Keywords (Case-insensitive)
PROCEDURE_K: [Pp][Rr][Oo][Cc][Ee][Dd][Uu][Rr][Ee];
PROC_K: [Pp][Rr][Oo][Cc];
ENTRY_K: [Ee][Nn][Tt][Rr][Yy];
RETURNS_K: [Rr][Ee][Tt][Uu][Rr][Nn][Ss];
END_K: [Ee][Nn][Dd];
DECLARE_K: [Dd][Ee][Cc][Ll][Aa][Rr][Ee];
DCL_K: [Dd][Cc][Ll];
ON_K: [Oo][Nn];
ALLOCATE_K: [Aa][Ll][Ll][Oo][Cc][Aa][Tt][Ee];
FREE_K: [Ff][Rr][Ee][Ee];
DO_K: [Dd][Oo];
IF_K: [Ii][Ff];
THEN_K: [Tt][Hh][Ee][Nn];
ELSE_K: [Ee][Ll][Ss][Ee];
TO_K: [Tt][Oo];
BY_K: [Bb][Yy];
CALL_K: [Cc][Aa][Ll][Ll];
RETURN_K: [Rr][Ee][Tt][Uu][Rr][Nn];
PUT_K: [Pp][Uu][Tt];
GET_K: [Gg][Ee][Tt];
LIST_K: [Ll][Ii][Ss][Tt];
EDIT_K: [Ee][Dd][Ii][Tt];
SKIP_K: [Ss][Kk][Ii][Pp];
DATA_K: [Dd][Aa][Tt][Aa];
OPTIONS_K: [Oo][Pp][Tt][Ii][Oo][Nn][Ss];
PICTURE_K: [Pp][Ii][Cc][Tt][Uu][Rr][Ee];
TASK_K: [Tt][Aa][Ss][Kk];
VARYING_K: [Vv][Aa][Rr][Yy][Ii][Nn][Gg];
ALIGNED_K: [Aa][Ll][Ii][Gg][Nn][Ee][Dd];
FIXED_K: [Ff][Ii][Xx][Ee][Dd];
FLOAT_K: [Ff][Ll][Oo][Aa][Tt];
CHARACTER_K: [Cc][Hh][Aa][Rr][Aa][Cc][Tt][Ee][Rr];
CHAR_K: [Cc][Hh][Aa][Rr];
BINARY_K: [Bb][Ii][Nn][Aa][Rr][Yy];
BIN_K: [Bb][Ii][Nn];
DECIMAL_K: [Dd][Ee][Cc][Ii][Mm][Aa][Ll];
DEC_K: [Dd][Ee][Cc];
POINTER_K: [Pp][Oo][Ii][Nn][Tt][Ee][Rr];
BIT_K: [Bb][Ii][Tt];
INIT_K: [Ii][Nn][Ii][Tt];
SET_K: [Ss][Ee][Tt];

ID: [A-Za-z][A-Za-z0-9_]*;
STRING: '\'' (~['] | '\'\'')* '\'';
NUMBER: [0-9]+ ('.' [0-9]*)?;
WS: [ \t\r\n]+ -> skip;
COMMENT: '/*' .*? '*/' -> skip;
