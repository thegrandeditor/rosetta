grammar RPG;

program: line* EOF;

line
    : h_spec
    | f_spec
    | d_spec
    | c_spec
    | o_spec
    | comment
    | NL
    ;

h_spec: 'H' OTHER? NL ;
f_spec: 'F' OTHER? NL ;
d_spec: 'D' OTHER? NL ;
o_spec: 'O' OTHER? NL ;

c_spec: 'C' (f1=factor)? opcode (f2=factor)? (res=ID)? (ind=indicator)? NL ;

factor: ID | NUMBER | STRING ;
indicator: '*' ID ;
opcode: ID ;

comment: '*' OTHER? NL ;

ID: [a-zA-Z#@][a-zA-Z0-9#@]* ;
NUMBER: [0-9]+ ;
STRING: '\'' (~['])* '\'' ;
OTHER: ~[\r\n]+ ;
WS: [ \t]+ -> skip ;
NL: [\r\n]+ ;
