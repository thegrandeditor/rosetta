grammar ML;

program: (declaration SEMI? | expr SEMI?)* EOF;

declaration
    : val_decl
    | fun_decl
    | datatype_decl
    ;

val_decl: 'val' pattern '=' expr ;

fun_decl: 'fun' ID param+ '=' expr ;

datatype_decl: 'datatype' ID '=' constructor ('|' constructor)* ;

constructor: ID ('of' type_expr)? ;

param: pattern ;

pattern
    : ID                                        # IdPat
    | literal                                   # LitPat
    | '(' pattern ')'                           # ParenPat
    | '(' pattern (',' pattern)* ')'            # TuplePat
    | ID pattern                                # ConstrPat
    ;

expr
    : primary                                   # PrimaryExpr
    | expr primary                              # AppExpr
    | expr op=( '*' | '/' ) expr               # BinExpr
    | expr op=( '+' | '-' ) expr               # BinExpr
    | expr op=( '::' | '@' ) expr              # BinExpr
    | expr op=( '=' | '<' | '>' ) expr         # BinExpr
    | 'let' (declaration SEMI?)* 'in' expr 'end' # LetExpr
    | 'case' expr 'of' branch ('|' branch)*    # CaseExpr
    ;

branch: pattern '=>' expr ;

primary
    : literal
    | ID
    | '(' expr ')'
    | '(' expr (',' expr)* ')'
    ;

literal: NUMBER | STRING | 'true' | 'false' | '[]' ;

type_expr
    : ID
    | type_expr '->' type_expr
    | type_expr '*' type_expr
    | '(' type_expr ')'
    ;

SEMI: ';' ;
NUMBER: '-'? [0-9]+ ;
STRING: '"' (~["])* '"' ;
ID: [a-zA-Z_][a-zA-Z0-9_']* ;
WS: [ \t\r\n]+ -> skip ;
