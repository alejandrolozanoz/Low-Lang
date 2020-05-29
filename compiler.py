from antlr4 import *
from function import Function
from variable import Variable
from semantic_cube import SemanticCube

class Compiler:
    def __init__(self):
        self.function_table = {}
        self.variable_table = {}
        self.quadruples = []
        self.semantic_cube = SemanticCube()
    
    def add_function(self, function: Function):
         self.function_table.append(function)

    def add_variable(self, variable: Variable):
         self.variable_table.append(variable)