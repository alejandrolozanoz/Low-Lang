from antlr4 import *

class Operations:
    ADDITION = "+"
    SUBTRACTION = "-"
    MULTIPLICATION = "*"
    DIVISION = "/"

    GREATER = ">"
    LESS = "<"
    EQUAL = "=="
    NOT_EQUAL = "!="
    LESS_OR_EQUAL = "<="
    GREATER_OR_EQUAL = ">="
    ASSIGN = "="

class Types:
    CHAR = "char"
    INT = "int"
    FLOAT = "float"
    STRING = "string"
    BOOL = "bool"
    ERROR = "error"

class SemanticCube: 
	semantic_cube = {
		# INT
		(Types.INT, Types.INT, Operations.ADDITION): Types.INT,
		(Types.INT, Types.INT, Operations.SUBTRACTION): Types.INT,
		(Types.INT, Types.INT, Operations.DIVISION): Types.INT,
		(Types.INT, Types.INT, Operations.MULTIPLICATION): Types.INT,
		(Types.INT, Types.INT, Operations.EQUAL): Types.BOOL,
		(Types.INT, Types.INT, Operations.GREATER): Types.BOOL,
		(Types.INT, Types.INT, Operations.LESS): Types.BOOL,
		(Types.INT, Types.INT, Operations.NOT_EQUAL): Types.BOOL,
		(Types.INT, Types.INT, Operations.ASSIGN): Types.INT,

		# FLOAT
		(Types.FLOAT, Types.FLOAT, Operations.ADDITION): Types.FLOAT,
		(Types.FLOAT, Types.FLOAT, Operations.SUBTRACTION): Types.FLOAT,
		(Types.FLOAT, Types.FLOAT, Operations.DIVISION): Types.FLOAT,
		(Types.FLOAT, Types.FLOAT, Operations.MULTIPLICATION): Types.FLOAT,
		(Types.FLOAT, Types.FLOAT, Operations.EQUAL): Types.BOOL,
		(Types.FLOAT, Types.FLOAT, Operations.GREATER): Types.BOOL,
		(Types.FLOAT, Types.FLOAT, Operations.LESS): Types.BOOL,
		(Types.FLOAT, Types.FLOAT, Operations.NOT_EQUAL): Types.BOOL,
		(Types.FLOAT, Types.FLOAT, Operations.ASSIGN): Types.FLOAT,

		# CHAR
		(Types.CHAR, Types.CHAR, Operations.EQUAL): Types.BOOL,
		(Types.CHAR, Types.CHAR, Operations.NOT_EQUAL): Types.BOOL,
		(Types.CHAR, Types.CHAR, Operations.ASSIGN): Types.CHAR,

		# STRING
		(Types.STRING, Types.STRING, Operations.EQUAL): Types.BOOL,
		(Types.STRING, Types.STRING, Operations.NOT_EQUAL): Types.BOOL,
		(Types.STRING, Types.STRING, Operations.ASSIGN): Types.STRING,

		# BOOL
		(Types.BOOL, Types.BOOL, Operations.ASSIGN): Types.BOOL,
		(Types.BOOL, Types.BOOL, Operations.NOT_EQUAL): Types.BOOL,
		(Types.BOOL, Types.BOOL, Operations.EQUAL): Types.BOOL,
	}
