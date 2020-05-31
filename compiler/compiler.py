from antlr4 import *
from compiler.function import Function
from compiler.functions_table import FunctionsTable
from compiler.variable import Variable
from compiler.quadruples_table import QuadruplesTable
from semantics.types import Types
from semantics.operations import Operations
from semantics.semantic_cube import SemanticCube

class Compiler:
    def __init__(self):
        self.functions_table = FunctionsTable()
        self.current_function = Function("void", "global", {}, {})
        self.semantic_cube = SemanticCube()
        self.quadruples = QuadruplesTable()
        self.operators_stack = []
        self.operands_stack = []
        self.jumps_stack = []
        self.types_stack = []

        self.counter = 0
        
    def add_function(self, function: Function):
        self.functions_table.add_function(function)

    def add_variable(self, variable_name):
        if variable_name in self.current_function.function_variables:
            self.operands_stack.append(variable_name)
            self.add_type(self.current_function.function_variables[variable_name].variable_type)
        
        elif variable_name in self.functions_table.functions["global"].function_variables:
            self.operands_stack.append(variable_name)
            self.add_type(self.functions_table.functions["global"].function_variables[variable_name].variable_type)
        
        else:
            print('La variable ' + str(variable_name) + ' no está declarada')

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
    
    def operation_quadruple(self):
        right_operand = self.operands_stack.pop()
        left_operand = self.operands_stack.pop()
        operator = self.operators_stack.pop()
        right_operand_type = self.types_stack.pop()
        left_operand_type = self.types_stack.pop()
        if SemanticCube().check_operation(left_operand_type, right_operand_type, operator) == Types().ERROR:
            print('ERROR: Los tipos de datos de la operación no son compatibles.')
        else:
            self.quadruples.append(operator, left_operand, right_operand, "_")

    def read_quadruple(self, operand):
        if (operand in self.current_function.function_type) or (operand in self.functions_table.functions["global"].function_type):
            self.quadruples.append("read", operand, None, "_")
        else:
            print('La variable ' + str(operand) + ' no está declarada')
    
    def write_quadruple(self):
        printed_operand = self.operands_stack.pop()
        self.types_stack.pop()
        self.quadruples.append("print", printed_operand, None, "_")


    def assign_quadruple(self):
        if self.operators_stack and self.operators_stack[-1] == "=":
            right_operand = self.operands_stack.pop()
            left_operand = self.operands_stack.pop()
            operator = self.operators_stack.pop()
            right_operand_type = self.types_stack.pop()
            left_operand_type = self.types_stack.pop()
            
            if SemanticCube().check_operation(left_operand_type, right_operand_type, operator) == Types().ERROR:
                print('ERROR: Los tipos de datos de la asignación no son compatibles.')
    
            self.quadruples.append(operator, left_operand, right_operand, "_")

    def check_for_mult_or_div(self):
        if len(self.operators_stack) is not 0 and self.operators_stack[-1] in [Operations.MULTIPLICATION, Operations.DIVISION]:
            self.operation_quadruple()

    def check_for_add_or_subs(self):
        if len(self.operators_stack) > 0 and self.operators_stack[-1] in [Operations.ADDITION, Operations.SUBTRACTION]:
            self.operation_quadruple()

    def check_for_relational_operators(self):
        if len(self.operators_stack) > 0 and self.operators_stack[-1] in [Operations.EQUAL, Operations.NOT_EQUAL,  Operations.GREATER_OR_EQUAL, Operations.LESS_OR_EQUAL, Operations.GREATER, Operations.LESS]:
            self.operation_quadruple()

    def check_for_logic_operators(self):
        if len(self.operators_stack) > 0 and self.operators_stack[-1] in [Operations.AND, Operations.OR]:
            self.operation_quadruple()
