from antlr4 import *
from compiler.function import Function
from compiler.variable import Variable
from compiler.quadruple import Quadruple
from semantics.types import Types
from semantics.operations import Operations
from semantics.semantic_cube import SemanticCube

class Compiler:
    def __init__(self):
        self.functions_table = []
        self.variables_table = []
        self.quadruples = []
        self.operators_stack = []
        self.operands_stack = []
        self.jumps_stack = []
        self.types_stack = []
        self.semantic_cube = SemanticCube()
        self.counter = 0
        
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

    def left_parenthesis(self):
        self.operators_stack.append('(')
        print('(')

    def right_parenthesis(self):
        self.operators_stack.pop()
        print(')')
    
    def generate_quadruple(self):
        right_operand = self.operands_stack.pop()
        left_operand = self.operands_stack.pop()
        operator = self.operators_stack.pop()
        right_operand_type = self.types_stack.pop()
        left_operand_type = self.types_stack.pop()
        operation_result_type = SemanticCube().check_operation(left_operand_type, right_operand_type, operator)
        if operation_result_type == Types().ERROR:
            print('ERROR: Types error.')
        else:
            quadruple = Quadruple(operator, left_operand, right_operand, self.counter)
            print(operator, left_operand, right_operand, self.counter)
            self.counter+=1
            self.quadruples.append(quadruple)
        

    def check_for_mult_or_div(self):
        if len(self.operators_stack) is not 0:
            if self.operators_stack[-1] == "*" or self.operators_stack[-1] == "/":
                self.generate_quadruple()

    def check_for_add_or_subs(self):
        if len(self.operators_stack) > 0:
            if self.operators_stack[-1] == "+" or self.operators_stack[-1] == "-":
                self.generate_quadruple()

    def check_for_comparison(self):
        if len(self.operators_stack) > 0:
            if self.operators_stack[-1] == "==" or self.operators_stack[-1] == "!=" or self.operators_stack[-1] == ">=" or self.operators_stack[-1] == "<=" or self.operators_stack[-1] == ">" or self.operators_stack[-1] == "<":
                self.generate_quadruple()

    def check_for_logic_operators(self):
        if len(self.operators_stack) > 0:
            if self.operators_stack[-1] == "&" or self.operators_stack[-1] == "|":
                self.generate_quadruple()

    def check_for_assignment(self):
        if len(self.operators_stack) > 0:
            if self.operators_stack[-1] == "=":
                self.generate_quadruple()