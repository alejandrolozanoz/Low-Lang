from antlr4 import *
from compiler.variable import Variable

class Function:
    def __init__(self, function_type, function_name, function_parameters, function_variables):
        self.function_type = function_type
        self.function_name = function_name
        self.function_parameters = function_parameters
        self.function_variables = function_variables

    def update_parameters(self, type, name ):
        if name not in self.function_parameters:
            self.function_parameters[name] = Variable(type, name, None)
            self.function_variables[name] = Variable(type, name, None)
        else:
            print("No se puede tener más de un parámetro con el mismo nombre")

    def update_variables(self, type, name ):
        if name not in self.function_variables:
            self.function_variables[name] = Variable(type, name, None)
        else:
            print("No se puede tener más de una variable con el mismo nombre")