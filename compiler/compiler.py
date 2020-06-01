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
        self.from_variables_stack = []
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
        result_type = SemanticCube().check_operation(left_operand_type, right_operand_type, operator) == Types().ERROR
        if result_type:
            print('ERROR: Los tipos de datos de la operación no son compatibles.')
        else:
            # Create quadruple and add its type and and result to type and operand stacks
            self.quadruples.append(operator, left_operand, right_operand, None)
            self.types_stack.append(SemanticCube().check_operation(left_operand_type, right_operand_type, operator))
            self.operands_stack.append(None)

    def read_quadruple(self, operand):
        if (operand in self.current_function.function_type) or (operand in self.functions_table.functions["global"].function_type):
            self.quadruples.append("read", operand, None, None)
        else:
            print('La variable ' + str(operand) + ' no está declarada')
    
    def write_quadruple(self):
        printed_operand = self.operands_stack.pop()
        self.types_stack.pop()
        self.quadruples.append("print", printed_operand, None, None)


    def assign_quadruple(self):
        if self.operators_stack and self.operators_stack[-1] == "=":
            right_operand = self.operands_stack.pop()
            left_operand = self.operands_stack.pop()
            operator = self.operators_stack.pop()
            right_operand_type = self.types_stack.pop()
            left_operand_type = self.types_stack.pop()
            
            if SemanticCube().check_operation(left_operand_type, right_operand_type, operator) == Types().ERROR:
                print('ERROR: Los tipos de datos de la asignación no son compatibles.')
    
            self.quadruples.append(operator, left_operand, right_operand, None)

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

    def check_for_assignment(self):
        if len(self.operators_stack) > 0 and self.operators_stack[-1] == Operations.ASSIGN:
            self.operation_quadruple()

    def if_statement(self):
        if len(self.operands_stack) != 0:
            # Check if while statement is valid
            conditionVar = self.operands_stack.pop()
            typeConditionVar = self.types_stack.pop()
            if typeConditionVar == Types.BOOL:
                # Create GOTOF and save quad in jumps stack to fill when we know false jump location
                self.jumps_stack.append(self.quadruples.length())
                self.quadruples.append("GOTOF", conditionVar, None, None)
            else:
                print('Error: ' + conditionVar + ' is not a boolean, its ' + typeConditionVar)

    def else_statement(self):
        # Create GOTO and save quad in jumps stack to fill when we know jump location
        self.jumps_stack.append(self.quadruples.length())
        self.quadruples.append("GOTO", None , None, None)

    def end_if_else_function(self):
        # Fill if's GOTOF quad with current index
        GOTOF = self.jumps_stack.pop()
        self.quadruples.quads[GOTOF].result = self.quadruples.length()

    def while_statement(self):
        # Save while statement quad in jumps stack to fill when we know jump location
        self.jumps_stack.append(self.quadruples.length())

    def while_statutes(self):
        if len(self.operands_stack) != 0:
            conditionVar = self.operands_stack.pop()
            typeConditionVar = self.types_stack.pop()
            if typeConditionVar == Types().Bool:
                # Save begin statutes quad in jumps stack to fill when we know jump location
                self.jumps_stack.append(self.quadruples.length())
                self.quadruples.append("GOTOF", conditionVar, None, None)
            else:
                print('Error: ' + conditionVar + ' is ' + typeConditionVar + ' + ' + 'insted of a boolean')

    def while_end(self):
        # Get while statement index to generate GOTO quad to loop in while
        while_statement_index = self.jumps_stack.pop()
        self.quadruples.append("GOTO", None, None, while_statement_index)
        # Fill while statutes quad with ending of while
        while_statutes_index = self.jumps_stack.pop()
        self.quadruples.quads[while_statutes_index].result = self.quadruples.length()
    
    def from_initialize(self, operand):
        # From variable was already declared locally or globally 
        if (operand in self.current_function.function_variables) or (operand in self.functions_table.functions["global"].function_variables):
            # Check if variable is INT to procede
            if (self.current_function.function_variables[operand].variable_type == Types.INT) or (self.functions_table.functions["global"].function_variables[operand].variable_type == Types.INT):
                # Create 'from_function' in function table and add variable
                self.add_function(self.current_function)
                self.current_function = Function('void', 'from_function', {}, {})

                # Pop variable value and save
                from_variable_value = self.operands_stack.pop()
                self.current_function.function_variables['from_variable'] = Variable(Types.INT, 'from_variable', from_variable_value)

                # Save from statement quad in jumps stack to fill when we know jump location
                self.jumps_stack.append(self.quadruples.length())

            else:
                print('The variable ' + operand + 'is not an int')

        else:
            print('The variable ' + operand + ' is not declared')

    def from_statutes(self):                
        if len(self.operands_stack) != 0:

            # Get the initial and limit values of the from loop
            from_variable = self.current_function.function_variables['from_variable']
            from_variable_limit_value = self.operands_stack.pop()
            from_variable_limit_type = self.types_stack.pop()

            if from_variable_limit_type == Types.INT:
                # Add point to jump stack and create GOTOF
                self.jumps_stack.append(self.quadruples.length())
                self.quadruples.append("GOTOF", None, None, None)
                
                if (from_variable < from_variable_limit_value):
                    self.current_function.function_variables['from_variable'].variable_value += 1
            else:
                print('Error: The expression resulting in {expResult} must be an integer')
    
    def end_from(self):
        # Get from statutes index to generate GOTO quad to loop back to from
        from_statement_index = self.jumps_stack.pop()
        self.quadruples.append("GOTO", None, None, from_statement_index)
        # Fill from statutes quad with ending of while
        from_statutes_index = self.jumps_stack.pop()
        self.quadruples.quads[from_statutes_index].result = self.quadruples.length()
