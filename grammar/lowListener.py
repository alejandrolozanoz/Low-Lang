# Generated from grammar/low.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .lowParser import lowParser
else:
    from lowParser import lowParser

from compiler.compiler import Compiler
from compiler.function import Function
compiler = Compiler()


# This class defines a complete listener for a parse tree produced by lowParser.
class lowListener(ParseTreeListener):

    # Enter a parse tree produced by lowParser#program.
    def enterProgram(self, ctx:lowParser.ProgramContext):
        pass

    # Exit a parse tree produced by lowParser#program.
    def exitProgram(self, ctx:lowParser.ProgramContext):
        pass


    # Enter a parse tree produced by lowParser#variable_declaration.
    def enterVariable_declaration(self, ctx:lowParser.Variable_declarationContext):
        pass

    # Exit a parse tree produced by lowParser#variable_declaration.
    def exitVariable_declaration(self, ctx:lowParser.Variable_declarationContext):
        pass


    # Enter a parse tree produced by lowParser#variables.
    def enterVariables(self, ctx:lowParser.VariablesContext):
        pass

    # Exit a parse tree produced by lowParser#variables.
    def exitVariables(self, ctx:lowParser.VariablesContext):
        pass


    # Enter a parse tree produced by lowParser#declaration_array_brackets.
    def enterDeclaration_array_brackets(self, ctx:lowParser.Declaration_array_bracketsContext):
        pass

    # Exit a parse tree produced by lowParser#declaration_array_brackets.
    def exitDeclaration_array_brackets(self, ctx:lowParser.Declaration_array_bracketsContext):
        pass


    # Enter a parse tree produced by lowParser#data_type.
    def enterData_type(self, ctx:lowParser.Data_typeContext):
        pass

    # Exit a parse tree produced by lowParser#data_type.
    def exitData_type(self, ctx:lowParser.Data_typeContext):
        pass


    # Enter a parse tree produced by lowParser#constant.
    def enterConstant(self, ctx:lowParser.ConstantContext):
        pass

    # Exit a parse tree produced by lowParser#constant.
    def exitConstant(self, ctx:lowParser.ConstantContext):
        pass


    # Enter a parse tree produced by lowParser#functions.
    def enterFunctions(self, ctx:lowParser.FunctionsContext):
        pass

    # Exit a parse tree produced by lowParser#functions.
    def exitFunctions(self, ctx:lowParser.FunctionsContext):
        pass


    # Enter a parse tree produced by lowParser#function.
    def enterFunction(self, ctx:lowParser.FunctionContext):
        pass

    # Exit a parse tree produced by lowParser#function.
    def exitFunction(self, ctx:lowParser.FunctionContext):
        pass


    # Enter a parse tree produced by lowParser#function_type.
    def enterFunction_type(self, ctx:lowParser.Function_typeContext):
        pass

    # Exit a parse tree produced by lowParser#function_type.
    def exitFunction_type(self, ctx:lowParser.Function_typeContext):
        pass


    # Enter a parse tree produced by lowParser#parameters.
    def enterParameters(self, ctx:lowParser.ParametersContext):
        pass

    # Exit a parse tree produced by lowParser#parameters.
    def exitParameters(self, ctx:lowParser.ParametersContext):
        pass


    # Enter a parse tree produced by lowParser#logic_expresions.
    def enterLogic_expresions(self, ctx:lowParser.Logic_expresionsContext):
        pass

    # Exit a parse tree produced by lowParser#logic_expresions.
    def exitLogic_expresions(self, ctx:lowParser.Logic_expresionsContext):
        pass


    # Enter a parse tree produced by lowParser#relational_expresions.
    def enterRelational_expresions(self, ctx:lowParser.Relational_expresionsContext):
        pass

    # Exit a parse tree produced by lowParser#relational_expresions.
    def exitRelational_expresions(self, ctx:lowParser.Relational_expresionsContext):
        pass


    # Enter a parse tree produced by lowParser#addition_substraction_expresions.
    def enterAddition_substraction_expresions(self, ctx:lowParser.Addition_substraction_expresionsContext):
        pass

    # Exit a parse tree produced by lowParser#addition_substraction_expresions.
    def exitAddition_substraction_expresions(self, ctx:lowParser.Addition_substraction_expresionsContext):
        pass


    # Enter a parse tree produced by lowParser#multiplication_division_expresions.
    def enterMultiplication_division_expresions(self, ctx:lowParser.Multiplication_division_expresionsContext):
        pass

    # Exit a parse tree produced by lowParser#multiplication_division_expresions.
    def exitMultiplication_division_expresions(self, ctx:lowParser.Multiplication_division_expresionsContext):
        pass


    # Enter a parse tree produced by lowParser#expresion.
    def enterExpresion(self, ctx:lowParser.ExpresionContext):
        pass

    # Exit a parse tree produced by lowParser#expresion.
    def exitExpresion(self, ctx:lowParser.ExpresionContext):
        pass


    # Enter a parse tree produced by lowParser#array_brackets.
    def enterArray_brackets(self, ctx:lowParser.Array_bracketsContext):
        pass

    # Exit a parse tree produced by lowParser#array_brackets.
    def exitArray_brackets(self, ctx:lowParser.Array_bracketsContext):
        pass


    # Enter a parse tree produced by lowParser#function_call.
    def enterFunction_call(self, ctx:lowParser.Function_callContext):
        pass

    # Exit a parse tree produced by lowParser#function_call.
    def exitFunction_call(self, ctx:lowParser.Function_callContext):
        pass


    # Enter a parse tree produced by lowParser#main_function.
    def enterMain_function(self, ctx:lowParser.Main_functionContext):
        pass

    # Exit a parse tree produced by lowParser#main_function.
    def exitMain_function(self, ctx:lowParser.Main_functionContext):
        pass


    # Enter a parse tree produced by lowParser#statutes.
    def enterStatutes(self, ctx:lowParser.StatutesContext):
        pass

    # Exit a parse tree produced by lowParser#statutes.
    def exitStatutes(self, ctx:lowParser.StatutesContext):
        pass


    # Enter a parse tree produced by lowParser#assignation.
    def enterAssignation(self, ctx:lowParser.AssignationContext):
        pass

    # Exit a parse tree produced by lowParser#assignation.
    def exitAssignation(self, ctx:lowParser.AssignationContext):
        pass


    # Enter a parse tree produced by lowParser#read_function_call.
    def enterRead_function_call(self, ctx:lowParser.Read_function_callContext):
        pass

    # Exit a parse tree produced by lowParser#read_function_call.
    def exitRead_function_call(self, ctx:lowParser.Read_function_callContext):
        pass


    # Enter a parse tree produced by lowParser#write_function_call.
    def enterWrite_function_call(self, ctx:lowParser.Write_function_callContext):
        pass

    # Exit a parse tree produced by lowParser#write_function_call.
    def exitWrite_function_call(self, ctx:lowParser.Write_function_callContext):
        pass


    # Enter a parse tree produced by lowParser#void_function_call.
    def enterVoid_function_call(self, ctx:lowParser.Void_function_callContext):
        pass

    # Exit a parse tree produced by lowParser#void_function_call.
    def exitVoid_function_call(self, ctx:lowParser.Void_function_callContext):
        pass


    # Enter a parse tree produced by lowParser#return_statement.
    def enterReturn_statement(self, ctx:lowParser.Return_statementContext):
        pass

    # Exit a parse tree produced by lowParser#return_statement.
    def exitReturn_statement(self, ctx:lowParser.Return_statementContext):
        pass


    # Enter a parse tree produced by lowParser#conditional_function.
    def enterConditional_function(self, ctx:lowParser.Conditional_functionContext):
        pass

    # Exit a parse tree produced by lowParser#conditional_function.
    def exitConditional_function(self, ctx:lowParser.Conditional_functionContext):
        pass


    # Enter a parse tree produced by lowParser#while_function.
    def enterWhile_function(self, ctx:lowParser.While_functionContext):
        pass

    # Exit a parse tree produced by lowParser#while_function.
    def exitWhile_function(self, ctx:lowParser.While_functionContext):
        pass


    # Enter a parse tree produced by lowParser#from_function.
    def enterFrom_function(self, ctx:lowParser.From_functionContext):
        pass

    # Exit a parse tree produced by lowParser#from_function.
    def exitFrom_function(self, ctx:lowParser.From_functionContext):
        pass



del lowParser