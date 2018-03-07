/*
 * The MIT License (MIT)
 *
 * Copyright (c) 2014 by Bart Kiers
 *
 * Permission is hereby granted, free of charge, to any person
 * obtaining a copy of this software and associated documentation
 * files (the "Software"), to deal in the Software without
 * restriction, including without limitation the rights to use,
 * copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the
 * Software is furnished to do so, subject to the following
 * conditions:
 *
 * The above copyright notice and this permission notice shall be
 * included in all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
 * EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
 * OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
 * NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
 * HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
 * WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
 * FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 * OTHER DEALINGS IN THE SOFTWARE.
 *
 * Project      : python3-parser; an ANTLR4 grammar for Python 3
 *                https://github.com/bkiers/python3-parser
 * Developed by : Bart Kiers, bart@big-o.nl
 *
 * Notes: This has been modified to fit a custom language. The license
 * remains unchanged.
 */
grammar Chipy8;

tokens { INDENT, DEDENT }

//Note that indentation of code inside

@lexer::header{
from antlr4.Token import CommonToken
import re
import importlib

# Allow languages to extend the lexer and parser, by loading the parser dinamically
module_path = __name__[:-5]
language_name = __name__.split('.')[-1]
language_name = language_name[:-5]  # Remove Lexer from name
LanguageParser = getattr(importlib.import_module('{}Parser'.format(module_path)), '{}Parser'.format(language_name))
}

@lexer::members {
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
}

/*
 * parser rules
 */

single_input
 : NEWLINE
 | simple_stmt
 | compound_stmt NEWLINE
 ;

file_input
 : ( NEWLINE | stmt )* EOF
 ;

eval_input
 : testlist NEWLINE* EOF
 ;

funcdef
 : DEF NAME parameters ( '->' test )? ':' suite
 ;

parameters
 : '(' typedargslist? ')'
 ;

typedargslist
 : tfpdef ( '=' test )? ( ',' tfpdef ( '=' test )? )* ( ',' ( '*' tfpdef? ( ',' tfpdef ( '=' test )? )* ( ',' '**' tfpdef )?
                                                            | '**' tfpdef
                                                            )?
                                                      )?
 | '*' tfpdef? ( ',' tfpdef ( '=' test )? )* ( ',' '**' tfpdef )?
 | '**' tfpdef
 ;

tfpdef
 : NAME ( ':' test )?
 ;

varargslist
 : vfpdef ( '=' test )? ( ',' vfpdef ( '=' test )? )* ( ',' ( '*' vfpdef? ( ',' vfpdef ( '=' test )? )* ( ',' '**' vfpdef )?
                                                            | '**' vfpdef
                                                            )?
                                                      )?
 | '*' vfpdef? ( ',' vfpdef ( '=' test )? )* ( ',' '**' vfpdef )?
 | '**' vfpdef
 ;

vfpdef
 : NAME
 ;

stmt
 : simple_stmt
 | compound_stmt
 ;

simple_stmt
 : small_stmt ( ';' small_stmt )* ';'? NEWLINE
 ;

small_stmt
 : expr_stmt
 | del_stmt
 | pass_stmt
 | flow_stmt
 ;

expr_stmt
 : testlist_star_expr ( augassign ( testlist)
                      | ( '=' ( testlist_star_expr ) )*
                      )
 ;

testlist_star_expr
 : ( test | star_expr ) ( ',' ( test |  star_expr ) )* ','?
 ;

augassign
 : '+='
 | '-='
 | '*='
 | '/='
 | '%='
 | '&='
 | '|='
 | '^='
 | '<<='
 | '>>='
 | '**='
 ;

del_stmt
 : DEL exprlist
 ;

pass_stmt
 : PASS
 ;

flow_stmt
 : break_stmt
 | continue_stmt
 | return_stmt
 ;

break_stmt
 : BREAK
 ;

continue_stmt
 : CONTINUE
 ;

return_stmt
 : RETURN testlist?
 ;

compound_stmt
 : if_stmt
 | while_stmt
 | funcdef
 ;

if_stmt
 : IF test ':' suite ( ELIF test ':' suite )* ( ELSE ':' suite )?
 ;

while_stmt
 : WHILE test ':' suite ( ELSE ':' suite )?
 ;

suite
 : simple_stmt
 | NEWLINE INDENT stmt+ DEDENT
 ;

test
 : or_test ( IF or_test ELSE test )?
 ;

test_nocond
 : or_test
 ;

or_test
 : and_test ( OR and_test )*
 ;

and_test
 : not_test ( AND not_test )*
 ;

not_test
 : NOT not_test
 | comparison
 ;

comparison
 : star_expr ( comp_op star_expr )*
 ;

comp_op
 : '<'
 | '>'
 | '=='
 | '>='
 | '<='
 | '<>'
 | '!='
 ;

star_expr
 : '*'? expr
 ;

expr
 : xor_expr ( '|' xor_expr )*
 ;

xor_expr
 : and_expr ( '^' and_expr )*
 ;

and_expr
 : shift_expr ( '&' shift_expr )*
 ;

shift_expr
 : arith_expr ( '<<' arith_expr
              | '>>' arith_expr
              )*
 ;

arith_expr
 : term ( '+' term
        | '-' term
        )*
 ;

term
 : factor ( '*' factor
          | '/' factor
          | '%' factor
          | '//' factor
          )*
 ;

factor
 : '+' factor
 | '-' factor
 | '~' factor
 ;

atom
 : '(' ( testlist_comp )? ')'
 | '[' testlist_comp? ']'
 | '{' dictorsetmaker? '}'
 | NAME
 | integer
 ;

testlist_comp
 : test ( ( ',' test )* ','? )
 ;

exprlist
 : star_expr ( ',' star_expr )* ','?
 ;

testlist
 : test ( ',' test )* ','?
 ;

dictorsetmaker
 : test ':' test ( ( ',' test ':' test )* ','? )
 | test ( ( ',' test )* ','? )
 ;

arglist
 : ( argument ',' )* ( argument ','?
                     | '*' test ( ',' argument )* ( ',' '**' test )?
                     | '**' test
                     )
 ;

argument
 : test ?
 | test '=' test
 ;

comp_if
 : IF test_nocond comp_if?
 ;

integer
 : DECIMAL_INTEGER
 | OCT_INTEGER
 | HEX_INTEGER
 | BIN_INTEGER
 ;

/*
 * lexer rules
 */

DEF : 'def';
RETURN : 'return';
IF : 'if';
ELIF : 'elif';
ELSE : 'else';
WHILE : 'while';
OR : 'or';
AND : 'and';
NOT : 'not';
DEL : 'del';
PASS : 'pass';
CONTINUE : 'continue';
BREAK : 'break';

NEWLINE
 : ( {self.atStartOfInput()}?   SPACES
   | ( '\r'? '\n' | '\r' ) SPACES?
   )
   {
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
    }
 ;

NAME
 : ID_START ID_CONTINUE*
 ;

DECIMAL_INTEGER
 : NON_ZERO_DIGIT DIGIT*
 | '0'+
 ;

OCT_INTEGER
 : '0' [oO] OCT_DIGIT+
 ;

HEX_INTEGER
 : '0' [xX] HEX_DIGIT+
 ;

BIN_INTEGER
 : '0' [bB] BIN_DIGIT+
 ;

OPEN_PAREN : '(' {self.opened += 1};
CLOSE_PAREN : ')' {self.opened -= 1};
COMMA : ',';
COLON : ':';
SEMI_COLON : ';';
ASSIGN : '=';
OPEN_BRACK : '[' {self.opened += 1};
CLOSE_BRACK : ']' {self.opened -= 1};
OR_OP : '|';
XOR : '^';
AND_OP : '&';
LEFT_SHIFT : '<<';
RIGHT_SHIFT : '>>';
ADD : '+';
MINUS : '-';
DIV : '/';
MOD : '%';
NOT_OP : '~';
OPEN_BRACE : '{' {self.opened += 1};
CLOSE_BRACE : '}' {self.opened -= 1};
LESS_THAN : '<';
GREATER_THAN : '>';
EQUALS : '==';
GT_EQ : '>=';
LT_EQ : '<=';
NOT_EQ_1 : '<>';
NOT_EQ_2 : '!=';
ARROW : '->';
ADD_ASSIGN : '+=';
SUB_ASSIGN : '-=';
MULT_ASSIGN : '*=';
DIV_ASSIGN : '/=';
MOD_ASSIGN : '%=';
AND_ASSIGN : '&=';
OR_ASSIGN : '|=';
XOR_ASSIGN : '^=';
LEFT_SHIFT_ASSIGN : '<<=';
RIGHT_SHIFT_ASSIGN : '>>=';

SKIP_
 : ( SPACES | COMMENT | LINE_JOINING ) -> skip
 ;

UNKNOWN_CHAR
 : .
 ;

/*
 * fragments
 */

fragment SHORT_STRING
 : '\'' ( STRING_ESCAPE_SEQ | ~[\\\r\n'] )* '\''
 | '"' ( STRING_ESCAPE_SEQ | ~[\\\r\n"] )* '"'
 ;

fragment STRING_ESCAPE_SEQ
 : '\\' .
 ;

fragment NON_ZERO_DIGIT
 : [1-9]
 ;

fragment DIGIT
 : [0-9]
 ;

fragment OCT_DIGIT
 : [0-7]
 ;

fragment HEX_DIGIT
 : [0-9a-fA-F]
 ;

fragment BIN_DIGIT
 : [01]
 ;

fragment INT_PART
 : DIGIT+
 ;

fragment SPACES
 : [ \t]+
 ;

fragment COMMENT
 : '#' ~[\r\n]*
 ;

fragment LINE_JOINING
 : '\\' SPACES? ( '\r'? '\n' | '\r' )
 ;

fragment ID_START
 : '_'
 | [A-Z]
 | [a-z]
 ;

fragment ID_CONTINUE
 : ID_START
 | [0-9]
 ;
