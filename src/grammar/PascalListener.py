# Generated from Pascal.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PascalParser import PascalParser
else:
    from PascalParser import PascalParser

# This class defines a complete listener for a parse tree produced by PascalParser.
class PascalListener(ParseTreeListener):

    # Enter a parse tree produced by PascalParser#program.
    def enterProgram(self, ctx:PascalParser.ProgramContext):
        pass

    # Exit a parse tree produced by PascalParser#program.
    def exitProgram(self, ctx:PascalParser.ProgramContext):
        pass


    # Enter a parse tree produced by PascalParser#declarations.
    def enterDeclarations(self, ctx:PascalParser.DeclarationsContext):
        pass

    # Exit a parse tree produced by PascalParser#declarations.
    def exitDeclarations(self, ctx:PascalParser.DeclarationsContext):
        pass


    # Enter a parse tree produced by PascalParser#variableDeclaration.
    def enterVariableDeclaration(self, ctx:PascalParser.VariableDeclarationContext):
        pass

    # Exit a parse tree produced by PascalParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx:PascalParser.VariableDeclarationContext):
        pass


    # Enter a parse tree produced by PascalParser#type.
    def enterType(self, ctx:PascalParser.TypeContext):
        pass

    # Exit a parse tree produced by PascalParser#type.
    def exitType(self, ctx:PascalParser.TypeContext):
        pass


    # Enter a parse tree produced by PascalParser#block.
    def enterBlock(self, ctx:PascalParser.BlockContext):
        pass

    # Exit a parse tree produced by PascalParser#block.
    def exitBlock(self, ctx:PascalParser.BlockContext):
        pass


    # Enter a parse tree produced by PascalParser#statement.
    def enterStatement(self, ctx:PascalParser.StatementContext):
        pass

    # Exit a parse tree produced by PascalParser#statement.
    def exitStatement(self, ctx:PascalParser.StatementContext):
        pass


    # Enter a parse tree produced by PascalParser#returnStatement.
    def enterReturnStatement(self, ctx:PascalParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by PascalParser#returnStatement.
    def exitReturnStatement(self, ctx:PascalParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by PascalParser#assignment.
    def enterAssignment(self, ctx:PascalParser.AssignmentContext):
        pass

    # Exit a parse tree produced by PascalParser#assignment.
    def exitAssignment(self, ctx:PascalParser.AssignmentContext):
        pass


    # Enter a parse tree produced by PascalParser#printStatement.
    def enterPrintStatement(self, ctx:PascalParser.PrintStatementContext):
        pass

    # Exit a parse tree produced by PascalParser#printStatement.
    def exitPrintStatement(self, ctx:PascalParser.PrintStatementContext):
        pass


    # Enter a parse tree produced by PascalParser#expression.
    def enterExpression(self, ctx:PascalParser.ExpressionContext):
        pass

    # Exit a parse tree produced by PascalParser#expression.
    def exitExpression(self, ctx:PascalParser.ExpressionContext):
        pass


    # Enter a parse tree produced by PascalParser#term.
    def enterTerm(self, ctx:PascalParser.TermContext):
        pass

    # Exit a parse tree produced by PascalParser#term.
    def exitTerm(self, ctx:PascalParser.TermContext):
        pass


    # Enter a parse tree produced by PascalParser#factor.
    def enterFactor(self, ctx:PascalParser.FactorContext):
        pass

    # Exit a parse tree produced by PascalParser#factor.
    def exitFactor(self, ctx:PascalParser.FactorContext):
        pass


    # Enter a parse tree produced by PascalParser#variable.
    def enterVariable(self, ctx:PascalParser.VariableContext):
        pass

    # Exit a parse tree produced by PascalParser#variable.
    def exitVariable(self, ctx:PascalParser.VariableContext):
        pass



del PascalParser