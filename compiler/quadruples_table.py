from antlr4 import *
from compiler.quadruple import Quadruple

class QuadruplesTable:
    def __init__(self):
	    self.quads = []

    def append(self, operator, left_operand, right_operand, result = None):
        # print(operator, left_operand, right_operand, result)
        quadruple = Quadruple(operator, left_operand, right_operand, result)
        self.quads.append(quadruple)
    
    def length(self):
        return len(self.quads)
    
    def print(self):
        for (key, quad) in enumerate(self.quads):
            print(key, "\t", quad.operator, "\t", quad.left_operand, "\t", quad.right_operand, "\t", quad.result)
