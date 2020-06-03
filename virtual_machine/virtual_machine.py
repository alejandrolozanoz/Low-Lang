from antlr4 import *
from compiler.function import Function
from compiler.functions_table import FunctionsTable
from compiler.variable import Variable
from compiler.quadruples_table import QuadruplesTable
from semantics.semantic_cube import SemanticCube
from memory.exec_memory import ExecMemory
from memory.constants import MemoryConstants

class VirtualMachine:
    def __init__(self, quadruples, constant_memory):
        self.quadruples = quadruples
        self.constant_memory = constant_memory

        self.current_index = 0

        self.global_memory = ExecMemory(MemoryConstants.GLOBAL_INITIAL)
        self.local_memory_stack = [ExecMemory(MemoryConstants.LOCAL_INITIAL)]
        self.temporal_memory_stack = [ExecMemory(MemoryConstants.TEMPORAL_INITIAL)]
        self.param_memory = ExecMemory(-1)
        self.temporal_memory_stack = [ExecMemory(MemoryConstants.TEMPORAL_INITIAL)]
        self.param_temporal_memory = ExecMemory(-1)
        self.semantic_cube = SemanticCube()

        self.jumps_stack = []
        
    def find_value(self, address):
        if (address >= 30000):
            return self.constant_memory.values[address]
        
        elif (address >= 20000):
            memory = self.temporal_memory_stack[len(self.temporal_memory_stack) - 1]
            return memory.values[address]
        
        elif (address >= 10000):
            memory = self.local_memory_stack[len(self.local_memory_stack)-1]
            return memory.values[address]

        else:
            return self.global_memory.values[address]
    
    def save_value(self, address, value):
        if (address >= 30000):
            self.constant_memory.values[address] = value
        elif (address >= 20000):
            memory = self.temporal_memory_stack[len(self.temporal_memory_stack)-1]
            memory.values[address] = value        
        elif (address >= 10000):
            memory = self.local_memory_stack[len(self.local_memory_stack)-1]
            memory.values[address] = value
        else:
            self.global_memory.values[address] = value

    def print_func(self, quad):
        value = self.find_value(quad.result)
        print(f"print {value}")
    
    def addition(self, quad):
        left_value = self.find_value(quad.left_operand)
        right_value = self.find_value(quad.right_operand)
        result = left_value + right_value
        self.save_value(quad.result, result)
    
    def substraction(self, quad):
        left_value = self.find_value(quad.left_operand)
        right_value = self.find_value(quad.right_operand)
        result = left_value - right_value
        self.save_value(quad.result, result)

    def multiplication(self, quad):
        left_value = self.find_value(quad.left_operand)
        right_value = self.find_value(quad.right_operand)
        result = left_value * right_value
        self.save_value(quad.result, result)

    def division(self, quad):
        left_value = self.find_value(quad.left_operand)
        right_value = self.find_value(quad.right_operand)
        result = left_value / right_value
        self.save_value(quad.result, result)

    def greater_than(self, quad):
        left_value = self.find_value(quad.left_operand)
        right_value = self.find_value(quad.right_operand)
        result = left_value > right_value
        self.save_value(quad.result, result)
    
    def less_than(self, quad):
        left_value = self.find_value(quad.left_operand)
        right_value = self.find_value(quad.right_operand)
        result = left_value < right_value
        self.save_value(quad.result, result)

    def greater_or_equal(self, quad):
        left_value = self.find_value(quad.left_operand)
        right_value = self.find_value(quad.right_operand)
        result = left_value >= right_value
        self.save_value(quad.result, result)

    def less_or_equal(self, quad):
        left_value = self.find_value(quad.left_operand)
        right_value = self.find_value(quad.right_operand)
        result = left_value <= right_value
        self.save_value(quad.result, result)

    def not_equal(self, quad):
        left_value = self.find_value(quad.left_operand)
        right_value = self.find_value(quad.right_operand)
        result = left_value != right_value
        self.save_value(quad.result, result)

    def equal(self, quad):
        left_value = self.find_value(quad.left_operand)
        right_value = self.find_value(quad.right_operand)
        result = left_value == right_value
        self.save_value(quad.result, result)

    def and_operator(self, quad):
        left_value = self.find_value(quad.left_operand)
        right_value = self.find_value(quad.right_operand)
        result = left_value and right_value
        self.save_value(quad.result, result)

    def or_operator(self, quad):
        left_value = self.find_value(quad.left_operand)
        right_value = self.find_value(quad.right_operand)
        result = left_value or right_value
        self.save_value(quad.result, result)

    def assign(self, quad):
        left_operand = self.find_value(quad.left_operand)
        self.save_value(quad.result, left_operand)

    def parameter_assign(self, quad):
        left_operand = self.find_value(quad.left_operand)
        self.save_value(quad.result, left_operand) # here I might need to do something else to save as parameter

    def return_func(self, quad):
        temporal = self.find_value(quad.left_operand)
        self.save_value(quad.result, temporal)
        # Pop from jumps stack and jump
        self.current_index = self.jumps_stack.pop()
    
    def gotoF(self, quad):
        bool_test = self.find_value(quad.left_operand)
        if bool_test is False:
            self.current_index = quad.result
        else:
            self.current_index += 1

    def verify(self, quad):
        pass
    
    def save_address_value(self, address, value):
        pass

    def add_array_base(self, quad):
        pass

    def execute(self):    
        while self.current_index < self.quadruples.length():
            quad = self.quadruples.quads[self.current_index]
            if quad.operator == "print":
                self.print_func(quad)
                self.current_index += 1
            elif quad.operator == "+":
                self.addition(quad)
                self.current_index += 1
            elif quad.operator == "-":
                self.substraction(quad)
                self.current_index += 1
            elif quad.operator == "*":
                self.multiplication(quad)
                self.current_index += 1
            elif quad.operator == "/":
                self.division(quad)
                self.current_index += 1
            elif quad.operator == "=":
                self.assign(quad)
                self.current_index += 1
            elif quad.operator == ">":
                self.greater_than(quad)
                self.current_index += 1
            elif quad.operator == "<":
                self.less_than(quad)
                self.current_index += 1
            elif quad.operator == ">=":
                self.greater_or_equal(quad)
                self.current_index += 1
            elif quad.operator == "<=":
                self.less_or_equal(quad)
                self.current_index += 1
            elif quad.operator == "!=":
                self.not_equal(quad)
                self.current_index += 1
            elif quad.operator == "==":
                self.equal(quad)
                self.current_index += 1
            elif quad.operator == "&":
                self.and_operator(quad)
                self.current_index += 1
            elif quad.operator == "|":
                self.or_operator(quad)
                self.current_index += 1
            elif quad.operator == "GOTO":
                self.current_index = quad.result
            elif quad.operator == "GOTOF":
                self.gotoF(quad)
            elif quad.operator == "VER":
                self.verify(quad)
                self.current_index += 1
            elif quad.operator == "+arr":
                self.add_array_base(quad)
                self.current_index += 1
            elif quad.operator == "ERA":
                self.param_memory = ExecMemory(30000)
                self.param_temporal_memory = ExecMemory(20000)
                self.current_index += 1
            elif quad.operator == "GOSUB":
                self.local_memory_stack.append(self.param_memory)
                self.temporal_memory_stack.append(self.param_temporal_memory)
                # Reset params memory
                self.param_memory = ExecMemory(-1)
                self.param_temporal_memory = ExecMemory(-1)
                self.jumps_stack.append(self.current_index + 1)
                self.current_index = quad.left_operand
            elif quad.operator == "PARAM":
                self.parameter_assign(quad)
                self.current_index += 1
            elif quad.operator == "RETURN":
                self.return_func(quad)
                self.local_memory_stack.pop()
                self.temporal_memory_stack.pop()
            elif quad.operator == "ENDPROC":
                self.local_memory_stack.pop()
                self.temporal_memory_stack.pop()
                self.current_index = self.jumps_stack.pop()
            elif quad.operator == "END":
                self.local_memory_stack.pop()
                self.temporal_memory_stack.pop()
                self.current_index += 1
            else:
                print("ERROR: Operador inesperado en máquina virtual.")
                print(quad)
                break
