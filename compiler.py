from antlr4 import *
from function import Function
from variable import Variable
from functions_table import FunctionsTable
from variables_table import VariablesTable
from semantic_cube import SemanticCube

class Compiler:
    def __init__(self):
        self.functions_table = FunctionsTable
        self.variables_table = VariablesTable
        self.quadruples = []
        self.operators_stack = []
        self.operands_stack = []
        self.jumps_stack = []
        self.types_stack =[]
        self.semantic_cube = SemanticCube()
        
    def add_function(self, function: Function):
        self.function_table.append(function)

    def add_variable(self, variable: Variable):
        self.variable_table.append(variable)

    def add_operator(self, operator):
        self.operatorStack.append(operator)

    def add_type(self, type):
        self.typesStack.append(type)
]
    def add_operand(self, operand):
        self.operandStack.append(operand)

    def add_parenthesis(self):
        self.operatorStack.append('(')

    def remove_parenthesis(self):
        self.operatorStack.pop()