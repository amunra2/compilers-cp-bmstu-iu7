grammar Pascal;

// Правила для программного кода
program : 'program' ID ';' declarations? block '.' ;

// Правила для объявления переменных
declarations : 'var' variableDeclaration (',' variableDeclaration)* ';' ;

// Объявление переменной
variableDeclaration : variable ':' type ;

// Тип переменной
type : 'integer' | 'real' | 'boolean' | 'char' ;

// Правила для блока кода
block : 'begin' statement+ 'end' ;

// Правила для выражений и операций
statement : assignment
          | returnStatement
          | printStatement
          | block // Вложенные блоки кода
          ;

// Возврат значения
returnStatement: 'exit' '(' variable ')' ';' ; 

// Присваивание значения переменной
assignment : variable ':=' expression ';' ;

// Печать в консоль
printStatement : 'writeln' '(' variable ')' ';' ;

// Выражения
expression : term (('+' | '-') term)* ;
term : factor (('*' | '/') factor)* ;
factor : INT
       | REAL
       | variable
       | '(' expression ')'
       | BOOLEAN
       | CHAR
       ;

// Переменная
variable : ID ;

// Лексемы
ID : [a-zA-Z_][a-zA-Z0-9_]* ;
INT : [0-9]+ ;
REAL : [0-9]+ '.' [0-9]* ;
BOOLEAN : 'true' | 'false' ;
CHAR : '\'' [a-zA-Z] '\'' ;
WS : [ \t\n\r]+ -> skip ;
