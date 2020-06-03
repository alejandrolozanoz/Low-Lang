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
        print(f"PRINT {value}")
    
    def add(self, quad):
        left_value = self.find_value(quad.left_operand)
        right_value = self.find_value(quad.right_operand)
        result = left_value + right_value
        self.save_value(quad.result, result)
    
    def assign(self, quad):
        left_operand = self.find_value(quad.left_operand)
        self.save_value(quad.result, left_operand)
    
    def execute(self):    
        while self.current_index < self.quadruples.length():
            quad = self.quadruples.quads[self.current_index]
            if quad.operator == "print":
                self.print_func(quad)
                self.current_index += 1
            elif quad.operator == "+":
                self.add(quad)
                self.current_index += 1
            elif quad.operator == "=":
                self.assign(quad)
                self.current_index += 1
            elif quad.operator == "GOTO":
                self.current_index = quad.result
            elif quad.operator == "END":
                self.local_memory_stack.pop()
                self.temporal_memory_stack.pop()
                self.current_index += 1
            else:
                print("Unexpected operator")
                print(quad)
