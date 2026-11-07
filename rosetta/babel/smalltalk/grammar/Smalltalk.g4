grammar Smalltalk;

program : (executable_unit)* EOF;

executable_unit
    : class_definition
    | expression '.'
    ;

class_definition : identifier SUBCLASS_K (symbol | identifier) INSTANCE_VARIABLE_NAMES_K string_literal (method_definition)* ;

method_definition : (symbol | identifier) (keyword_selector | binary_selector | unary_selector) block ;

expression
    : assignment
    | cascade
    | message_expression
    ;

assignment : identifier ':=' expression ;

cascade : message_expression (';' messages)+ ;

message_expression
    : primary (messages)*
    ;

messages
    : keyword_message
    | binary_message
    | unary_message
    ;

keyword_message : (KEYWORD expression)+ ;
binary_message : BINARY_SELECTOR primary ;
unary_message : identifier ;

primary
    : identifier
    | literal
    | block
    | '(' expression ')'
    ;

block : '[' (':' identifier)* ('|')? (expression '.')* ']' ;

literal
    : number
    | string_literal
    | symbol
    | array_literal
    ;

number : NUMBER ;
string_literal : STRING ;
symbol : '#' (identifier | KEYWORD | BINARY_SELECTOR) ;
array_literal : '#(' (literal)* ')' ;

identifier : IDENTIFIER ;
keyword_selector : KEYWORD ;
binary_selector : BINARY_SELECTOR ;
unary_selector : identifier ;

SUBCLASS_K : 'subclass:' ;
INSTANCE_VARIABLE_NAMES_K : 'instanceVariableNames:' ;

IDENTIFIER : [a-zA-Z][a-zA-Z0-9_]* ;
KEYWORD : [a-zA-Z][a-zA-Z0-9_]* ':' ;
BINARY_SELECTOR : [+*/\\=><,@%&|~?]+ ;
NUMBER : [0-9]+ ('.' [0-9]+)? ;
STRING : '\'' (~['\r\n])* '\'' ;

NEWLINE : [\r\n]+ -> skip ;
WS : [ \t]+ -> skip ;
COMMENT : '"' ~'"'* '"' -> skip ;
