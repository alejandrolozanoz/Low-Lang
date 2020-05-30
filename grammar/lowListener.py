# Generated from grammar/low.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .lowParser import lowParser
else:
    from lowParser import lowParser

from compiler.compiler import Compiler
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


    # Enter a parse tree produced by lowParser#var_types.
    def enterVar_types(self, ctx:lowParser.Var_typesContext):
        pass

    # Exit a parse tree produced by lowParser#var_types.
    def exitVar_types(self, ctx:lowParser.Var_typesContext):
        pass


    # Enter a parse tree produced by lowParser#constant.
    def enterConstant(self, ctx:lowParser.ConstantContext):
        pass

    # Exit a parse tree produced by lowParser#constant.
    def exitConstant(self, ctx:lowParser.ConstantContext):
        pass


    # Enter a parse tree produced by lowParser#varindividual.
    def enterVarindividual(self, ctx:lowParser.VarindividualContext):
        pass

    # Exit a parse tree produced by lowParser#varindividual.
    def exitVarindividual(self, ctx:lowParser.VarindividualContext):
        pass


    # Enter a parse tree produced by lowParser#function_declaration.
    def enterFunction_declaration(self, ctx:lowParser.Function_declarationContext):
        pass

    # Exit a parse tree produced by lowParser#function_declaration.
    def exitFunction_declaration(self, ctx:lowParser.Function_declarationContext):
        pass


    # Enter a parse tree produced by lowParser#function.
    def enterFunction(self, ctx:lowParser.FunctionContext):
        pass

    # Exit a parse tree produced by lowParser#function.
    def exitFunction(self, ctx:lowParser.FunctionContext):
        pass


    # Enter a parse tree produced by lowParser#parameters.
    def enterParameters(self, ctx:lowParser.ParametersContext):
        pass

    # Exit a parse tree produced by lowParser#parameters.
    def exitParameters(self, ctx:lowParser.ParametersContext):
        pass


    # Enter a parse tree produced by lowParser#expresions.
    def enterExpresions(self, ctx:lowParser.ExpresionsContext):
        pass

    # Exit a parse tree produced by lowParser#expresions.
    def exitExpresions(self, ctx:lowParser.ExpresionsContext):
        pass


    # Enter a parse tree produced by lowParser#multiple_expresions.
    def enterMultiple_expresions(self, ctx:lowParser.Multiple_expresionsContext):
        pass

    # Exit a parse tree produced by lowParser#multiple_expresions.
    def exitMultiple_expresions(self, ctx:lowParser.Multiple_expresionsContext):
        pass


    # Enter a parse tree produced by lowParser#expresion_comparison.
    def enterExpresion_comparison(self, ctx:lowParser.Expresion_comparisonContext):
        pass

    # Exit a parse tree produced by lowParser#expresion_comparison.
    def exitExpresion_comparison(self, ctx:lowParser.Expresion_comparisonContext):
        pass


    # Enter a parse tree produced by lowParser#expresion.
    def enterExpresion(self, ctx:lowParser.ExpresionContext):
        pass

    # Exit a parse tree produced by lowParser#expresion.
    def exitExpresion(self, ctx:lowParser.ExpresionContext):
        pass


    # Enter a parse tree produced by lowParser#term.
    def enterTerm(self, ctx:lowParser.TermContext):
        pass

    # Exit a parse tree produced by lowParser#term.
    def exitTerm(self, ctx:lowParser.TermContext):
        pass


    # Enter a parse tree produced by lowParser#factor.
    def enterFactor(self, ctx:lowParser.FactorContext):
        pass

    # Exit a parse tree produced by lowParser#factor.
    def exitFactor(self, ctx:lowParser.FactorContext):
        pass


    # Enter a parse tree produced by lowParser#statute.
    def enterStatute(self, ctx:lowParser.StatuteContext):
        pass

    # Exit a parse tree produced by lowParser#statute.
    def exitStatute(self, ctx:lowParser.StatuteContext):
        pass


    # Enter a parse tree produced by lowParser#assignation.
    def enterAssignation(self, ctx:lowParser.AssignationContext):
        pass

    # Exit a parse tree produced by lowParser#assignation.
    def exitAssignation(self, ctx:lowParser.AssignationContext):
        pass


    # Enter a parse tree produced by lowParser#voidcall.
    def enterVoidcall(self, ctx:lowParser.VoidcallContext):
        pass

    # Exit a parse tree produced by lowParser#voidcall.
    def exitVoidcall(self, ctx:lowParser.VoidcallContext):
        pass


    # Enter a parse tree produced by lowParser#returncall.
    def enterReturncall(self, ctx:lowParser.ReturncallContext):
        pass

    # Exit a parse tree produced by lowParser#returncall.
    def exitReturncall(self, ctx:lowParser.ReturncallContext):
        pass


    # Enter a parse tree produced by lowParser#indexvariable.
    def enterIndexvariable(self, ctx:lowParser.IndexvariableContext):
        pass

    # Exit a parse tree produced by lowParser#indexvariable.
    def exitIndexvariable(self, ctx:lowParser.IndexvariableContext):
        pass


    # Enter a parse tree produced by lowParser#read.
    def enterRead(self, ctx:lowParser.ReadContext):
        pass

    # Exit a parse tree produced by lowParser#read.
    def exitRead(self, ctx:lowParser.ReadContext):
        pass


    # Enter a parse tree produced by lowParser#write.
    def enterWrite(self, ctx:lowParser.WriteContext):
        pass

    # Exit a parse tree produced by lowParser#write.
    def exitWrite(self, ctx:lowParser.WriteContext):
        pass


    # Enter a parse tree produced by lowParser#conditional.
    def enterConditional(self, ctx:lowParser.ConditionalContext):
        pass

    # Exit a parse tree produced by lowParser#conditional.
    def exitConditional(self, ctx:lowParser.ConditionalContext):
        pass


    # Enter a parse tree produced by lowParser#whileloop.
    def enterWhileloop(self, ctx:lowParser.WhileloopContext):
        pass

    # Exit a parse tree produced by lowParser#whileloop.
    def exitWhileloop(self, ctx:lowParser.WhileloopContext):
        pass


    # Enter a parse tree produced by lowParser#fromloop.
    def enterFromloop(self, ctx:lowParser.FromloopContext):
        pass

    # Exit a parse tree produced by lowParser#fromloop.
    def exitFromloop(self, ctx:lowParser.FromloopContext):
        pass


    # Enter a parse tree produced by lowParser#main_function.
    def enterMain_function(self, ctx:lowParser.Main_functionContext):
        pass

    # Exit a parse tree produced by lowParser#main_function.
    def exitMain_function(self, ctx:lowParser.Main_functionContext):
        pass



del lowParser