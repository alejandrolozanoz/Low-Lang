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
    
    sintax_errors = parser.getNumberOfSyntaxErrors()
    if sintax_errors == 0:
      print("Programa sin errores de sintaxis")
    else:
      print("Hay con " + sintax_errors + "errores de sintaxis en el código.")

if __name__ == '__main__':
    main(sys.argv)
