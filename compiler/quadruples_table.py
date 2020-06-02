from antlr4 import *
from compiler.quadruple import Quadruple

class QuadruplesTable:
    def __init__(self):
	    self.quads = []

    def append(self, operator, left_operand, right_operand, result = None):
        print(operator, left_operand, right_operand, result)
        quadruple = Quadruple(operator, left_operand, right_operand, result)
        self.quads.append(quadruple)

    def length(self):
        return len(self.quads)
    
    def print(self):
        for quad in self.quads:
            print(quad.operator, quad.left_operand, quad.right_operand, quad.result)
