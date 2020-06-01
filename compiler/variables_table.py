from antlr4 import *
from variable import Variable 

class VariablesTable:
	def __init__(self):
		self.variables = {}

	def add_variable(self, variable_type, variable_name, variable_value):
		if variable_name in self.variables:
			print('ERROR: La variable' + str(variable_name) + ' ya estaba definida en la tabla de variables.')

		else:
			var = Variable(variable_type, variable_name, variable_value)
			self.variables[variable_name] = var

	def get_variable(self, variable_name):
		if variable_name not in self.variables:
			print('ERROR: La variable' + str(variable_name) + ' no existe en la tabla de variables.')
		        
		else:
			return self.variables[variable_name]
