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
        buf.write("\u017d\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\3\3\3\6\3@\n\3\r\3\16\3A\3\4\3\4\3\4\3\4\7\4H\n\4\f")
        buf.write("\4\16\4K\13\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\5\5Y\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\5\6e\n\6\3\7\3\7\3\7\5\7j\n\7\3\7\5\7m\n\7\3\b\7")
        buf.write("\bp\n\b\f\b\16\bs\13\b\3\t\3\t\3\t\5\tx\n\t\3\t\3\t\3")
        buf.write("\t\5\t}\n\t\3\t\3\t\5\t\u0081\n\t\3\t\3\t\5\t\u0085\n")
        buf.write("\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\7\n\u008f\n\n\f\n\16")
        buf.write("\n\u0092\13\n\3\13\3\13\3\13\7\13\u0097\n\13\f\13\16\13")
        buf.write("\u009a\13\13\3\f\3\f\3\f\3\f\3\f\5\f\u00a1\n\f\3\f\7\f")
        buf.write("\u00a4\n\f\f\f\16\f\u00a7\13\f\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00b7\n\r\3\r\5\r")
        buf.write("\u00ba\n\r\3\16\3\16\3\16\3\16\3\16\3\16\5\16\u00c2\n")
        buf.write("\16\3\16\7\16\u00c5\n\16\f\16\16\16\u00c8\13\16\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\5\17\u00d0\n\17\3\17\7\17\u00d3")
        buf.write("\n\17\f\17\16\17\u00d6\13\17\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\7\20\u00e4\n\20\f")
        buf.write("\20\16\20\u00e7\13\20\5\20\u00e9\n\20\3\20\3\20\3\20\3")
        buf.write("\20\5\20\u00ef\n\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\7\21\u00f9\n\21\f\21\16\21\u00fc\13\21\3\22\3\22")
        buf.write("\3\22\3\22\3\22\5\22\u0103\n\22\3\22\3\22\3\22\3\22\3")
        buf.write("\23\3\23\3\23\3\23\3\23\7\23\u010e\n\23\f\23\16\23\u0111")
        buf.write("\13\23\5\23\u0113\n\23\3\23\3\23\3\23\3\24\3\24\3\24\3")
        buf.write("\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\5\25\u0123\n\25")
        buf.write("\3\26\3\26\3\26\3\26\3\26\7\26\u012a\n\26\f\26\16\26\u012d")
        buf.write("\13\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\5\27\u0136\n")
        buf.write("\27\3\27\3\27\3\27\5\27\u013b\n\27\7\27\u013d\n\27\f\27")
        buf.write("\16\27\u0140\13\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\5\30\u0156\n\30\3\30\3\30\3\30\3\30\3\30\5")
        buf.write("\30\u015d\n\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\32\3\32\3\32\5\32\u016b\n\32\3\32\3\32\3\32\3")
        buf.write("\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\2\2\34\2\4\6\b\n\f\16\20\22\24\26\30\32")
        buf.write("\34\36 \"$&(*,.\60\62\64\2\2\2\u0199\2\66\3\2\2\2\4=\3")
        buf.write("\2\2\2\6C\3\2\2\2\bX\3\2\2\2\nd\3\2\2\2\ff\3\2\2\2\16")
        buf.write("q\3\2\2\2\20t\3\2\2\2\22\u0088\3\2\2\2\24\u0093\3\2\2")
        buf.write("\2\26\u009b\3\2\2\2\30\u00a8\3\2\2\2\32\u00bb\3\2\2\2")
        buf.write("\34\u00c9\3\2\2\2\36\u00ee\3\2\2\2 \u00fa\3\2\2\2\"\u00fd")
        buf.write("\3\2\2\2$\u0108\3\2\2\2&\u0117\3\2\2\2(\u011d\3\2\2\2")
        buf.write("*\u0124\3\2\2\2,\u0131\3\2\2\2.\u0144\3\2\2\2\60\u015e")
        buf.write("\3\2\2\2\62\u0167\3\2\2\2\64\u0175\3\2\2\2\66\67\7\3\2")
        buf.write("\2\678\7\63\2\289\7\32\2\29:\5\4\3\2:;\5\16\b\2;<\5\64")
        buf.write("\33\2<\3\3\2\2\2=?\7(\2\2>@\5\6\4\2?>\3\2\2\2@A\3\2\2")
        buf.write("\2A?\3\2\2\2AB\3\2\2\2B\5\3\2\2\2CD\5\b\5\2DI\5\f\7\2")
        buf.write("EF\7\30\2\2FH\5\f\7\2GE\3\2\2\2HK\3\2\2\2IG\3\2\2\2IJ")
        buf.write("\3\2\2\2JL\3\2\2\2KI\3\2\2\2LM\7\32\2\2M\7\3\2\2\2NO\7")
        buf.write("+\2\2OY\b\5\1\2PQ\7-\2\2QY\b\5\1\2RS\7,\2\2SY\b\5\1\2")
        buf.write("TU\7)\2\2UY\b\5\1\2VW\7*\2\2WY\b\5\1\2XN\3\2\2\2XP\3\2")
        buf.write("\2\2XR\3\2\2\2XT\3\2\2\2XV\3\2\2\2Y\t\3\2\2\2Z[\7\62\2")
        buf.write("\2[e\b\6\1\2\\]\7\61\2\2]e\b\6\1\2^_\7\60\2\2_e\b\6\1")
        buf.write("\2`a\7/\2\2ae\b\6\1\2bc\7.\2\2ce\b\6\1\2dZ\3\2\2\2d\\")
        buf.write("\3\2\2\2d^\3\2\2\2d`\3\2\2\2db\3\2\2\2e\13\3\2\2\2fl\7")
        buf.write("\63\2\2gi\7\24\2\2hj\7\60\2\2ih\3\2\2\2ij\3\2\2\2jk\3")
        buf.write("\2\2\2km\7\25\2\2lg\3\2\2\2lm\3\2\2\2m\r\3\2\2\2np\5\20")
        buf.write("\t\2on\3\2\2\2ps\3\2\2\2qo\3\2\2\2qr\3\2\2\2r\17\3\2\2")
        buf.write("\2sq\3\2\2\2tw\7\5\2\2ux\5\b\5\2vx\7\21\2\2wu\3\2\2\2")
        buf.write("wv\3\2\2\2xy\3\2\2\2yz\7\63\2\2z|\7\22\2\2{}\5\22\n\2")
        buf.write("|{\3\2\2\2|}\3\2\2\2}~\3\2\2\2~\u0080\7\23\2\2\177\u0081")
        buf.write("\5\4\3\2\u0080\177\3\2\2\2\u0080\u0081\3\2\2\2\u0081\u0082")
        buf.write("\3\2\2\2\u0082\u0084\7\26\2\2\u0083\u0085\5 \21\2\u0084")
        buf.write("\u0083\3\2\2\2\u0084\u0085\3\2\2\2\u0085\u0086\3\2\2\2")
        buf.write("\u0086\u0087\7\27\2\2\u0087\21\3\2\2\2\u0088\u0089\5\b")
        buf.write("\5\2\u0089\u0090\7\63\2\2\u008a\u008b\7\30\2\2\u008b\u008c")
        buf.write("\5\b\5\2\u008c\u008d\7\63\2\2\u008d\u008f\3\2\2\2\u008e")
        buf.write("\u008a\3\2\2\2\u008f\u0092\3\2\2\2\u0090\u008e\3\2\2\2")
        buf.write("\u0090\u0091\3\2\2\2\u0091\23\3\2\2\2\u0092\u0090\3\2")
        buf.write("\2\2\u0093\u0098\5\26\f\2\u0094\u0095\7!\2\2\u0095\u0097")
        buf.write("\5\26\f\2\u0096\u0094\3\2\2\2\u0097\u009a\3\2\2\2\u0098")
        buf.write("\u0096\3\2\2\2\u0098\u0099\3\2\2\2\u0099\25\3\2\2\2\u009a")
        buf.write("\u0098\3\2\2\2\u009b\u00a5\5\30\r\2\u009c\u009d\7\"\2")
        buf.write("\2\u009d\u00a1\b\f\1\2\u009e\u009f\7#\2\2\u009f\u00a1")
        buf.write("\b\f\1\2\u00a0\u009c\3\2\2\2\u00a0\u009e\3\2\2\2\u00a1")
        buf.write("\u00a2\3\2\2\2\u00a2\u00a4\5\30\r\2\u00a3\u00a0\3\2\2")
        buf.write("\2\u00a4\u00a7\3\2\2\2\u00a5\u00a3\3\2\2\2\u00a5\u00a6")
        buf.write("\3\2\2\2\u00a6\27\3\2\2\2\u00a7\u00a5\3\2\2\2\u00a8\u00a9")
        buf.write("\5\32\16\2\u00a9\u00b9\b\r\1\2\u00aa\u00ab\7\34\2\2\u00ab")
        buf.write("\u00b7\b\r\1\2\u00ac\u00ad\7\33\2\2\u00ad\u00b7\b\r\1")
        buf.write("\2\u00ae\u00af\7\36\2\2\u00af\u00b7\b\r\1\2\u00b0\u00b1")
        buf.write("\7\35\2\2\u00b1\u00b7\b\r\1\2\u00b2\u00b3\7 \2\2\u00b3")
        buf.write("\u00b7\b\r\1\2\u00b4\u00b5\7\37\2\2\u00b5\u00b7\b\r\1")
        buf.write("\2\u00b6\u00aa\3\2\2\2\u00b6\u00ac\3\2\2\2\u00b6\u00ae")
        buf.write("\3\2\2\2\u00b6\u00b0\3\2\2\2\u00b6\u00b2\3\2\2\2\u00b6")
        buf.write("\u00b4\3\2\2\2\u00b7\u00b8\3\2\2\2\u00b8\u00ba\5\32\16")
        buf.write("\2\u00b9\u00b6\3\2\2\2\u00b9\u00ba\3\2\2\2\u00ba\31\3")
        buf.write("\2\2\2\u00bb\u00bc\5\34\17\2\u00bc\u00c6\b\16\1\2\u00bd")
        buf.write("\u00be\7$\2\2\u00be\u00c2\b\16\1\2\u00bf\u00c0\7%\2\2")
        buf.write("\u00c0\u00c2\b\16\1\2\u00c1\u00bd\3\2\2\2\u00c1\u00bf")
        buf.write("\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c3\u00c5\5\34\17\2\u00c4")
        buf.write("\u00c1\3\2\2\2\u00c5\u00c8\3\2\2\2\u00c6\u00c4\3\2\2\2")
        buf.write("\u00c6\u00c7\3\2\2\2\u00c7\33\3\2\2\2\u00c8\u00c6\3\2")
        buf.write("\2\2\u00c9\u00ca\5\36\20\2\u00ca\u00d4\b\17\1\2\u00cb")
        buf.write("\u00cc\7&\2\2\u00cc\u00d0\b\17\1\2\u00cd\u00ce\7\'\2\2")
        buf.write("\u00ce\u00d0\b\17\1\2\u00cf\u00cb\3\2\2\2\u00cf\u00cd")
        buf.write("\3\2\2\2\u00d0\u00d1\3\2\2\2\u00d1\u00d3\5\36\20\2\u00d2")
        buf.write("\u00cf\3\2\2\2\u00d3\u00d6\3\2\2\2\u00d4\u00d2\3\2\2\2")
        buf.write("\u00d4\u00d5\3\2\2\2\u00d5\35\3\2\2\2\u00d6\u00d4\3\2")
        buf.write("\2\2\u00d7\u00d8\7\22\2\2\u00d8\u00d9\b\20\1\2\u00d9\u00da")
        buf.write("\5\24\13\2\u00da\u00db\7\23\2\2\u00db\u00dc\b\20\1\2\u00dc")
        buf.write("\u00ef\3\2\2\2\u00dd\u00de\7\63\2\2\u00de\u00df\7\22\2")
        buf.write("\2\u00df\u00e8\b\20\1\2\u00e0\u00e5\5\26\f\2\u00e1\u00e2")
        buf.write("\7\30\2\2\u00e2\u00e4\5\26\f\2\u00e3\u00e1\3\2\2\2\u00e4")
        buf.write("\u00e7\3\2\2\2\u00e5\u00e3\3\2\2\2\u00e5\u00e6\3\2\2\2")
        buf.write("\u00e6\u00e9\3\2\2\2\u00e7\u00e5\3\2\2\2\u00e8\u00e0\3")
        buf.write("\2\2\2\u00e8\u00e9\3\2\2\2\u00e9\u00ea\3\2\2\2\u00ea\u00eb")
        buf.write("\7\23\2\2\u00eb\u00ef\b\20\1\2\u00ec\u00ef\5(\25\2\u00ed")
        buf.write("\u00ef\5\n\6\2\u00ee\u00d7\3\2\2\2\u00ee\u00dd\3\2\2\2")
        buf.write("\u00ee\u00ec\3\2\2\2\u00ee\u00ed\3\2\2\2\u00ef\37\3\2")
        buf.write("\2\2\u00f0\u00f9\5\"\22\2\u00f1\u00f9\5$\23\2\u00f2\u00f9")
        buf.write("\5&\24\2\u00f3\u00f9\5*\26\2\u00f4\u00f9\5,\27\2\u00f5")
        buf.write("\u00f9\5.\30\2\u00f6\u00f9\5\60\31\2\u00f7\u00f9\5\62")
        buf.write("\32\2\u00f8\u00f0\3\2\2\2\u00f8\u00f1\3\2\2\2\u00f8\u00f2")
        buf.write("\3\2\2\2\u00f8\u00f3\3\2\2\2\u00f8\u00f4\3\2\2\2\u00f8")
        buf.write("\u00f5\3\2\2\2\u00f8\u00f6\3\2\2\2\u00f8\u00f7\3\2\2\2")
        buf.write("\u00f9\u00fc\3\2\2\2\u00fa\u00f8\3\2\2\2\u00fa\u00fb\3")
        buf.write("\2\2\2\u00fb!\3\2\2\2\u00fc\u00fa\3\2\2\2\u00fd\u0102")
        buf.write("\7\63\2\2\u00fe\u00ff\7\24\2\2\u00ff\u0100\5\26\f\2\u0100")
        buf.write("\u0101\7\25\2\2\u0101\u0103\3\2\2\2\u0102\u00fe\3\2\2")
        buf.write("\2\u0102\u0103\3\2\2\2\u0103\u0104\3\2\2\2\u0104\u0105")
        buf.write("\7!\2\2\u0105\u0106\5\24\13\2\u0106\u0107\7\32\2\2\u0107")
        buf.write("#\3\2\2\2\u0108\u0109\7\63\2\2\u0109\u0112\7\22\2\2\u010a")
        buf.write("\u010f\5\26\f\2\u010b\u010c\7\30\2\2\u010c\u010e\5\26")
        buf.write("\f\2\u010d\u010b\3\2\2\2\u010e\u0111\3\2\2\2\u010f\u010d")
        buf.write("\3\2\2\2\u010f\u0110\3\2\2\2\u0110\u0113\3\2\2\2\u0111")
        buf.write("\u010f\3\2\2\2\u0112\u010a\3\2\2\2\u0112\u0113\3\2\2\2")
        buf.write("\u0113\u0114\3\2\2\2\u0114\u0115\7\23\2\2\u0115\u0116")
        buf.write("\7\32\2\2\u0116%\3\2\2\2\u0117\u0118\7\6\2\2\u0118\u0119")
        buf.write("\7\22\2\2\u0119\u011a\5\24\13\2\u011a\u011b\7\23\2\2\u011b")
        buf.write("\u011c\7\32\2\2\u011c\'\3\2\2\2\u011d\u0122\7\63\2\2\u011e")
        buf.write("\u011f\7\24\2\2\u011f\u0120\5\26\f\2\u0120\u0121\7\25")
        buf.write("\2\2\u0121\u0123\3\2\2\2\u0122\u011e\3\2\2\2\u0122\u0123")
        buf.write("\3\2\2\2\u0123)\3\2\2\2\u0124\u0125\7\7\2\2\u0125\u0126")
        buf.write("\7\22\2\2\u0126\u012b\5(\25\2\u0127\u0128\7\30\2\2\u0128")
        buf.write("\u012a\5(\25\2\u0129\u0127\3\2\2\2\u012a\u012d\3\2\2\2")
        buf.write("\u012b\u0129\3\2\2\2\u012b\u012c\3\2\2\2\u012c\u012e\3")
        buf.write("\2\2\2\u012d\u012b\3\2\2\2\u012e\u012f\7\23\2\2\u012f")
        buf.write("\u0130\7\32\2\2\u0130+\3\2\2\2\u0131\u0132\7\b\2\2\u0132")
        buf.write("\u0135\7\22\2\2\u0133\u0136\5\24\13\2\u0134\u0136\7.\2")
        buf.write("\2\u0135\u0133\3\2\2\2\u0135\u0134\3\2\2\2\u0136\u013e")
        buf.write("\3\2\2\2\u0137\u013a\7\30\2\2\u0138\u013b\5\24\13\2\u0139")
        buf.write("\u013b\7.\2\2\u013a\u0138\3\2\2\2\u013a\u0139\3\2\2\2")
        buf.write("\u013b\u013d\3\2\2\2\u013c\u0137\3\2\2\2\u013d\u0140\3")
        buf.write("\2\2\2\u013e\u013c\3\2\2\2\u013e\u013f\3\2\2\2\u013f\u0141")
        buf.write("\3\2\2\2\u0140\u013e\3\2\2\2\u0141\u0142\7\23\2\2\u0142")
        buf.write("\u0143\7\32\2\2\u0143-\3\2\2\2\u0144\u0145\7\t\2\2\u0145")
        buf.write("\u0146\7\22\2\2\u0146\u0147\5\26\f\2\u0147\u0148\7\23")
        buf.write("\2\2\u0148\u0149\7\n\2\2\u0149\u014a\7\26\2\2\u014a\u014b")
        buf.write("\5 \21\2\u014b\u0155\7\27\2\2\u014c\u014d\7\13\2\2\u014d")
        buf.write("\u014e\7\22\2\2\u014e\u014f\5\26\f\2\u014f\u0150\7\23")
        buf.write("\2\2\u0150\u0151\7\n\2\2\u0151\u0152\7\26\2\2\u0152\u0153")
        buf.write("\5 \21\2\u0153\u0154\7\27\2\2\u0154\u0156\3\2\2\2\u0155")
        buf.write("\u014c\3\2\2\2\u0155\u0156\3\2\2\2\u0156\u015c\3\2\2\2")
        buf.write("\u0157\u0158\7\f\2\2\u0158\u0159\7\26\2\2\u0159\u015a")
        buf.write("\5 \21\2\u015a\u015b\7\27\2\2\u015b\u015d\3\2\2\2\u015c")
        buf.write("\u0157\3\2\2\2\u015c\u015d\3\2\2\2\u015d/\3\2\2\2\u015e")
        buf.write("\u015f\7\r\2\2\u015f\u0160\7\22\2\2\u0160\u0161\5\26\f")
        buf.write("\2\u0161\u0162\7\23\2\2\u0162\u0163\7\16\2\2\u0163\u0164")
        buf.write("\7\26\2\2\u0164\u0165\5 \21\2\u0165\u0166\7\27\2\2\u0166")
        buf.write("\61\3\2\2\2\u0167\u0168\7\17\2\2\u0168\u016a\7\63\2\2")
        buf.write("\u0169\u016b\5(\25\2\u016a\u0169\3\2\2\2\u016a\u016b\3")
        buf.write("\2\2\2\u016b\u016c\3\2\2\2\u016c\u016d\7!\2\2\u016d\u016e")
        buf.write("\5\26\f\2\u016e\u016f\7\20\2\2\u016f\u0170\5\26\f\2\u0170")
        buf.write("\u0171\7\16\2\2\u0171\u0172\7\26\2\2\u0172\u0173\5 \21")
        buf.write("\2\u0173\u0174\7\27\2\2\u0174\63\3\2\2\2\u0175\u0176\7")
        buf.write("\4\2\2\u0176\u0177\7\22\2\2\u0177\u0178\7\23\2\2\u0178")
        buf.write("\u0179\7\26\2\2\u0179\u017a\5 \21\2\u017a\u017b\7\27\2")
        buf.write("\2\u017b\65\3\2\2\2\'AIXdilqw|\u0080\u0084\u0090\u0098")
        buf.write("\u00a0\u00a5\u00b6\u00b9\u00c1\u00c6\u00cf\u00d4\u00e5")
        buf.write("\u00e8\u00ee\u00f8\u00fa\u0102\u010f\u0112\u0122\u012b")
        buf.write("\u0135\u013a\u013e\u0155\u015c\u016a")
        return buf.getvalue()


class lowParser ( Parser ):

    grammarFileName = "low.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'programa'", "'principal'", "'funcion'", 
                     "'regresa'", "'lee'", "'escribe'", "'si'", "'entonces'", 
                     "'o si'", "'sino'", "'mientras'", "'hacer'", "'desde'", 
                     "'hasta'", "'void'", "'('", "')'", "'['", "']'", "'{'", 
                     "'}'", "','", "':'", "';'", "'<'", "'>'", "'<='", "'>='", 
                     "'=='", "'!='", "'='", "'&'", "'|'", "'+'", "'-'", 
                     "'*'", "'/'", "'var'", "'string'", "'char'", "'int'", 
                     "'float'", "'bool'" ]

    symbolicNames = [ "<INVALID>", "PROGRAM", "MAIN", "FUNCTION", "RETURN", 
                      "INPUT", "OUTPUT", "IF", "THEN", "ELSE_IF", "ELSE", 
                      "WHILE", "DO", "FROM", "TO", "VOID", "LEFT_PARENTHESIS", 
                      "RIGHT_PARENTHESIS", "LEFT_BRACKET", "RIGHT_BRACKET", 
                      "LEFT_CURLY", "RIGHT_CURLY", "COMMA", "COLON", "SEMICOLON", 
                      "LESS", "GREATER", "LESS_OR_EQUAL", "GREATER_OR_EQUAL", 
                      "EQUAL", "NOT_EQUAL", "ASSIGN", "AND", "OR", "ADDITION", 
                      "SUBTRACTION", "MULTIPLICATION", "DIVISION", "VAR", 
                      "STRING", "CHAR", "INT", "FLOAT", "BOOL", "STRING_CONSTANT", 
                      "CHAR_CONSTANT", "INT_CONSTANT", "FLOAT_CONSTANT", 
                      "BOOL_CONSTANT", "VAR_NAME", "COMMENT_BLOCK", "COMMENT_LINE", 
                      "WHITESPACE" ]

    RULE_program = 0
    RULE_variable_declaration = 1
    RULE_variables = 2
    RULE_var_types = 3
    RULE_constant = 4
    RULE_varindividual = 5
    RULE_function_declaration = 6
    RULE_function = 7
    RULE_parameters = 8
    RULE_expresions = 9
    RULE_multiple_expresions = 10
    RULE_expresion_comparison = 11
    RULE_expresion = 12
    RULE_term = 13
    RULE_factor = 14
    RULE_statute = 15
    RULE_assignation = 16
    RULE_voidcall = 17
    RULE_returncall = 18
    RULE_indexvariable = 19
    RULE_read = 20
    RULE_write = 21
    RULE_conditional = 22
    RULE_whileloop = 23
    RULE_fromloop = 24
    RULE_main_function = 25

    ruleNames =  [ "program", "variable_declaration", "variables", "var_types", 
                   "constant", "varindividual", "function_declaration", 
                   "function", "parameters", "expresions", "multiple_expresions", 
                   "expresion_comparison", "expresion", "term", "factor", 
                   "statute", "assignation", "voidcall", "returncall", "indexvariable", 
                   "read", "write", "conditional", "whileloop", "fromloop", 
                   "main_function" ]

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
    LEFT_PARENTHESIS=16
    RIGHT_PARENTHESIS=17
    LEFT_BRACKET=18
    RIGHT_BRACKET=19
    LEFT_CURLY=20
    RIGHT_CURLY=21
    COMMA=22
    COLON=23
    SEMICOLON=24
    LESS=25
    GREATER=26
    LESS_OR_EQUAL=27
    GREATER_OR_EQUAL=28
    EQUAL=29
    NOT_EQUAL=30
    ASSIGN=31
    AND=32
    OR=33
    ADDITION=34
    SUBTRACTION=35
    MULTIPLICATION=36
    DIVISION=37
    VAR=38
    STRING=39
    CHAR=40
    INT=41
    FLOAT=42
    BOOL=43
    STRING_CONSTANT=44
    CHAR_CONSTANT=45
    INT_CONSTANT=46
    FLOAT_CONSTANT=47
    BOOL_CONSTANT=48
    VAR_NAME=49
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

        def VAR_NAME(self):
            return self.getToken(lowParser.VAR_NAME, 0)

        def SEMICOLON(self):
            return self.getToken(lowParser.SEMICOLON, 0)

        def variable_declaration(self):
            return self.getTypedRuleContext(lowParser.Variable_declarationContext,0)


        def function_declaration(self):
            return self.getTypedRuleContext(lowParser.Function_declarationContext,0)


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
            self.match(lowParser.VAR_NAME)
            self.state = 54
            self.match(lowParser.SEMICOLON)
            self.state = 55
            self.variable_declaration()
            self.state = 56
            self.function_declaration()
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

        def var_types(self):
            return self.getTypedRuleContext(lowParser.Var_typesContext,0)


        def varindividual(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lowParser.VarindividualContext)
            else:
                return self.getTypedRuleContext(lowParser.VarindividualContext,i)


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
            self.var_types()
            self.state = 66
            self.varindividual()
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==lowParser.COMMA:
                self.state = 67
                self.match(lowParser.COMMA)
                self.state = 68
                self.varindividual()
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


    class Var_typesContext(ParserRuleContext):

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
            return lowParser.RULE_var_types

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_types" ):
                listener.enterVar_types(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_types" ):
                listener.exitVar_types(self)




    def var_types(self):

        localctx = lowParser.Var_typesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_var_types)
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


    class VarindividualContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR_NAME(self):
            return self.getToken(lowParser.VAR_NAME, 0)

        def LEFT_BRACKET(self):
            return self.getToken(lowParser.LEFT_BRACKET, 0)

        def RIGHT_BRACKET(self):
            return self.getToken(lowParser.RIGHT_BRACKET, 0)

        def INT_CONSTANT(self):
            return self.getToken(lowParser.INT_CONSTANT, 0)

        def getRuleIndex(self):
            return lowParser.RULE_varindividual

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarindividual" ):
                listener.enterVarindividual(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarindividual" ):
                listener.exitVarindividual(self)




    def varindividual(self):

        localctx = lowParser.VarindividualContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_varindividual)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(lowParser.VAR_NAME)
            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==lowParser.LEFT_BRACKET:
                self.state = 101
                self.match(lowParser.LEFT_BRACKET)
                self.state = 103
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==lowParser.INT_CONSTANT:
                    self.state = 102
                    self.match(lowParser.INT_CONSTANT)


                self.state = 105
                self.match(lowParser.RIGHT_BRACKET)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lowParser.FunctionContext)
            else:
                return self.getTypedRuleContext(lowParser.FunctionContext,i)


        def getRuleIndex(self):
            return lowParser.RULE_function_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_declaration" ):
                listener.enterFunction_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_declaration" ):
                listener.exitFunction_declaration(self)




    def function_declaration(self):

        localctx = lowParser.Function_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_function_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==lowParser.FUNCTION:
                self.state = 108
                self.function()
                self.state = 113
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

        def VAR_NAME(self):
            return self.getToken(lowParser.VAR_NAME, 0)

        def LEFT_PARENTHESIS(self):
            return self.getToken(lowParser.LEFT_PARENTHESIS, 0)

        def RIGHT_PARENTHESIS(self):
            return self.getToken(lowParser.RIGHT_PARENTHESIS, 0)

        def LEFT_CURLY(self):
            return self.getToken(lowParser.LEFT_CURLY, 0)

        def RIGHT_CURLY(self):
            return self.getToken(lowParser.RIGHT_CURLY, 0)

        def var_types(self):
            return self.getTypedRuleContext(lowParser.Var_typesContext,0)


        def VOID(self):
            return self.getToken(lowParser.VOID, 0)

        def parameters(self):
            return self.getTypedRuleContext(lowParser.ParametersContext,0)


        def variable_declaration(self):
            return self.getTypedRuleContext(lowParser.Variable_declarationContext,0)


        def statute(self):
            return self.getTypedRuleContext(lowParser.StatuteContext,0)


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
            self.state = 114
            self.match(lowParser.FUNCTION)
            self.state = 117
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [lowParser.STRING, lowParser.CHAR, lowParser.INT, lowParser.FLOAT, lowParser.BOOL]:
                self.state = 115
                self.var_types()
                pass
            elif token in [lowParser.VOID]:
                self.state = 116
                self.match(lowParser.VOID)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 119
            self.match(lowParser.VAR_NAME)
            self.state = 120
            self.match(lowParser.LEFT_PARENTHESIS)
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << lowParser.STRING) | (1 << lowParser.CHAR) | (1 << lowParser.INT) | (1 << lowParser.FLOAT) | (1 << lowParser.BOOL))) != 0):
                self.state = 121
                self.parameters()


            self.state = 124
            self.match(lowParser.RIGHT_PARENTHESIS)
            self.state = 126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==lowParser.VAR:
                self.state = 125
                self.variable_declaration()


            self.state = 128
            self.match(lowParser.LEFT_CURLY)
            self.state = 130
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 129
                self.statute()


            self.state = 132
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

        def var_types(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lowParser.Var_typesContext)
            else:
                return self.getTypedRuleContext(lowParser.Var_typesContext,i)


        def VAR_NAME(self, i:int=None):
            if i is None:
                return self.getTokens(lowParser.VAR_NAME)
            else:
                return self.getToken(lowParser.VAR_NAME, i)

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
            self.state = 134
            self.var_types()
            self.state = 135
            self.match(lowParser.VAR_NAME)
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==lowParser.COMMA:
                self.state = 136
                self.match(lowParser.COMMA)
                self.state = 137
                self.var_types()
                self.state = 138
                self.match(lowParser.VAR_NAME)
                self.state = 144
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiple_expresions(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lowParser.Multiple_expresionsContext)
            else:
                return self.getTypedRuleContext(lowParser.Multiple_expresionsContext,i)


        def ASSIGN(self, i:int=None):
            if i is None:
                return self.getTokens(lowParser.ASSIGN)
            else:
                return self.getToken(lowParser.ASSIGN, i)

        def getRuleIndex(self):
            return lowParser.RULE_expresions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresions" ):
                listener.enterExpresions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresions" ):
                listener.exitExpresions(self)




    def expresions(self):

        localctx = lowParser.ExpresionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_expresions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.multiple_expresions()
            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==lowParser.ASSIGN:
                self.state = 146
                self.match(lowParser.ASSIGN)
                self.state = 147
                self.multiple_expresions()
                self.state = 152
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Multiple_expresionsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._AND = None # Token
            self._OR = None # Token

        def expresion_comparison(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lowParser.Expresion_comparisonContext)
            else:
                return self.getTypedRuleContext(lowParser.Expresion_comparisonContext,i)


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
            return lowParser.RULE_multiple_expresions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiple_expresions" ):
                listener.enterMultiple_expresions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiple_expresions" ):
                listener.exitMultiple_expresions(self)




    def multiple_expresions(self):

        localctx = lowParser.Multiple_expresionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_multiple_expresions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.expresion_comparison()
            self.state = 163
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==lowParser.AND or _la==lowParser.OR:
                self.state = 158
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [lowParser.AND]:
                    self.state = 154
                    localctx._AND = self.match(lowParser.AND)
                    compiler.add_operator((None if localctx._AND is None else localctx._AND.text))
                    pass
                elif token in [lowParser.OR]:
                    self.state = 156
                    localctx._OR = self.match(lowParser.OR)
                    compiler.add_operator((None if localctx._OR is None else localctx._OR.text))
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 160
                self.expresion_comparison()
                self.state = 165
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expresion_comparisonContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._GREATER = None # Token
            self._LESS = None # Token
            self._GREATER_OR_EQUAL = None # Token
            self._LESS_OR_EQUAL = None # Token
            self._NOT_EQUAL = None # Token
            self._EQUAL = None # Token

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lowParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(lowParser.ExpresionContext,i)


        def GREATER(self):
            return self.getToken(lowParser.GREATER, 0)

        def LESS(self):
            return self.getToken(lowParser.LESS, 0)

        def GREATER_OR_EQUAL(self):
            return self.getToken(lowParser.GREATER_OR_EQUAL, 0)

        def LESS_OR_EQUAL(self):
            return self.getToken(lowParser.LESS_OR_EQUAL, 0)

        def NOT_EQUAL(self):
            return self.getToken(lowParser.NOT_EQUAL, 0)

        def EQUAL(self):
            return self.getToken(lowParser.EQUAL, 0)

        def getRuleIndex(self):
            return lowParser.RULE_expresion_comparison

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresion_comparison" ):
                listener.enterExpresion_comparison(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresion_comparison" ):
                listener.exitExpresion_comparison(self)




    def expresion_comparison(self):

        localctx = lowParser.Expresion_comparisonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_expresion_comparison)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.expresion()
            compiler.add_operator((None if localctx._GREATER is None else localctx._GREATER.text))
            self.state = 183
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << lowParser.LESS) | (1 << lowParser.GREATER) | (1 << lowParser.LESS_OR_EQUAL) | (1 << lowParser.GREATER_OR_EQUAL) | (1 << lowParser.EQUAL) | (1 << lowParser.NOT_EQUAL))) != 0):
                self.state = 180
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [lowParser.GREATER]:
                    self.state = 168
                    localctx._GREATER = self.match(lowParser.GREATER)
                    compiler.add_operator((None if localctx._GREATER is None else localctx._GREATER.text))
                    pass
                elif token in [lowParser.LESS]:
                    self.state = 170
                    localctx._LESS = self.match(lowParser.LESS)
                    compiler.add_operator((None if localctx._LESS is None else localctx._LESS.text))
                    pass
                elif token in [lowParser.GREATER_OR_EQUAL]:
                    self.state = 172
                    localctx._GREATER_OR_EQUAL = self.match(lowParser.GREATER_OR_EQUAL)
                    compiler.add_operator((None if localctx._GREATER_OR_EQUAL is None else localctx._GREATER_OR_EQUAL.text))
                    pass
                elif token in [lowParser.LESS_OR_EQUAL]:
                    self.state = 174
                    localctx._LESS_OR_EQUAL = self.match(lowParser.LESS_OR_EQUAL)
                    compiler.add_operator((None if localctx._LESS_OR_EQUAL is None else localctx._LESS_OR_EQUAL.text))
                    pass
                elif token in [lowParser.NOT_EQUAL]:
                    self.state = 176
                    localctx._NOT_EQUAL = self.match(lowParser.NOT_EQUAL)
                    compiler.add_operator((None if localctx._NOT_EQUAL is None else localctx._NOT_EQUAL.text))
                    pass
                elif token in [lowParser.EQUAL]:
                    self.state = 178
                    localctx._EQUAL = self.match(lowParser.EQUAL)
                    compiler.add_operator((None if localctx._EQUAL is None else localctx._EQUAL.text))
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 182
                self.expresion()


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
            self._ADDITION = None # Token
            self._SUBTRACTION = None # Token

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lowParser.TermContext)
            else:
                return self.getTypedRuleContext(lowParser.TermContext,i)


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
            return lowParser.RULE_expresion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresion" ):
                listener.enterExpresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresion" ):
                listener.exitExpresion(self)




    def expresion(self):

        localctx = lowParser.ExpresionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_expresion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.term()
            compiler.check_for_add_or_subs()
            self.state = 196
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==lowParser.ADDITION or _la==lowParser.SUBTRACTION:
                self.state = 191
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [lowParser.ADDITION]:
                    self.state = 187
                    localctx._ADDITION = self.match(lowParser.ADDITION)
                    compiler.add_operator((None if localctx._ADDITION is None else localctx._ADDITION.text))
                    pass
                elif token in [lowParser.SUBTRACTION]:
                    self.state = 189
                    localctx._SUBTRACTION = self.match(lowParser.SUBTRACTION)
                    compiler.add_operator((None if localctx._SUBTRACTION is None else localctx._SUBTRACTION.text))
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 193
                self.term()
                self.state = 198
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._MULTIPLICATION = None # Token
            self._DIVISION = None # Token

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lowParser.FactorContext)
            else:
                return self.getTypedRuleContext(lowParser.FactorContext,i)


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
            return lowParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)




    def term(self):

        localctx = lowParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.factor()
            compiler.check_for_mult_or_div()
            self.state = 210
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==lowParser.MULTIPLICATION or _la==lowParser.DIVISION:
                self.state = 205
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [lowParser.MULTIPLICATION]:
                    self.state = 201
                    localctx._MULTIPLICATION = self.match(lowParser.MULTIPLICATION)
                    compiler.add_operator((None if localctx._MULTIPLICATION is None else localctx._MULTIPLICATION.text))
                    pass
                elif token in [lowParser.DIVISION]:
                    self.state = 203
                    localctx._DIVISION = self.match(lowParser.DIVISION)
                    compiler.add_operator((None if localctx._DIVISION is None else localctx._DIVISION.text))
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 207
                self.factor()
                self.state = 212
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_PARENTHESIS(self):
            return self.getToken(lowParser.LEFT_PARENTHESIS, 0)

        def expresions(self):
            return self.getTypedRuleContext(lowParser.ExpresionsContext,0)


        def RIGHT_PARENTHESIS(self):
            return self.getToken(lowParser.RIGHT_PARENTHESIS, 0)

        def VAR_NAME(self):
            return self.getToken(lowParser.VAR_NAME, 0)

        def multiple_expresions(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lowParser.Multiple_expresionsContext)
            else:
                return self.getTypedRuleContext(lowParser.Multiple_expresionsContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(lowParser.COMMA)
            else:
                return self.getToken(lowParser.COMMA, i)

        def indexvariable(self):
            return self.getTypedRuleContext(lowParser.IndexvariableContext,0)


        def constant(self):
            return self.getTypedRuleContext(lowParser.ConstantContext,0)


        def getRuleIndex(self):
            return lowParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)




    def factor(self):

        localctx = lowParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.state = 236
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 213
                self.match(lowParser.LEFT_PARENTHESIS)
                compiler.left_parenthesis()
                self.state = 215
                self.expresions()
                self.state = 216
                self.match(lowParser.RIGHT_PARENTHESIS)
                compiler.right_parenthesis()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 219
                self.match(lowParser.VAR_NAME)
                self.state = 220
                self.match(lowParser.LEFT_PARENTHESIS)
                compiler.left_parenthesis()
                self.state = 230
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << lowParser.LEFT_PARENTHESIS) | (1 << lowParser.STRING_CONSTANT) | (1 << lowParser.CHAR_CONSTANT) | (1 << lowParser.INT_CONSTANT) | (1 << lowParser.FLOAT_CONSTANT) | (1 << lowParser.BOOL_CONSTANT) | (1 << lowParser.VAR_NAME))) != 0):
                    self.state = 222
                    self.multiple_expresions()
                    self.state = 227
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==lowParser.COMMA:
                        self.state = 223
                        self.match(lowParser.COMMA)
                        self.state = 224
                        self.multiple_expresions()
                        self.state = 229
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 232
                self.match(lowParser.RIGHT_PARENTHESIS)
                compiler.right_parenthesis()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 234
                self.indexvariable()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 235
                self.constant()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatuteContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lowParser.AssignationContext)
            else:
                return self.getTypedRuleContext(lowParser.AssignationContext,i)


        def voidcall(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lowParser.VoidcallContext)
            else:
                return self.getTypedRuleContext(lowParser.VoidcallContext,i)


        def returncall(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lowParser.ReturncallContext)
            else:
                return self.getTypedRuleContext(lowParser.ReturncallContext,i)


        def read(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lowParser.ReadContext)
            else:
                return self.getTypedRuleContext(lowParser.ReadContext,i)


        def write(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lowParser.WriteContext)
            else:
                return self.getTypedRuleContext(lowParser.WriteContext,i)


        def conditional(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lowParser.ConditionalContext)
            else:
                return self.getTypedRuleContext(lowParser.ConditionalContext,i)


        def whileloop(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lowParser.WhileloopContext)
            else:
                return self.getTypedRuleContext(lowParser.WhileloopContext,i)


        def fromloop(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lowParser.FromloopContext)
            else:
                return self.getTypedRuleContext(lowParser.FromloopContext,i)


        def getRuleIndex(self):
            return lowParser.RULE_statute

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatute" ):
                listener.enterStatute(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatute" ):
                listener.exitStatute(self)




    def statute(self):

        localctx = lowParser.StatuteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_statute)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << lowParser.RETURN) | (1 << lowParser.INPUT) | (1 << lowParser.OUTPUT) | (1 << lowParser.IF) | (1 << lowParser.WHILE) | (1 << lowParser.FROM) | (1 << lowParser.VAR_NAME))) != 0):
                self.state = 246
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                if la_ == 1:
                    self.state = 238
                    self.assignation()
                    pass

                elif la_ == 2:
                    self.state = 239
                    self.voidcall()
                    pass

                elif la_ == 3:
                    self.state = 240
                    self.returncall()
                    pass

                elif la_ == 4:
                    self.state = 241
                    self.read()
                    pass

                elif la_ == 5:
                    self.state = 242
                    self.write()
                    pass

                elif la_ == 6:
                    self.state = 243
                    self.conditional()
                    pass

                elif la_ == 7:
                    self.state = 244
                    self.whileloop()
                    pass

                elif la_ == 8:
                    self.state = 245
                    self.fromloop()
                    pass


                self.state = 250
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

        def VAR_NAME(self):
            return self.getToken(lowParser.VAR_NAME, 0)

        def ASSIGN(self):
            return self.getToken(lowParser.ASSIGN, 0)

        def expresions(self):
            return self.getTypedRuleContext(lowParser.ExpresionsContext,0)


        def SEMICOLON(self):
            return self.getToken(lowParser.SEMICOLON, 0)

        def LEFT_BRACKET(self):
            return self.getToken(lowParser.LEFT_BRACKET, 0)

        def multiple_expresions(self):
            return self.getTypedRuleContext(lowParser.Multiple_expresionsContext,0)


        def RIGHT_BRACKET(self):
            return self.getToken(lowParser.RIGHT_BRACKET, 0)

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
        self.enterRule(localctx, 32, self.RULE_assignation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.match(lowParser.VAR_NAME)
            self.state = 256
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==lowParser.LEFT_BRACKET:
                self.state = 252
                self.match(lowParser.LEFT_BRACKET)
                self.state = 253
                self.multiple_expresions()
                self.state = 254
                self.match(lowParser.RIGHT_BRACKET)


            self.state = 258
            self.match(lowParser.ASSIGN)
            self.state = 259
            self.expresions()
            self.state = 260
            self.match(lowParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VoidcallContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR_NAME(self):
            return self.getToken(lowParser.VAR_NAME, 0)

        def LEFT_PARENTHESIS(self):
            return self.getToken(lowParser.LEFT_PARENTHESIS, 0)

        def RIGHT_PARENTHESIS(self):
            return self.getToken(lowParser.RIGHT_PARENTHESIS, 0)

        def SEMICOLON(self):
            return self.getToken(lowParser.SEMICOLON, 0)

        def multiple_expresions(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lowParser.Multiple_expresionsContext)
            else:
                return self.getTypedRuleContext(lowParser.Multiple_expresionsContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(lowParser.COMMA)
            else:
                return self.getToken(lowParser.COMMA, i)

        def getRuleIndex(self):
            return lowParser.RULE_voidcall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVoidcall" ):
                listener.enterVoidcall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVoidcall" ):
                listener.exitVoidcall(self)




    def voidcall(self):

        localctx = lowParser.VoidcallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_voidcall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self.match(lowParser.VAR_NAME)
            self.state = 263
            self.match(lowParser.LEFT_PARENTHESIS)
            self.state = 272
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << lowParser.LEFT_PARENTHESIS) | (1 << lowParser.STRING_CONSTANT) | (1 << lowParser.CHAR_CONSTANT) | (1 << lowParser.INT_CONSTANT) | (1 << lowParser.FLOAT_CONSTANT) | (1 << lowParser.BOOL_CONSTANT) | (1 << lowParser.VAR_NAME))) != 0):
                self.state = 264
                self.multiple_expresions()
                self.state = 269
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==lowParser.COMMA:
                    self.state = 265
                    self.match(lowParser.COMMA)
                    self.state = 266
                    self.multiple_expresions()
                    self.state = 271
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 274
            self.match(lowParser.RIGHT_PARENTHESIS)
            self.state = 275
            self.match(lowParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturncallContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(lowParser.RETURN, 0)

        def LEFT_PARENTHESIS(self):
            return self.getToken(lowParser.LEFT_PARENTHESIS, 0)

        def expresions(self):
            return self.getTypedRuleContext(lowParser.ExpresionsContext,0)


        def RIGHT_PARENTHESIS(self):
            return self.getToken(lowParser.RIGHT_PARENTHESIS, 0)

        def SEMICOLON(self):
            return self.getToken(lowParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return lowParser.RULE_returncall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturncall" ):
                listener.enterReturncall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturncall" ):
                listener.exitReturncall(self)




    def returncall(self):

        localctx = lowParser.ReturncallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_returncall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self.match(lowParser.RETURN)
            self.state = 278
            self.match(lowParser.LEFT_PARENTHESIS)
            self.state = 279
            self.expresions()
            self.state = 280
            self.match(lowParser.RIGHT_PARENTHESIS)
            self.state = 281
            self.match(lowParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexvariableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR_NAME(self):
            return self.getToken(lowParser.VAR_NAME, 0)

        def LEFT_BRACKET(self):
            return self.getToken(lowParser.LEFT_BRACKET, 0)

        def multiple_expresions(self):
            return self.getTypedRuleContext(lowParser.Multiple_expresionsContext,0)


        def RIGHT_BRACKET(self):
            return self.getToken(lowParser.RIGHT_BRACKET, 0)

        def getRuleIndex(self):
            return lowParser.RULE_indexvariable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIndexvariable" ):
                listener.enterIndexvariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIndexvariable" ):
                listener.exitIndexvariable(self)




    def indexvariable(self):

        localctx = lowParser.IndexvariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_indexvariable)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            self.match(lowParser.VAR_NAME)
            self.state = 288
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==lowParser.LEFT_BRACKET:
                self.state = 284
                self.match(lowParser.LEFT_BRACKET)
                self.state = 285
                self.multiple_expresions()
                self.state = 286
                self.match(lowParser.RIGHT_BRACKET)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReadContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INPUT(self):
            return self.getToken(lowParser.INPUT, 0)

        def LEFT_PARENTHESIS(self):
            return self.getToken(lowParser.LEFT_PARENTHESIS, 0)

        def indexvariable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lowParser.IndexvariableContext)
            else:
                return self.getTypedRuleContext(lowParser.IndexvariableContext,i)


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
            return lowParser.RULE_read

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRead" ):
                listener.enterRead(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRead" ):
                listener.exitRead(self)




    def read(self):

        localctx = lowParser.ReadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_read)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 290
            self.match(lowParser.INPUT)
            self.state = 291
            self.match(lowParser.LEFT_PARENTHESIS)
            self.state = 292
            self.indexvariable()
            self.state = 297
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==lowParser.COMMA:
                self.state = 293
                self.match(lowParser.COMMA)
                self.state = 294
                self.indexvariable()
                self.state = 299
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 300
            self.match(lowParser.RIGHT_PARENTHESIS)
            self.state = 301
            self.match(lowParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WriteContext(ParserRuleContext):

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

        def expresions(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lowParser.ExpresionsContext)
            else:
                return self.getTypedRuleContext(lowParser.ExpresionsContext,i)


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
            return lowParser.RULE_write

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWrite" ):
                listener.enterWrite(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWrite" ):
                listener.exitWrite(self)




    def write(self):

        localctx = lowParser.WriteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_write)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.match(lowParser.OUTPUT)
            self.state = 304
            self.match(lowParser.LEFT_PARENTHESIS)
            self.state = 307
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 305
                self.expresions()
                pass

            elif la_ == 2:
                self.state = 306
                self.match(lowParser.STRING_CONSTANT)
                pass


            self.state = 316
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==lowParser.COMMA:
                self.state = 309
                self.match(lowParser.COMMA)
                self.state = 312
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
                if la_ == 1:
                    self.state = 310
                    self.expresions()
                    pass

                elif la_ == 2:
                    self.state = 311
                    self.match(lowParser.STRING_CONSTANT)
                    pass


                self.state = 318
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 319
            self.match(lowParser.RIGHT_PARENTHESIS)
            self.state = 320
            self.match(lowParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionalContext(ParserRuleContext):

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

        def multiple_expresions(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lowParser.Multiple_expresionsContext)
            else:
                return self.getTypedRuleContext(lowParser.Multiple_expresionsContext,i)


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

        def statute(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lowParser.StatuteContext)
            else:
                return self.getTypedRuleContext(lowParser.StatuteContext,i)


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
            return lowParser.RULE_conditional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditional" ):
                listener.enterConditional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditional" ):
                listener.exitConditional(self)




    def conditional(self):

        localctx = lowParser.ConditionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_conditional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 322
            self.match(lowParser.IF)
            self.state = 323
            self.match(lowParser.LEFT_PARENTHESIS)
            self.state = 324
            self.multiple_expresions()
            self.state = 325
            self.match(lowParser.RIGHT_PARENTHESIS)
            self.state = 326
            self.match(lowParser.THEN)
            self.state = 327
            self.match(lowParser.LEFT_CURLY)
            self.state = 328
            self.statute()
            self.state = 329
            self.match(lowParser.RIGHT_CURLY)
            self.state = 339
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==lowParser.ELSE_IF:
                self.state = 330
                self.match(lowParser.ELSE_IF)
                self.state = 331
                self.match(lowParser.LEFT_PARENTHESIS)
                self.state = 332
                self.multiple_expresions()
                self.state = 333
                self.match(lowParser.RIGHT_PARENTHESIS)
                self.state = 334
                self.match(lowParser.THEN)
                self.state = 335
                self.match(lowParser.LEFT_CURLY)
                self.state = 336
                self.statute()
                self.state = 337
                self.match(lowParser.RIGHT_CURLY)


            self.state = 346
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==lowParser.ELSE:
                self.state = 341
                self.match(lowParser.ELSE)
                self.state = 342
                self.match(lowParser.LEFT_CURLY)
                self.state = 343
                self.statute()
                self.state = 344
                self.match(lowParser.RIGHT_CURLY)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileloopContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(lowParser.WHILE, 0)

        def LEFT_PARENTHESIS(self):
            return self.getToken(lowParser.LEFT_PARENTHESIS, 0)

        def multiple_expresions(self):
            return self.getTypedRuleContext(lowParser.Multiple_expresionsContext,0)


        def RIGHT_PARENTHESIS(self):
            return self.getToken(lowParser.RIGHT_PARENTHESIS, 0)

        def DO(self):
            return self.getToken(lowParser.DO, 0)

        def LEFT_CURLY(self):
            return self.getToken(lowParser.LEFT_CURLY, 0)

        def statute(self):
            return self.getTypedRuleContext(lowParser.StatuteContext,0)


        def RIGHT_CURLY(self):
            return self.getToken(lowParser.RIGHT_CURLY, 0)

        def getRuleIndex(self):
            return lowParser.RULE_whileloop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileloop" ):
                listener.enterWhileloop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileloop" ):
                listener.exitWhileloop(self)




    def whileloop(self):

        localctx = lowParser.WhileloopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_whileloop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 348
            self.match(lowParser.WHILE)
            self.state = 349
            self.match(lowParser.LEFT_PARENTHESIS)
            self.state = 350
            self.multiple_expresions()
            self.state = 351
            self.match(lowParser.RIGHT_PARENTHESIS)
            self.state = 352
            self.match(lowParser.DO)
            self.state = 353
            self.match(lowParser.LEFT_CURLY)
            self.state = 354
            self.statute()
            self.state = 355
            self.match(lowParser.RIGHT_CURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FromloopContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FROM(self):
            return self.getToken(lowParser.FROM, 0)

        def VAR_NAME(self):
            return self.getToken(lowParser.VAR_NAME, 0)

        def ASSIGN(self):
            return self.getToken(lowParser.ASSIGN, 0)

        def multiple_expresions(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lowParser.Multiple_expresionsContext)
            else:
                return self.getTypedRuleContext(lowParser.Multiple_expresionsContext,i)


        def TO(self):
            return self.getToken(lowParser.TO, 0)

        def DO(self):
            return self.getToken(lowParser.DO, 0)

        def LEFT_CURLY(self):
            return self.getToken(lowParser.LEFT_CURLY, 0)

        def statute(self):
            return self.getTypedRuleContext(lowParser.StatuteContext,0)


        def RIGHT_CURLY(self):
            return self.getToken(lowParser.RIGHT_CURLY, 0)

        def indexvariable(self):
            return self.getTypedRuleContext(lowParser.IndexvariableContext,0)


        def getRuleIndex(self):
            return lowParser.RULE_fromloop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFromloop" ):
                listener.enterFromloop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFromloop" ):
                listener.exitFromloop(self)




    def fromloop(self):

        localctx = lowParser.FromloopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_fromloop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
            self.match(lowParser.FROM)
            self.state = 358
            self.match(lowParser.VAR_NAME)
            self.state = 360
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==lowParser.VAR_NAME:
                self.state = 359
                self.indexvariable()


            self.state = 362
            self.match(lowParser.ASSIGN)
            self.state = 363
            self.multiple_expresions()
            self.state = 364
            self.match(lowParser.TO)
            self.state = 365
            self.multiple_expresions()
            self.state = 366
            self.match(lowParser.DO)
            self.state = 367
            self.match(lowParser.LEFT_CURLY)
            self.state = 368
            self.statute()
            self.state = 369
            self.match(lowParser.RIGHT_CURLY)
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

        def statute(self):
            return self.getTypedRuleContext(lowParser.StatuteContext,0)


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
        self.enterRule(localctx, 50, self.RULE_main_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 371
            self.match(lowParser.MAIN)
            self.state = 372
            self.match(lowParser.LEFT_PARENTHESIS)
            self.state = 373
            self.match(lowParser.RIGHT_PARENTHESIS)
            self.state = 374
            self.match(lowParser.LEFT_CURLY)
            self.state = 375
            self.statute()
            self.state = 376
            self.match(lowParser.RIGHT_CURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





