# Generated from grammar/low.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from compiler.compiler import Compiler
compiler = Compiler()



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\66")
        buf.write("\u016c\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3")
        buf.write("\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25")
        buf.write("\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32")
        buf.write("\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%")
        buf.write("\3&\3&\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3(\3)\3)\3)\3")
        buf.write(")\3)\3*\3*\3*\3*\3+\3+\3+\3+\3+\3+\3,\3,\3,\3,\3,\3-\3")
        buf.write("-\7-\u0122\n-\f-\16-\u0125\13-\3-\3-\3.\3.\3/\6/\u012c")
        buf.write("\n/\r/\16/\u012d\3\60\6\60\u0131\n\60\r\60\16\60\u0132")
        buf.write("\3\60\3\60\6\60\u0137\n\60\r\60\16\60\u0138\3\61\3\61")
        buf.write("\3\61\3\61\3\61\3\61\3\61\3\61\3\61\5\61\u0144\n\61\3")
        buf.write("\62\3\62\7\62\u0148\n\62\f\62\16\62\u014b\13\62\3\63\3")
        buf.write("\63\3\63\3\63\7\63\u0151\n\63\f\63\16\63\u0154\13\63\3")
        buf.write("\63\3\63\3\63\3\63\3\63\3\64\3\64\3\64\3\64\7\64\u015f")
        buf.write("\n\64\f\64\16\64\u0162\13\64\3\64\3\64\3\65\6\65\u0167")
        buf.write("\n\65\r\65\16\65\u0168\3\65\3\65\4\u0123\u0152\2\66\3")
        buf.write("\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61")
        buf.write("\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*")
        buf.write("S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66\3\2\b\3\2\60\60")
        buf.write("\3\2\62;\5\2C\\aac|\6\2\62;C\\aac|\4\2\f\f\17\17\5\2\13")
        buf.write("\f\17\17\"\"\2\u0174\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2")
        buf.write("\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2")
        buf.write("\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31")
        buf.write("\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2")
        buf.write("\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3")
        buf.write("\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2")
        buf.write("\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3")
        buf.write("\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G")
        buf.write("\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2")
        buf.write("Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2")
        buf.write("\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2")
        buf.write("\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\3k\3\2\2\2\5t\3\2")
        buf.write("\2\2\7~\3\2\2\2\t\u0086\3\2\2\2\13\u008e\3\2\2\2\r\u0092")
        buf.write("\3\2\2\2\17\u009a\3\2\2\2\21\u009d\3\2\2\2\23\u00a6\3")
        buf.write("\2\2\2\25\u00ab\3\2\2\2\27\u00b0\3\2\2\2\31\u00b9\3\2")
        buf.write("\2\2\33\u00bf\3\2\2\2\35\u00c5\3\2\2\2\37\u00cb\3\2\2")
        buf.write("\2!\u00d0\3\2\2\2#\u00d2\3\2\2\2%\u00d4\3\2\2\2\'\u00d6")
        buf.write("\3\2\2\2)\u00d8\3\2\2\2+\u00da\3\2\2\2-\u00dc\3\2\2\2")
        buf.write("/\u00de\3\2\2\2\61\u00e0\3\2\2\2\63\u00e2\3\2\2\2\65\u00e4")
        buf.write("\3\2\2\2\67\u00e6\3\2\2\29\u00e9\3\2\2\2;\u00ec\3\2\2")
        buf.write("\2=\u00ef\3\2\2\2?\u00f2\3\2\2\2A\u00f4\3\2\2\2C\u00f6")
        buf.write("\3\2\2\2E\u00f8\3\2\2\2G\u00fa\3\2\2\2I\u00fc\3\2\2\2")
        buf.write("K\u00fe\3\2\2\2M\u0100\3\2\2\2O\u0104\3\2\2\2Q\u010b\3")
        buf.write("\2\2\2S\u0110\3\2\2\2U\u0114\3\2\2\2W\u011a\3\2\2\2Y\u011f")
        buf.write("\3\2\2\2[\u0128\3\2\2\2]\u012b\3\2\2\2_\u0130\3\2\2\2")
        buf.write("a\u0143\3\2\2\2c\u0145\3\2\2\2e\u014c\3\2\2\2g\u015a\3")
        buf.write("\2\2\2i\u0166\3\2\2\2kl\7r\2\2lm\7t\2\2mn\7q\2\2no\7i")
        buf.write("\2\2op\7t\2\2pq\7c\2\2qr\7o\2\2rs\7c\2\2s\4\3\2\2\2tu")
        buf.write("\7r\2\2uv\7t\2\2vw\7k\2\2wx\7p\2\2xy\7e\2\2yz\7k\2\2z")
        buf.write("{\7r\2\2{|\7c\2\2|}\7n\2\2}\6\3\2\2\2~\177\7h\2\2\177")
        buf.write("\u0080\7w\2\2\u0080\u0081\7p\2\2\u0081\u0082\7e\2\2\u0082")
        buf.write("\u0083\7k\2\2\u0083\u0084\7q\2\2\u0084\u0085\7p\2\2\u0085")
        buf.write("\b\3\2\2\2\u0086\u0087\7t\2\2\u0087\u0088\7g\2\2\u0088")
        buf.write("\u0089\7i\2\2\u0089\u008a\7t\2\2\u008a\u008b\7g\2\2\u008b")
        buf.write("\u008c\7u\2\2\u008c\u008d\7c\2\2\u008d\n\3\2\2\2\u008e")
        buf.write("\u008f\7n\2\2\u008f\u0090\7g\2\2\u0090\u0091\7g\2\2\u0091")
        buf.write("\f\3\2\2\2\u0092\u0093\7g\2\2\u0093\u0094\7u\2\2\u0094")
        buf.write("\u0095\7e\2\2\u0095\u0096\7t\2\2\u0096\u0097\7k\2\2\u0097")
        buf.write("\u0098\7d\2\2\u0098\u0099\7g\2\2\u0099\16\3\2\2\2\u009a")
        buf.write("\u009b\7u\2\2\u009b\u009c\7k\2\2\u009c\20\3\2\2\2\u009d")
        buf.write("\u009e\7g\2\2\u009e\u009f\7p\2\2\u009f\u00a0\7v\2\2\u00a0")
        buf.write("\u00a1\7q\2\2\u00a1\u00a2\7p\2\2\u00a2\u00a3\7e\2\2\u00a3")
        buf.write("\u00a4\7g\2\2\u00a4\u00a5\7u\2\2\u00a5\22\3\2\2\2\u00a6")
        buf.write("\u00a7\7q\2\2\u00a7\u00a8\7\"\2\2\u00a8\u00a9\7u\2\2\u00a9")
        buf.write("\u00aa\7k\2\2\u00aa\24\3\2\2\2\u00ab\u00ac\7u\2\2\u00ac")
        buf.write("\u00ad\7k\2\2\u00ad\u00ae\7p\2\2\u00ae\u00af\7q\2\2\u00af")
        buf.write("\26\3\2\2\2\u00b0\u00b1\7o\2\2\u00b1\u00b2\7k\2\2\u00b2")
        buf.write("\u00b3\7g\2\2\u00b3\u00b4\7p\2\2\u00b4\u00b5\7v\2\2\u00b5")
        buf.write("\u00b6\7t\2\2\u00b6\u00b7\7c\2\2\u00b7\u00b8\7u\2\2\u00b8")
        buf.write("\30\3\2\2\2\u00b9\u00ba\7j\2\2\u00ba\u00bb\7c\2\2\u00bb")
        buf.write("\u00bc\7e\2\2\u00bc\u00bd\7g\2\2\u00bd\u00be\7t\2\2\u00be")
        buf.write("\32\3\2\2\2\u00bf\u00c0\7f\2\2\u00c0\u00c1\7g\2\2\u00c1")
        buf.write("\u00c2\7u\2\2\u00c2\u00c3\7f\2\2\u00c3\u00c4\7g\2\2\u00c4")
        buf.write("\34\3\2\2\2\u00c5\u00c6\7j\2\2\u00c6\u00c7\7c\2\2\u00c7")
        buf.write("\u00c8\7u\2\2\u00c8\u00c9\7v\2\2\u00c9\u00ca\7c\2\2\u00ca")
        buf.write("\36\3\2\2\2\u00cb\u00cc\7x\2\2\u00cc\u00cd\7q\2\2\u00cd")
        buf.write("\u00ce\7k\2\2\u00ce\u00cf\7f\2\2\u00cf \3\2\2\2\u00d0")
        buf.write("\u00d1\7*\2\2\u00d1\"\3\2\2\2\u00d2\u00d3\7+\2\2\u00d3")
        buf.write("$\3\2\2\2\u00d4\u00d5\7]\2\2\u00d5&\3\2\2\2\u00d6\u00d7")
        buf.write("\7_\2\2\u00d7(\3\2\2\2\u00d8\u00d9\7}\2\2\u00d9*\3\2\2")
        buf.write("\2\u00da\u00db\7\177\2\2\u00db,\3\2\2\2\u00dc\u00dd\7")
        buf.write(".\2\2\u00dd.\3\2\2\2\u00de\u00df\7<\2\2\u00df\60\3\2\2")
        buf.write("\2\u00e0\u00e1\7=\2\2\u00e1\62\3\2\2\2\u00e2\u00e3\7>")
        buf.write("\2\2\u00e3\64\3\2\2\2\u00e4\u00e5\7@\2\2\u00e5\66\3\2")
        buf.write("\2\2\u00e6\u00e7\7>\2\2\u00e7\u00e8\7?\2\2\u00e88\3\2")
        buf.write("\2\2\u00e9\u00ea\7@\2\2\u00ea\u00eb\7?\2\2\u00eb:\3\2")
        buf.write("\2\2\u00ec\u00ed\7?\2\2\u00ed\u00ee\7?\2\2\u00ee<\3\2")
        buf.write("\2\2\u00ef\u00f0\7#\2\2\u00f0\u00f1\7?\2\2\u00f1>\3\2")
        buf.write("\2\2\u00f2\u00f3\7?\2\2\u00f3@\3\2\2\2\u00f4\u00f5\7(")
        buf.write("\2\2\u00f5B\3\2\2\2\u00f6\u00f7\7~\2\2\u00f7D\3\2\2\2")
        buf.write("\u00f8\u00f9\7-\2\2\u00f9F\3\2\2\2\u00fa\u00fb\7/\2\2")
        buf.write("\u00fbH\3\2\2\2\u00fc\u00fd\7,\2\2\u00fdJ\3\2\2\2\u00fe")
        buf.write("\u00ff\7\61\2\2\u00ffL\3\2\2\2\u0100\u0101\7x\2\2\u0101")
        buf.write("\u0102\7c\2\2\u0102\u0103\7t\2\2\u0103N\3\2\2\2\u0104")
        buf.write("\u0105\7u\2\2\u0105\u0106\7v\2\2\u0106\u0107\7t\2\2\u0107")
        buf.write("\u0108\7k\2\2\u0108\u0109\7p\2\2\u0109\u010a\7i\2\2\u010a")
        buf.write("P\3\2\2\2\u010b\u010c\7e\2\2\u010c\u010d\7j\2\2\u010d")
        buf.write("\u010e\7c\2\2\u010e\u010f\7t\2\2\u010fR\3\2\2\2\u0110")
        buf.write("\u0111\7k\2\2\u0111\u0112\7p\2\2\u0112\u0113\7v\2\2\u0113")
        buf.write("T\3\2\2\2\u0114\u0115\7h\2\2\u0115\u0116\7n\2\2\u0116")
        buf.write("\u0117\7q\2\2\u0117\u0118\7c\2\2\u0118\u0119\7v\2\2\u0119")
        buf.write("V\3\2\2\2\u011a\u011b\7d\2\2\u011b\u011c\7q\2\2\u011c")
        buf.write("\u011d\7q\2\2\u011d\u011e\7n\2\2\u011eX\3\2\2\2\u011f")
        buf.write("\u0123\7$\2\2\u0120\u0122\13\2\2\2\u0121\u0120\3\2\2\2")
        buf.write("\u0122\u0125\3\2\2\2\u0123\u0124\3\2\2\2\u0123\u0121\3")
        buf.write("\2\2\2\u0124\u0126\3\2\2\2\u0125\u0123\3\2\2\2\u0126\u0127")
        buf.write("\7$\2\2\u0127Z\3\2\2\2\u0128\u0129\t\2\2\2\u0129\\\3\2")
        buf.write("\2\2\u012a\u012c\t\3\2\2\u012b\u012a\3\2\2\2\u012c\u012d")
        buf.write("\3\2\2\2\u012d\u012b\3\2\2\2\u012d\u012e\3\2\2\2\u012e")
        buf.write("^\3\2\2\2\u012f\u0131\t\3\2\2\u0130\u012f\3\2\2\2\u0131")
        buf.write("\u0132\3\2\2\2\u0132\u0130\3\2\2\2\u0132\u0133\3\2\2\2")
        buf.write("\u0133\u0134\3\2\2\2\u0134\u0136\13\2\2\2\u0135\u0137")
        buf.write("\t\3\2\2\u0136\u0135\3\2\2\2\u0137\u0138\3\2\2\2\u0138")
        buf.write("\u0136\3\2\2\2\u0138\u0139\3\2\2\2\u0139`\3\2\2\2\u013a")
        buf.write("\u013b\7v\2\2\u013b\u013c\7t\2\2\u013c\u013d\7w\2\2\u013d")
        buf.write("\u0144\7g\2\2\u013e\u013f\7h\2\2\u013f\u0140\7c\2\2\u0140")
        buf.write("\u0141\7n\2\2\u0141\u0142\7u\2\2\u0142\u0144\7g\2\2\u0143")
        buf.write("\u013a\3\2\2\2\u0143\u013e\3\2\2\2\u0144b\3\2\2\2\u0145")
        buf.write("\u0149\t\4\2\2\u0146\u0148\t\5\2\2\u0147\u0146\3\2\2\2")
        buf.write("\u0148\u014b\3\2\2\2\u0149\u0147\3\2\2\2\u0149\u014a\3")
        buf.write("\2\2\2\u014ad\3\2\2\2\u014b\u0149\3\2\2\2\u014c\u014d")
        buf.write("\7\61\2\2\u014d\u014e\7,\2\2\u014e\u0152\3\2\2\2\u014f")
        buf.write("\u0151\13\2\2\2\u0150\u014f\3\2\2\2\u0151\u0154\3\2\2")
        buf.write("\2\u0152\u0153\3\2\2\2\u0152\u0150\3\2\2\2\u0153\u0155")
        buf.write("\3\2\2\2\u0154\u0152\3\2\2\2\u0155\u0156\7,\2\2\u0156")
        buf.write("\u0157\7\61\2\2\u0157\u0158\3\2\2\2\u0158\u0159\b\63\2")
        buf.write("\2\u0159f\3\2\2\2\u015a\u015b\7\'\2\2\u015b\u015c\7\'")
        buf.write("\2\2\u015c\u0160\3\2\2\2\u015d\u015f\n\6\2\2\u015e\u015d")
        buf.write("\3\2\2\2\u015f\u0162\3\2\2\2\u0160\u015e\3\2\2\2\u0160")
        buf.write("\u0161\3\2\2\2\u0161\u0163\3\2\2\2\u0162\u0160\3\2\2\2")
        buf.write("\u0163\u0164\b\64\2\2\u0164h\3\2\2\2\u0165\u0167\t\7\2")
        buf.write("\2\u0166\u0165\3\2\2\2\u0167\u0168\3\2\2\2\u0168\u0166")
        buf.write("\3\2\2\2\u0168\u0169\3\2\2\2\u0169\u016a\3\2\2\2\u016a")
        buf.write("\u016b\b\65\2\2\u016bj\3\2\2\2\f\2\u0123\u012d\u0132\u0138")
        buf.write("\u0143\u0149\u0152\u0160\u0168\3\b\2\2")
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
    ELSE_IF = 9
    ELSE = 10
    WHILE = 11
    DO = 12
    FROM = 13
    TO = 14
    VOID = 15
    LEFT_PARENTHESIS = 16
    RIGHT_PARENTHESIS = 17
    LEFT_BRACKET = 18
    RIGHT_BRACKET = 19
    LEFT_CURLY = 20
    RIGHT_CURLY = 21
    COMMA = 22
    COLON = 23
    SEMICOLON = 24
    LESS = 25
    GREATER = 26
    LESS_OR_EQUAL = 27
    GREATER_OR_EQUAL = 28
    EQUAL = 29
    NOT_EQUAL = 30
    ASSIGN = 31
    AND = 32
    OR = 33
    ADDITION = 34
    SUBTRACTION = 35
    MULTIPLICATION = 36
    DIVISION = 37
    VAR = 38
    STRING = 39
    CHAR = 40
    INT = 41
    FLOAT = 42
    BOOL = 43
    STRING_CONSTANT = 44
    CHAR_CONSTANT = 45
    INT_CONSTANT = 46
    FLOAT_CONSTANT = 47
    BOOL_CONSTANT = 48
    VAR_NAME = 49
    COMMENT_BLOCK = 50
    COMMENT_LINE = 51
    WHITESPACE = 52

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'programa'", "'principal'", "'funcion'", "'regresa'", "'lee'", 
            "'escribe'", "'si'", "'entonces'", "'o si'", "'sino'", "'mientras'", 
            "'hacer'", "'desde'", "'hasta'", "'void'", "'('", "')'", "'['", 
            "']'", "'{'", "'}'", "','", "':'", "';'", "'<'", "'>'", "'<='", 
            "'>='", "'=='", "'!='", "'='", "'&'", "'|'", "'+'", "'-'", "'*'", 
            "'/'", "'var'", "'string'", "'char'", "'int'", "'float'", "'bool'" ]

    symbolicNames = [ "<INVALID>",
            "PROGRAM", "MAIN", "FUNCTION", "RETURN", "INPUT", "OUTPUT", 
            "IF", "THEN", "ELSE_IF", "ELSE", "WHILE", "DO", "FROM", "TO", 
            "VOID", "LEFT_PARENTHESIS", "RIGHT_PARENTHESIS", "LEFT_BRACKET", 
            "RIGHT_BRACKET", "LEFT_CURLY", "RIGHT_CURLY", "COMMA", "COLON", 
            "SEMICOLON", "LESS", "GREATER", "LESS_OR_EQUAL", "GREATER_OR_EQUAL", 
            "EQUAL", "NOT_EQUAL", "ASSIGN", "AND", "OR", "ADDITION", "SUBTRACTION", 
            "MULTIPLICATION", "DIVISION", "VAR", "STRING", "CHAR", "INT", 
            "FLOAT", "BOOL", "STRING_CONSTANT", "CHAR_CONSTANT", "INT_CONSTANT", 
            "FLOAT_CONSTANT", "BOOL_CONSTANT", "VAR_NAME", "COMMENT_BLOCK", 
            "COMMENT_LINE", "WHITESPACE" ]

    ruleNames = [ "PROGRAM", "MAIN", "FUNCTION", "RETURN", "INPUT", "OUTPUT", 
                  "IF", "THEN", "ELSE_IF", "ELSE", "WHILE", "DO", "FROM", 
                  "TO", "VOID", "LEFT_PARENTHESIS", "RIGHT_PARENTHESIS", 
                  "LEFT_BRACKET", "RIGHT_BRACKET", "LEFT_CURLY", "RIGHT_CURLY", 
                  "COMMA", "COLON", "SEMICOLON", "LESS", "GREATER", "LESS_OR_EQUAL", 
                  "GREATER_OR_EQUAL", "EQUAL", "NOT_EQUAL", "ASSIGN", "AND", 
                  "OR", "ADDITION", "SUBTRACTION", "MULTIPLICATION", "DIVISION", 
                  "VAR", "STRING", "CHAR", "INT", "FLOAT", "BOOL", "STRING_CONSTANT", 
                  "CHAR_CONSTANT", "INT_CONSTANT", "FLOAT_CONSTANT", "BOOL_CONSTANT", 
                  "VAR_NAME", "COMMENT_BLOCK", "COMMENT_LINE", "WHITESPACE" ]

    grammarFileName = "low.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


