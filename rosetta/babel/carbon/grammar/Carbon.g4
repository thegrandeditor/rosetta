grammar Carbon;

program: element* EOF;

element
    : function_decl
    | class_decl
    | interface_decl
    | impl_decl
    | package_decl
    | var_decl
    | assignment
    | statement
    ;

package_decl: 'package' ID ('api' | 'impl')? ';' ;

function_decl: 'fn' ID '(' param_list? ')' ('->' type_name)? block ;

param_list: parameter (',' parameter)* ;
parameter: ID ':' type_name ;

class_decl: 'class' ID '{' class_element* '}' ;
class_element
    : var_decl
    | function_decl
    ;

interface_decl: 'interface' ID '{' interface_element* '}' ;
interface_element: function_decl ;

impl_decl: 'impl' type_name 'as' type_name '{' class_element* '}' ;

var_decl: ( 'var' | 'let' ) ID (':' type_name)? ('=' expression)? ';' ;

assignment: ID '=' expression ';' ;

type_name: ID ;

block: '{' statement* '}' ;

statement
    : var_decl
    | assignment
    | if_stmt
    | while_stmt
    | return_stmt
    | match_stmt
    | expression_stmt
    ;

if_stmt: 'if' '(' expression ')' statement ( 'else' statement )? ;
while_stmt: 'while' '(' expression ')' statement ;
return_stmt: 'return' expression? ';' ;

match_stmt: 'match' '(' expression ')' '{' match_case* '}' ;
match_case: 'case' expression '=>' statement ;

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
NUMBER: [0-9]+ ;
STRING: '"' (~["])* '"' | '\'' (~['])* '\'' ;
WS: [ \t\r\n]+ -> skip ;
COMMENT: ('//' ~[\r\n]* | '/*' .*? '*/') -> skip ;
