import sys
from antlr4 import *
from grammar.lowLexer import lowLexer
from grammar.lowParser import lowParser
from antlr4.tree.Trees import Trees


def main(argv):
    # Read the first argument as a filestream
    input = FileStream(argv[1])
    # Call lexer and parser
    lexer = lowLexer(input) 
    stream = CommonTokenStream(lexer)
    parser = lowParser(stream)
    # Start from the parser rule "Program"
    tree = parser.program()
    
    if parser.getNumberOfSyntaxErrors() == 0:
      print("¡Programa Compilado Correctamente!")
    else:
      print("Error al Compilar.")

if __name__ == '__main__':
    main(sys.argv)
