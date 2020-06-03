from antlr4 import *
from semantics.operations import Operations
from semantics.types import Types

class SemanticCube: 
	semantic_cube = {
		Types.INT: {
			Types.INT: {
				Operations.ADDITION: Types.INT,
				Operations.SUBTRACTION: Types.INT,
				Operations.DIVISION: Types.INT,
				Operations.MULTIPLICATION: Types.INT,
				Operations.ASSIGN: Types.INT,
				Operations.EQUAL: Types.BOOL,
				Operations.NOT_EQUAL: Types.BOOL,	
				Operations.GREATER: Types.BOOL,
				Operations.GREATER_OR_EQUAL: Types.BOOL,	
				Operations.LESS: Types.BOOL,
				Operations.LESS_OR_EQUAL: Types.BOOL,	
			},
			Types.FLOAT: {
				Operations.ADDITION: Types.FLOAT,
				Operations.SUBTRACTION: Types.FLOAT,
				Operations.DIVISION: Types.FLOAT,
				Operations.MULTIPLICATION: Types.FLOAT,
				Operations.ASSIGN: Types.FLOAT,
				Operations.EQUAL: Types.BOOL,
				Operations.NOT_EQUAL: Types.BOOL,		
				Operations.GREATER: Types.BOOL,
				Operations.GREATER_OR_EQUAL: Types.BOOL,
				Operations.LESS: Types.BOOL,
				Operations.LESS_OR_EQUAL: Types.BOOL,	
			}
		},
		Types.FLOAT: {
			Types.FLOAT: {
				Operations.ADDITION: Types.FLOAT,
				Operations.SUBTRACTION: Types.FLOAT,
				Operations.DIVISION: Types.FLOAT,
				Operations.MULTIPLICATION: Types.FLOAT,
				Operations.ASSIGN: Types.FLOAT,
				Operations.EQUAL: Types.BOOL,
				Operations.NOT_EQUAL: Types.BOOL,		
				Operations.GREATER: Types.BOOL,
				Operations.LESS: Types.BOOL,
			},
			Types.INT: {
				Operations.ADDITION: Types.FLOAT,
				Operations.SUBTRACTION: Types.FLOAT,
				Operations.DIVISION: Types.FLOAT,
				Operations.MULTIPLICATION: Types.FLOAT,
				Operations.ASSIGN: Types.FLOAT,
				Operations.EQUAL: Types.BOOL,
				Operations.NOT_EQUAL: Types.BOOL,		
				Operations.GREATER: Types.BOOL,
				Operations.LESS: Types.BOOL,
			}
		},
		Types.CHAR: {
			Types.CHAR: {
				Operations.ASSIGN: Types.CHAR,
				Operations.EQUAL: Types.BOOL,
				Operations.NOT_EQUAL: Types.BOOL,		
			}
		},
		Types.STRING: {
			Types.STRING: {
				Operations.ASSIGN: Types.CHAR,
				Operations.EQUAL: Types.BOOL,
				Operations.NOT_EQUAL: Types.BOOL,		
			}
		},
		Types.BOOL: {
			Types.BOOL: {
				Operations.ASSIGN: Types.BOOL,
				Operations.EQUAL: Types.BOOL,
				Operations.NOT_EQUAL: Types.BOOL,		
				Operations.AND: Types.BOOL,
				Operations.OR: Types.BOOL,
			}
		}
	}

	def check_operation(self, left_operand, right_operand, operator):
		# print('Operación:', left_operand, right_operand, operator)
		try:
			result_operator = self.semantic_cube[left_operand][right_operand][operator]
			return result_operator
		except KeyError:
			return Types.ERROR
