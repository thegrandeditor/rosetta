grammar test_grammar;
program : statement* EOF ;
statement : function_decl | assignment ;
function_decl : 'fn' ID '(' ')' '{' statement* '}' ;
assignment : ID '=' ID ';' ;
ID : [a-zA-Z_][a-zA-Z0-9_]* ;
WS : [ \t\r\n]+ -> skip ;
