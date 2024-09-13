from ast.AST import *
from grammar.PascalListener import PascalListener
from grammar.PascalParser import PascalParser
from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
from grammar.PascalLexer import PascalLexer
from grammar.PascalParser import PascalParser
from antlr4.tree import Tree

import llvmlite.binding as llvm
from llvmlite import binding
import ctypes


def compile_and_run(module):
    binding.initialize()
    binding.initialize_native_target()
    binding.initialize_native_asmprinter()  # требуется для печати
    target = binding.Target.from_default_triple()
    target_machine = target.create_target_machine()
    
    llvm_ir = str(module)
    compiled_module = binding.parse_assembly(llvm_ir)
    compiled_module.verify()

    # Создание JIT-компилятора
    engine = binding.create_mcjit_compiler(compiled_module, target_machine)
    engine.finalize_object()
    engine.run_static_constructors()

    # Выполнение функции main
    func_ptr = engine.get_function_address("main")
    cfunc = ctypes.CFUNCTYPE(ctypes.c_int)(func_ptr)
    result = cfunc()
    print("Program returned:", result)


def buildAST(file_name: str = "./test/test.pas"):
    input_stream = FileStream(file_name)
    lexer = PascalLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = PascalParser(stream)
    tree = parser.program()
    
    walker = ParseTreeWalker()
    astb = ASTBuilder()
    walker.walk(astb, tree)
    return astb


class ASTBuilder(PascalListener):
    def __init__(self):
        llvm.initialize()
        llvm.initialize_native_target()
        llvm.initialize_native_asmprinter()
        self.prop={}
        self.function_name_table = {}
        self.function_symbol_table = {}
        self.var_symbolTBL = {}
        self.var_ptr_symbolTBL = {}
        # self.var_ptr_symbolTBL['var_symbolTBL'] = self.var_symbolTBL

        self.tm = llvm.Target.from_default_triple().create_target_machine()
        
    def generateLLVMCode(self, outFile: str = "./test/out.ll", printCode: bool = False) -> str:
        programAst: ProgramAST = self.prop["program"]
        mod = programAst.codeGenerate(self.var_ptr_symbolTBL)
        strmod = str(mod)
        
        with open(outFile, "w") as f:
            f.write(strmod)
            
        if printCode:
            print(f"\n{strmod}")

        return strmod
        
    def add_var(self, name, ast):
        if name in self.var_symbolTBL.keys():
           self.var_symbolTBL[name].append(ast)
        else:
           self.var_symbolTBL[name] = []
           self.var_symbolTBL[name].append(ast)

    def enterProgram(self, ctx: PascalParser.ProgramContext):
        pass
    
    def exitProgram(self, ctx: PascalParser.ProgramContext):
        programAst = ProgramAST()
        for child in ctx.getChildren():
            if (not isinstance(child, Tree.TerminalNodeImpl)):
                child_ast = self.prop[child]
                programAst.asts.append(child_ast)
     
        self.prop["program"] = programAst

                
    def enterDeclarations(self, ctx: PascalParser.DeclarationsContext):
        return super().enterDeclarations(ctx)
    
    def exitDeclarations(self, ctx: PascalParser.DeclarationsContext):
        declarationsAST = DeclarationsAST()
        self.prop[ctx] = declarationsAST
        
        for varDecl in ctx.getChildren():
             if varDecl in self.prop:
                declarationsAST.pushAST(self.prop[varDecl])
    
    def enterVariableDeclaration(self, ctx: PascalParser.VariableDeclarationContext):
        return super().enterVariableDeclaration(ctx)
    
    def exitVariableDeclaration(self, ctx: PascalParser.VariableDeclarationContext):
        if (ctx.getChildCount() == 3):
            type = self.prop[ctx.getChild(2)]
            name = self.prop[ctx.getChild(0)]
            ast = VarDeclAST(name=name, type=type)

            self.add_var(name, ast)
            self.function_symbol_table[name] = ast
            self.prop[ctx] = ast
    
    def enterType(self, ctx: PascalParser.TypeContext):
        return super().enterType(ctx)
    
    def exitType(self, ctx: PascalParser.TypeContext):
        type = ctx.getChild(0).getText()
        ast = TypeAST(type)
        self.prop[ctx] = ast
        
    def enterVariable(self, ctx: PascalParser.VariableContext):
        return super().enterVariable(ctx)
    
    def exitVariable(self, ctx: PascalParser.VariableContext):
        name = ctx.getChild(0).getText()
        ast = VariableAST(name)
        self.prop[ctx] = ast
        
    def enterBlock(self, ctx: PascalParser.BlockContext):
        return super().enterBlock(ctx)
    
    def exitBlock(self, ctx: PascalParser.BlockContext):
        blockAST = BlockAST()
        self.prop[ctx] = blockAST
        
        for stm in ctx.getChildren():
             if stm in self.prop:
                blockAST.pushAST(self.prop[stm])
    
    def enterStatement(self, ctx: PascalParser.StatementContext):
        return super().enterStatement(ctx)
    
    def exitStatement(self, ctx: PascalParser.StatementContext):
        if (isinstance(ctx.getChild(0), PascalParser.AssignmentContext)):
            assignmentStm = self.prop[ctx.assignment()]
            ast = StatementAST(assignmentStm)
        elif (isinstance(ctx.getChild(0), PascalParser.ReturnStatementContext)):
            returnStm = self.prop[ctx.returnStatement()]
            ast = StatementAST(returnStm)
            
        self.prop[ctx] = ast
            
    
    def enterAssignment(self, ctx: PascalParser.AssignmentContext):
        return super().enterAssignment(ctx)
    
    def exitAssignment(self, ctx: PascalParser.AssignmentContext):
        s1 = self.prop[ctx.variable()]
        op = ctx.getChild(1).getText()
        s2 = self.prop[ctx.expression()]
        ast = AssignmentAST(s1, op, s2)
        self.add_var(s1,s2)
        
        self.prop[ctx] = ast
    
    def enterExpression(self, ctx: PascalParser.ExpressionContext):
        return super().enterExpression(ctx)
    
    def exitExpression(self, ctx: PascalParser.ExpressionContext):
        if (ctx.getChildCount() == 1):
            ast = ExprAST(self.prop[ctx.term(0)])
        if (ctx.getChildCount() == 3):
            s1 = self.prop[ctx.term(0)]
            s2 = self.prop[ctx.term(1)]
            op = ctx.getChild(1).getText()
            ast = BinaryAST(s1, s2, op)
            
        self.prop[ctx] = ast
    
    def enterTerm(self, ctx: PascalParser.TermContext):
        return super().enterTerm(ctx)
    
    def exitTerm(self, ctx: PascalParser.TermContext):
        if (ctx.getChildCount() == 1):
            ast = TermAST(self.prop[ctx.factor(0)])
        if (ctx.getChildCount() == 3):
            s1 = self.prop[ctx.factor(0)]
            s2 = self.prop[ctx.factor(1)]
            op = ctx.getChild(1).getText()
            ast = BinaryAST(s1, s2, op)
            
        self.prop[ctx] = ast
    
    def enterFactor(self, ctx: PascalParser.FactorContext):
        return super().enterFactor(ctx)
    
    
    def exitFactor(self, ctx: PascalParser.FactorContext):
        if (ctx.getChildCount() == 3):
            pass
        else:
            if (isinstance(ctx.getChild(0), PascalParser.VariableContext)):
                data: VariableAST = self.prop[ctx.getChild(0)]
                ast = FactorAST(data.codeGenerate())
                self.prop[ctx] = ast
            else:
                ast = FactorAST(ctx.INT())
                self.prop[ctx] = ast
                
    def enterReturnStatement(self, ctx: PascalParser.ReturnStatementContext):
        return super().enterReturnStatement(ctx)
    
    def exitReturnStatement(self, ctx: PascalParser.ReturnStatementContext):
        if (ctx.getChildCount() == 5):
            variable = self.prop[ctx.variable()]
            ast = ReturnAST(variable)
            
        self.prop[ctx] = ast
    
# print("=== Generated IR code ===\n")
# print(strmod)
# with open("output.ll", 'w') as f:
#     f.write(strmod)
    
# llmod = llvm.parse_assembly(strmod)
# llmod.verify()
# with llvm.create_mcjit_compiler(llmod, self.tm) as ee:
#     ee.finalize_object()
#     print("=== Generated assembly code ===\n")
#     print(self.tm.emit_assembly(llmod))
#     with open("output.asm", 'w') as f:
#         f.write(self.tm.emit_assembly(llmod))

# answer = input('Do you want to create CFG Graph? (y/n) : ')
#         if answer.lower() == 'y': 
#             for cfg in cfg_list:
#                 dot = llvm.get_function_cfg(cfg)
#                 llvm.view_dot_graph(dot ,filename=cfg.name,view = True)