// Guide: https://github.com/antlr/antlr4/blob/master/doc/grammars.md

grammar low;

@header {
from compiler.compiler import Compiler
compiler = Compiler()
}

/* ---TOKENS--- */

// Reserved Words
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

// Data types
VAR: 'var';
STRING: 'string';
CHAR: 'char';
INT: 'int';
FLOAT: 'float';
BOOL: 'bool';

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
ASSIGN: '=';
AND: '&';
OR: '|';
LESS: '<';
LESS_OR_EQUAL: '<=';
GREATER: '>';
GREATER_OR_EQUAL: '>=';
EQUAL: '==';
NOT_EQUAL: '!=';
ADDITION: '+';
SUBTRACTION: '-';
MULTIPLICATION: '*';
DIVISION: '/';

//Constants
STRING_CONSTANT: '"' .*? '"';
CHAR_CONSTANT: [A-Za-z];
INT_CONSTANT: [0-9]+;
FLOAT_CONSTANT: [0-9]+.[0-9]+;
BOOL_CONSTANT: 'true' | 'false';
ID: [A-Za-z]([_A-Za-z0-9])*;

// Whitespace and comments
COMMENT_BLOCK: '/*' .*? '*/' -> skip;
COMMENT_LINE: '%%' ~[\r\n]* -> skip;
WHITESPACE : [ \t\r\n]+ -> skip ;


program:
  PROGRAM ID SEMICOLON variable_declaration functions main_function
;

variable_declaration:
  VAR variables+
;

variables:
  data_type initialized_variable (COMMA initialized_variable)* SEMICOLON
;

data_type:
  INT {compiler.add_type($INT.text)} |
  BOOL {compiler.add_type($BOOL.text)} |
  FLOAT {compiler.add_type($FLOAT.text)} |
  STRING {compiler.add_type($STRING.text)} |
  CHAR {compiler.add_type($CHAR.text)}
;

constant:
  BOOL_CONSTANT {compiler.add_operand($BOOL_CONSTANT.text)} |
  FLOAT_CONSTANT {compiler.add_operand($FLOAT_CONSTANT.text)} |
  INT_CONSTANT {compiler.add_operand($INT_CONSTANT.text)} |
  CHAR_CONSTANT {compiler.add_operand($CHAR_CONSTANT.text)} |
  STRING_CONSTANT {compiler.add_operand($STRING_CONSTANT.text)}
;

initialized_variable:
  ID (LEFT_BRACKET INT_CONSTANT RIGHT_BRACKET)?
;

functions:
  function*
;

function:
  FUNCTION (data_type | VOID) ID LEFT_PARENTHESIS parameters? RIGHT_PARENTHESIS variable_declaration? LEFT_CURLY statutes RIGHT_CURLY
;

parameters:
  data_type ID (COMMA data_type ID)*
;

logic_expresions:
  relational_expresions ((AND {compiler.add_operator($AND.text)} | OR {compiler.add_operator($OR.text)}) relational_expresions)*
;

relational_expresions:
  addition_substraction_expresions {compiler.add_operator($GREATER.text)} ((GREATER {compiler.add_operator($GREATER.text)} |
    LESS {compiler.add_operator($LESS.text)} |
    LESS_OR_EQUAL {compiler.add_operator($LESS_OR_EQUAL.text)} |
    GREATER {compiler.add_operator($GREATER_OR_EQUAL.text)} |
    GREATER_OR_EQUAL {compiler.add_operator($GREATER_OR_EQUAL.text)} |
    NOT_EQUAL {compiler.add_operator($NOT_EQUAL.text)} |
    EQUAL {compiler.add_operator($EQUAL.text)}) addition_substraction_expresions)?
;

addition_substraction_expresions:
  multiplication_division_expresions {compiler.check_for_add_or_subs()} ((ADDITION {compiler.add_operator($ADDITION.text)} | SUBTRACTION {compiler.add_operator($SUBTRACTION.text)}) multiplication_division_expresions)*
;

multiplication_division_expresions:
  expresion {compiler.check_for_mult_or_div()} ((MULTIPLICATION {compiler.add_operator($MULTIPLICATION.text)} | DIVISION {compiler.add_operator($DIVISION.text)}) expresion)*
;

expresion:
  constant |
  variable |
  LEFT_PARENTHESIS {compiler.left_parenthesis()} logic_expresions  RIGHT_PARENTHESIS {compiler.right_parenthesis()} |
  function_call
;

variable:
  ID (LEFT_BRACKET logic_expresions RIGHT_BRACKET)?
;

function_call:
  ID LEFT_PARENTHESIS (logic_expresions (COMMA logic_expresions)* )? RIGHT_PARENTHESIS
;

main_function:
  MAIN LEFT_PARENTHESIS RIGHT_PARENTHESIS LEFT_CURLY statutes RIGHT_CURLY
;

statutes:
  (assignation |
  read_function_call |
  write_function_call |
  void_function_call |
  return_statement |
  conditional_function |
  while_function |
  from_function )*
;

assignation: 
  variable ASSIGN logic_expresions SEMICOLON
;

read_function_call:
  INPUT LEFT_PARENTHESIS variable (COMMA variable)* RIGHT_PARENTHESIS SEMICOLON
;

write_function_call:
  OUTPUT LEFT_PARENTHESIS (logic_expresions | STRING_CONSTANT) (COMMA (logic_expresions | STRING_CONSTANT))* RIGHT_PARENTHESIS SEMICOLON
;

void_function_call:
  function_call SEMICOLON
;

return_statement:
  RETURN LEFT_PARENTHESIS logic_expresions  RIGHT_PARENTHESIS SEMICOLON
;

conditional_function:
  IF LEFT_PARENTHESIS logic_expresions RIGHT_PARENTHESIS THEN LEFT_CURLY statutes RIGHT_CURLY
  (ELSE_IF LEFT_PARENTHESIS logic_expresions RIGHT_PARENTHESIS THEN LEFT_CURLY statutes RIGHT_CURLY)?
  (ELSE LEFT_CURLY statutes RIGHT_CURLY)?
;

while_function:
  WHILE LEFT_PARENTHESIS logic_expresions RIGHT_PARENTHESIS DO LEFT_CURLY statutes RIGHT_CURLY
;

from_function:
  FROM variable ASSIGN logic_expresions TO logic_expresions DO LEFT_CURLY statutes RIGHT_CURLY
;
