# Generated from Chipy8.g4 by ANTLR 4.5.1
from antlr4 import *
from io import StringIO


from antlr4.Token import CommonToken
import re
import importlib

# Allow languages to extend the lexer and parser, by loading the parser dinamically
module_path = __name__[:-5]
language_name = __name__.split('.')[-1]
language_name = language_name[:-5]  # Remove Lexer from name
LanguageParser = getattr(importlib.import_module('{}Parser'.format(module_path)), '{}Parser'.format(language_name))


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2A")
        buf.write("\u01d5\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\3\2\3\2\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3")
        buf.write("\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b")
        buf.write("\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16")
        buf.write("\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\5\23\u00ec\n")
        buf.write("\23\3\23\3\23\5\23\u00f0\n\23\3\23\5\23\u00f3\n\23\5\23")
        buf.write("\u00f5\n\23\3\23\3\23\3\24\3\24\7\24\u00fb\n\24\f\24\16")
        buf.write("\24\u00fe\13\24\3\25\3\25\7\25\u0102\n\25\f\25\16\25\u0105")
        buf.write("\13\25\3\25\6\25\u0108\n\25\r\25\16\25\u0109\5\25\u010c")
        buf.write("\n\25\3\26\3\26\3\26\6\26\u0111\n\26\r\26\16\26\u0112")
        buf.write("\3\27\3\27\3\27\6\27\u0118\n\27\r\27\16\27\u0119\3\30")
        buf.write("\3\30\3\30\6\30\u011f\n\30\r\30\16\30\u0120\3\31\3\31")
        buf.write("\3\31\3\32\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36")
        buf.write("\3\36\3\37\3\37\3\37\3 \3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3")
        buf.write("$\3$\3%\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3")
        buf.write("+\3,\3,\3,\3-\3-\3.\3.\3/\3/\3/\3\60\3\60\3\60\3\61\3")
        buf.write("\61\3\61\3\62\3\62\3\62\3\63\3\63\3\63\3\64\3\64\3\64")
        buf.write("\3\65\3\65\3\65\3\66\3\66\3\66\3\67\3\67\3\67\38\38\3")
        buf.write("8\39\39\39\3:\3:\3:\3;\3;\3;\3<\3<\3<\3=\3=\3=\3=\3>\3")
        buf.write(">\3>\3>\3?\3?\3?\5?\u018c\n?\3?\3?\3@\3@\3A\3A\3A\7A\u0195")
        buf.write("\nA\fA\16A\u0198\13A\3A\3A\3A\3A\7A\u019e\nA\fA\16A\u01a1")
        buf.write("\13A\3A\5A\u01a4\nA\3B\3B\3B\3C\3C\3D\3D\3E\3E\3F\3F\3")
        buf.write("G\3G\3H\6H\u01b4\nH\rH\16H\u01b5\3I\6I\u01b9\nI\rI\16")
        buf.write("I\u01ba\3J\3J\7J\u01bf\nJ\fJ\16J\u01c2\13J\3K\3K\5K\u01c6")
        buf.write("\nK\3K\5K\u01c9\nK\3K\3K\5K\u01cd\nK\3L\5L\u01d0\nL\3")
        buf.write("M\3M\5M\u01d4\nM\2\2N\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24")
        buf.write("\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37")
        buf.write("= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64")
        buf.write("g\65i\66k\67m8o9q:s;u<w=y>{?}@\177A\u0081\2\u0083\2\u0085")
        buf.write("\2\u0087\2\u0089\2\u008b\2\u008d\2\u008f\2\u0091\2\u0093")
        buf.write("\2\u0095\2\u0097\2\u0099\2\3\2\17\4\2QQqq\4\2ZZzz\4\2")
        buf.write("DDdd\6\2\f\f\17\17))^^\6\2\f\f\17\17$$^^\3\2\63;\3\2\62")
        buf.write(";\3\2\629\5\2\62;CHch\3\2\62\63\4\2\13\13\"\"\4\2\f\f")
        buf.write("\17\17\5\2C\\aac|\u01e0\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3")
        buf.write("\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2")
        buf.write("\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2")
        buf.write("\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2")
        buf.write("!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2")
        buf.write("\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3")
        buf.write("\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2")
        buf.write("\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2")
        buf.write("\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2")
        buf.write("\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3")
        buf.write("\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c")
        buf.write("\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2")
        buf.write("m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2")
        buf.write("\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2")
        buf.write("\2\2\3\u009b\3\2\2\2\5\u009d\3\2\2\2\7\u00a0\3\2\2\2\t")
        buf.write("\u00a4\3\2\2\2\13\u00a7\3\2\2\2\r\u00ab\3\2\2\2\17\u00b2")
        buf.write("\3\2\2\2\21\u00b5\3\2\2\2\23\u00ba\3\2\2\2\25\u00bf\3")
        buf.write("\2\2\2\27\u00c5\3\2\2\2\31\u00c8\3\2\2\2\33\u00cc\3\2")
        buf.write("\2\2\35\u00d0\3\2\2\2\37\u00d4\3\2\2\2!\u00d9\3\2\2\2")
        buf.write("#\u00e2\3\2\2\2%\u00f4\3\2\2\2\'\u00f8\3\2\2\2)\u010b")
        buf.write("\3\2\2\2+\u010d\3\2\2\2-\u0114\3\2\2\2/\u011b\3\2\2\2")
        buf.write("\61\u0122\3\2\2\2\63\u0125\3\2\2\2\65\u0128\3\2\2\2\67")
        buf.write("\u012a\3\2\2\29\u012c\3\2\2\2;\u012e\3\2\2\2=\u0130\3")
        buf.write("\2\2\2?\u0133\3\2\2\2A\u0136\3\2\2\2C\u0138\3\2\2\2E\u013a")
        buf.write("\3\2\2\2G\u013c\3\2\2\2I\u013f\3\2\2\2K\u0142\3\2\2\2")
        buf.write("M\u0144\3\2\2\2O\u0146\3\2\2\2Q\u0148\3\2\2\2S\u014a\3")
        buf.write("\2\2\2U\u014c\3\2\2\2W\u014f\3\2\2\2Y\u0152\3\2\2\2[\u0154")
        buf.write("\3\2\2\2]\u0156\3\2\2\2_\u0159\3\2\2\2a\u015c\3\2\2\2")
        buf.write("c\u015f\3\2\2\2e\u0162\3\2\2\2g\u0165\3\2\2\2i\u0168\3")
        buf.write("\2\2\2k\u016b\3\2\2\2m\u016e\3\2\2\2o\u0171\3\2\2\2q\u0174")
        buf.write("\3\2\2\2s\u0177\3\2\2\2u\u017a\3\2\2\2w\u017d\3\2\2\2")
        buf.write("y\u0180\3\2\2\2{\u0184\3\2\2\2}\u018b\3\2\2\2\177\u018f")
        buf.write("\3\2\2\2\u0081\u01a3\3\2\2\2\u0083\u01a5\3\2\2\2\u0085")
        buf.write("\u01a8\3\2\2\2\u0087\u01aa\3\2\2\2\u0089\u01ac\3\2\2\2")
        buf.write("\u008b\u01ae\3\2\2\2\u008d\u01b0\3\2\2\2\u008f\u01b3\3")
        buf.write("\2\2\2\u0091\u01b8\3\2\2\2\u0093\u01bc\3\2\2\2\u0095\u01c3")
        buf.write("\3\2\2\2\u0097\u01cf\3\2\2\2\u0099\u01d3\3\2\2\2\u009b")
        buf.write("\u009c\7,\2\2\u009c\4\3\2\2\2\u009d\u009e\7,\2\2\u009e")
        buf.write("\u009f\7,\2\2\u009f\6\3\2\2\2\u00a0\u00a1\7,\2\2\u00a1")
        buf.write("\u00a2\7,\2\2\u00a2\u00a3\7?\2\2\u00a3\b\3\2\2\2\u00a4")
        buf.write("\u00a5\7\61\2\2\u00a5\u00a6\7\61\2\2\u00a6\n\3\2\2\2\u00a7")
        buf.write("\u00a8\7f\2\2\u00a8\u00a9\7g\2\2\u00a9\u00aa\7h\2\2\u00aa")
        buf.write("\f\3\2\2\2\u00ab\u00ac\7t\2\2\u00ac\u00ad\7g\2\2\u00ad")
        buf.write("\u00ae\7v\2\2\u00ae\u00af\7w\2\2\u00af\u00b0\7t\2\2\u00b0")
        buf.write("\u00b1\7p\2\2\u00b1\16\3\2\2\2\u00b2\u00b3\7k\2\2\u00b3")
        buf.write("\u00b4\7h\2\2\u00b4\20\3\2\2\2\u00b5\u00b6\7g\2\2\u00b6")
        buf.write("\u00b7\7n\2\2\u00b7\u00b8\7k\2\2\u00b8\u00b9\7h\2\2\u00b9")
        buf.write("\22\3\2\2\2\u00ba\u00bb\7g\2\2\u00bb\u00bc\7n\2\2\u00bc")
        buf.write("\u00bd\7u\2\2\u00bd\u00be\7g\2\2\u00be\24\3\2\2\2\u00bf")
        buf.write("\u00c0\7y\2\2\u00c0\u00c1\7j\2\2\u00c1\u00c2\7k\2\2\u00c2")
        buf.write("\u00c3\7n\2\2\u00c3\u00c4\7g\2\2\u00c4\26\3\2\2\2\u00c5")
        buf.write("\u00c6\7q\2\2\u00c6\u00c7\7t\2\2\u00c7\30\3\2\2\2\u00c8")
        buf.write("\u00c9\7c\2\2\u00c9\u00ca\7p\2\2\u00ca\u00cb\7f\2\2\u00cb")
        buf.write("\32\3\2\2\2\u00cc\u00cd\7p\2\2\u00cd\u00ce\7q\2\2\u00ce")
        buf.write("\u00cf\7v\2\2\u00cf\34\3\2\2\2\u00d0\u00d1\7f\2\2\u00d1")
        buf.write("\u00d2\7g\2\2\u00d2\u00d3\7n\2\2\u00d3\36\3\2\2\2\u00d4")
        buf.write("\u00d5\7r\2\2\u00d5\u00d6\7c\2\2\u00d6\u00d7\7u\2\2\u00d7")
        buf.write("\u00d8\7u\2\2\u00d8 \3\2\2\2\u00d9\u00da\7e\2\2\u00da")
        buf.write("\u00db\7q\2\2\u00db\u00dc\7p\2\2\u00dc\u00dd\7v\2\2\u00dd")
        buf.write("\u00de\7k\2\2\u00de\u00df\7p\2\2\u00df\u00e0\7w\2\2\u00e0")
        buf.write("\u00e1\7g\2\2\u00e1\"\3\2\2\2\u00e2\u00e3\7d\2\2\u00e3")
        buf.write("\u00e4\7t\2\2\u00e4\u00e5\7g\2\2\u00e5\u00e6\7c\2\2\u00e6")
        buf.write("\u00e7\7m\2\2\u00e7$\3\2\2\2\u00e8\u00e9\6\23\2\2\u00e9")
        buf.write("\u00f5\5\u0091I\2\u00ea\u00ec\7\17\2\2\u00eb\u00ea\3\2")
        buf.write("\2\2\u00eb\u00ec\3\2\2\2\u00ec\u00ed\3\2\2\2\u00ed\u00f0")
        buf.write("\7\f\2\2\u00ee\u00f0\7\17\2\2\u00ef\u00eb\3\2\2\2\u00ef")
        buf.write("\u00ee\3\2\2\2\u00f0\u00f2\3\2\2\2\u00f1\u00f3\5\u0091")
        buf.write("I\2\u00f2\u00f1\3\2\2\2\u00f2\u00f3\3\2\2\2\u00f3\u00f5")
        buf.write("\3\2\2\2\u00f4\u00e8\3\2\2\2\u00f4\u00ef\3\2\2\2\u00f5")
        buf.write("\u00f6\3\2\2\2\u00f6\u00f7\b\23\2\2\u00f7&\3\2\2\2\u00f8")
        buf.write("\u00fc\5\u0097L\2\u00f9\u00fb\5\u0099M\2\u00fa\u00f9\3")
        buf.write("\2\2\2\u00fb\u00fe\3\2\2\2\u00fc\u00fa\3\2\2\2\u00fc\u00fd")
        buf.write("\3\2\2\2\u00fd(\3\2\2\2\u00fe\u00fc\3\2\2\2\u00ff\u0103")
        buf.write("\5\u0085C\2\u0100\u0102\5\u0087D\2\u0101\u0100\3\2\2\2")
        buf.write("\u0102\u0105\3\2\2\2\u0103\u0101\3\2\2\2\u0103\u0104\3")
        buf.write("\2\2\2\u0104\u010c\3\2\2\2\u0105\u0103\3\2\2\2\u0106\u0108")
        buf.write("\7\62\2\2\u0107\u0106\3\2\2\2\u0108\u0109\3\2\2\2\u0109")
        buf.write("\u0107\3\2\2\2\u0109\u010a\3\2\2\2\u010a\u010c\3\2\2\2")
        buf.write("\u010b\u00ff\3\2\2\2\u010b\u0107\3\2\2\2\u010c*\3\2\2")
        buf.write("\2\u010d\u010e\7\62\2\2\u010e\u0110\t\2\2\2\u010f\u0111")
        buf.write("\5\u0089E\2\u0110\u010f\3\2\2\2\u0111\u0112\3\2\2\2\u0112")
        buf.write("\u0110\3\2\2\2\u0112\u0113\3\2\2\2\u0113,\3\2\2\2\u0114")
        buf.write("\u0115\7\62\2\2\u0115\u0117\t\3\2\2\u0116\u0118\5\u008b")
        buf.write("F\2\u0117\u0116\3\2\2\2\u0118\u0119\3\2\2\2\u0119\u0117")
        buf.write("\3\2\2\2\u0119\u011a\3\2\2\2\u011a.\3\2\2\2\u011b\u011c")
        buf.write("\7\62\2\2\u011c\u011e\t\4\2\2\u011d\u011f\5\u008dG\2\u011e")
        buf.write("\u011d\3\2\2\2\u011f\u0120\3\2\2\2\u0120\u011e\3\2\2\2")
        buf.write("\u0120\u0121\3\2\2\2\u0121\60\3\2\2\2\u0122\u0123\7*\2")
        buf.write("\2\u0123\u0124\b\31\3\2\u0124\62\3\2\2\2\u0125\u0126\7")
        buf.write("+\2\2\u0126\u0127\b\32\4\2\u0127\64\3\2\2\2\u0128\u0129")
        buf.write("\7.\2\2\u0129\66\3\2\2\2\u012a\u012b\7<\2\2\u012b8\3\2")
        buf.write("\2\2\u012c\u012d\7=\2\2\u012d:\3\2\2\2\u012e\u012f\7?")
        buf.write("\2\2\u012f<\3\2\2\2\u0130\u0131\7]\2\2\u0131\u0132\b\37")
        buf.write("\5\2\u0132>\3\2\2\2\u0133\u0134\7_\2\2\u0134\u0135\b ")
        buf.write("\6\2\u0135@\3\2\2\2\u0136\u0137\7~\2\2\u0137B\3\2\2\2")
        buf.write("\u0138\u0139\7`\2\2\u0139D\3\2\2\2\u013a\u013b\7(\2\2")
        buf.write("\u013bF\3\2\2\2\u013c\u013d\7>\2\2\u013d\u013e\7>\2\2")
        buf.write("\u013eH\3\2\2\2\u013f\u0140\7@\2\2\u0140\u0141\7@\2\2")
        buf.write("\u0141J\3\2\2\2\u0142\u0143\7-\2\2\u0143L\3\2\2\2\u0144")
        buf.write("\u0145\7/\2\2\u0145N\3\2\2\2\u0146\u0147\7\61\2\2\u0147")
        buf.write("P\3\2\2\2\u0148\u0149\7\'\2\2\u0149R\3\2\2\2\u014a\u014b")
        buf.write("\7\u0080\2\2\u014bT\3\2\2\2\u014c\u014d\7}\2\2\u014d\u014e")
        buf.write("\b+\7\2\u014eV\3\2\2\2\u014f\u0150\7\177\2\2\u0150\u0151")
        buf.write("\b,\b\2\u0151X\3\2\2\2\u0152\u0153\7>\2\2\u0153Z\3\2\2")
        buf.write("\2\u0154\u0155\7@\2\2\u0155\\\3\2\2\2\u0156\u0157\7?\2")
        buf.write("\2\u0157\u0158\7?\2\2\u0158^\3\2\2\2\u0159\u015a\7@\2")
        buf.write("\2\u015a\u015b\7?\2\2\u015b`\3\2\2\2\u015c\u015d\7>\2")
        buf.write("\2\u015d\u015e\7?\2\2\u015eb\3\2\2\2\u015f\u0160\7>\2")
        buf.write("\2\u0160\u0161\7@\2\2\u0161d\3\2\2\2\u0162\u0163\7#\2")
        buf.write("\2\u0163\u0164\7?\2\2\u0164f\3\2\2\2\u0165\u0166\7/\2")
        buf.write("\2\u0166\u0167\7@\2\2\u0167h\3\2\2\2\u0168\u0169\7-\2")
        buf.write("\2\u0169\u016a\7?\2\2\u016aj\3\2\2\2\u016b\u016c\7/\2")
        buf.write("\2\u016c\u016d\7?\2\2\u016dl\3\2\2\2\u016e\u016f\7,\2")
        buf.write("\2\u016f\u0170\7?\2\2\u0170n\3\2\2\2\u0171\u0172\7\61")
        buf.write("\2\2\u0172\u0173\7?\2\2\u0173p\3\2\2\2\u0174\u0175\7\'")
        buf.write("\2\2\u0175\u0176\7?\2\2\u0176r\3\2\2\2\u0177\u0178\7(")
        buf.write("\2\2\u0178\u0179\7?\2\2\u0179t\3\2\2\2\u017a\u017b\7~")
        buf.write("\2\2\u017b\u017c\7?\2\2\u017cv\3\2\2\2\u017d\u017e\7`")
        buf.write("\2\2\u017e\u017f\7?\2\2\u017fx\3\2\2\2\u0180\u0181\7>")
        buf.write("\2\2\u0181\u0182\7>\2\2\u0182\u0183\7?\2\2\u0183z\3\2")
        buf.write("\2\2\u0184\u0185\7@\2\2\u0185\u0186\7@\2\2\u0186\u0187")
        buf.write("\7?\2\2\u0187|\3\2\2\2\u0188\u018c\5\u0091I\2\u0189\u018c")
        buf.write("\5\u0093J\2\u018a\u018c\5\u0095K\2\u018b\u0188\3\2\2\2")
        buf.write("\u018b\u0189\3\2\2\2\u018b\u018a\3\2\2\2\u018c\u018d\3")
        buf.write("\2\2\2\u018d\u018e\b?\t\2\u018e~\3\2\2\2\u018f\u0190\13")
        buf.write("\2\2\2\u0190\u0080\3\2\2\2\u0191\u0196\7)\2\2\u0192\u0195")
        buf.write("\5\u0083B\2\u0193\u0195\n\5\2\2\u0194\u0192\3\2\2\2\u0194")
        buf.write("\u0193\3\2\2\2\u0195\u0198\3\2\2\2\u0196\u0194\3\2\2\2")
        buf.write("\u0196\u0197\3\2\2\2\u0197\u0199\3\2\2\2\u0198\u0196\3")
        buf.write("\2\2\2\u0199\u01a4\7)\2\2\u019a\u019f\7$\2\2\u019b\u019e")
        buf.write("\5\u0083B\2\u019c\u019e\n\6\2\2\u019d\u019b\3\2\2\2\u019d")
        buf.write("\u019c\3\2\2\2\u019e\u01a1\3\2\2\2\u019f\u019d\3\2\2\2")
        buf.write("\u019f\u01a0\3\2\2\2\u01a0\u01a2\3\2\2\2\u01a1\u019f\3")
        buf.write("\2\2\2\u01a2\u01a4\7$\2\2\u01a3\u0191\3\2\2\2\u01a3\u019a")
        buf.write("\3\2\2\2\u01a4\u0082\3\2\2\2\u01a5\u01a6\7^\2\2\u01a6")
        buf.write("\u01a7\13\2\2\2\u01a7\u0084\3\2\2\2\u01a8\u01a9\t\7\2")
        buf.write("\2\u01a9\u0086\3\2\2\2\u01aa\u01ab\t\b\2\2\u01ab\u0088")
        buf.write("\3\2\2\2\u01ac\u01ad\t\t\2\2\u01ad\u008a\3\2\2\2\u01ae")
        buf.write("\u01af\t\n\2\2\u01af\u008c\3\2\2\2\u01b0\u01b1\t\13\2")
        buf.write("\2\u01b1\u008e\3\2\2\2\u01b2\u01b4\5\u0087D\2\u01b3\u01b2")
        buf.write("\3\2\2\2\u01b4\u01b5\3\2\2\2\u01b5\u01b3\3\2\2\2\u01b5")
        buf.write("\u01b6\3\2\2\2\u01b6\u0090\3\2\2\2\u01b7\u01b9\t\f\2\2")
        buf.write("\u01b8\u01b7\3\2\2\2\u01b9\u01ba\3\2\2\2\u01ba\u01b8\3")
        buf.write("\2\2\2\u01ba\u01bb\3\2\2\2\u01bb\u0092\3\2\2\2\u01bc\u01c0")
        buf.write("\7%\2\2\u01bd\u01bf\n\r\2\2\u01be\u01bd\3\2\2\2\u01bf")
        buf.write("\u01c2\3\2\2\2\u01c0\u01be\3\2\2\2\u01c0\u01c1\3\2\2\2")
        buf.write("\u01c1\u0094\3\2\2\2\u01c2\u01c0\3\2\2\2\u01c3\u01c5\7")
        buf.write("^\2\2\u01c4\u01c6\5\u0091I\2\u01c5\u01c4\3\2\2\2\u01c5")
        buf.write("\u01c6\3\2\2\2\u01c6\u01cc\3\2\2\2\u01c7\u01c9\7\17\2")
        buf.write("\2\u01c8\u01c7\3\2\2\2\u01c8\u01c9\3\2\2\2\u01c9\u01ca")
        buf.write("\3\2\2\2\u01ca\u01cd\7\f\2\2\u01cb\u01cd\7\17\2\2\u01cc")
        buf.write("\u01c8\3\2\2\2\u01cc\u01cb\3\2\2\2\u01cd\u0096\3\2\2\2")
        buf.write("\u01ce\u01d0\t\16\2\2\u01cf\u01ce\3\2\2\2\u01d0\u0098")
        buf.write("\3\2\2\2\u01d1\u01d4\5\u0097L\2\u01d2\u01d4\t\b\2\2\u01d3")
        buf.write("\u01d1\3\2\2\2\u01d3\u01d2\3\2\2\2\u01d4\u009a\3\2\2\2")
        buf.write("\34\2\u00eb\u00ef\u00f2\u00f4\u00fc\u0103\u0109\u010b")
        buf.write("\u0112\u0119\u0120\u018b\u0194\u0196\u019d\u019f\u01a3")
        buf.write("\u01b5\u01ba\u01c0\u01c5\u01c8\u01cc\u01cf\u01d3\n\3\23")
        buf.write("\2\3\31\3\3\32\4\3\37\5\3 \6\3+\7\3,\b\b\2\2")
        return buf.getvalue()


class Chipy8Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]


    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    DEF = 5
    RETURN = 6
    IF = 7
    ELIF = 8
    ELSE = 9
    WHILE = 10
    OR = 11
    AND = 12
    NOT = 13
    DEL = 14
    PASS = 15
    CONTINUE = 16
    BREAK = 17
    NEWLINE = 18
    NAME = 19
    DECIMAL_INTEGER = 20
    OCT_INTEGER = 21
    HEX_INTEGER = 22
    BIN_INTEGER = 23
    OPEN_PAREN = 24
    CLOSE_PAREN = 25
    COMMA = 26
    COLON = 27
    SEMI_COLON = 28
    ASSIGN = 29
    OPEN_BRACK = 30
    CLOSE_BRACK = 31
    OR_OP = 32
    XOR = 33
    AND_OP = 34
    LEFT_SHIFT = 35
    RIGHT_SHIFT = 36
    ADD = 37
    MINUS = 38
    DIV = 39
    MOD = 40
    NOT_OP = 41
    OPEN_BRACE = 42
    CLOSE_BRACE = 43
    LESS_THAN = 44
    GREATER_THAN = 45
    EQUALS = 46
    GT_EQ = 47
    LT_EQ = 48
    NOT_EQ_1 = 49
    NOT_EQ_2 = 50
    ARROW = 51
    ADD_ASSIGN = 52
    SUB_ASSIGN = 53
    MULT_ASSIGN = 54
    DIV_ASSIGN = 55
    MOD_ASSIGN = 56
    AND_ASSIGN = 57
    OR_ASSIGN = 58
    XOR_ASSIGN = 59
    LEFT_SHIFT_ASSIGN = 60
    RIGHT_SHIFT_ASSIGN = 61
    SKIP_ = 62
    UNKNOWN_CHAR = 63

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'*'", "'**'", "'**='", "'//'", "'def'", "'return'", "'if'", 
            "'elif'", "'else'", "'while'", "'or'", "'and'", "'not'", "'del'", 
            "'pass'", "'continue'", "'break'", "'('", "')'", "','", "':'", 
            "';'", "'='", "'['", "']'", "'|'", "'^'", "'&'", "'<<'", "'>>'", 
            "'+'", "'-'", "'/'", "'%'", "'~'", "'{'", "'}'", "'<'", "'>'", 
            "'=='", "'>='", "'<='", "'<>'", "'!='", "'->'", "'+='", "'-='", 
            "'*='", "'/='", "'%='", "'&='", "'|='", "'^='", "'<<='", "'>>='" ]

    symbolicNames = [ "<INVALID>",
            "DEF", "RETURN", "IF", "ELIF", "ELSE", "WHILE", "OR", "AND", 
            "NOT", "DEL", "PASS", "CONTINUE", "BREAK", "NEWLINE", "NAME", 
            "DECIMAL_INTEGER", "OCT_INTEGER", "HEX_INTEGER", "BIN_INTEGER", 
            "OPEN_PAREN", "CLOSE_PAREN", "COMMA", "COLON", "SEMI_COLON", 
            "ASSIGN", "OPEN_BRACK", "CLOSE_BRACK", "OR_OP", "XOR", "AND_OP", 
            "LEFT_SHIFT", "RIGHT_SHIFT", "ADD", "MINUS", "DIV", "MOD", "NOT_OP", 
            "OPEN_BRACE", "CLOSE_BRACE", "LESS_THAN", "GREATER_THAN", "EQUALS", 
            "GT_EQ", "LT_EQ", "NOT_EQ_1", "NOT_EQ_2", "ARROW", "ADD_ASSIGN", 
            "SUB_ASSIGN", "MULT_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", "AND_ASSIGN", 
            "OR_ASSIGN", "XOR_ASSIGN", "LEFT_SHIFT_ASSIGN", "RIGHT_SHIFT_ASSIGN", 
            "SKIP_", "UNKNOWN_CHAR" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "DEF", "RETURN", "IF", 
                  "ELIF", "ELSE", "WHILE", "OR", "AND", "NOT", "DEL", "PASS", 
                  "CONTINUE", "BREAK", "NEWLINE", "NAME", "DECIMAL_INTEGER", 
                  "OCT_INTEGER", "HEX_INTEGER", "BIN_INTEGER", "OPEN_PAREN", 
                  "CLOSE_PAREN", "COMMA", "COLON", "SEMI_COLON", "ASSIGN", 
                  "OPEN_BRACK", "CLOSE_BRACK", "OR_OP", "XOR", "AND_OP", 
                  "LEFT_SHIFT", "RIGHT_SHIFT", "ADD", "MINUS", "DIV", "MOD", 
                  "NOT_OP", "OPEN_BRACE", "CLOSE_BRACE", "LESS_THAN", "GREATER_THAN", 
                  "EQUALS", "GT_EQ", "LT_EQ", "NOT_EQ_1", "NOT_EQ_2", "ARROW", 
                  "ADD_ASSIGN", "SUB_ASSIGN", "MULT_ASSIGN", "DIV_ASSIGN", 
                  "MOD_ASSIGN", "AND_ASSIGN", "OR_ASSIGN", "XOR_ASSIGN", 
                  "LEFT_SHIFT_ASSIGN", "RIGHT_SHIFT_ASSIGN", "SKIP_", "UNKNOWN_CHAR", 
                  "SHORT_STRING", "STRING_ESCAPE_SEQ", "NON_ZERO_DIGIT", 
                  "DIGIT", "OCT_DIGIT", "HEX_DIGIT", "BIN_DIGIT", "INT_PART", 
                  "SPACES", "COMMENT", "LINE_JOINING", "ID_START", "ID_CONTINUE" ]

    grammarFileName = "Chipy8.g4"

    def __init__(self, input=None):
        super().__init__(input)
        self.checkVersion("4.5.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    @property
    def tokens(self):
        try:
            return self._tokens
        except AttributeError:
            self._tokens = []
            return self._tokens

    @property
    def indents(self):
        try:
            return self._indents
        except AttributeError:
            self._indents = []
            return self._indents

    @property
    def opened(self):
        try:
            return self._opened
        except AttributeError:
            self._opened = 0
            return self._opened

    @opened.setter
    def opened(self, value):
        self._opened = value

    @property
    def lastToken(self):
        try:
            return self._lastToken
        except AttributeError:
            self._lastToken = None
            return self._lastToken

    @lastToken.setter
    def lastToken(self, value):
        self._lastToken = value

    def reset(self):
        super().reset()
        self.tokens = []
        self.indents = []
        self.opened = 0
        self.lastToken = None

    def emitToken(self, t):
        super().emitToken(t)
        self.tokens.append(t)

    def nextToken(self):
        if self._input.LA(1) == Token.EOF and self.indents:
            for i in range(len(self.tokens)-1,-1,-1):
                if self.tokens[i].type == Token.EOF:
                    self.tokens.pop(i)

            self.emitToken(self.commonToken(LanguageParser.NEWLINE, '\n'))
            while self.indents:
                self.emitToken(self.createDedent())
                self.indents.pop()

            self.emitToken(self.commonToken(LanguageParser.EOF, "<EOF>"))
        next = super().nextToken()
        if next.channel == Token.DEFAULT_CHANNEL:
            self.lastToken = next
        return next if not self.tokens else self.tokens.pop(0)

    def createDedent(self):
        dedent = self.commonToken(LanguageParser.DEDENT, "")
        dedent.line = self.lastToken.line
        return dedent

    def commonToken(self, type, text, indent=0):
        stop = self.getCharIndex()-1-indent
        start = (stop - len(text) + 1) if text else stop
        return CommonToken(self._tokenFactorySourcePair, type, super().DEFAULT_TOKEN_CHANNEL, start, stop)

    @staticmethod
    def getIndentationCount(spaces):
        count = 0
        for ch in spaces:
            if ch == '\t':
                count += 8 - (count % 8)
            else:
                count += 1
        return count

    def atStartOfInput(self):
        return Lexer.column.fget(self) == 0 and Lexer.line.fget(self) == 1


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
    	if self._actions is None:
    		actions = dict()
    		actions[17] = self.NEWLINE_action 
    		actions[23] = self.OPEN_PAREN_action 
    		actions[24] = self.CLOSE_PAREN_action 
    		actions[29] = self.OPEN_BRACK_action 
    		actions[30] = self.CLOSE_BRACK_action 
    		actions[41] = self.OPEN_BRACE_action 
    		actions[42] = self.CLOSE_BRACE_action 
    		self._actions = actions
    	action = self._actions.get(ruleIndex, None)
    	if action is not None:
    		action(localctx, actionIndex)
    	else:
    		raise Exception("No registered action for:" + str(ruleIndex))

    def NEWLINE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            tempt = Lexer.text.fget(self)
            newLine = re.sub("[^\r\n]+", "", tempt)
            spaces = re.sub("[\r\n]+", "", tempt)
            la_char = ""
            try:
                la = self._input.LA(1)
                la_char = chr(la)       # Python does not compare char to ints directly
            except ValueError:          # End of file
                pass

            if self.opened > 0 or la_char == '\r' or la_char == '\n' or la_char == '#':
                self.skip()
            else:
                indent = self.getIndentationCount(spaces)
                previous = self.indents[-1] if self.indents else 0
                self.emitToken(self.commonToken(self.NEWLINE, newLine, indent=indent))      # NEWLINE is actually the '\n' char
                if indent == previous:
                    self.skip()
                elif indent > previous:
                    self.indents.append(indent)
                    self.emitToken(self.commonToken(LanguageParser.INDENT, spaces))
                else:
                    while self.indents and self.indents[-1] > indent:
                        self.emitToken(self.createDedent())
                        self.indents.pop()
                
     

    def OPEN_PAREN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.opened += 1
     

    def CLOSE_PAREN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.opened -= 1
     

    def OPEN_BRACK_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            self.opened += 1
     

    def CLOSE_BRACK_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            self.opened -= 1
     

    def OPEN_BRACE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            self.opened += 1
     

    def CLOSE_BRACE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:
            self.opened -= 1
     

    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates is None:
            preds = dict()
            preds[17] = self.NEWLINE_sempred
            self._predicates = preds
        pred = self._predicates.get(ruleIndex, None)
        if pred is not None:
            return pred(localctx, predIndex)
        else:
            raise Exception("No registered predicate for:" + str(ruleIndex))

    def NEWLINE_sempred(self, localctx:RuleContext, predIndex:int):
            if predIndex == 0:
                return self.atStartOfInput()
         


