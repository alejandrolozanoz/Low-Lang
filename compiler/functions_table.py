from antlr4 import *
from compiler.function import Function
from compiler.variable import Variable

class FunctionsTable:
	def __init__(self):
		self.functions = {}

	def add_function(self, function: Function):
		if function.function_name not in self.functions:
			self.functions[function.function_name] = function
		else:
			print('ERROR: La función ' + str(function.name) + ' ya estaba declarada.')

	def get_function(self, function_name):
		if function_name not in self.functions:
			print('ERROR: La función ' + str(function_name) + ' no existe en la tabla de funciones.')

		else:
			return self.functions[function_name]
