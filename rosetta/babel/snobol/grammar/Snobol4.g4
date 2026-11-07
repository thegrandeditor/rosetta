grammar Snobol4;

program: (line | NEWLINE)* EOF;

line: (COMMENT | statement) (NEWLINE | EOF);

statement
    : label? WS (content (WS transfer)?)
    | label? WS transfer
    | label
    ;

content
    : patternMatch
    | assignment
    | expression
    ;

label: ID;

assignment: subject WS? '=' WS? expression;

patternMatch: subject WS pattern (WS? '=' WS? replacement)?;

subject: expression;
pattern: expression;
replacement: expression;

transfer: ':' WS? transfer_dest;

transfer_dest
    : '(' direct_goto ')'
    | conditional_gotos
    | direct_goto
    ;

direct_goto: ID;

conditional_gotos: (success_goto | failure_goto)+;

success_goto: 'S' '(' ID ')';
failure_goto: 'F' '(' ID ')';

expression
    : alternation_expr
    ;

alternation_expr
    : concatenation_expr (WS? '|' WS? concatenation_expr)*
    ;

concatenation_expr
    : capture_expr (WS capture_expr)*
    ;

capture_expr
    : additive_expr (WS? ('.' | '$') WS? ID)*
    ;

additive_expr
    : multiplicative_expr (WS? (PLUS | MINUS) WS? multiplicative_expr)*
    ;

multiplicative_expr
    : primary (WS? (TIMES | DIV) WS? primary)*
    ;

primary
    : ID
    | STRING
    | NUMBER
    | '(' expression ')'
    | function_call
    | unary_expr
    | array_access
    ;

array_access: ID '<' expression (',' expression)* '>';

unary_expr
    : ('.' | '$' | '*' | '&' | '@' | PLUS | MINUS) primary
    ;

function_call: ID '(' (expression (',' expression)*)? ')';

PLUS: '+';
MINUS: '-';
TIMES: '*';
DIV: '/';
ID: [A-Za-z][A-Za-z0-9_.]*;
STRING: '"' (~["] | '""')* '"' | '\'' (~['] | '\'\'')* '\'';
NUMBER: [0-9]+;
COMMENT: '*' ~[\r\n]*;
WS: [ \t]+;
NEWLINE: '\r'? '\n';
