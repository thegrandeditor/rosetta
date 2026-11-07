grammar Forth;

program: element* EOF;

element
    : definition
    | if_stmt
    | do_loop
    | begin_until
    | stack_op
    | literal
    | call
    ;

definition: ':' name=ID body+=element* ';' ;

if_stmt: 'IF' consequent+=element* ('ELSE' alternate+=element*)? 'THEN' ;

do_loop: 'DO' body+=element* 'LOOP' ;

begin_until: 'BEGIN' body+=element* 'UNTIL' ;

stack_op: op=STACK_CMD ;

literal: val=NUMBER ;

call: name=ID ;

STACK_CMD
    : 'DUP' | 'DROP' | 'SWAP' | 'OVER' | 'ROT'
    | '+' | '-' | '*' | '/' | 'MOD'
    | '.' | 'EMIT' | 'CR'
    | '=' | '<' | '>' | '<=' | '>='
    ;

ID: ~[ \t\r\n0-9] ~[ \t\r\n]* ;
NUMBER: '-'? [0-9]+ ;
WS: [ \t\r\n]+ -> skip;
