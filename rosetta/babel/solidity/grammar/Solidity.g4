grammar Solidity;

program: source_unit* EOF;

source_unit
    : pragma_directive
    | import_directive
    | contract_definition
    | interface_definition
    | library_definition
    ;

pragma_directive: 'pragma' ID expression ';' ;

import_directive: 'import' STRING ';' ;

contract_definition: 'contract' ID ('is' id_list)? '{' contract_body_element* '}' ;

interface_definition: 'interface' ID '{' contract_body_element* '}' ;

library_definition: 'library' ID '{' contract_body_element* '}' ;

id_list: ID (',' ID)* ;

contract_body_element
    : state_variable_declaration
    | event_definition
    | modifier_definition
    | function_definition
    | constructor_definition
    | mapping_declaration
    ;

state_variable_declaration: type_name visibility? ('constant' | 'immutable')? ID ('=' expression)? ';' ;

event_definition: 'event' ID '(' event_param_list? ')' ';' ;

modifier_definition: 'modifier' ID '(' param_list? ')' block ;

function_definition: 'function' ID '(' param_list? ')' visibility? mutability? ('returns' '(' param_list ')')? (block | ';') ;

constructor_definition: 'constructor' '(' param_list? ')' visibility? mutability? block ;

mapping_declaration: 'mapping' '(' key_type '=>' type_name ')' visibility? ID ';' ;

key_type: ID | 'address' | 'uint' | 'int' | 'string' | 'bytes' ;

type_name: key_type | 'mapping' '(' key_type '=>' type_name ')' ;

visibility: 'public' | 'private' | 'internal' | 'external' ;

mutability: 'pure' | 'view' | 'payable' ;

event_param_list: event_param (',' event_param)* ;
event_param: type_name 'indexed'? ID? ;

param_list: parameter (',' parameter)* ;
parameter: type_name storage_location? ID? ;

storage_location: 'memory' | 'storage' | 'calldata' ;

block: '{' statement* '}' ;

statement
    : expression_statement
    | if_statement
    | for_statement
    | while_statement
    | return_statement
    | emit_statement
    | variable_declaration_statement
    ;

expression_statement: expression ';' ;

if_statement: 'if' '(' expression ')' statement ('else' statement)? ;

for_statement: 'for' '(' (variable_declaration_statement | expression_statement | ';') expression? ';' expression? ')' statement ;

while_statement: 'while' '(' expression ')' statement ;

return_statement: 'return' expression? ';' ;

emit_statement: 'emit' expression ';' ;

variable_declaration_statement: type_name storage_location? ID ('=' expression)? ';' ;

expression
    : primary
    | expression '(' argument_list? ')'
    | expression op=( '*' | '/' | '%' ) expression
    | expression op=( '+' | '-' ) expression
    | expression op=( '==' | '!=' | '<' | '>' | '<=' | '>=' ) expression
    | expression op=( '&&' | '||' ) expression
    | expression '=' expression
    ;

argument_list: expression (',' expression)* ;

primary
    : ID
    | NUMBER
    | STRING
    | 'true'
    | 'false'
    | '(' expression ')'
    ;

ID: [a-zA-Z_$][a-zA-Z0-9_$]* ;
NUMBER: [0-9]+ ('.' [0-9]*)? ;
STRING: '"' (~["])* '"' | '\'' (~['])* '\'' ;
WS: [ \t\r\n]+ -> skip ;
COMMENT: ('//' ~[\r\n]* | '/*' .*? '*/') -> skip ;
