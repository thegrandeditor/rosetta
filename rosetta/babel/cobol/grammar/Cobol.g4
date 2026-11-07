grammar Cobol;

program : (copyStatement | identificationDivision | environmentDivision | dataDivision | procedureDivision)* EOF ;

copyStatement : 'COPY' cobolName (REPLACING_K cobolName BY_K cobolName)* '.' ;

identificationDivision
    : 'IDENTIFICATION' 'DIVISION' '.'
      'PROGRAM-ID' '.' programName '.'
      identificationEntry*
    ;

identificationEntry
    : ('AUTHOR' | 'INSTALLATION' | 'DATE-WRITTEN' | 'DATE-COMPILED' | 'SECURITY') '.' identificationValue* '.'
    ;

identificationValue : cobolName | anyNumber | '/' | ':' | '-' ;

programName : cobolName ;

environmentDivision : 'ENVIRONMENT' 'DIVISION' '.' inputOutputSection? ;
inputOutputSection : 'INPUT-OUTPUT' 'SECTION' '.' fileControl? ;
fileControl : 'FILE-CONTROL' '.' selectStatement* ;

selectStatement
    : 'SELECT' cobolName 'ASSIGN' 'TO' cobolName selectClause* '.'
    ;

selectClause
    : 'ORGANIZATION' 'IS'? ('SEQUENTIAL' | 'INDEXED' | 'RELATIVE')
    | 'ACCESS' 'MODE'? 'IS'? ('SEQUENTIAL' | 'RANDOM' | 'DYNAMIC')
    | 'FILE' 'STATUS' 'IS'? cobolName
    ;

dataDivision : 'DATA' 'DIVISION' '.' (fileSection | workingStorageSection | linkageSection)* ;
fileSection : 'FILE' 'SECTION' '.' fileDescriptionEntry* ;

fileDescriptionEntry
    : 'FD' cobolName fdClause* '.' dataDescriptionEntry*
    ;

fdClause
    : 'RECORD' 'CONTAINS' anyNumber ('TO' anyNumber)? 'CHARACTERS'?
    | 'LABEL' 'RECORDS' 'ARE'? ('STANDARD' | 'OMITTED')
    | 'BLOCK' 'CONTAINS' anyNumber 'RECORDS'?
    | 'DATA' 'RECORD' 'IS'? cobolName
    ;

workingStorageSection : 'WORKING-STORAGE' 'SECTION' '.' dataDescriptionEntry* ;
linkageSection : 'LINKAGE' 'SECTION' '.' dataDescriptionEntry* ;

dataDescriptionEntry
    : LEVEL_NUMBER cobolName dataClause* '.'
    | LEVEL_88 cobolName 'VALUE' 'IS'? literal ('THRU' literal)? '.'
    ;

dataClause
    : REDEFINES_K cobolName
    | ('PIC' | 'PICTURE') 'IS'? PICTURE_STRING
    | usageClause
    | 'OCCURS' anyNumber (TO_K anyNumber)? (DEPENDING_K 'ON'? cobolName)?
    | 'VALUE' 'IS'? literal
    | 'INDEXED' 'BY' cobolName
    ;

usageClause
    : ('USAGE' 'IS'?)? ('COMP-3' | 'COMPUTATIONAL-3' | 'COMP' | 'COMPUTATIONAL' | 'BINARY' | 'DISPLAY' | 'PACKED-DECIMAL')
    ;

procedureDivision : 'PROCEDURE' 'DIVISION' '.' procedureBody ;
procedureBody : paragraph* ;
paragraph : cobolName '.' statement* ;

statement
    : moveStatement
    | displayStatement
    | stopRunStatement
    | ifStatement
    | performStatement
    | computeStatement
    | evaluateStatement
    | callStatement
    | goToStatement
    | sqlStatement
    | fileStatement
    | addStatement
    | subtractStatement
    | multiplyStatement
    | divideStatement
    | initializeStatement
    | setStatement
    ;

moveStatement : 'MOVE' expression 'TO' cobolName+ '.' ;
displayStatement : 'DISPLAY' expression+ '.' ;
stopRunStatement : 'STOP' 'RUN' '.' ;
addStatement : 'ADD' expression+ 'TO' cobolName ROUNDED_K? '.' ;
subtractStatement : 'SUBTRACT' expression+ 'FROM' cobolName ROUNDED_K? '.' ;
multiplyStatement : 'MULTIPLY' expression 'BY' cobolName ROUNDED_K? '.' ;
divideStatement : 'DIVIDE' expression ('INTO' | 'BY') cobolName ROUNDED_K? '.' ;
initializeStatement : 'INITIALIZE' cobolName+ '.' ;
setStatement : 'SET' cobolName+ 'TO' ('TRUE' | 'FALSE' | expression) '.' ;

ifStatement : 'IF' condition statement+ ('ELSE' statement+)? 'END-IF'? '.' ;

performStatement
    : 'PERFORM' cobolName '.'
    | 'PERFORM' cobolName 'UNTIL' condition '.'
    | 'PERFORM' cobolName 'VARYING' cobolName 'FROM' expression 'BY' expression 'UNTIL' condition '.'
    | 'PERFORM' statement+ 'UNTIL' condition 'END-PERFORM' '.'
    ;

computeStatement : 'COMPUTE' cobolName ROUNDED_K? '=' expression '.' ;

evaluateStatement
    : 'EVALUATE' expression
      whenClause+
      whenOtherClause?
      'END-EVALUATE' '.'
    ;

whenClause : 'WHEN' expression statement+ ;
whenOtherClause : 'WHEN' 'OTHER' statement+ ;

callStatement : 'CALL' literal ('USING' expression+)? '.' ;
goToStatement : 'GO' 'TO' cobolName '.' ;
sqlStatement : EXEC_SQL_BLOCK '.' ;

fileStatement
    : 'OPEN' openPhrase+ '.'
    | 'READ' cobolName ('INTO' cobolName)?
      ('AT' 'END' statement+)?
      ('NOT' 'AT' 'END' statement+)?
      'END-READ'? '.'
    | 'WRITE' cobolName ('FROM' cobolName)? '.'
    | 'CLOSE' cobolName+ '.'
    ;

openPhrase : ('INPUT' | 'OUTPUT' | 'I-O' | 'EXTEND') cobolName+ ;

condition
    : expression operator expression
    | 'NOT' condition
    | condition 'AND' condition
    | condition 'OR' condition
    | cobolName
    ;

operator : '=' | '<' | '>' | '<=' | '>=' | 'NOT' '=' | 'NOT' '<' | 'NOT' '>' ;

expression
    : cobolName
    | literal
    | '(' expression ')'
    | expression ('+' | '-' | '*' | '/') expression
    ;

literal : STRING | anyNumber | specialLiteral ;

specialLiteral
    : 'SPACES' | 'SPACE'
    | 'ZEROS' | 'ZERO' | 'ZEROES'
    | 'HIGH-VALUES' | 'HIGH-VALUE'
    | 'LOW-VALUES' | 'LOW-VALUE'
    | 'TRUE' | 'FALSE'
    ;

anyNumber : NUMBER | LEVEL_NUMBER | LEVEL_88 | DECIMAL ;
cobolName : IDENTIFIER | NUMID ;

LEVEL_NUMBER   : '0'[1-9] | [1-4][0-9] | '66' | '77' | '78' ;
LEVEL_88       : '88' ;
ROUNDED_K      : 'ROUNDED' ;
REDEFINES_K    : 'REDEFINES' ;
REPLACING_K    : 'REPLACING' ;
BY_K           : 'BY' ;
TO_K           : 'TO' ;
DEPENDING_K    : 'DEPENDING' ;
ON_K           : 'ON' ;
EXEC_SQL_BLOCK : 'EXEC' [ \t\r\n]+ 'SQL' .*? 'END-EXEC' ;
NUMID          : [0-9]+ '-' [a-zA-Z] [a-zA-Z0-9-]* ;
PICTURE_STRING : [-$X9AVSPBZ,*()+/0-9]+ ('.' [0-9]+)? ;
IDENTIFIER     : [a-zA-Z] [a-zA-Z0-9-]* ;
DECIMAL        : '.' [0-9]+ ;
STRING         : '\'' (~'\'')* '\'' | '"' (~'"')* '"' ;
NUMBER         : [0-9]+ ('.' [0-9]+)? ;
WS             : [ \t\r\n]+ -> skip ;
COMMENT        : '*' ~[\r\n]* -> skip ;