# Generated from Pascal.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PascalParser import PascalParser
else:
    from PascalParser import PascalParser

# This class defines a complete generic visitor for a parse tree produced by PascalParser.

class PascalVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PascalParser#program.
    def visitProgram(self, ctx:PascalParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalParser#declarations.
    def visitDeclarations(self, ctx:PascalParser.DeclarationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:PascalParser.VariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalParser#type.
    def visitType(self, ctx:PascalParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalParser#block.
    def visitBlock(self, ctx:PascalParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalParser#statement.
    def visitStatement(self, ctx:PascalParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalParser#returnStatement.
    def visitReturnStatement(self, ctx:PascalParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalParser#assignment.
    def visitAssignment(self, ctx:PascalParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalParser#printStatement.
    def visitPrintStatement(self, ctx:PascalParser.PrintStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalParser#expression.
    def visitExpression(self, ctx:PascalParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalParser#term.
    def visitTerm(self, ctx:PascalParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalParser#factor.
    def visitFactor(self, ctx:PascalParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalParser#variable.
    def visitVariable(self, ctx:PascalParser.VariableContext):
        return self.visitChildren(ctx)



del PascalParser