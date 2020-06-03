# Generated from grammar/low.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from compiler.compiler import Compiler
from compiler.function import Function
from memory.memory import Memory
from memory.constants import MemoryConstants
from semantics.types import Types
compiler = Compiler()



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\65")
        buf.write("\u0167\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30")
        buf.write("\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36")
        buf.write("\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3#\3$\3$\3%")
        buf.write("\3%\3%\3&\3&\3&\3\'\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3")
        buf.write(",\3,\7,\u011b\n,\f,\16,\u011e\13,\3,\3,\3-\3-\3-\3-\3")
        buf.write(".\6.\u0127\n.\r.\16.\u0128\3/\6/\u012c\n/\r/\16/\u012d")
        buf.write("\3/\3/\6/\u0132\n/\r/\16/\u0133\3\60\3\60\3\60\3\60\3")
        buf.write("\60\3\60\3\60\3\60\3\60\5\60\u013f\n\60\3\61\3\61\7\61")
        buf.write("\u0143\n\61\f\61\16\61\u0146\13\61\3\62\3\62\3\62\3\62")
        buf.write("\7\62\u014c\n\62\f\62\16\62\u014f\13\62\3\62\3\62\3\62")
        buf.write("\3\62\3\62\3\63\3\63\3\63\3\63\7\63\u015a\n\63\f\63\16")
        buf.write("\63\u015d\13\63\3\63\3\63\3\64\6\64\u0162\n\64\r\64\16")
        buf.write("\64\u0163\3\64\3\64\4\u011c\u014d\2\65\3\3\5\4\7\5\t\6")
        buf.write("\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20")
        buf.write("\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65")
        buf.write("\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60")
        buf.write("_\61a\62c\63e\64g\65\3\2\7\3\2\62;\5\2C\\aac|\6\2\62;")
        buf.write("C\\aac|\4\2\f\f\17\17\5\2\13\f\17\17\"\"\2\u016f\2\3\3")
        buf.write("\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2")
        buf.write("\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2")
        buf.write("\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2")
        buf.write("\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2")
        buf.write("\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3")
        buf.write("\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2")
        buf.write("\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3")
        buf.write("\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K")
        buf.write("\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2")
        buf.write("U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2")
        buf.write("\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2")
        buf.write("\2\3i\3\2\2\2\5r\3\2\2\2\7|\3\2\2\2\t\u0084\3\2\2\2\13")
        buf.write("\u008c\3\2\2\2\r\u0090\3\2\2\2\17\u0098\3\2\2\2\21\u009b")
        buf.write("\3\2\2\2\23\u00a4\3\2\2\2\25\u00a9\3\2\2\2\27\u00b2\3")
        buf.write("\2\2\2\31\u00b8\3\2\2\2\33\u00be\3\2\2\2\35\u00c4\3\2")
        buf.write("\2\2\37\u00c9\3\2\2\2!\u00cd\3\2\2\2#\u00d4\3\2\2\2%\u00d9")
        buf.write("\3\2\2\2\'\u00dd\3\2\2\2)\u00e3\3\2\2\2+\u00e8\3\2\2\2")
        buf.write("-\u00ea\3\2\2\2/\u00ec\3\2\2\2\61\u00ee\3\2\2\2\63\u00f0")
        buf.write("\3\2\2\2\65\u00f2\3\2\2\2\67\u00f4\3\2\2\29\u00f6\3\2")
        buf.write("\2\2;\u00f8\3\2\2\2=\u00fa\3\2\2\2?\u00fc\3\2\2\2A\u00fe")
        buf.write("\3\2\2\2C\u0100\3\2\2\2E\u0102\3\2\2\2G\u0105\3\2\2\2")
        buf.write("I\u0107\3\2\2\2K\u010a\3\2\2\2M\u010d\3\2\2\2O\u0110\3")
        buf.write("\2\2\2Q\u0112\3\2\2\2S\u0114\3\2\2\2U\u0116\3\2\2\2W\u0118")
        buf.write("\3\2\2\2Y\u0121\3\2\2\2[\u0126\3\2\2\2]\u012b\3\2\2\2")
        buf.write("_\u013e\3\2\2\2a\u0140\3\2\2\2c\u0147\3\2\2\2e\u0155\3")
        buf.write("\2\2\2g\u0161\3\2\2\2ij\7r\2\2jk\7t\2\2kl\7q\2\2lm\7i")
        buf.write("\2\2mn\7t\2\2no\7c\2\2op\7o\2\2pq\7c\2\2q\4\3\2\2\2rs")
        buf.write("\7r\2\2st\7t\2\2tu\7k\2\2uv\7p\2\2vw\7e\2\2wx\7k\2\2x")
        buf.write("y\7r\2\2yz\7c\2\2z{\7n\2\2{\6\3\2\2\2|}\7h\2\2}~\7w\2")
        buf.write("\2~\177\7p\2\2\177\u0080\7e\2\2\u0080\u0081\7k\2\2\u0081")
        buf.write("\u0082\7q\2\2\u0082\u0083\7p\2\2\u0083\b\3\2\2\2\u0084")
        buf.write("\u0085\7t\2\2\u0085\u0086\7g\2\2\u0086\u0087\7i\2\2\u0087")
        buf.write("\u0088\7t\2\2\u0088\u0089\7g\2\2\u0089\u008a\7u\2\2\u008a")
        buf.write("\u008b\7c\2\2\u008b\n\3\2\2\2\u008c\u008d\7n\2\2\u008d")
        buf.write("\u008e\7g\2\2\u008e\u008f\7g\2\2\u008f\f\3\2\2\2\u0090")
        buf.write("\u0091\7g\2\2\u0091\u0092\7u\2\2\u0092\u0093\7e\2\2\u0093")
        buf.write("\u0094\7t\2\2\u0094\u0095\7k\2\2\u0095\u0096\7d\2\2\u0096")
        buf.write("\u0097\7g\2\2\u0097\16\3\2\2\2\u0098\u0099\7u\2\2\u0099")
        buf.write("\u009a\7k\2\2\u009a\20\3\2\2\2\u009b\u009c\7g\2\2\u009c")
        buf.write("\u009d\7p\2\2\u009d\u009e\7v\2\2\u009e\u009f\7q\2\2\u009f")
        buf.write("\u00a0\7p\2\2\u00a0\u00a1\7e\2\2\u00a1\u00a2\7g\2\2\u00a2")
        buf.write("\u00a3\7u\2\2\u00a3\22\3\2\2\2\u00a4\u00a5\7u\2\2\u00a5")
        buf.write("\u00a6\7k\2\2\u00a6\u00a7\7p\2\2\u00a7\u00a8\7q\2\2\u00a8")
        buf.write("\24\3\2\2\2\u00a9\u00aa\7o\2\2\u00aa\u00ab\7k\2\2\u00ab")
        buf.write("\u00ac\7g\2\2\u00ac\u00ad\7p\2\2\u00ad\u00ae\7v\2\2\u00ae")
        buf.write("\u00af\7t\2\2\u00af\u00b0\7c\2\2\u00b0\u00b1\7u\2\2\u00b1")
        buf.write("\26\3\2\2\2\u00b2\u00b3\7j\2\2\u00b3\u00b4\7c\2\2\u00b4")
        buf.write("\u00b5\7e\2\2\u00b5\u00b6\7g\2\2\u00b6\u00b7\7t\2\2\u00b7")
        buf.write("\30\3\2\2\2\u00b8\u00b9\7f\2\2\u00b9\u00ba\7g\2\2\u00ba")
        buf.write("\u00bb\7u\2\2\u00bb\u00bc\7f\2\2\u00bc\u00bd\7g\2\2\u00bd")
        buf.write("\32\3\2\2\2\u00be\u00bf\7j\2\2\u00bf\u00c0\7c\2\2\u00c0")
        buf.write("\u00c1\7u\2\2\u00c1\u00c2\7v\2\2\u00c2\u00c3\7c\2\2\u00c3")
        buf.write("\34\3\2\2\2\u00c4\u00c5\7x\2\2\u00c5\u00c6\7q\2\2\u00c6")
        buf.write("\u00c7\7k\2\2\u00c7\u00c8\7f\2\2\u00c8\36\3\2\2\2\u00c9")
        buf.write("\u00ca\7x\2\2\u00ca\u00cb\7c\2\2\u00cb\u00cc\7t\2\2\u00cc")
        buf.write(" \3\2\2\2\u00cd\u00ce\7u\2\2\u00ce\u00cf\7v\2\2\u00cf")
        buf.write("\u00d0\7t\2\2\u00d0\u00d1\7k\2\2\u00d1\u00d2\7p\2\2\u00d2")
        buf.write("\u00d3\7i\2\2\u00d3\"\3\2\2\2\u00d4\u00d5\7e\2\2\u00d5")
        buf.write("\u00d6\7j\2\2\u00d6\u00d7\7c\2\2\u00d7\u00d8\7t\2\2\u00d8")
        buf.write("$\3\2\2\2\u00d9\u00da\7k\2\2\u00da\u00db\7p\2\2\u00db")
        buf.write("\u00dc\7v\2\2\u00dc&\3\2\2\2\u00dd\u00de\7h\2\2\u00de")
        buf.write("\u00df\7n\2\2\u00df\u00e0\7q\2\2\u00e0\u00e1\7c\2\2\u00e1")
        buf.write("\u00e2\7v\2\2\u00e2(\3\2\2\2\u00e3\u00e4\7d\2\2\u00e4")
        buf.write("\u00e5\7q\2\2\u00e5\u00e6\7q\2\2\u00e6\u00e7\7n\2\2\u00e7")
        buf.write("*\3\2\2\2\u00e8\u00e9\7*\2\2\u00e9,\3\2\2\2\u00ea\u00eb")
        buf.write("\7+\2\2\u00eb.\3\2\2\2\u00ec\u00ed\7]\2\2\u00ed\60\3\2")
        buf.write("\2\2\u00ee\u00ef\7_\2\2\u00ef\62\3\2\2\2\u00f0\u00f1\7")
        buf.write("}\2\2\u00f1\64\3\2\2\2\u00f2\u00f3\7\177\2\2\u00f3\66")
        buf.write("\3\2\2\2\u00f4\u00f5\7.\2\2\u00f58\3\2\2\2\u00f6\u00f7")
        buf.write("\7<\2\2\u00f7:\3\2\2\2\u00f8\u00f9\7=\2\2\u00f9<\3\2\2")
        buf.write("\2\u00fa\u00fb\7?\2\2\u00fb>\3\2\2\2\u00fc\u00fd\7(\2")
        buf.write("\2\u00fd@\3\2\2\2\u00fe\u00ff\7~\2\2\u00ffB\3\2\2\2\u0100")
        buf.write("\u0101\7>\2\2\u0101D\3\2\2\2\u0102\u0103\7>\2\2\u0103")
        buf.write("\u0104\7?\2\2\u0104F\3\2\2\2\u0105\u0106\7@\2\2\u0106")
        buf.write("H\3\2\2\2\u0107\u0108\7@\2\2\u0108\u0109\7?\2\2\u0109")
        buf.write("J\3\2\2\2\u010a\u010b\7?\2\2\u010b\u010c\7?\2\2\u010c")
        buf.write("L\3\2\2\2\u010d\u010e\7#\2\2\u010e\u010f\7?\2\2\u010f")
        buf.write("N\3\2\2\2\u0110\u0111\7-\2\2\u0111P\3\2\2\2\u0112\u0113")
        buf.write("\7/\2\2\u0113R\3\2\2\2\u0114\u0115\7,\2\2\u0115T\3\2\2")
        buf.write("\2\u0116\u0117\7\61\2\2\u0117V\3\2\2\2\u0118\u011c\7$")
        buf.write("\2\2\u0119\u011b\13\2\2\2\u011a\u0119\3\2\2\2\u011b\u011e")
        buf.write("\3\2\2\2\u011c\u011d\3\2\2\2\u011c\u011a\3\2\2\2\u011d")
        buf.write("\u011f\3\2\2\2\u011e\u011c\3\2\2\2\u011f\u0120\7$\2\2")
        buf.write("\u0120X\3\2\2\2\u0121\u0122\7)\2\2\u0122\u0123\13\2\2")
        buf.write("\2\u0123\u0124\7)\2\2\u0124Z\3\2\2\2\u0125\u0127\t\2\2")
        buf.write("\2\u0126\u0125\3\2\2\2\u0127\u0128\3\2\2\2\u0128\u0126")
        buf.write("\3\2\2\2\u0128\u0129\3\2\2\2\u0129\\\3\2\2\2\u012a\u012c")
        buf.write("\t\2\2\2\u012b\u012a\3\2\2\2\u012c\u012d\3\2\2\2\u012d")
        buf.write("\u012b\3\2\2\2\u012d\u012e\3\2\2\2\u012e\u012f\3\2\2\2")
        buf.write("\u012f\u0131\7\60\2\2\u0130\u0132\t\2\2\2\u0131\u0130")
        buf.write("\3\2\2\2\u0132\u0133\3\2\2\2\u0133\u0131\3\2\2\2\u0133")
        buf.write("\u0134\3\2\2\2\u0134^\3\2\2\2\u0135\u0136\7v\2\2\u0136")
        buf.write("\u0137\7t\2\2\u0137\u0138\7w\2\2\u0138\u013f\7g\2\2\u0139")
        buf.write("\u013a\7h\2\2\u013a\u013b\7c\2\2\u013b\u013c\7n\2\2\u013c")
        buf.write("\u013d\7u\2\2\u013d\u013f\7g\2\2\u013e\u0135\3\2\2\2\u013e")
        buf.write("\u0139\3\2\2\2\u013f`\3\2\2\2\u0140\u0144\t\3\2\2\u0141")
        buf.write("\u0143\t\4\2\2\u0142\u0141\3\2\2\2\u0143\u0146\3\2\2\2")
        buf.write("\u0144\u0142\3\2\2\2\u0144\u0145\3\2\2\2\u0145b\3\2\2")
        buf.write("\2\u0146\u0144\3\2\2\2\u0147\u0148\7\61\2\2\u0148\u0149")
        buf.write("\7,\2\2\u0149\u014d\3\2\2\2\u014a\u014c\13\2\2\2\u014b")
        buf.write("\u014a\3\2\2\2\u014c\u014f\3\2\2\2\u014d\u014e\3\2\2\2")
        buf.write("\u014d\u014b\3\2\2\2\u014e\u0150\3\2\2\2\u014f\u014d\3")
        buf.write("\2\2\2\u0150\u0151\7,\2\2\u0151\u0152\7\61\2\2\u0152\u0153")
        buf.write("\3\2\2\2\u0153\u0154\b\62\2\2\u0154d\3\2\2\2\u0155\u0156")
        buf.write("\7\'\2\2\u0156\u0157\7\'\2\2\u0157\u015b\3\2\2\2\u0158")
        buf.write("\u015a\n\5\2\2\u0159\u0158\3\2\2\2\u015a\u015d\3\2\2\2")
        buf.write("\u015b\u0159\3\2\2\2\u015b\u015c\3\2\2\2\u015c\u015e\3")
        buf.write("\2\2\2\u015d\u015b\3\2\2\2\u015e\u015f\b\63\2\2\u015f")
        buf.write("f\3\2\2\2\u0160\u0162\t\6\2\2\u0161\u0160\3\2\2\2\u0162")
        buf.write("\u0163\3\2\2\2\u0163\u0161\3\2\2\2\u0163\u0164\3\2\2\2")
        buf.write("\u0164\u0165\3\2\2\2\u0165\u0166\b\64\2\2\u0166h\3\2\2")
        buf.write("\2\f\2\u011c\u0128\u012d\u0133\u013e\u0144\u014d\u015b")
        buf.write("\u0163\3\b\2\2")
        return buf.getvalue()


class lowLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    PROGRAM = 1
    MAIN = 2
    FUNCTION = 3
    RETURN = 4
    INPUT = 5
    OUTPUT = 6
    IF = 7
    THEN = 8
    ELSE = 9
    WHILE = 10
    DO = 11
    FROM = 12
    TO = 13
    VOID = 14
    VAR = 15
    STRING = 16
    CHAR = 17
    INT = 18
    FLOAT = 19
    BOOL = 20
    LEFT_PARENTHESIS = 21
    RIGHT_PARENTHESIS = 22
    LEFT_BRACKET = 23
    RIGHT_BRACKET = 24
    LEFT_CURLY = 25
    RIGHT_CURLY = 26
    COMMA = 27
    COLON = 28
    SEMICOLON = 29
    ASSIGN = 30
    AND = 31
    OR = 32
    LESS = 33
    LESS_OR_EQUAL = 34
    GREATER = 35
    GREATER_OR_EQUAL = 36
    EQUAL = 37
    NOT_EQUAL = 38
    ADDITION = 39
    SUBTRACTION = 40
    MULTIPLICATION = 41
    DIVISION = 42
    STRING_CONSTANT = 43
    CHAR_CONSTANT = 44
    INT_CONSTANT = 45
    FLOAT_CONSTANT = 46
    BOOL_CONSTANT = 47
    ID = 48
    COMMENT_BLOCK = 49
    COMMENT_LINE = 50
    WHITESPACE = 51

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'programa'", "'principal'", "'funcion'", "'regresa'", "'lee'", 
            "'escribe'", "'si'", "'entonces'", "'sino'", "'mientras'", "'hacer'", 
            "'desde'", "'hasta'", "'void'", "'var'", "'string'", "'char'", 
            "'int'", "'float'", "'bool'", "'('", "')'", "'['", "']'", "'{'", 
            "'}'", "','", "':'", "';'", "'='", "'&'", "'|'", "'<'", "'<='", 
            "'>'", "'>='", "'=='", "'!='", "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>",
            "PROGRAM", "MAIN", "FUNCTION", "RETURN", "INPUT", "OUTPUT", 
            "IF", "THEN", "ELSE", "WHILE", "DO", "FROM", "TO", "VOID", "VAR", 
            "STRING", "CHAR", "INT", "FLOAT", "BOOL", "LEFT_PARENTHESIS", 
            "RIGHT_PARENTHESIS", "LEFT_BRACKET", "RIGHT_BRACKET", "LEFT_CURLY", 
            "RIGHT_CURLY", "COMMA", "COLON", "SEMICOLON", "ASSIGN", "AND", 
            "OR", "LESS", "LESS_OR_EQUAL", "GREATER", "GREATER_OR_EQUAL", 
            "EQUAL", "NOT_EQUAL", "ADDITION", "SUBTRACTION", "MULTIPLICATION", 
            "DIVISION", "STRING_CONSTANT", "CHAR_CONSTANT", "INT_CONSTANT", 
            "FLOAT_CONSTANT", "BOOL_CONSTANT", "ID", "COMMENT_BLOCK", "COMMENT_LINE", 
            "WHITESPACE" ]

    ruleNames = [ "PROGRAM", "MAIN", "FUNCTION", "RETURN", "INPUT", "OUTPUT", 
                  "IF", "THEN", "ELSE", "WHILE", "DO", "FROM", "TO", "VOID", 
                  "VAR", "STRING", "CHAR", "INT", "FLOAT", "BOOL", "LEFT_PARENTHESIS", 
                  "RIGHT_PARENTHESIS", "LEFT_BRACKET", "RIGHT_BRACKET", 
                  "LEFT_CURLY", "RIGHT_CURLY", "COMMA", "COLON", "SEMICOLON", 
                  "ASSIGN", "AND", "OR", "LESS", "LESS_OR_EQUAL", "GREATER", 
                  "GREATER_OR_EQUAL", "EQUAL", "NOT_EQUAL", "ADDITION", 
                  "SUBTRACTION", "MULTIPLICATION", "DIVISION", "STRING_CONSTANT", 
                  "CHAR_CONSTANT", "INT_CONSTANT", "FLOAT_CONSTANT", "BOOL_CONSTANT", 
                  "ID", "COMMENT_BLOCK", "COMMENT_LINE", "WHITESPACE" ]

    grammarFileName = "low.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


