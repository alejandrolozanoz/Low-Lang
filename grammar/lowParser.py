# Generated from grammar/low.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


from compiler.compiler import Compiler
compiler = Compiler()


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\66")
        buf.write("\u015e\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\3\3\3\6\3@\n\3\r\3\16\3A\3\4\3\4\3\4\3\4\7\4H\n\4\f")
        buf.write("\4\16\4K\13\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\5\5Y\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\5\6e\n\6\3\7\3\7\3\7\3\7\5\7k\n\7\3\b\7\bn\n\b\f")
        buf.write("\b\16\bq\13\b\3\t\3\t\3\t\5\tv\n\t\3\t\3\t\3\t\5\t{\n")
        buf.write("\t\3\t\3\t\5\t\177\n\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\7\n\u008b\n\n\f\n\16\n\u008e\13\n\3\13\3\13\3")
        buf.write("\13\3\13\3\13\5\13\u0095\n\13\3\13\7\13\u0098\n\13\f\13")
        buf.write("\16\13\u009b\13\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u00ad\n\f\3\f\5\f\u00b0")
        buf.write("\n\f\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00b8\n\r\3\r\7\r\u00bb")
        buf.write("\n\r\f\r\16\r\u00be\13\r\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\5\16\u00c6\n\16\3\16\7\16\u00c9\n\16\f\16\16\16\u00cc")
        buf.write("\13\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\5")
        buf.write("\17\u00d7\n\17\3\20\3\20\3\20\3\20\3\20\5\20\u00de\n\20")
        buf.write("\3\21\3\21\3\21\3\21\3\21\7\21\u00e5\n\21\f\21\16\21\u00e8")
        buf.write("\13\21\5\21\u00ea\n\21\3\21\3\21\3\22\3\22\3\22\3\22\3")
        buf.write("\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\7\23\u00fd\n\23\f\23\16\23\u0100\13\23\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\25\3\25\7\25\u010c\n\25\f")
        buf.write("\25\16\25\u010f\13\25\3\25\3\25\3\25\3\26\3\26\3\26\3")
        buf.write("\26\5\26\u0118\n\26\3\26\3\26\3\26\5\26\u011d\n\26\7\26")
        buf.write("\u011f\n\26\f\26\16\26\u0122\13\26\3\26\3\26\3\26\3\27")
        buf.write("\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\5\31\u0141\n\31\3\31\3\31\3\31\3\31\3")
        buf.write("\31\5\31\u0148\n\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\2\2\34\2\4\6\b\n\f\16\20\22\24\26\30\32")
        buf.write("\34\36 \"$&(*,.\60\62\64\2\2\2\u0174\2\66\3\2\2\2\4=\3")
        buf.write("\2\2\2\6C\3\2\2\2\bX\3\2\2\2\nd\3\2\2\2\ff\3\2\2\2\16")
        buf.write("o\3\2\2\2\20r\3\2\2\2\22\u0084\3\2\2\2\24\u008f\3\2\2")
        buf.write("\2\26\u009c\3\2\2\2\30\u00b1\3\2\2\2\32\u00bf\3\2\2\2")
        buf.write("\34\u00d6\3\2\2\2\36\u00d8\3\2\2\2 \u00df\3\2\2\2\"\u00ed")
        buf.write("\3\2\2\2$\u00fe\3\2\2\2&\u0101\3\2\2\2(\u0106\3\2\2\2")
        buf.write("*\u0113\3\2\2\2,\u0126\3\2\2\2.\u0129\3\2\2\2\60\u012f")
        buf.write("\3\2\2\2\62\u0149\3\2\2\2\64\u0152\3\2\2\2\66\67\7\3\2")
        buf.write("\2\678\7\63\2\289\7 \2\29:\5\4\3\2:;\5\16\b\2;<\5\"\22")
        buf.write("\2<\3\3\2\2\2=?\7\22\2\2>@\5\6\4\2?>\3\2\2\2@A\3\2\2\2")
        buf.write("A?\3\2\2\2AB\3\2\2\2B\5\3\2\2\2CD\5\b\5\2DI\5\f\7\2EF")
        buf.write("\7\36\2\2FH\5\f\7\2GE\3\2\2\2HK\3\2\2\2IG\3\2\2\2IJ\3")
        buf.write("\2\2\2JL\3\2\2\2KI\3\2\2\2LM\7 \2\2M\7\3\2\2\2NO\7\25")
        buf.write("\2\2OY\b\5\1\2PQ\7\27\2\2QY\b\5\1\2RS\7\26\2\2SY\b\5\1")
        buf.write("\2TU\7\23\2\2UY\b\5\1\2VW\7\24\2\2WY\b\5\1\2XN\3\2\2\2")
        buf.write("XP\3\2\2\2XR\3\2\2\2XT\3\2\2\2XV\3\2\2\2Y\t\3\2\2\2Z[")
        buf.write("\7\62\2\2[e\b\6\1\2\\]\7\61\2\2]e\b\6\1\2^_\7\60\2\2_")
        buf.write("e\b\6\1\2`a\7/\2\2ae\b\6\1\2bc\7.\2\2ce\b\6\1\2dZ\3\2")
        buf.write("\2\2d\\\3\2\2\2d^\3\2\2\2d`\3\2\2\2db\3\2\2\2e\13\3\2")
        buf.write("\2\2fj\7\63\2\2gh\7\32\2\2hi\7\60\2\2ik\7\33\2\2jg\3\2")
        buf.write("\2\2jk\3\2\2\2k\r\3\2\2\2ln\5\20\t\2ml\3\2\2\2nq\3\2\2")
        buf.write("\2om\3\2\2\2op\3\2\2\2p\17\3\2\2\2qo\3\2\2\2ru\7\5\2\2")
        buf.write("sv\5\b\5\2tv\7\21\2\2us\3\2\2\2ut\3\2\2\2vw\3\2\2\2wx")
        buf.write("\7\63\2\2xz\7\30\2\2y{\5\22\n\2zy\3\2\2\2z{\3\2\2\2{|")
        buf.write("\3\2\2\2|~\7\31\2\2}\177\5\4\3\2~}\3\2\2\2~\177\3\2\2")
        buf.write("\2\177\u0080\3\2\2\2\u0080\u0081\7\34\2\2\u0081\u0082")
        buf.write("\5$\23\2\u0082\u0083\7\35\2\2\u0083\21\3\2\2\2\u0084\u0085")
        buf.write("\5\b\5\2\u0085\u008c\7\63\2\2\u0086\u0087\7\36\2\2\u0087")
        buf.write("\u0088\5\b\5\2\u0088\u0089\7\63\2\2\u0089\u008b\3\2\2")
        buf.write("\2\u008a\u0086\3\2\2\2\u008b\u008e\3\2\2\2\u008c\u008a")
        buf.write("\3\2\2\2\u008c\u008d\3\2\2\2\u008d\23\3\2\2\2\u008e\u008c")
        buf.write("\3\2\2\2\u008f\u0099\5\26\f\2\u0090\u0091\7\"\2\2\u0091")
        buf.write("\u0095\b\13\1\2\u0092\u0093\7#\2\2\u0093\u0095\b\13\1")
        buf.write("\2\u0094\u0090\3\2\2\2\u0094\u0092\3\2\2\2\u0095\u0096")
        buf.write("\3\2\2\2\u0096\u0098\5\26\f\2\u0097\u0094\3\2\2\2\u0098")
        buf.write("\u009b\3\2\2\2\u0099\u0097\3\2\2\2\u0099\u009a\3\2\2\2")
        buf.write("\u009a\25\3\2\2\2\u009b\u0099\3\2\2\2\u009c\u009d\5\30")
        buf.write("\r\2\u009d\u00af\b\f\1\2\u009e\u009f\7&\2\2\u009f\u00ad")
        buf.write("\b\f\1\2\u00a0\u00a1\7$\2\2\u00a1\u00ad\b\f\1\2\u00a2")
        buf.write("\u00a3\7%\2\2\u00a3\u00ad\b\f\1\2\u00a4\u00a5\7&\2\2\u00a5")
        buf.write("\u00ad\b\f\1\2\u00a6\u00a7\7\'\2\2\u00a7\u00ad\b\f\1\2")
        buf.write("\u00a8\u00a9\7)\2\2\u00a9\u00ad\b\f\1\2\u00aa\u00ab\7")
        buf.write("(\2\2\u00ab\u00ad\b\f\1\2\u00ac\u009e\3\2\2\2\u00ac\u00a0")
        buf.write("\3\2\2\2\u00ac\u00a2\3\2\2\2\u00ac\u00a4\3\2\2\2\u00ac")
        buf.write("\u00a6\3\2\2\2\u00ac\u00a8\3\2\2\2\u00ac\u00aa\3\2\2\2")
        buf.write("\u00ad\u00ae\3\2\2\2\u00ae\u00b0\5\30\r\2\u00af\u00ac")
        buf.write("\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0\27\3\2\2\2\u00b1\u00b2")
        buf.write("\5\32\16\2\u00b2\u00bc\b\r\1\2\u00b3\u00b4\7*\2\2\u00b4")
        buf.write("\u00b8\b\r\1\2\u00b5\u00b6\7+\2\2\u00b6\u00b8\b\r\1\2")
        buf.write("\u00b7\u00b3\3\2\2\2\u00b7\u00b5\3\2\2\2\u00b8\u00b9\3")
        buf.write("\2\2\2\u00b9\u00bb\5\32\16\2\u00ba\u00b7\3\2\2\2\u00bb")
        buf.write("\u00be\3\2\2\2\u00bc\u00ba\3\2\2\2\u00bc\u00bd\3\2\2\2")
        buf.write("\u00bd\31\3\2\2\2\u00be\u00bc\3\2\2\2\u00bf\u00c0\5\34")
        buf.write("\17\2\u00c0\u00ca\b\16\1\2\u00c1\u00c2\7,\2\2\u00c2\u00c6")
        buf.write("\b\16\1\2\u00c3\u00c4\7-\2\2\u00c4\u00c6\b\16\1\2\u00c5")
        buf.write("\u00c1\3\2\2\2\u00c5\u00c3\3\2\2\2\u00c6\u00c7\3\2\2\2")
        buf.write("\u00c7\u00c9\5\34\17\2\u00c8\u00c5\3\2\2\2\u00c9\u00cc")
        buf.write("\3\2\2\2\u00ca\u00c8\3\2\2\2\u00ca\u00cb\3\2\2\2\u00cb")
        buf.write("\33\3\2\2\2\u00cc\u00ca\3\2\2\2\u00cd\u00d7\5\n\6\2\u00ce")
        buf.write("\u00d7\5\36\20\2\u00cf\u00d0\7\30\2\2\u00d0\u00d1\b\17")
        buf.write("\1\2\u00d1\u00d2\5\24\13\2\u00d2\u00d3\7\31\2\2\u00d3")
        buf.write("\u00d4\b\17\1\2\u00d4\u00d7\3\2\2\2\u00d5\u00d7\5 \21")
        buf.write("\2\u00d6\u00cd\3\2\2\2\u00d6\u00ce\3\2\2\2\u00d6\u00cf")
        buf.write("\3\2\2\2\u00d6\u00d5\3\2\2\2\u00d7\35\3\2\2\2\u00d8\u00dd")
        buf.write("\7\63\2\2\u00d9\u00da\7\32\2\2\u00da\u00db\5\24\13\2\u00db")
        buf.write("\u00dc\7\33\2\2\u00dc\u00de\3\2\2\2\u00dd\u00d9\3\2\2")
        buf.write("\2\u00dd\u00de\3\2\2\2\u00de\37\3\2\2\2\u00df\u00e0\7")
        buf.write("\63\2\2\u00e0\u00e9\7\30\2\2\u00e1\u00e6\5\24\13\2\u00e2")
        buf.write("\u00e3\7\36\2\2\u00e3\u00e5\5\24\13\2\u00e4\u00e2\3\2")
        buf.write("\2\2\u00e5\u00e8\3\2\2\2\u00e6\u00e4\3\2\2\2\u00e6\u00e7")
        buf.write("\3\2\2\2\u00e7\u00ea\3\2\2\2\u00e8\u00e6\3\2\2\2\u00e9")
        buf.write("\u00e1\3\2\2\2\u00e9\u00ea\3\2\2\2\u00ea\u00eb\3\2\2\2")
        buf.write("\u00eb\u00ec\7\31\2\2\u00ec!\3\2\2\2\u00ed\u00ee\7\4\2")
        buf.write("\2\u00ee\u00ef\7\30\2\2\u00ef\u00f0\7\31\2\2\u00f0\u00f1")
        buf.write("\7\34\2\2\u00f1\u00f2\5$\23\2\u00f2\u00f3\7\35\2\2\u00f3")
        buf.write("#\3\2\2\2\u00f4\u00fd\5&\24\2\u00f5\u00fd\5(\25\2\u00f6")
        buf.write("\u00fd\5*\26\2\u00f7\u00fd\5,\27\2\u00f8\u00fd\5.\30\2")
        buf.write("\u00f9\u00fd\5\60\31\2\u00fa\u00fd\5\62\32\2\u00fb\u00fd")
        buf.write("\5\64\33\2\u00fc\u00f4\3\2\2\2\u00fc\u00f5\3\2\2\2\u00fc")
        buf.write("\u00f6\3\2\2\2\u00fc\u00f7\3\2\2\2\u00fc\u00f8\3\2\2\2")
        buf.write("\u00fc\u00f9\3\2\2\2\u00fc\u00fa\3\2\2\2\u00fc\u00fb\3")
        buf.write("\2\2\2\u00fd\u0100\3\2\2\2\u00fe\u00fc\3\2\2\2\u00fe\u00ff")
        buf.write("\3\2\2\2\u00ff%\3\2\2\2\u0100\u00fe\3\2\2\2\u0101\u0102")
        buf.write("\5\36\20\2\u0102\u0103\7!\2\2\u0103\u0104\5\24\13\2\u0104")
        buf.write("\u0105\7 \2\2\u0105\'\3\2\2\2\u0106\u0107\7\7\2\2\u0107")
        buf.write("\u0108\7\30\2\2\u0108\u010d\5\36\20\2\u0109\u010a\7\36")
        buf.write("\2\2\u010a\u010c\5\36\20\2\u010b\u0109\3\2\2\2\u010c\u010f")
        buf.write("\3\2\2\2\u010d\u010b\3\2\2\2\u010d\u010e\3\2\2\2\u010e")
        buf.write("\u0110\3\2\2\2\u010f\u010d\3\2\2\2\u0110\u0111\7\31\2")
        buf.write("\2\u0111\u0112\7 \2\2\u0112)\3\2\2\2\u0113\u0114\7\b\2")
        buf.write("\2\u0114\u0117\7\30\2\2\u0115\u0118\5\24\13\2\u0116\u0118")
        buf.write("\7.\2\2\u0117\u0115\3\2\2\2\u0117\u0116\3\2\2\2\u0118")
        buf.write("\u0120\3\2\2\2\u0119\u011c\7\36\2\2\u011a\u011d\5\24\13")
        buf.write("\2\u011b\u011d\7.\2\2\u011c\u011a\3\2\2\2\u011c\u011b")
        buf.write("\3\2\2\2\u011d\u011f\3\2\2\2\u011e\u0119\3\2\2\2\u011f")
        buf.write("\u0122\3\2\2\2\u0120\u011e\3\2\2\2\u0120\u0121\3\2\2\2")
        buf.write("\u0121\u0123\3\2\2\2\u0122\u0120\3\2\2\2\u0123\u0124\7")
        buf.write("\31\2\2\u0124\u0125\7 \2\2\u0125+\3\2\2\2\u0126\u0127")
        buf.write("\5 \21\2\u0127\u0128\7 \2\2\u0128-\3\2\2\2\u0129\u012a")
        buf.write("\7\6\2\2\u012a\u012b\7\30\2\2\u012b\u012c\5\24\13\2\u012c")
        buf.write("\u012d\7\31\2\2\u012d\u012e\7 \2\2\u012e/\3\2\2\2\u012f")
        buf.write("\u0130\7\t\2\2\u0130\u0131\7\30\2\2\u0131\u0132\5\24\13")
        buf.write("\2\u0132\u0133\7\31\2\2\u0133\u0134\7\n\2\2\u0134\u0135")
        buf.write("\7\34\2\2\u0135\u0136\5$\23\2\u0136\u0140\7\35\2\2\u0137")
        buf.write("\u0138\7\13\2\2\u0138\u0139\7\30\2\2\u0139\u013a\5\24")
        buf.write("\13\2\u013a\u013b\7\31\2\2\u013b\u013c\7\n\2\2\u013c\u013d")
        buf.write("\7\34\2\2\u013d\u013e\5$\23\2\u013e\u013f\7\35\2\2\u013f")
        buf.write("\u0141\3\2\2\2\u0140\u0137\3\2\2\2\u0140\u0141\3\2\2\2")
        buf.write("\u0141\u0147\3\2\2\2\u0142\u0143\7\f\2\2\u0143\u0144\7")
        buf.write("\34\2\2\u0144\u0145\5$\23\2\u0145\u0146\7\35\2\2\u0146")
        buf.write("\u0148\3\2\2\2\u0147\u0142\3\2\2\2\u0147\u0148\3\2\2\2")
        buf.write("\u0148\61\3\2\2\2\u0149\u014a\7\r\2\2\u014a\u014b\7\30")
        buf.write("\2\2\u014b\u014c\5\24\13\2\u014c\u014d\7\31\2\2\u014d")
        buf.write("\u014e\7\16\2\2\u014e\u014f\7\34\2\2\u014f\u0150\5$\23")
        buf.write("\2\u0150\u0151\7\35\2\2\u0151\63\3\2\2\2\u0152\u0153\7")
        buf.write("\17\2\2\u0153\u0154\5\36\20\2\u0154\u0155\7!\2\2\u0155")
        buf.write("\u0156\5\24\13\2\u0156\u0157\7\20\2\2\u0157\u0158\5\24")
        buf.write("\13\2\u0158\u0159\7\16\2\2\u0159\u015a\7\34\2\2\u015a")
        buf.write("\u015b\5$\23\2\u015b\u015c\7\35\2\2\u015c\65\3\2\2\2 ")
        buf.write("AIXdjouz~\u008c\u0094\u0099\u00ac\u00af\u00b7\u00bc\u00c5")
        buf.write("\u00ca\u00d6\u00dd\u00e6\u00e9\u00fc\u00fe\u010d\u0117")
        buf.write("\u011c\u0120\u0140\u0147")
        return buf.getvalue()


class lowParser ( Parser ):

    grammarFileName = "low.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'programa'", "'principal'", "'funcion'", 
                     "'regresa'", "'lee'", "'escribe'", "'si'", "'entonces'", 
                     "'o si'", "'sino'", "'mientras'", "'hacer'", "'desde'", 
                     "'hasta'", "'void'", "'var'", "'string'", "'char'", 
                     "'int'", "'float'", "'bool'", "'('", "')'", "'['", 
                     "']'", "'{'", "'}'", "','", "':'", "';'", "'='", "'&'", 
                     "'|'", "'<'", "'<='", "'>'", "'>='", "'=='", "'!='", 
                     "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>", "PROGRAM", "MAIN", "FUNCTION", "RETURN", 
                      "INPUT", "OUTPUT", "IF", "THEN", "ELSE_IF", "ELSE", 
                      "WHILE", "DO", "FROM", "TO", "VOID", "VAR", "STRING", 
                      "CHAR", "INT", "FLOAT", "BOOL", "LEFT_PARENTHESIS", 
                      "RIGHT_PARENTHESIS", "LEFT_BRACKET", "RIGHT_BRACKET", 
                      "LEFT_CURLY", "RIGHT_CURLY", "COMMA", "COLON", "SEMICOLON", 
                      "ASSIGN", "AND", "OR", "LESS", "LESS_OR_EQUAL", "GREATER", 
                      "GREATER_OR_EQUAL", "EQUAL", "NOT_EQUAL", "ADDITION", 
                      "SUBTRACTION", "MULTIPLICATION", "DIVISION", "STRING_CONSTANT", 
                      "CHAR_CONSTANT", "INT_CONSTANT", "FLOAT_CONSTANT", 
                      "BOOL_CONSTANT", "ID", "COMMENT_BLOCK", "COMMENT_LINE", 
                      "WHITESPACE" ]

    RULE_program = 0
    RULE_variable_declaration = 1
    RULE_variables = 2
    RULE_data_type = 3
    RULE_constant = 4
    RULE_initialized_variable = 5
    RULE_functions = 6
    RULE_function = 7
    RULE_parameters = 8
    RULE_logic_expresions = 9
    RULE_relational_expresions = 10
    RULE_addition_substraction_expresions = 11
    RULE_multiplication_division_expresions = 12
    RULE_expresion = 13
    RULE_variable = 14
    RULE_function_call = 15
    RULE_main_function = 16
    RULE_statutes = 17
    RULE_assignation = 18
    RULE_read_function_call = 19
    RULE_write_function_call = 20
    RULE_void_function_call = 21
    RULE_return_statement = 22
    RULE_conditional_function = 23
    RULE_while_function = 24
    RULE_from_function = 25

    ruleNames =  [ "program", "variable_declaration", "variables", "data_type", 
                   "constant", "initialized_variable", "functions", "function", 
                   "parameters", "logic_expresions", "relational_expresions", 
                   "addition_substraction_expresions", "multiplication_division_expresions", 
                   "expresion", "variable", "function_call", "main_function", 
                   "statutes", "assignation", "read_function_call", "write_function_call", 
                   "void_function_call", "return_statement", "conditional_function", 
                   "while_function", "from_function" ]

    EOF = Token.EOF
    PROGRAM=1
    MAIN=2
    FUNCTION=3
    RETURN=4
    INPUT=5
    OUTPUT=6
    IF=7
    THEN=8
    ELSE_IF=9
    ELSE=10
    WHILE=11
    DO=12
    FROM=13
    TO=14
    VOID=15
    VAR=16
    STRING=17
    CHAR=18
    INT=19
    FLOAT=20
    BOOL=21
    LEFT_PARENTHESIS=22
    RIGHT_PARENTHESIS=23
    LEFT_BRACKET=24
    RIGHT_BRACKET=25
    LEFT_CURLY=26
    RIGHT_CURLY=27
    COMMA=28
    COLON=29
    SEMICOLON=30
    ASSIGN=31
    AND=32
    OR=33
    LESS=34
    LESS_OR_EQUAL=35
    GREATER=36
    GREATER_OR_EQUAL=37
    EQUAL=38
    NOT_EQUAL=39
    ADDITION=40
    SUBTRACTION=41
    MULTIPLICATION=42
    DIVISION=43
    STRING_CONSTANT=44
    CHAR_CONSTANT=45
    INT_CONSTANT=46
    FLOAT_CONSTANT=47
    BOOL_CONSTANT=48
    ID=49
    COMMENT_BLOCK=50
    COMMENT_LINE=51
    WHITESPACE=52

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROGRAM(self):
            return self.getToken(lowParser.PROGRAM, 0)

        def ID(self):
            return self.getToken(lowParser.ID, 0)

        def SEMICOLON(self):
            return self.getToken(lowParser.SEMICOLON, 0)

        def variable_declaration(self):
            return self.getTypedRuleContext(lowParser.Variable_declarationContext,0)


        def functions(self):
            return self.getTypedRuleContext(lowParser.FunctionsContext,0)


        def main_function(self):
            return self.getTypedRuleContext(lowParser.Main_functionContext,0)


        def getRuleIndex(self):
            return lowParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = lowParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(lowParser.PROGRAM)
            self.state = 53
            self.match(lowParser.ID)
            self.state = 54
            self.match(lowParser.SEMICOLON)
            self.state = 55
            self.variable_declaration()
            self.state = 56
            self.functions()
            self.state = 57
            self.main_function()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(lowParser.VAR, 0)

        def variables(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lowParser.VariablesContext)
            else:
                return self.getTypedRuleContext(lowParser.VariablesContext,i)


        def getRuleIndex(self):
            return lowParser.RULE_variable_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable_declaration" ):
                listener.enterVariable_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable_declaration" ):
                listener.exitVariable_declaration(self)




    def variable_declaration(self):

        localctx = lowParser.Variable_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_variable_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(lowParser.VAR)
            self.state = 61 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 60
                self.variables()
                self.state = 63 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << lowParser.STRING) | (1 << lowParser.CHAR) | (1 << lowParser.INT) | (1 << lowParser.FLOAT) | (1 << lowParser.BOOL))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariablesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def data_type(self):
            return self.getTypedRuleContext(lowParser.Data_typeContext,0)


        def initialized_variable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lowParser.Initialized_variableContext)
            else:
                return self.getTypedRuleContext(lowParser.Initialized_variableContext,i)


        def SEMICOLON(self):
            return self.getToken(lowParser.SEMICOLON, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(lowParser.COMMA)
            else:
                return self.getToken(lowParser.COMMA, i)

        def getRuleIndex(self):
            return lowParser.RULE_variables

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariables" ):
                listener.enterVariables(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariables" ):
                listener.exitVariables(self)




    def variables(self):

        localctx = lowParser.VariablesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_variables)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.data_type()
            self.state = 66
            self.initialized_variable()
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==lowParser.COMMA:
                self.state = 67
                self.match(lowParser.COMMA)
                self.state = 68
                self.initialized_variable()
                self.state = 73
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 74
            self.match(lowParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Data_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._INT = None # Token
            self._BOOL = None # Token
            self._FLOAT = None # Token
            self._STRING = None # Token
            self._CHAR = None # Token

        def INT(self):
            return self.getToken(lowParser.INT, 0)

        def BOOL(self):
            return self.getToken(lowParser.BOOL, 0)

        def FLOAT(self):
            return self.getToken(lowParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(lowParser.STRING, 0)

        def CHAR(self):
            return self.getToken(lowParser.CHAR, 0)

        def getRuleIndex(self):
            return lowParser.RULE_data_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterData_type" ):
                listener.enterData_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitData_type" ):
                listener.exitData_type(self)




    def data_type(self):

        localctx = lowParser.Data_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_data_type)
        try:
            self.state = 86
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [lowParser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 76
                localctx._INT = self.match(lowParser.INT)
                compiler.add_type((None if localctx._INT is None else localctx._INT.text))
                pass
            elif token in [lowParser.BOOL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 78
                localctx._BOOL = self.match(lowParser.BOOL)
                compiler.add_type((None if localctx._BOOL is None else localctx._BOOL.text))
                pass
            elif token in [lowParser.FLOAT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 80
                localctx._FLOAT = self.match(lowParser.FLOAT)
                compiler.add_type((None if localctx._FLOAT is None else localctx._FLOAT.text))
                pass
            elif token in [lowParser.STRING]:
                self.enterOuterAlt(localctx, 4)
                self.state = 82
                localctx._STRING = self.match(lowParser.STRING)
                compiler.add_type((None if localctx._STRING is None else localctx._STRING.text))
                pass
            elif token in [lowParser.CHAR]:
                self.enterOuterAlt(localctx, 5)
                self.state = 84
                localctx._CHAR = self.match(lowParser.CHAR)
                compiler.add_type((None if localctx._CHAR is None else localctx._CHAR.text))
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstantContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._BOOL_CONSTANT = None # Token
            self._FLOAT_CONSTANT = None # Token
            self._INT_CONSTANT = None # Token
            self._CHAR_CONSTANT = None # Token
            self._STRING_CONSTANT = None # Token

        def BOOL_CONSTANT(self):
            return self.getToken(lowParser.BOOL_CONSTANT, 0)

        def FLOAT_CONSTANT(self):
            return self.getToken(lowParser.FLOAT_CONSTANT, 0)

        def INT_CONSTANT(self):
            return self.getToken(lowParser.INT_CONSTANT, 0)

        def CHAR_CONSTANT(self):
            return self.getToken(lowParser.CHAR_CONSTANT, 0)

        def STRING_CONSTANT(self):
            return self.getToken(lowParser.STRING_CONSTANT, 0)

        def getRuleIndex(self):
            return lowParser.RULE_constant

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstant" ):
                listener.enterConstant(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstant" ):
                listener.exitConstant(self)




    def constant(self):

        localctx = lowParser.ConstantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_constant)
        try:
            self.state = 98
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [lowParser.BOOL_CONSTANT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 88
                localctx._BOOL_CONSTANT = self.match(lowParser.BOOL_CONSTANT)
                compiler.add_operand((None if localctx._BOOL_CONSTANT is None else localctx._BOOL_CONSTANT.text))
                pass
            elif token in [lowParser.FLOAT_CONSTANT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 90
                localctx._FLOAT_CONSTANT = self.match(lowParser.FLOAT_CONSTANT)
                compiler.add_operand((None if localctx._FLOAT_CONSTANT is None else localctx._FLOAT_CONSTANT.text))
                pass
            elif token in [lowParser.INT_CONSTANT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 92
                localctx._INT_CONSTANT = self.match(lowParser.INT_CONSTANT)
                compiler.add_operand((None if localctx._INT_CONSTANT is None else localctx._INT_CONSTANT.text))
                pass
            elif token in [lowParser.CHAR_CONSTANT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 94
                localctx._CHAR_CONSTANT = self.match(lowParser.CHAR_CONSTANT)
                compiler.add_operand((None if localctx._CHAR_CONSTANT is None else localctx._CHAR_CONSTANT.text))
                pass
            elif token in [lowParser.STRING_CONSTANT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 96
                localctx._STRING_CONSTANT = self.match(lowParser.STRING_CONSTANT)
                compiler.add_operand((None if localctx._STRING_CONSTANT is None else localctx._STRING_CONSTANT.text))
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Initialized_variableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(lowParser.ID, 0)

        def LEFT_BRACKET(self):
            return self.getToken(lowParser.LEFT_BRACKET, 0)

        def INT_CONSTANT(self):
            return self.getToken(lowParser.INT_CONSTANT, 0)

        def RIGHT_BRACKET(self):
            return self.getToken(lowParser.RIGHT_BRACKET, 0)

        def getRuleIndex(self):
            return lowParser.RULE_initialized_variable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInitialized_variable" ):
                listener.enterInitialized_variable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInitialized_variable" ):
                listener.exitInitialized_variable(self)




    def initialized_variable(self):

        localctx = lowParser.Initialized_variableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_initialized_variable)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(lowParser.ID)
            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==lowParser.LEFT_BRACKET:
                self.state = 101
                self.match(lowParser.LEFT_BRACKET)
                self.state = 102
                self.match(lowParser.INT_CONSTANT)
                self.state = 103
                self.match(lowParser.RIGHT_BRACKET)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lowParser.FunctionContext)
            else:
                return self.getTypedRuleContext(lowParser.FunctionContext,i)


        def getRuleIndex(self):
            return lowParser.RULE_functions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctions" ):
                listener.enterFunctions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctions" ):
                listener.exitFunctions(self)




    def functions(self):

        localctx = lowParser.FunctionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_functions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==lowParser.FUNCTION:
                self.state = 106
                self.function()
                self.state = 111
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(lowParser.FUNCTION, 0)

        def ID(self):
            return self.getToken(lowParser.ID, 0)

        def LEFT_PARENTHESIS(self):
            return self.getToken(lowParser.LEFT_PARENTHESIS, 0)

        def RIGHT_PARENTHESIS(self):
            return self.getToken(lowParser.RIGHT_PARENTHESIS, 0)

        def LEFT_CURLY(self):
            return self.getToken(lowParser.LEFT_CURLY, 0)

        def statutes(self):
            return self.getTypedRuleContext(lowParser.StatutesContext,0)


        def RIGHT_CURLY(self):
            return self.getToken(lowParser.RIGHT_CURLY, 0)

        def data_type(self):
            return self.getTypedRuleContext(lowParser.Data_typeContext,0)


        def VOID(self):
            return self.getToken(lowParser.VOID, 0)

        def parameters(self):
            return self.getTypedRuleContext(lowParser.ParametersContext,0)


        def variable_declaration(self):
            return self.getTypedRuleContext(lowParser.Variable_declarationContext,0)


        def getRuleIndex(self):
            return lowParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)




    def function(self):

        localctx = lowParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(lowParser.FUNCTION)
            self.state = 115
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [lowParser.STRING, lowParser.CHAR, lowParser.INT, lowParser.FLOAT, lowParser.BOOL]:
                self.state = 113
                self.data_type()
                pass
            elif token in [lowParser.VOID]:
                self.state = 114
                self.match(lowParser.VOID)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 117
            self.match(lowParser.ID)
            self.state = 118
            self.match(lowParser.LEFT_PARENTHESIS)
            self.state = 120
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << lowParser.STRING) | (1 << lowParser.CHAR) | (1 << lowParser.INT) | (1 << lowParser.FLOAT) | (1 << lowParser.BOOL))) != 0):
                self.state = 119
                self.parameters()


            self.state = 122
            self.match(lowParser.RIGHT_PARENTHESIS)
            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==lowParser.VAR:
                self.state = 123
                self.variable_declaration()


            self.state = 126
            self.match(lowParser.LEFT_CURLY)
            self.state = 127
            self.statutes()
            self.state = 128
            self.match(lowParser.RIGHT_CURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametersContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def data_type(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lowParser.Data_typeContext)
            else:
                return self.getTypedRuleContext(lowParser.Data_typeContext,i)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(lowParser.ID)
            else:
                return self.getToken(lowParser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(lowParser.COMMA)
            else:
                return self.getToken(lowParser.COMMA, i)

        def getRuleIndex(self):
            return lowParser.RULE_parameters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameters" ):
                listener.enterParameters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameters" ):
                listener.exitParameters(self)




    def parameters(self):

        localctx = lowParser.ParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.data_type()
            self.state = 131
            self.match(lowParser.ID)
            self.state = 138
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==lowParser.COMMA:
                self.state = 132
                self.match(lowParser.COMMA)
                self.state = 133
                self.data_type()
                self.state = 134
                self.match(lowParser.ID)
                self.state = 140
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Logic_expresionsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._AND = None # Token
            self._OR = None # Token

        def relational_expresions(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lowParser.Relational_expresionsContext)
            else:
                return self.getTypedRuleContext(lowParser.Relational_expresionsContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(lowParser.AND)
            else:
                return self.getToken(lowParser.AND, i)

        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(lowParser.OR)
            else:
                return self.getToken(lowParser.OR, i)

        def getRuleIndex(self):
            return lowParser.RULE_logic_expresions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogic_expresions" ):
                listener.enterLogic_expresions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogic_expresions" ):
                listener.exitLogic_expresions(self)




    def logic_expresions(self):

        localctx = lowParser.Logic_expresionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_logic_expresions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.relational_expresions()
            self.state = 151
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==lowParser.AND or _la==lowParser.OR:
                self.state = 146
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [lowParser.AND]:
                    self.state = 142
                    localctx._AND = self.match(lowParser.AND)
                    compiler.add_operator((None if localctx._AND is None else localctx._AND.text))
                    pass
                elif token in [lowParser.OR]:
                    self.state = 144
                    localctx._OR = self.match(lowParser.OR)
                    compiler.add_operator((None if localctx._OR is None else localctx._OR.text))
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 148
                self.relational_expresions()
                self.state = 153
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Relational_expresionsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._GREATER = None # Token
            self._LESS = None # Token
            self._LESS_OR_EQUAL = None # Token
            self._GREATER_OR_EQUAL = None # Token
            self._NOT_EQUAL = None # Token
            self._EQUAL = None # Token

        def addition_substraction_expresions(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lowParser.Addition_substraction_expresionsContext)
            else:
                return self.getTypedRuleContext(lowParser.Addition_substraction_expresionsContext,i)


        def GREATER(self):
            return self.getToken(lowParser.GREATER, 0)

        def LESS(self):
            return self.getToken(lowParser.LESS, 0)

        def LESS_OR_EQUAL(self):
            return self.getToken(lowParser.LESS_OR_EQUAL, 0)

        def GREATER_OR_EQUAL(self):
            return self.getToken(lowParser.GREATER_OR_EQUAL, 0)

        def NOT_EQUAL(self):
            return self.getToken(lowParser.NOT_EQUAL, 0)

        def EQUAL(self):
            return self.getToken(lowParser.EQUAL, 0)

        def getRuleIndex(self):
            return lowParser.RULE_relational_expresions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelational_expresions" ):
                listener.enterRelational_expresions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelational_expresions" ):
                listener.exitRelational_expresions(self)




    def relational_expresions(self):

        localctx = lowParser.Relational_expresionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_relational_expresions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.addition_substraction_expresions()
            compiler.add_operator((None if localctx._GREATER is None else localctx._GREATER.text))
            self.state = 173
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << lowParser.LESS) | (1 << lowParser.LESS_OR_EQUAL) | (1 << lowParser.GREATER) | (1 << lowParser.GREATER_OR_EQUAL) | (1 << lowParser.EQUAL) | (1 << lowParser.NOT_EQUAL))) != 0):
                self.state = 170
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                if la_ == 1:
                    self.state = 156
                    localctx._GREATER = self.match(lowParser.GREATER)
                    compiler.add_operator((None if localctx._GREATER is None else localctx._GREATER.text))
                    pass

                elif la_ == 2:
                    self.state = 158
                    localctx._LESS = self.match(lowParser.LESS)
                    compiler.add_operator((None if localctx._LESS is None else localctx._LESS.text))
                    pass

                elif la_ == 3:
                    self.state = 160
                    localctx._LESS_OR_EQUAL = self.match(lowParser.LESS_OR_EQUAL)
                    compiler.add_operator((None if localctx._LESS_OR_EQUAL is None else localctx._LESS_OR_EQUAL.text))
                    pass

                elif la_ == 4:
                    self.state = 162
                    localctx._GREATER = self.match(lowParser.GREATER)
                    compiler.add_operator((None if localctx._GREATER_OR_EQUAL is None else localctx._GREATER_OR_EQUAL.text))
                    pass

                elif la_ == 5:
                    self.state = 164
                    localctx._GREATER_OR_EQUAL = self.match(lowParser.GREATER_OR_EQUAL)
                    compiler.add_operator((None if localctx._GREATER_OR_EQUAL is None else localctx._GREATER_OR_EQUAL.text))
                    pass

                elif la_ == 6:
                    self.state = 166
                    localctx._NOT_EQUAL = self.match(lowParser.NOT_EQUAL)
                    compiler.add_operator((None if localctx._NOT_EQUAL is None else localctx._NOT_EQUAL.text))
                    pass

                elif la_ == 7:
                    self.state = 168
                    localctx._EQUAL = self.match(lowParser.EQUAL)
                    compiler.add_operator((None if localctx._EQUAL is None else localctx._EQUAL.text))
                    pass


                self.state = 172
                self.addition_substraction_expresions()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Addition_substraction_expresionsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ADDITION = None # Token
            self._SUBTRACTION = None # Token

        def multiplication_division_expresions(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lowParser.Multiplication_division_expresionsContext)
            else:
                return self.getTypedRuleContext(lowParser.Multiplication_division_expresionsContext,i)


        def ADDITION(self, i:int=None):
            if i is None:
                return self.getTokens(lowParser.ADDITION)
            else:
                return self.getToken(lowParser.ADDITION, i)

        def SUBTRACTION(self, i:int=None):
            if i is None:
                return self.getTokens(lowParser.SUBTRACTION)
            else:
                return self.getToken(lowParser.SUBTRACTION, i)

        def getRuleIndex(self):
            return lowParser.RULE_addition_substraction_expresions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddition_substraction_expresions" ):
                listener.enterAddition_substraction_expresions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddition_substraction_expresions" ):
                listener.exitAddition_substraction_expresions(self)




    def addition_substraction_expresions(self):

        localctx = lowParser.Addition_substraction_expresionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_addition_substraction_expresions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.multiplication_division_expresions()
            compiler.check_for_add_or_subs()
            self.state = 186
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==lowParser.ADDITION or _la==lowParser.SUBTRACTION:
                self.state = 181
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [lowParser.ADDITION]:
                    self.state = 177
                    localctx._ADDITION = self.match(lowParser.ADDITION)
                    compiler.add_operator((None if localctx._ADDITION is None else localctx._ADDITION.text))
                    pass
                elif token in [lowParser.SUBTRACTION]:
                    self.state = 179
                    localctx._SUBTRACTION = self.match(lowParser.SUBTRACTION)
                    compiler.add_operator((None if localctx._SUBTRACTION is None else localctx._SUBTRACTION.text))
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 183
                self.multiplication_division_expresions()
                self.state = 188
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Multiplication_division_expresionsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._MULTIPLICATION = None # Token
            self._DIVISION = None # Token

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lowParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(lowParser.ExpresionContext,i)


        def MULTIPLICATION(self, i:int=None):
            if i is None:
                return self.getTokens(lowParser.MULTIPLICATION)
            else:
                return self.getToken(lowParser.MULTIPLICATION, i)

        def DIVISION(self, i:int=None):
            if i is None:
                return self.getTokens(lowParser.DIVISION)
            else:
                return self.getToken(lowParser.DIVISION, i)

        def getRuleIndex(self):
            return lowParser.RULE_multiplication_division_expresions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplication_division_expresions" ):
                listener.enterMultiplication_division_expresions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplication_division_expresions" ):
                listener.exitMultiplication_division_expresions(self)




    def multiplication_division_expresions(self):

        localctx = lowParser.Multiplication_division_expresionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_multiplication_division_expresions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.expresion()
            compiler.check_for_mult_or_div()
            self.state = 200
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==lowParser.MULTIPLICATION or _la==lowParser.DIVISION:
                self.state = 195
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [lowParser.MULTIPLICATION]:
                    self.state = 191
                    localctx._MULTIPLICATION = self.match(lowParser.MULTIPLICATION)
                    compiler.add_operator((None if localctx._MULTIPLICATION is None else localctx._MULTIPLICATION.text))
                    pass
                elif token in [lowParser.DIVISION]:
                    self.state = 193
                    localctx._DIVISION = self.match(lowParser.DIVISION)
                    compiler.add_operator((None if localctx._DIVISION is None else localctx._DIVISION.text))
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 197
                self.expresion()
                self.state = 202
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def constant(self):
            return self.getTypedRuleContext(lowParser.ConstantContext,0)


        def variable(self):
            return self.getTypedRuleContext(lowParser.VariableContext,0)


        def LEFT_PARENTHESIS(self):
            return self.getToken(lowParser.LEFT_PARENTHESIS, 0)

        def logic_expresions(self):
            return self.getTypedRuleContext(lowParser.Logic_expresionsContext,0)


        def RIGHT_PARENTHESIS(self):
            return self.getToken(lowParser.RIGHT_PARENTHESIS, 0)

        def function_call(self):
            return self.getTypedRuleContext(lowParser.Function_callContext,0)


        def getRuleIndex(self):
            return lowParser.RULE_expresion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresion" ):
                listener.enterExpresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresion" ):
                listener.exitExpresion(self)




    def expresion(self):

        localctx = lowParser.ExpresionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_expresion)
        try:
            self.state = 212
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 203
                self.constant()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 204
                self.variable()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 205
                self.match(lowParser.LEFT_PARENTHESIS)
                compiler.left_parenthesis()
                self.state = 207
                self.logic_expresions()
                self.state = 208
                self.match(lowParser.RIGHT_PARENTHESIS)
                compiler.right_parenthesis()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 211
                self.function_call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(lowParser.ID, 0)

        def LEFT_BRACKET(self):
            return self.getToken(lowParser.LEFT_BRACKET, 0)

        def logic_expresions(self):
            return self.getTypedRuleContext(lowParser.Logic_expresionsContext,0)


        def RIGHT_BRACKET(self):
            return self.getToken(lowParser.RIGHT_BRACKET, 0)

        def getRuleIndex(self):
            return lowParser.RULE_variable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)




    def variable(self):

        localctx = lowParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_variable)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.match(lowParser.ID)
            self.state = 219
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==lowParser.LEFT_BRACKET:
                self.state = 215
                self.match(lowParser.LEFT_BRACKET)
                self.state = 216
                self.logic_expresions()
                self.state = 217
                self.match(lowParser.RIGHT_BRACKET)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_callContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(lowParser.ID, 0)

        def LEFT_PARENTHESIS(self):
            return self.getToken(lowParser.LEFT_PARENTHESIS, 0)

        def RIGHT_PARENTHESIS(self):
            return self.getToken(lowParser.RIGHT_PARENTHESIS, 0)

        def logic_expresions(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lowParser.Logic_expresionsContext)
            else:
                return self.getTypedRuleContext(lowParser.Logic_expresionsContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(lowParser.COMMA)
            else:
                return self.getToken(lowParser.COMMA, i)

        def getRuleIndex(self):
            return lowParser.RULE_function_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_call" ):
                listener.enterFunction_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_call" ):
                listener.exitFunction_call(self)




    def function_call(self):

        localctx = lowParser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_function_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.match(lowParser.ID)
            self.state = 222
            self.match(lowParser.LEFT_PARENTHESIS)
            self.state = 231
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << lowParser.LEFT_PARENTHESIS) | (1 << lowParser.STRING_CONSTANT) | (1 << lowParser.CHAR_CONSTANT) | (1 << lowParser.INT_CONSTANT) | (1 << lowParser.FLOAT_CONSTANT) | (1 << lowParser.BOOL_CONSTANT) | (1 << lowParser.ID))) != 0):
                self.state = 223
                self.logic_expresions()
                self.state = 228
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==lowParser.COMMA:
                    self.state = 224
                    self.match(lowParser.COMMA)
                    self.state = 225
                    self.logic_expresions()
                    self.state = 230
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 233
            self.match(lowParser.RIGHT_PARENTHESIS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Main_functionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MAIN(self):
            return self.getToken(lowParser.MAIN, 0)

        def LEFT_PARENTHESIS(self):
            return self.getToken(lowParser.LEFT_PARENTHESIS, 0)

        def RIGHT_PARENTHESIS(self):
            return self.getToken(lowParser.RIGHT_PARENTHESIS, 0)

        def LEFT_CURLY(self):
            return self.getToken(lowParser.LEFT_CURLY, 0)

        def statutes(self):
            return self.getTypedRuleContext(lowParser.StatutesContext,0)


        def RIGHT_CURLY(self):
            return self.getToken(lowParser.RIGHT_CURLY, 0)

        def getRuleIndex(self):
            return lowParser.RULE_main_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMain_function" ):
                listener.enterMain_function(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMain_function" ):
                listener.exitMain_function(self)




    def main_function(self):

        localctx = lowParser.Main_functionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_main_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self.match(lowParser.MAIN)
            self.state = 236
            self.match(lowParser.LEFT_PARENTHESIS)
            self.state = 237
            self.match(lowParser.RIGHT_PARENTHESIS)
            self.state = 238
            self.match(lowParser.LEFT_CURLY)
            self.state = 239
            self.statutes()
            self.state = 240
            self.match(lowParser.RIGHT_CURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatutesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lowParser.AssignationContext)
            else:
                return self.getTypedRuleContext(lowParser.AssignationContext,i)


        def read_function_call(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lowParser.Read_function_callContext)
            else:
                return self.getTypedRuleContext(lowParser.Read_function_callContext,i)


        def write_function_call(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lowParser.Write_function_callContext)
            else:
                return self.getTypedRuleContext(lowParser.Write_function_callContext,i)


        def void_function_call(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lowParser.Void_function_callContext)
            else:
                return self.getTypedRuleContext(lowParser.Void_function_callContext,i)


        def return_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lowParser.Return_statementContext)
            else:
                return self.getTypedRuleContext(lowParser.Return_statementContext,i)


        def conditional_function(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lowParser.Conditional_functionContext)
            else:
                return self.getTypedRuleContext(lowParser.Conditional_functionContext,i)


        def while_function(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lowParser.While_functionContext)
            else:
                return self.getTypedRuleContext(lowParser.While_functionContext,i)


        def from_function(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lowParser.From_functionContext)
            else:
                return self.getTypedRuleContext(lowParser.From_functionContext,i)


        def getRuleIndex(self):
            return lowParser.RULE_statutes

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatutes" ):
                listener.enterStatutes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatutes" ):
                listener.exitStatutes(self)




    def statutes(self):

        localctx = lowParser.StatutesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_statutes)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << lowParser.RETURN) | (1 << lowParser.INPUT) | (1 << lowParser.OUTPUT) | (1 << lowParser.IF) | (1 << lowParser.WHILE) | (1 << lowParser.FROM) | (1 << lowParser.ID))) != 0):
                self.state = 250
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                if la_ == 1:
                    self.state = 242
                    self.assignation()
                    pass

                elif la_ == 2:
                    self.state = 243
                    self.read_function_call()
                    pass

                elif la_ == 3:
                    self.state = 244
                    self.write_function_call()
                    pass

                elif la_ == 4:
                    self.state = 245
                    self.void_function_call()
                    pass

                elif la_ == 5:
                    self.state = 246
                    self.return_statement()
                    pass

                elif la_ == 6:
                    self.state = 247
                    self.conditional_function()
                    pass

                elif la_ == 7:
                    self.state = 248
                    self.while_function()
                    pass

                elif la_ == 8:
                    self.state = 249
                    self.from_function()
                    pass


                self.state = 254
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(lowParser.VariableContext,0)


        def ASSIGN(self):
            return self.getToken(lowParser.ASSIGN, 0)

        def logic_expresions(self):
            return self.getTypedRuleContext(lowParser.Logic_expresionsContext,0)


        def SEMICOLON(self):
            return self.getToken(lowParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return lowParser.RULE_assignation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignation" ):
                listener.enterAssignation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignation" ):
                listener.exitAssignation(self)




    def assignation(self):

        localctx = lowParser.AssignationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_assignation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self.variable()
            self.state = 256
            self.match(lowParser.ASSIGN)
            self.state = 257
            self.logic_expresions()
            self.state = 258
            self.match(lowParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Read_function_callContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INPUT(self):
            return self.getToken(lowParser.INPUT, 0)

        def LEFT_PARENTHESIS(self):
            return self.getToken(lowParser.LEFT_PARENTHESIS, 0)

        def variable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lowParser.VariableContext)
            else:
                return self.getTypedRuleContext(lowParser.VariableContext,i)


        def RIGHT_PARENTHESIS(self):
            return self.getToken(lowParser.RIGHT_PARENTHESIS, 0)

        def SEMICOLON(self):
            return self.getToken(lowParser.SEMICOLON, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(lowParser.COMMA)
            else:
                return self.getToken(lowParser.COMMA, i)

        def getRuleIndex(self):
            return lowParser.RULE_read_function_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRead_function_call" ):
                listener.enterRead_function_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRead_function_call" ):
                listener.exitRead_function_call(self)




    def read_function_call(self):

        localctx = lowParser.Read_function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_read_function_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.match(lowParser.INPUT)
            self.state = 261
            self.match(lowParser.LEFT_PARENTHESIS)
            self.state = 262
            self.variable()
            self.state = 267
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==lowParser.COMMA:
                self.state = 263
                self.match(lowParser.COMMA)
                self.state = 264
                self.variable()
                self.state = 269
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 270
            self.match(lowParser.RIGHT_PARENTHESIS)
            self.state = 271
            self.match(lowParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Write_function_callContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OUTPUT(self):
            return self.getToken(lowParser.OUTPUT, 0)

        def LEFT_PARENTHESIS(self):
            return self.getToken(lowParser.LEFT_PARENTHESIS, 0)

        def RIGHT_PARENTHESIS(self):
            return self.getToken(lowParser.RIGHT_PARENTHESIS, 0)

        def SEMICOLON(self):
            return self.getToken(lowParser.SEMICOLON, 0)

        def logic_expresions(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lowParser.Logic_expresionsContext)
            else:
                return self.getTypedRuleContext(lowParser.Logic_expresionsContext,i)


        def STRING_CONSTANT(self, i:int=None):
            if i is None:
                return self.getTokens(lowParser.STRING_CONSTANT)
            else:
                return self.getToken(lowParser.STRING_CONSTANT, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(lowParser.COMMA)
            else:
                return self.getToken(lowParser.COMMA, i)

        def getRuleIndex(self):
            return lowParser.RULE_write_function_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWrite_function_call" ):
                listener.enterWrite_function_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWrite_function_call" ):
                listener.exitWrite_function_call(self)




    def write_function_call(self):

        localctx = lowParser.Write_function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_write_function_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self.match(lowParser.OUTPUT)
            self.state = 274
            self.match(lowParser.LEFT_PARENTHESIS)
            self.state = 277
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 275
                self.logic_expresions()
                pass

            elif la_ == 2:
                self.state = 276
                self.match(lowParser.STRING_CONSTANT)
                pass


            self.state = 286
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==lowParser.COMMA:
                self.state = 279
                self.match(lowParser.COMMA)
                self.state = 282
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
                if la_ == 1:
                    self.state = 280
                    self.logic_expresions()
                    pass

                elif la_ == 2:
                    self.state = 281
                    self.match(lowParser.STRING_CONSTANT)
                    pass


                self.state = 288
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 289
            self.match(lowParser.RIGHT_PARENTHESIS)
            self.state = 290
            self.match(lowParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Void_function_callContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_call(self):
            return self.getTypedRuleContext(lowParser.Function_callContext,0)


        def SEMICOLON(self):
            return self.getToken(lowParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return lowParser.RULE_void_function_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVoid_function_call" ):
                listener.enterVoid_function_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVoid_function_call" ):
                listener.exitVoid_function_call(self)




    def void_function_call(self):

        localctx = lowParser.Void_function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_void_function_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292
            self.function_call()
            self.state = 293
            self.match(lowParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(lowParser.RETURN, 0)

        def LEFT_PARENTHESIS(self):
            return self.getToken(lowParser.LEFT_PARENTHESIS, 0)

        def logic_expresions(self):
            return self.getTypedRuleContext(lowParser.Logic_expresionsContext,0)


        def RIGHT_PARENTHESIS(self):
            return self.getToken(lowParser.RIGHT_PARENTHESIS, 0)

        def SEMICOLON(self):
            return self.getToken(lowParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return lowParser.RULE_return_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn_statement" ):
                listener.enterReturn_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn_statement" ):
                listener.exitReturn_statement(self)




    def return_statement(self):

        localctx = lowParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_return_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self.match(lowParser.RETURN)
            self.state = 296
            self.match(lowParser.LEFT_PARENTHESIS)
            self.state = 297
            self.logic_expresions()
            self.state = 298
            self.match(lowParser.RIGHT_PARENTHESIS)
            self.state = 299
            self.match(lowParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Conditional_functionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(lowParser.IF, 0)

        def LEFT_PARENTHESIS(self, i:int=None):
            if i is None:
                return self.getTokens(lowParser.LEFT_PARENTHESIS)
            else:
                return self.getToken(lowParser.LEFT_PARENTHESIS, i)

        def logic_expresions(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lowParser.Logic_expresionsContext)
            else:
                return self.getTypedRuleContext(lowParser.Logic_expresionsContext,i)


        def RIGHT_PARENTHESIS(self, i:int=None):
            if i is None:
                return self.getTokens(lowParser.RIGHT_PARENTHESIS)
            else:
                return self.getToken(lowParser.RIGHT_PARENTHESIS, i)

        def THEN(self, i:int=None):
            if i is None:
                return self.getTokens(lowParser.THEN)
            else:
                return self.getToken(lowParser.THEN, i)

        def LEFT_CURLY(self, i:int=None):
            if i is None:
                return self.getTokens(lowParser.LEFT_CURLY)
            else:
                return self.getToken(lowParser.LEFT_CURLY, i)

        def statutes(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lowParser.StatutesContext)
            else:
                return self.getTypedRuleContext(lowParser.StatutesContext,i)


        def RIGHT_CURLY(self, i:int=None):
            if i is None:
                return self.getTokens(lowParser.RIGHT_CURLY)
            else:
                return self.getToken(lowParser.RIGHT_CURLY, i)

        def ELSE_IF(self):
            return self.getToken(lowParser.ELSE_IF, 0)

        def ELSE(self):
            return self.getToken(lowParser.ELSE, 0)

        def getRuleIndex(self):
            return lowParser.RULE_conditional_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditional_function" ):
                listener.enterConditional_function(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditional_function" ):
                listener.exitConditional_function(self)




    def conditional_function(self):

        localctx = lowParser.Conditional_functionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_conditional_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            self.match(lowParser.IF)
            self.state = 302
            self.match(lowParser.LEFT_PARENTHESIS)
            self.state = 303
            self.logic_expresions()
            self.state = 304
            self.match(lowParser.RIGHT_PARENTHESIS)
            self.state = 305
            self.match(lowParser.THEN)
            self.state = 306
            self.match(lowParser.LEFT_CURLY)
            self.state = 307
            self.statutes()
            self.state = 308
            self.match(lowParser.RIGHT_CURLY)
            self.state = 318
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==lowParser.ELSE_IF:
                self.state = 309
                self.match(lowParser.ELSE_IF)
                self.state = 310
                self.match(lowParser.LEFT_PARENTHESIS)
                self.state = 311
                self.logic_expresions()
                self.state = 312
                self.match(lowParser.RIGHT_PARENTHESIS)
                self.state = 313
                self.match(lowParser.THEN)
                self.state = 314
                self.match(lowParser.LEFT_CURLY)
                self.state = 315
                self.statutes()
                self.state = 316
                self.match(lowParser.RIGHT_CURLY)


            self.state = 325
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==lowParser.ELSE:
                self.state = 320
                self.match(lowParser.ELSE)
                self.state = 321
                self.match(lowParser.LEFT_CURLY)
                self.state = 322
                self.statutes()
                self.state = 323
                self.match(lowParser.RIGHT_CURLY)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_functionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(lowParser.WHILE, 0)

        def LEFT_PARENTHESIS(self):
            return self.getToken(lowParser.LEFT_PARENTHESIS, 0)

        def logic_expresions(self):
            return self.getTypedRuleContext(lowParser.Logic_expresionsContext,0)


        def RIGHT_PARENTHESIS(self):
            return self.getToken(lowParser.RIGHT_PARENTHESIS, 0)

        def DO(self):
            return self.getToken(lowParser.DO, 0)

        def LEFT_CURLY(self):
            return self.getToken(lowParser.LEFT_CURLY, 0)

        def statutes(self):
            return self.getTypedRuleContext(lowParser.StatutesContext,0)


        def RIGHT_CURLY(self):
            return self.getToken(lowParser.RIGHT_CURLY, 0)

        def getRuleIndex(self):
            return lowParser.RULE_while_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_function" ):
                listener.enterWhile_function(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_function" ):
                listener.exitWhile_function(self)




    def while_function(self):

        localctx = lowParser.While_functionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_while_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 327
            self.match(lowParser.WHILE)
            self.state = 328
            self.match(lowParser.LEFT_PARENTHESIS)
            self.state = 329
            self.logic_expresions()
            self.state = 330
            self.match(lowParser.RIGHT_PARENTHESIS)
            self.state = 331
            self.match(lowParser.DO)
            self.state = 332
            self.match(lowParser.LEFT_CURLY)
            self.state = 333
            self.statutes()
            self.state = 334
            self.match(lowParser.RIGHT_CURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class From_functionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FROM(self):
            return self.getToken(lowParser.FROM, 0)

        def variable(self):
            return self.getTypedRuleContext(lowParser.VariableContext,0)


        def ASSIGN(self):
            return self.getToken(lowParser.ASSIGN, 0)

        def logic_expresions(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lowParser.Logic_expresionsContext)
            else:
                return self.getTypedRuleContext(lowParser.Logic_expresionsContext,i)


        def TO(self):
            return self.getToken(lowParser.TO, 0)

        def DO(self):
            return self.getToken(lowParser.DO, 0)

        def LEFT_CURLY(self):
            return self.getToken(lowParser.LEFT_CURLY, 0)

        def statutes(self):
            return self.getTypedRuleContext(lowParser.StatutesContext,0)


        def RIGHT_CURLY(self):
            return self.getToken(lowParser.RIGHT_CURLY, 0)

        def getRuleIndex(self):
            return lowParser.RULE_from_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFrom_function" ):
                listener.enterFrom_function(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFrom_function" ):
                listener.exitFrom_function(self)




    def from_function(self):

        localctx = lowParser.From_functionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_from_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            self.match(lowParser.FROM)
            self.state = 337
            self.variable()
            self.state = 338
            self.match(lowParser.ASSIGN)
            self.state = 339
            self.logic_expresions()
            self.state = 340
            self.match(lowParser.TO)
            self.state = 341
            self.logic_expresions()
            self.state = 342
            self.match(lowParser.DO)
            self.state = 343
            self.match(lowParser.LEFT_CURLY)
            self.state = 344
            self.statutes()
            self.state = 345
            self.match(lowParser.RIGHT_CURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





