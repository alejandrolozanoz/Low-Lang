from antlr4 import *
from compiler.function import Function
from compiler.functions_table import FunctionsTable
from compiler.variable import Variable
from compiler.quadruples_table import QuadruplesTable
from semantics.types import Types
from semantics.operations import Operations
from semantics.semantic_cube import SemanticCube
from memory.memory import Memory
from memory.constants import MemoryConstants
from virtual_machine.virtual_machine import VirtualMachine
from memory.exec_memory import ExecMemory

class Compiler:
    def __init__(self):
        self.functions_table = FunctionsTable()
        self.current_function = Function("void", "global", [], {}, function_memory=Memory(MemoryConstants.GLOBAL_INITIAL))
        self.semantic_cube = SemanticCube()
        self.quadruples = QuadruplesTable()
        self.operators_stack = []
        self.operands_stack = []
        self.jumps_stack = []
        self.types_stack = []
        self.temporal_memory = Memory(MemoryConstants.TEMPORAL_INITIAL)
        self.constant_memory = Memory(MemoryConstants.CONSTANT_INITIAL)
        self.constant_exec_memory = ExecMemory(MemoryConstants.CONSTANT_INITIAL)

    def add_function(self, function: Function):
        self.current_function.start_quadruple = self.quadruples.length()
        self.functions_table.add_function(function)
        if function.function_type != "void":
            self.functions_table.functions["global"].update_variables(function.function_type, function.function_name)

    def add_variable(self, variable_name):
        if variable_name in self.current_function.function_variables:
            variable = self.current_function.function_variables[variable_name]
            self.operands_stack.append(variable.variable_address)
            self.add_type(variable.variable_type)
        
        elif variable_name in self.functions_table.functions["global"].function_variables:
            variable = self.functions_table.functions["global"].function_variables[variable_name]
            self.operands_stack.append(variable.variable_address)
            self.add_type(variable.variable_type)
        
        elif variable_name in self.functions_table.functions:
             if self.functions_table.functions[variable_name].function_type == 'void':
                 print('ERROR: No se puede asignar una función void ' + variable_name + ' a una variable')
             else:
                 self.operands_stack.append(variable_name)
                 self.add_type(self.functions_table.functions[variable_name].function_type)
        else:
            print('ERROR: La variable ' + str(variable_name) + ' no está declarada')

    def add_operator(self, operator):
        self.operators_stack.append(operator)
        # print('Operator: ', operator, self.operators_stack)

    def add_type(self, type):
        self.types_stack.append(type)
        # print('Type: ', type, self.types_stack)

    def add_constant_operand(self, operand, type):
        address = self.constant_memory.get_address(type)
        constant = Variable(type, operand, operand, address)
        self.constant_exec_memory.save_value(address, operand)
        self.operands_stack.append(constant.variable_address)
        self.types_stack.append(type)
        # print('Operand: ', operand, self.operators_stack)

    def left_parenthesis(self):
        self.operators_stack.append('(')
        # print('Parenthesis: (', self.operators_stack)

    def right_parenthesis(self):
        self.operators_stack.pop()
        # print('Parenthesis: )')
    
    def operation_quadruple(self):
        # print("Operation Quad Gen: ", self.operands_stack, self.operators_stack, self.types_stack)
        right_operand = self.operands_stack.pop()
        left_operand = self.operands_stack.pop()
        operator = self.operators_stack.pop()
        right_operand_type = self.types_stack.pop()
        left_operand_type = self.types_stack.pop()
        result_type = SemanticCube().check_operation(left_operand_type, right_operand_type, operator)
        if result_type == Types.ERROR:
            print('ERROR: Los tipos de datos de la operación no son compatibles.')
        else:
            # Create quadruple and add its type and and result to type and operand stacks
            result_address = self.temporal_memory.get_address(result_type)
            self.quadruples.append(operator, left_operand, right_operand, result_address)
            self.types_stack.append(result_type)
            self.operands_stack.append(result_address)

    def read_quadruple(self, operand):
        # print("Read Quad Gen: ", operand, operand in self.current_function.function_type, operand in self.functions_table.functions["global"].function_type)
        if (operand in self.current_function.function_type) or (operand in self.functions_table.functions["global"].function_type):
            self.quadruples.append("read", operand, None, self.quadruples.length())
        else:
            print('ERROR: La variable ' + str(operand) + ' no está declarada')
    
    def write_quadruple(self):
        # print("Write Quad Gen: ", self.operands_stack[len(self.operands_stack)-1])
        if len(self.operands_stack) == 0:
            print('ERROR: Se quiere hacer un print pero no hay operandos en el stack')
        else:
            printed_operand = self.operands_stack.pop()
            self.types_stack.pop()
            self.quadruples.append("print", None, None, printed_operand)


    def assign_quadruple(self):
        # print("Assign Quad Gen: ", self.operators_stack[len(self.operators_stack)-1], self.operands_stack)
        if self.operators_stack[len(self.operators_stack)-1] == '=':
            right_operand = self.operands_stack.pop()
            left_operand = self.operands_stack.pop()
            operator = self.operators_stack.pop()
            right_operand_type = self.types_stack.pop()
            left_operand_type = self.types_stack.pop()
            result_type = SemanticCube().check_operation(left_operand_type, right_operand_type, operator)
            if result_type == Types.ERROR:
                print('ERROR: Los tipos de datos de la asignación no son compatibles.')
            self.quadruples.append(operator, right_operand, None, left_operand)
        else:
            print('ERROR: Se entró a crear un quad de asignación pero no está el operando = en el stack.', self.operators_stack)

    def check_for_mult_or_div(self):
        # print("Mult/Div Check", len(self.operators_stack), self.operators_stack[-1:])
        if len(self.operators_stack) is not 0 and self.operators_stack[len(self.operators_stack)-1] in [Operations.MULTIPLICATION, Operations.DIVISION]:
            self.operation_quadruple()

    def check_for_add_or_subs(self):
        # print("Add/Sub Check", len(self.operators_stack), self.operators_stack[-1:])
        if len(self.operators_stack) > 0 and self.operators_stack[len(self.operators_stack)-1] in [Operations.ADDITION, Operations.SUBTRACTION]:
            self.operation_quadruple()

    def check_for_relational_operators(self):
        # print("Relational Check", len(self.operators_stack), self.operators_stack[-1:])
        if len(self.operators_stack) > 0 and self.operators_stack[len(self.operators_stack)-1] in [Operations.EQUAL, Operations.NOT_EQUAL,  Operations.GREATER_OR_EQUAL, Operations.LESS_OR_EQUAL, Operations.GREATER, Operations.LESS]:
            self.operation_quadruple()

    def check_for_logic_operators(self):
        # print("Logic Check", len(self.operators_stack), self.operators_stack[-1:])
        if len(self.operators_stack) > 0 and self.operators_stack[len(self.operators_stack)-1] in [Operations.AND, Operations.OR]:
            self.operation_quadruple()

    def check_for_assignment(self):
        # print("Asignment Check", len(self.operators_stack), self.operators_stack[-1:])
        if len(self.operators_stack) > 0 and self.operators_stack[len(self.operators_stack)-1] == Operations.ASSIGN:
            self.operation_quadruple()

    def if_statement(self):
        if len(self.operands_stack) != 0:
            # Check if while statement is valid
            condition_var = self.operands_stack.pop()
            type_condition_var = self.types_stack.pop()
            # print(self.operands_stack, self.operators_stack, self.types_stack, self.jumps_stack) 
            if type_condition_var == Types.BOOL:
                # Create GOTOF and save quad in jumps stack to fill when we know false jump location
                self.jumps_stack.append(self.quadruples.length())
                self.quadruples.append("GOTOF", condition_var, None, None)
            else:
                print('ERROR: ' + str(condition_var)+ ' no es un boolean, es ' + str(type_condition_var))

    def else_statement(self):
        self.quadruples.quads[self.jumps_stack.pop()].result = self.quadruples.length() + 1
        # Create GOTO and save quad in jumps stack to fill when we know jump location
        self.jumps_stack.append(self.quadruples.length())
        self.quadruples.append("GOTO", None , None, None)

    def end_if_else_function(self):
        # Fill if's GOTOF quad with current index
        self.quadruples.quads[self.jumps_stack.pop()].result = self.quadruples.length()

    def while_statement(self):
        # Save while statement quad in jumps stack to fill when we know jump location
        self.jumps_stack.append(self.quadruples.length())

    def while_statutes(self):
        if len(self.operands_stack) != 0:
            condition_var = self.operands_stack.pop()
            type_condition_var = self.types_stack.pop()
            if type_condition_var == Types.BOOL:
                # Save begin statutes quad in jumps stack to fill when we know jump location
                self.jumps_stack.append(self.quadruples.length())
                self.quadruples.append("GOTOF", condition_var, None, None)
            else:
                print('ERROR: ' + condition_var + ' es ' + type_condition_var + 'en vez de boolean.')

    def while_end(self):
        # Fill while statutes quad with ending of while
        while_statutes_index = self.jumps_stack.pop()
        self.quadruples.quads[while_statutes_index].result = self.quadruples.length() + 1
        # Get while statement index to generate GOTO quad to loop in while
        while_statement_index = self.jumps_stack.pop()
        self.quadruples.append("GOTO", None, None, while_statement_index)
    
    def from_initialize(self, operand):
        # From variable was already declared locally or globally 
        if (operand in self.current_function.function_variables) or (operand in self.functions_table.functions["global"].function_variables):
            # Check if variable is INT to procede
            if (self.current_function.function_variables[operand].variable_type == Types.INT) or (self.functions_table.functions["global"].function_variables[operand].variable_type == Types.INT):
                # Create 'from_function' in function table and add variable
                self.add_function(self.current_function)
                self.current_function = Function('void', 'from_function', [], {})

                # Pop variable value and save
                from_variable_value = self.operands_stack.pop()
                self.types_stack.pop()
                self.current_function.function_variables['from_variable'] = Variable(Types.INT, 'from_variable', from_variable_value)

                # Save from statement quad in jumps stack to fill when we know jump location
                self.jumps_stack.append(self.quadruples.length())

            else:
                print('ERROR: La variable ' + operand + 'no es un entero')
        else:
            print('ERROR: La variable ' + operand + ' no está declarada')

    def from_statutes(self):                
        if len(self.operands_stack) != 0:

            # Get the initial and limit values of the from loop
            try: 
                from_variable = self.current_function.function_variables['from_variable']
            except:
                print('ERROR: No se encontró la variable del loop desde-hasta')
            
            from_variable_limit_value = self.operands_stack.pop()
            from_variable_limit_type = self.types_stack.pop()

            if from_variable_limit_type == Types.INT:
                # Add point to jump stack and create GOTOF
                self.jumps_stack.append(self.quadruples.length())
                self.quadruples.append("GOTOF", None, None, None)
                
                if (from_variable < from_variable_limit_value):
                    self.current_function.function_variables['from_variable'].variable_value += 1
            else:
                print('ERROR: La expresión asignada a la variable del from debe de ser un entero')
    
    def end_from(self):
        # Get from statutes index to generate GOTO quad to loop back to from
        from_statement_index = self.jumps_stack.pop()
        self.quadruples.append("GOTO", None, None, from_statement_index)
        # Fill from statutes quad with ending of while
        from_statutes_index = self.jumps_stack.pop()
        self.quadruples.quads[from_statutes_index].result = self.quadruples.length()

    def add_function_operand_type(self, operand):
        if self.functions_table.functions[operand].function_type == 'void':
            print('ERROR: No se le puede asignar a la función void ' + operand + ' un valor.')
        else:
            self.operands_stack.append(operand)
            self.add_type(self.functions_table.functions[operand].function_type)


    def check_parameters(self, id, currentCounter):
        if len(self.functions_table.functions[id].function_parameters) == currentCounter:
            # reversed FOR because the function_parameters is reversed in relation to operands_stack
            # example: funccall(0, 1, 2) --> passed_parameter is the one we want to match with 2
            for parameter in reversed(self.functions_table.functions[id].function_parameters):
                passed_parameter = self.operands_stack.pop()
                passed_parameter_type = self.types_stack.pop()
                
                if (parameter.type != passed_parameter_type):
                    print('ERROR: El parámetro ' + passed_parameter + ' de tipo ' + passed_parameter_type + 'no se puede asignar a ' + parameter.type)
                else:
                    # tenemos que asignar a memoria aqui passed_parameter con su type
                    print("Parametros correctos")
        else:
            print('ERROR: Número de parámetros en llamada a la función ' + id + ' no coincide con la cantidad declarada.')

    def goto_main(self):
        self.jumps_stack.append(0)
        self.quadruples.append("GOTO", None, None, "_")

    def start_main(self):
        mainQuad = self.jumps_stack.pop()
        self.quadruples.quads[mainQuad].result = self.quadruples.length()

    def goto_function(self, id):
        self.quadruples.append('GOSUB', None, None, self.functions_table.functions[id].start_quadruple)
        if self.functions_table.functions[id].function_type != "void":
            ret_type = self.functions_table.functions[id].function_type
            ret_address = self.temporal_memory.get_address(ret_type)
            self.quadruples.append('=', self.functions_table.functions["global"].function_variables[id].variable_address, None, ret_address)
            self.operands_stack.append(ret_address)
            self.types_stack.append(ret_type)

    def create_era(self, function_name):
        self.quadruples.append("ERA", None, None, function_name)

    def add_param(self):
        self.types_stack.pop()
        self.quadruples.append("PARAM", None, None, self.operands_stack.pop())

    def end_function(self):
        self.current_function.end_quadruple = self.quadruples.length()
        self.quadruples.append('ENDPROC', None, None, None)

    def return_end_function(self):
        if self.current_function.function_type != "void":
            self.current_function.end_quadruple = self.quadruples.length()
            return_address = self.functions_table.functions["global"].function_variables[self.current_function.function_name].variable_address
            self.types_stack.pop()
            self.quadruples.append('RETURN', self.operands_stack.pop(), None, return_address)
        else:
            print('ERROR: La función void ' + self.current_function.function_name + ' no puede tener un estatuto regresa.')

    # def void_function(self, id):
    #     if id in self.functions_table.functions:
    #         if self.functions_table.functions[id].function_type != 'void':
    #             print('ERROR: Function ' + id + ' return value must be assigned')
    #         else:
    #             print('VOID FUNCTION: Pudimos llamar void function', {id})
    #     else:
    #         print('ERROR: Function ' + id + ' is not declared.')

    def void_end_function(self):
        if self.current_function.function_type == "void":
            self.current_function.end_quadruple = self.quadruples.length()
            self.quadruples.append('GOTO', None, None, '_')
        else:
            print('ERROR: No se encontró valor de retorno en la función' + self.current_function.name + 'de tipo ' + self.current_function.function_type)

    def finish_program(self):
        self.quadruples.append("END", None, None, None)
        print("Quadruplos del Programa: ")
        self.quadruples.print()
        print('Stack de operandos: ', self.operands_stack)
        print('Stack de operadores: ', self.operators_stack)
        print('Stack de tipos',  self.types_stack)
        print('Stack de saltos', self.jumps_stack)
        vm = VirtualMachine(self.quadruples, self.constant_exec_memory)
        vm.execute()
