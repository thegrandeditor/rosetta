grammar Grain;
prog : expr+ ;
expr : 'print' '(' ID ')' ;
ID : [a-z]+ ;