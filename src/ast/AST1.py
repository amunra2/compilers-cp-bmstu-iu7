from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
from nodes.Block import Block
from grammar.PascalLexer import PascalLexer
from grammar.PascalParser import PascalParser
from ast.ASTBuilder import ASTBuilder

# from src.visitors import *
# from src.nodes import *

# from src.LLVMContext import LLVMContext


def buildAST(file_name:str):
    input_stream = FileStream(file_name)
    
    lexer = PascalLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = PascalParser(stream)
    tree = parser.program()
    
    walker = ParseTreeWalker()
    astb = ASTBuilder()
    walker.walk(astb, tree)
    
    
    
    ast = AST(astb.getRoot())
    # errors = astb.getErrors()

    # ast.m_root.acceptVisitor(ASTPrunePass3())

    # return ast, errors


class AST:
    def __init__(self, r=None):
        if r is None:
            self.m_root = Block()
        else:
            self.m_root = r
            
    def acceptVisitor(self, visitor):
        self.m_root.acceptVisitor(visitor)
        
    def toLLVM(self):
        context = LLVMContext()
        self.m_root.generateLLVM(context)

        res = ''
        for line in context.code:
            res += line + '\n'

        return res

#     def toDot(self, showSymbolTable=True, showReachability=False):
#         dotList = ["digraph AST {", "rankdir = BT;"]

#         self.acceptVisitor(ASTDotVisitor(dotList, showSymbolTable, showReachability))

#         dotList.append("}")

#         dotString = ""
#         for line in dotList:
#             dotString += line + "\n"
#         return dotString

#     def toLLVM(self):
#         context = LLVMContext()
#         self.m_root.generateLLVM(context)

#         res = ''
#         for line in context.code:
#             res += line + '\n'

#         return res

#     def buildSymbolTable(self):
#         stb = ASTSymbolTableBuilder()
#         self.acceptVisitor(stb)
#         if len(stb.getErrors()) > 0:
#             return stb.getErrors()

#         self.acceptVisitor(ASTTypeDecorator())

#     def acceptVisitor(self, visitor):
#         self.m_root.acceptVisitor(visitor)
