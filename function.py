from antlr4 import *

class Function:
    def __init__(self, function_type, function_name, function_parameters):
        self.function_type = function_type
        self.function_name = function_name
        self.function_parameters = []
