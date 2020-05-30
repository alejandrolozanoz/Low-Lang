from antlr4 import *
from function import Function
from variable import Variable

class FunctionsTable:
	def __init__(self):
		self.functions = {}

	def add_function(self, function_type, function_name, function_parameters):
		if function_name in self.functions:
			raise Exception("{} was already defined in the functions table".format(function_name))

		else:
			self.functions[function_name] = Function(function_name, function_type, {})
			self.functions[function_name].function_parameters = function_parameters
			for i in range(len(function_parameters)):
				self.functions[function_name].function_parameters[i] = Variable(
					function_parameters[i].type, function_parameters[i].name, function_parameters[i].value)

	def get_function(self, function_name):
		if function_name not in self.functions:
			raise Exception("{} doesn't exist in the functions table.".format(function_name))

		else:
			return self.functions[function_name]
