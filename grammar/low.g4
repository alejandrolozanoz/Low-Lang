// Guide: https://github.com/antlr/antlr4/blob/master/doc/grammars.md

grammar low;

@header {
from compiler.compiler import Compiler
from compiler.function import Function
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
CHAR_CONSTANT: [.];
INT_CONSTANT: [0-9]+;
FLOAT_CONSTANT: [0-9]+.[0-9]+;
BOOL_CONSTANT: 'true' | 'false';
ID: [_A-Za-z]([_A-Za-z0-9])*;

// Whitespace and comments
COMMENT_BLOCK: '/*' .*? '*/' -> skip;
COMMENT_LINE: '%%' ~[\r\n]* -> skip;
WHITESPACE : [ \t\r\n]+ -> skip ;


program:
  PROGRAM ID {compiler.add_function(compiler.current_function)} SEMICOLON
  variable_declaration? {compiler.goto_main()}
  functions
  main_function
;

variable_declaration:
  VAR variables+
;

variables:
  data_type ID declaration_array_brackets? {compiler.current_function.update_variables($data_type.text, $ID.text)}
  (COMMA ID declaration_array_brackets? {compiler.current_function.update_variables($data_type.text, $ID.text)})* SEMICOLON
;

declaration_array_brackets:
  LEFT_BRACKET INT_CONSTANT? RIGHT_BRACKET
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

functions:
  function*
;

function:
  FUNCTION function_type ID {compiler.current_function=Function($function_type.text, $ID.text, [], {})}
  LEFT_PARENTHESIS parameters? RIGHT_PARENTHESIS
  variable_declaration? {compiler.add_function(compiler.current_function)}
  LEFT_CURLY statutes RIGHT_CURLY {compiler.end_function()}
;

function_type:
  (data_type | VOID)
;

parameters:
  {currentCounter=0} data_type ID {compiler.current_function.update_parameters($data_type.text, $ID.text)} {currentCounter += 1}
  (COMMA data_type ID {compiler.current_function.update_parameters($data_type.text, $ID.text)} {currentCounter += 1})*
;

logic_expresions:
  relational_expresions {compiler.check_for_logic_operators()}
  ((AND {compiler.add_operator($AND.text)} | OR {compiler.add_operator($OR.text)})
  relational_expresions {compiler.check_for_logic_operators()})*
;

relational_expresions:
  addition_substraction_expresions {compiler.check_for_relational_operators()}
    ((LESS {compiler.add_operator($LESS.text)} |
    LESS_OR_EQUAL {compiler.add_operator($LESS_OR_EQUAL.text)} |
    GREATER {compiler.add_operator($GREATER.text)} |
    GREATER_OR_EQUAL {compiler.add_operator($GREATER_OR_EQUAL.text)} |
    NOT_EQUAL {compiler.add_operator($NOT_EQUAL.text)} |
    EQUAL {compiler.add_operator($EQUAL.text)}) addition_substraction_expresions)?
;

addition_substraction_expresions:
  multiplication_division_expresions {compiler.check_for_add_or_subs()}
  ((ADDITION {compiler.add_operator($ADDITION.text)} | SUBTRACTION {compiler.add_operator($SUBTRACTION.text)})
  multiplication_division_expresions)*
;

multiplication_division_expresions:
  expresion {compiler.check_for_mult_or_div()}
  ((MULTIPLICATION {compiler.add_operator($MULTIPLICATION.text)} | DIVISION {compiler.add_operator($DIVISION.text)})
  expresion)*
;

expresion:
  constant |
  ID {compiler.add_variable($ID.text)} array_brackets? |
  LEFT_PARENTHESIS {compiler.left_parenthesis()} logic_expresions RIGHT_PARENTHESIS {compiler.right_parenthesis()} |
  function_call
  // function_parameters
;

// function_parameters:
//   ID {compiler.add_function_operand_type($ID.text)} LEFT_PARENTHESIS {compiler.addParenthesis()} {currentCounter=0}
//   (logic_expresions {currentCounter += 1} (COMMA logic_expresions {currentCounter += 1}))*
//   {compiler.goto_function($ID.text)} {compiler.check_parameters($ID.text, currentCounter)} RIGHT_PARENTHESIS {compiler.popParenthesis()})

// ;

array_brackets:
  (LEFT_BRACKET logic_expresions RIGHT_BRACKET)
;

function_call:
  ID LEFT_PARENTHESIS (logic_expresions (COMMA logic_expresions)* )? RIGHT_PARENTHESIS
;

main_function:
  MAIN {compiler.current_function=Function("void", "main", [], {})} LEFT_PARENTHESIS RIGHT_PARENTHESIS
  LEFT_CURLY {compiler.start_main()} statutes RIGHT_CURLY
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
  <assoc=right> ID {compiler.add_variable($ID.text)} array_brackets? ASSIGN {compiler.add_operator($ASSIGN.text)}
  logic_expresions SEMICOLON {compiler.assign_quadruple()}
;

// Aquí pudiera haber un error por los IDs que se mandan en read_quadruple, podrían cambiar los valores antes del punto neurálgico
read_function_call:
  INPUT LEFT_PARENTHESIS ID {compiler.add_variable($ID.text)} array_brackets? {compiler.read_quadruple($ID.text)}
  (COMMA ID {compiler.add_variable($ID.text)} array_brackets? {compiler.read_quadruple($ID.text)})* RIGHT_PARENTHESIS SEMICOLON
;

write_function_call:
  OUTPUT LEFT_PARENTHESIS logic_expresions {compiler.write_quadruple()} (COMMA (logic_expresions {compiler.write_quadruple()}))* RIGHT_PARENTHESIS SEMICOLON
;

void_function_call:
  ID {compiler.void_function($ID.text)}
  LEFT_PARENTHESIS (logic_expresions (COMMA logic_expresions)* )? RIGHT_PARENTHESIS SEMICOLON {compiler.void_end_function()}
;

return_statement:
  RETURN LEFT_PARENTHESIS logic_expresions RIGHT_PARENTHESIS SEMICOLON {compiler.return_end_function()}
;

conditional_function:
  IF LEFT_PARENTHESIS logic_expresions RIGHT_PARENTHESIS
  {compiler.if_statement()} THEN LEFT_CURLY statutes RIGHT_CURLY
  (ELSE {compiler.else_statement()} LEFT_CURLY statutes RIGHT_CURLY {compiler.end_if_else_function()})?
  {compiler.end_if_else_function()}
;

while_function:
  WHILE LEFT_PARENTHESIS {compiler.while_statement()} logic_expresions RIGHT_PARENTHESIS {compiler.while_statutes()}
  DO LEFT_CURLY statutes {compiler.while_end()} RIGHT_CURLY
;

from_function:
  FROM ID array_brackets? ASSIGN logic_expresions {compiler.from_initialize($ID.text)} 
  TO INT_CONSTANT {compiler.add_operand($INT_CONSTANT.text)} {compiler.from_statutes()}
  DO LEFT_CURLY statutes {compiler.end_from()} RIGHT_CURLY 
;
