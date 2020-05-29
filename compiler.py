from antlr4 import *
from function import Function
from variable import Variable
from semantic_cube import SemanticCube

class Compiler:
    def __init__(self):
        self.functions_table = []
        self.variables_table = []
        self.quadruples = []
        self.operators_stack = []
        self.operands_stack = []
        self.jumps_stack = []
        self.types_stack =[]
        self.semantic_cube = SemanticCube()
        
    def add_function(self, function: Function):
        self.functions_table.append(function)
        print(function)

    def add_variable(self, variable: Variable):
        self.variables_table.append(variable)
        print(variable)

    def add_operator(self, operator):
        self.operators_stack.append(operator)
        print(operator)

    def add_type(self, type):
        self.types_stack.append(type)
        print(type)

    def add_operand(self, operand):
        self.operands_stack.append(operand)
        print(operand)

    def add_parenthesis(self):
        self.operators_stack.append('(')
        print('(')

    def remove_parenthesis(self):
        self.operators_stack.pop()
        print(')')
