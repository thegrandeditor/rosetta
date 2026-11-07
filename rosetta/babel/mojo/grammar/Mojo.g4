grammar Mojo;

program: element* EOF;

element
    : function_decl
    | struct_decl
    | var_decl
    | assignment
    | statement
    ;

function_decl: decorator* ( 'fn' | 'def' ) ID '(' param_list? ')' ('->' type_name)? block ;

decorator: '@' ID ;

param_list: parameter (',' parameter)* ;
parameter: ( 'owned' | 'borrowed' | 'inout' )? ID (':' type_name)? ('=' expression)? ;

struct_decl: 'struct' ID '{' struct_element* '}' ;
struct_element
    : var_decl
    | function_decl
    ;

var_decl: ( 'let' | 'var' ) ID (':' type_name)? ('=' expression)? ';' ;

assignment: ID '=' expression ';' ;

type_name: ID ('[' type_name (',' type_name)* ']')? ;

block: '{' statement* '}' ;

statement
    : var_decl
    | assignment
    | if_stmt
    | while_stmt
    | return_stmt
    | expression_stmt
    ;

if_stmt: 'if' expression block ('else' block)? ;
while_stmt: 'while' expression block ;
return_stmt: 'return' expression? ';' ;
expression_stmt: expression ';' ;

expression
    : primary
    | expression '(' argument_list? ')'
    | expression op=( '+' | '-' | '*' | '/' | '==' | '!=' | '<' | '>' | '<=' | '>=' ) expression
    ;

argument_list: expression (',' expression)* ;

primary
    : ID
    | NUMBER
    | STRING
    | 'true'
    | 'false'
    ;

ID: [a-zA-Z_][a-zA-Z0-9_]* ;
NUMBER: [0-9]+ ('.' [0-9]*)? ;
STRING: '"' (~["])* '"' | '\'' (~['])* '\'' ;
WS: [ \t\r\n]+ -> skip ;
COMMENT: ('//' ~[\r\n]* | '/*' .*? '*/') -> skip ;
