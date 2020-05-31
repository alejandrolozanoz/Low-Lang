from antlr4 import *
from compiler.quadruple import Quadruple

class QuadruplesTable:
    def __init__(self):
	    self.quadruples = []

    def append(self, operator, left_operand, right_operand, result):
        quadruple = Quadruple(operator, left_operand, right_operand, '_')
        self.quadruples.append(quadruple)
        print(operator, left_operand, right_operand, '_')
