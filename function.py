from antlr4 import *

class Function:
    def __init__(self, name, parameters, type):
        self.name = name
        self.type = type
        self.parameters = []
    