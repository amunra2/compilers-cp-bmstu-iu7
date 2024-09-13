# Generated from Pascal.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,27,113,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,1,0,
        1,0,1,0,3,0,31,8,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,5,1,40,8,1,10,1,12,
        1,43,9,1,1,1,1,1,1,2,1,2,1,2,1,2,1,3,1,3,1,4,1,4,4,4,55,8,4,11,4,
        12,4,56,1,4,1,4,1,5,1,5,1,5,1,5,3,5,65,8,5,1,6,1,6,1,6,1,6,1,6,1,
        6,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,5,9,87,
        8,9,10,9,12,9,90,9,9,1,10,1,10,1,10,5,10,95,8,10,10,10,12,10,98,
        9,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,109,8,11,
        1,12,1,12,1,12,0,0,13,0,2,4,6,8,10,12,14,16,18,20,22,24,0,3,1,0,
        7,10,1,0,18,19,1,0,20,21,112,0,26,1,0,0,0,2,35,1,0,0,0,4,46,1,0,
        0,0,6,50,1,0,0,0,8,52,1,0,0,0,10,64,1,0,0,0,12,66,1,0,0,0,14,72,
        1,0,0,0,16,77,1,0,0,0,18,83,1,0,0,0,20,91,1,0,0,0,22,108,1,0,0,0,
        24,110,1,0,0,0,26,27,5,1,0,0,27,28,5,22,0,0,28,30,5,2,0,0,29,31,
        3,2,1,0,30,29,1,0,0,0,30,31,1,0,0,0,31,32,1,0,0,0,32,33,3,8,4,0,
        33,34,5,3,0,0,34,1,1,0,0,0,35,36,5,4,0,0,36,41,3,4,2,0,37,38,5,5,
        0,0,38,40,3,4,2,0,39,37,1,0,0,0,40,43,1,0,0,0,41,39,1,0,0,0,41,42,
        1,0,0,0,42,44,1,0,0,0,43,41,1,0,0,0,44,45,5,2,0,0,45,3,1,0,0,0,46,
        47,3,24,12,0,47,48,5,6,0,0,48,49,3,6,3,0,49,5,1,0,0,0,50,51,7,0,
        0,0,51,7,1,0,0,0,52,54,5,11,0,0,53,55,3,10,5,0,54,53,1,0,0,0,55,
        56,1,0,0,0,56,54,1,0,0,0,56,57,1,0,0,0,57,58,1,0,0,0,58,59,5,12,
        0,0,59,9,1,0,0,0,60,65,3,14,7,0,61,65,3,12,6,0,62,65,3,16,8,0,63,
        65,3,8,4,0,64,60,1,0,0,0,64,61,1,0,0,0,64,62,1,0,0,0,64,63,1,0,0,
        0,65,11,1,0,0,0,66,67,5,13,0,0,67,68,5,14,0,0,68,69,3,24,12,0,69,
        70,5,15,0,0,70,71,5,2,0,0,71,13,1,0,0,0,72,73,3,24,12,0,73,74,5,
        16,0,0,74,75,3,18,9,0,75,76,5,2,0,0,76,15,1,0,0,0,77,78,5,17,0,0,
        78,79,5,14,0,0,79,80,3,24,12,0,80,81,5,15,0,0,81,82,5,2,0,0,82,17,
        1,0,0,0,83,88,3,20,10,0,84,85,7,1,0,0,85,87,3,20,10,0,86,84,1,0,
        0,0,87,90,1,0,0,0,88,86,1,0,0,0,88,89,1,0,0,0,89,19,1,0,0,0,90,88,
        1,0,0,0,91,96,3,22,11,0,92,93,7,2,0,0,93,95,3,22,11,0,94,92,1,0,
        0,0,95,98,1,0,0,0,96,94,1,0,0,0,96,97,1,0,0,0,97,21,1,0,0,0,98,96,
        1,0,0,0,99,109,5,23,0,0,100,109,5,24,0,0,101,109,3,24,12,0,102,103,
        5,14,0,0,103,104,3,18,9,0,104,105,5,15,0,0,105,109,1,0,0,0,106,109,
        5,25,0,0,107,109,5,26,0,0,108,99,1,0,0,0,108,100,1,0,0,0,108,101,
        1,0,0,0,108,102,1,0,0,0,108,106,1,0,0,0,108,107,1,0,0,0,109,23,1,
        0,0,0,110,111,5,22,0,0,111,25,1,0,0,0,7,30,41,56,64,88,96,108
    ]

class PascalParser ( Parser ):

    grammarFileName = "Pascal.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'program'", "';'", "'.'", "'var'", "','", 
                     "':'", "'integer'", "'real'", "'boolean'", "'char'", 
                     "'begin'", "'end'", "'exit'", "'('", "')'", "':='", 
                     "'writeln'", "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "ID", "INT", "REAL", "BOOLEAN", 
                      "CHAR", "WS" ]

    RULE_program = 0
    RULE_declarations = 1
    RULE_variableDeclaration = 2
    RULE_type = 3
    RULE_block = 4
    RULE_statement = 5
    RULE_returnStatement = 6
    RULE_assignment = 7
    RULE_printStatement = 8
    RULE_expression = 9
    RULE_term = 10
    RULE_factor = 11
    RULE_variable = 12

    ruleNames =  [ "program", "declarations", "variableDeclaration", "type", 
                   "block", "statement", "returnStatement", "assignment", 
                   "printStatement", "expression", "term", "factor", "variable" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    ID=22
    INT=23
    REAL=24
    BOOLEAN=25
    CHAR=26
    WS=27

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PascalParser.ID, 0)

        def block(self):
            return self.getTypedRuleContext(PascalParser.BlockContext,0)


        def declarations(self):
            return self.getTypedRuleContext(PascalParser.DeclarationsContext,0)


        def getRuleIndex(self):
            return PascalParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = PascalParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(PascalParser.T__0)
            self.state = 27
            self.match(PascalParser.ID)
            self.state = 28
            self.match(PascalParser.T__1)
            self.state = 30
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 29
                self.declarations()


            self.state = 32
            self.block()
            self.state = 33
            self.match(PascalParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PascalParser.VariableDeclarationContext)
            else:
                return self.getTypedRuleContext(PascalParser.VariableDeclarationContext,i)


        def getRuleIndex(self):
            return PascalParser.RULE_declarations

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclarations" ):
                listener.enterDeclarations(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclarations" ):
                listener.exitDeclarations(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclarations" ):
                return visitor.visitDeclarations(self)
            else:
                return visitor.visitChildren(self)




    def declarations(self):

        localctx = PascalParser.DeclarationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declarations)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(PascalParser.T__3)
            self.state = 36
            self.variableDeclaration()
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 37
                self.match(PascalParser.T__4)
                self.state = 38
                self.variableDeclaration()
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 44
            self.match(PascalParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(PascalParser.VariableContext,0)


        def type_(self):
            return self.getTypedRuleContext(PascalParser.TypeContext,0)


        def getRuleIndex(self):
            return PascalParser.RULE_variableDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDeclaration" ):
                listener.enterVariableDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDeclaration" ):
                listener.exitVariableDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableDeclaration" ):
                return visitor.visitVariableDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def variableDeclaration(self):

        localctx = PascalParser.VariableDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_variableDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.variable()
            self.state = 47
            self.match(PascalParser.T__5)
            self.state = 48
            self.type_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PascalParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = PascalParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1920) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PascalParser.StatementContext)
            else:
                return self.getTypedRuleContext(PascalParser.StatementContext,i)


        def getRuleIndex(self):
            return PascalParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = PascalParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(PascalParser.T__10)
            self.state = 54 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 53
                self.statement()
                self.state = 56 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 4335616) != 0)):
                    break

            self.state = 58
            self.match(PascalParser.T__11)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(PascalParser.AssignmentContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(PascalParser.ReturnStatementContext,0)


        def printStatement(self):
            return self.getTypedRuleContext(PascalParser.PrintStatementContext,0)


        def block(self):
            return self.getTypedRuleContext(PascalParser.BlockContext,0)


        def getRuleIndex(self):
            return PascalParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = PascalParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_statement)
        try:
            self.state = 64
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                self.enterOuterAlt(localctx, 1)
                self.state = 60
                self.assignment()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 61
                self.returnStatement()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 3)
                self.state = 62
                self.printStatement()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 4)
                self.state = 63
                self.block()
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


    class ReturnStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(PascalParser.VariableContext,0)


        def getRuleIndex(self):
            return PascalParser.RULE_returnStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStatement" ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStatement" ):
                listener.exitReturnStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStatement" ):
                return visitor.visitReturnStatement(self)
            else:
                return visitor.visitChildren(self)




    def returnStatement(self):

        localctx = PascalParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_returnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(PascalParser.T__12)
            self.state = 67
            self.match(PascalParser.T__13)
            self.state = 68
            self.variable()
            self.state = 69
            self.match(PascalParser.T__14)
            self.state = 70
            self.match(PascalParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(PascalParser.VariableContext,0)


        def expression(self):
            return self.getTypedRuleContext(PascalParser.ExpressionContext,0)


        def getRuleIndex(self):
            return PascalParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = PascalParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.variable()
            self.state = 73
            self.match(PascalParser.T__15)
            self.state = 74
            self.expression()
            self.state = 75
            self.match(PascalParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(PascalParser.VariableContext,0)


        def getRuleIndex(self):
            return PascalParser.RULE_printStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStatement" ):
                listener.enterPrintStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStatement" ):
                listener.exitPrintStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStatement" ):
                return visitor.visitPrintStatement(self)
            else:
                return visitor.visitChildren(self)




    def printStatement(self):

        localctx = PascalParser.PrintStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_printStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(PascalParser.T__16)
            self.state = 78
            self.match(PascalParser.T__13)
            self.state = 79
            self.variable()
            self.state = 80
            self.match(PascalParser.T__14)
            self.state = 81
            self.match(PascalParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PascalParser.TermContext)
            else:
                return self.getTypedRuleContext(PascalParser.TermContext,i)


        def getRuleIndex(self):
            return PascalParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = PascalParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.term()
            self.state = 88
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==18 or _la==19:
                self.state = 84
                _la = self._input.LA(1)
                if not(_la==18 or _la==19):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 85
                self.term()
                self.state = 90
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PascalParser.FactorContext)
            else:
                return self.getTypedRuleContext(PascalParser.FactorContext,i)


        def getRuleIndex(self):
            return PascalParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = PascalParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.factor()
            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20 or _la==21:
                self.state = 92
                _la = self._input.LA(1)
                if not(_la==20 or _la==21):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 93
                self.factor()
                self.state = 98
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(PascalParser.INT, 0)

        def REAL(self):
            return self.getToken(PascalParser.REAL, 0)

        def variable(self):
            return self.getTypedRuleContext(PascalParser.VariableContext,0)


        def expression(self):
            return self.getTypedRuleContext(PascalParser.ExpressionContext,0)


        def BOOLEAN(self):
            return self.getToken(PascalParser.BOOLEAN, 0)

        def CHAR(self):
            return self.getToken(PascalParser.CHAR, 0)

        def getRuleIndex(self):
            return PascalParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = PascalParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_factor)
        try:
            self.state = 108
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23]:
                self.enterOuterAlt(localctx, 1)
                self.state = 99
                self.match(PascalParser.INT)
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 2)
                self.state = 100
                self.match(PascalParser.REAL)
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 3)
                self.state = 101
                self.variable()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 4)
                self.state = 102
                self.match(PascalParser.T__13)
                self.state = 103
                self.expression()
                self.state = 104
                self.match(PascalParser.T__14)
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 5)
                self.state = 106
                self.match(PascalParser.BOOLEAN)
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 6)
                self.state = 107
                self.match(PascalParser.CHAR)
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


    class VariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PascalParser.ID, 0)

        def getRuleIndex(self):
            return PascalParser.RULE_variable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)




    def variable(self):

        localctx = PascalParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(PascalParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





