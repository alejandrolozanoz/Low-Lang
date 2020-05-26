// Guide: https://github.com/antlr/antlr4/blob/master/doc/grammars.md

grammar low;


/* ---TOKENS--- */

// Logic
PROGRAM: 'programa';
MAIN: 'principal';
FUNCTION: 'funcion';
RETURN: 'regresa';
INPUT: 'lee';
OUTPUT: 'escribe';
IF: 'si';
THEN: 'entonces';
ELSE_IF: 'o si';
ELSE: 'sino';
WHILE: 'mientras';
DO: 'hacer';
FROM: 'desde';
TO: 'hasta';
VOID: 'void';

// Syntax Symbols
LEFT_PARENTHESIS: '(';
RIGHT_PARENTHESIS: ')';
LEFT_BRACKET: '[';
RIGHT_BRACKET: ']';
LEFT_CURLY: '{';
RIGHT_CURLY: '}';
COMMA: ',';
COLON: ':';
SEMICOLON: ';';

// Operators
LESS: '<';
GREATER: '>';
LESS_OR_EQUAL: '<=';
GREATER_OR_EQUAL: '>=';
EQUAL: '==';
NOT_EQUAL: '!=';
ASSIGN: '=';
AND: '&';
OR: '|';
ADDITION: '+';
SUBTRACTION: '-';
MULTIPLICATION: '*';
DIVISION: '/';

// Data types
VAR: 'var';
STRING: 'string';
CHAR: 'char';
INT: 'int';
FLOAT: 'float';
BOOL: 'bool';

//Constants
STRING_CONSTANT: '"' .*? '"';
CHAR_CONSTANT: [.];
INTEGER_CONSTANT: [0-9]+;
FLOAT_CONSTANT: [0-9]+.[0-9]+;
BOOL_CONSTANT: 'true' | 'false';
VAR_NAME: [_A-Za-z]([_A-Za-z0-9])*;

// Whitespace and comments
COMMENT_BLOCK: '/*' .*? '*/' -> skip;
COMMENT_LINE: '%%' ~[\r\n]* -> skip;
WHITESPACE : [ \t\r\n]+ -> skip ;


program:
  PROGRAM VAR_NAME SEMICOLON variable_declaration function_declaration main_function
;

variable_declaration:
  VAR variables+
;

variables:
  var_types varindividual (COMMA varindividual)* SEMICOLON
;

var_types:
  INT |
  BOOL |
  FLOAT |
  STRING |
  CHAR
;

constant:
  BOOL_CONSTANT |
  FLOAT_CONSTANT |
  INTEGER_CONSTANT |
  CHAR_CONSTANT |
  STRING_CONSTANT
;

varindividual:
  VAR_NAME (LEFT_BRACKET INTEGER_CONSTANT? RIGHT_BRACKET)?
;

function_declaration:
  function*
;

function:
  FUNCTION (var_types | VOID) VAR_NAME LEFT_PARENTHESIS parameters? RIGHT_PARENTHESIS variable_declaration? LEFT_CURLY statute? RIGHT_CURLY
;

parameters:
  var_types VAR_NAME (COMMA var_types VAR_NAME)*
;

expresions:
  multiple_expresions (ASSIGN multiple_expresions)*
;

multiple_expresions:
  expresion_comparison ((AND | OR) expresion_comparison)*
;

expresion_comparison:
  expresion ((GREATER | LESS | GREATER_OR_EQUAL | LESS_OR_EQUAL | NOT_EQUAL | EQUAL) expresion)?
;

expresion:
  term ((ADDITION | SUBTRACTION) term)*
;

term:
  factor ((MULTIPLICATION | DIVISION) factor)*
;

factor:
  LEFT_PARENTHESIS expresions RIGHT_PARENTHESIS |
  VAR_NAME LEFT_PARENTHESIS ( multiple_expresions (COMMA multiple_expresions)* )? RIGHT_PARENTHESIS |
  indexvariable |
  constant
;

statute:
  (assignation |
  voidcall |
  returncall |
  read |
  write |
  conditional |
  whileloop |
  fromloop )*
;

assignation: 
  VAR_NAME (LEFT_BRACKET multiple_expresions RIGHT_BRACKET)? ASSIGN expresions SEMICOLON
;

voidcall:
  VAR_NAME LEFT_PARENTHESIS ( multiple_expresions (COMMA multiple_expresions)* )? RIGHT_PARENTHESIS SEMICOLON
;

returncall:
  RETURN LEFT_PARENTHESIS expresions RIGHT_PARENTHESIS SEMICOLON
;

indexvariable:
  VAR_NAME (LEFT_BRACKET multiple_expresions RIGHT_BRACKET)?
;

read:
  INPUT LEFT_PARENTHESIS indexvariable (COMMA indexvariable)* RIGHT_PARENTHESIS SEMICOLON
;

write:
  OUTPUT LEFT_PARENTHESIS (expresions | STRING_CONSTANT) (COMMA (expresions | STRING_CONSTANT))* RIGHT_PARENTHESIS SEMICOLON
;

conditional:
  IF LEFT_PARENTHESIS multiple_expresions RIGHT_PARENTHESIS THEN LEFT_CURLY statute RIGHT_CURLY (ELSE_IF LEFT_PARENTHESIS multiple_expresions RIGHT_PARENTHESIS THEN LEFT_CURLY statute RIGHT_CURLY)? (ELSE LEFT_CURLY statute RIGHT_CURLY)?
;

whileloop:
  WHILE LEFT_PARENTHESIS multiple_expresions RIGHT_PARENTHESIS DO LEFT_CURLY statute RIGHT_CURLY
;

fromloop:
  FROM VAR_NAME indexvariable? ASSIGN multiple_expresions TO multiple_expresions DO LEFT_CURLY statute RIGHT_CURLY
;

main_function:
  MAIN LEFT_PARENTHESIS RIGHT_PARENTHESIS LEFT_CURLY statute RIGHT_CURLY
;