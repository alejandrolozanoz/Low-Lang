from antlr4 import *
from compiler.variable import Variable

class Function:
    def __init__(self, function_type, function_name, function_parameters, function_variables, function_memory):
        self.function_type = function_type
        self.function_name = function_name
        self.function_parameters = []
        self.function_variables = function_variables
        self.function_memory = function_memory
        self.start_quadruple = -1
        self.end_quadruple = -1
        self.variables_count = 0

    def update_parameters(self, type, name ):
        if name not in self.function_parameters:
            address = self.function_memory.get_address(type)
            self.function_parameters.append(Variable(type, name, None, address))
            self.update_variables(type, name)
        else:
            print("ERROR: No se puede tener más de un parámetro con el mismo nombre")

    def update_variables(self, type, name ):
        if name not in self.function_variables:
            address = self.function_memory.get_address(type)
            self.function_variables[name] = Variable(type, name, None, address)
            self.variables_count += 1
        else:
            print("ERROR: No se puede tener más de una variable con el mismo nombre")