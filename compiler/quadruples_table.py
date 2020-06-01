from antlr4 import *
from compiler.quadruple import Quadruple

class QuadruplesTable:
    def __init__(self):
	    self.quads = []

    def append(self, operator, left_operand, right_operand, result = None):
        quadruple = Quadruple(operator, left_operand, right_operand, result)
        self.quads.append(quadruple)
        print('Quad: ', operator, left_operand, right_operand, result)
    
    def length(self):
        return len(self.quads)