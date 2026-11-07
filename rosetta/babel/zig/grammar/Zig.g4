grammar Zig;

program: element* EOF;

element
    : function_decl
    | struct_decl
    | var_decl
    | assignment
    | statement
    ;

function_decl: ( 'pub' )? ( 'inline' )? 'fn' ID '(' param_list? ')' ('!'? type_name)? block ;

param_list: parameter (',' parameter)* ;
parameter: ID ':' type_name ;

struct_decl: ( 'pub' )? ( 'packed' | 'extern' )? 'struct' '{' struct_element* '}' ;
struct_element
    : var_decl
    | function_decl
    ;

var_decl: ( 'pub' )? ( 'const' | 'var' ) ID (':' type_name)? ('=' expression)? ';' ;

assignment: ID '=' expression ';' ;

type_name: ( '?' )? ID ;

block: '{' statement* '}' ;

statement
    : var_decl
    | assignment
    | if_stmt
    | while_stmt
    | for_stmt
    | return_stmt
    | defer_stmt
    | expression_stmt
    ;

if_stmt: 'if' '(' expression ')' statement ( 'else' statement )? ;
while_stmt: ( 'inline' )? 'while' '(' expression ')' statement ;
for_stmt: ( 'inline' )? 'for' '(' expression ')' statement ;
return_stmt: 'return' expression? ';' ;

defer_stmt: ( 'errdefer' | 'defer' ) statement ;

expression_stmt: expression ';' ;

expression
    : primary
    | 'try' expression
    | 'catch' expression
    | 'comptime' expression
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
    | '@import' '(' STRING ')'
    ;

ID: [a-zA-Z_][a-zA-Z0-9_]* ;
NUMBER: [0-9]+ ;
STRING: '"' (~["])* '"' | '\'' (~['])* '\'' ;
WS: [ \t\r\n]+ -> skip ;
COMMENT: ('//' ~[\r\n]* | '/*' .*? '*/') -> skip ;
