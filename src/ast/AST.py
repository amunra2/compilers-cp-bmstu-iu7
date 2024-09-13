import llvmlite
import llvmlite.ir as ll
import llvmlite.binding as llvm

function_set = {}
cfg_list = []
    
    # ast = AST(astb.getRoot())
    # errors = astb.getErrors()

    # ast.m_root.acceptVisitor(ASTPrunePass3())

    # return ast, errors

def int32(value):
   return ll.Constant(ll.IntType(32),value)

class BaseAST(object):
   def __init__(self):
      pass

   def codeGenerate(self):
      pass


class ProgramAST(BaseAST):
   def __init__(self):
      self.asts = []

   def codeGenerate(self,var_ptr_symbolTBL):
      module = ll.Module(name="course")
      func_type = ll.FunctionType(ll.IntType(32), [])
      func = ll.Function(module, func_type, name="main")

      block = func.append_basic_block(name="entry")
      builder = ll.IRBuilder(block)
      for ast in self.asts:
         ast.codeGenerate(builder, var_ptr_symbolTBL)
      return module
   
class TypeAST(BaseAST):
   def __init__(self, type: str):
      self.type = type
   
   def codeGenerate(self):
      if self.type == "integer":
         return ll.IntType(32)
      if self.type == "real":
         return ll.DoubleType()
      if self.type == "boolean":
         return ll.IntType(1)
      # if self.type == "void":
      #    return ll.VoidType()
      
      
class DeclarationsAST(BaseAST):
   def __init__(self):
      self.ast_list: list[VarDeclAST] = []
      
   def codeGenerate(self,builder,var_ptr_symbolTBL):
      for ast in self.ast_list:
         ast.codeGenerate(builder,var_ptr_symbolTBL)
         
   def pushAST(self, ast):
      self.ast_list.append(ast)
     
      
class VariableAST(BaseAST):
   def __init__(self, name: str):
      self.name = name
      
   def codeGenerate(self, builder: ll.IRBuilder, var_ptr_symbolTBL):
      return self.name
   
   
class FactorAST(BaseAST):
   def __init__(self, data):
      self.data = data
      
   def codeGenerate(self, builder: ll.IRBuilder, var_ptr_symbolTBL):
      return int32(self.data)
   
   
class TermAST(BaseAST):
   def __init__(self, data: FactorAST):
      self.data = data
      
   def codeGenerate(self, builder: ll.IRBuilder, var_ptr_symbolTBL):
      return self.data.codeGenerate(builder, var_ptr_symbolTBL)
   

class ExprAST(BaseAST):
   def __init__(self, data: TermAST):
      self.data = data
      
   def codeGenerate(self, builder: ll.IRBuilder, var_ptr_symbolTBL):
      return self.data.codeGenerate(builder, var_ptr_symbolTBL)
      
     
class BinaryAST(BaseAST):

   def __init__(self, s1: FactorAST | TermAST, s2: FactorAST | TermAST, op: str):
      self.s1 = s1
      self.op = op
      self.s2 = s2

   def codeGenerate(self, builder: ll.IRBuilder, var_ptr_symbolTBL):
      s1_load = self.s1.codeGenerate(builder, var_ptr_symbolTBL)
      s2_load = self.s2.codeGenerate(builder, var_ptr_symbolTBL)
      if self.op == "+":
         return builder.add(s1_load,s2_load)
      elif self.op == "-":
         return builder.sub(s1_load,s2_load)
      elif self.op == "*":
         return builder.mul(s1_load,s2_load)
      elif self.op == "/":
         return builder.sdiv(s1_load,s2_load)

      
class VarDeclAST(BaseAST):
   def __init__(self, name: VariableAST, type: TypeAST, value: str = None):
      self.name = name
      self.type = type
      self.value = value

   def codeGenerate(self, builder: ll.IRBuilder, var_ptr_symbolTBL):
      type = self.type.codeGenerate()
      name = self.name.codeGenerate(None, None)
      decl = builder.alloca(typ=type, name=name)
      if self.value != None:
         builder.store(ll.Constant(decl.type.pointee, self.value), decl)

      var_ptr_symbolTBL[name] = decl
      return builder


class AssignmentAST(BaseAST):
   def __init__(self, s1: VariableAST, op: str, s2: ExprAST | BinaryAST):
      self.s1 = s1
      self.op = op
      self.s2 = s2

   def codeGenerate(self,builder: ll.IRBuilder, var_ptr_symbolTBL):
      if self.op == ":=":
         s2_load = self.s2.codeGenerate(builder,var_ptr_symbolTBL)
         name = self.s1.name
         s1_ptr = var_ptr_symbolTBL[name]
         builder.store(s2_load,s1_ptr)
         
         
class ReturnAST(BaseAST):
   def __init__(self, variable: VariableAST):
      self.variable = variable
      
   def codeGenerate(self, builder: ll.IRBuilder, var_ptr_symbolTBL):
      name = self.variable.name
      ptr = var_ptr_symbolTBL[name]
      text = builder.load(ptr)
      builder.ret(text)
         
         
class StatementAST(BaseAST):
   def __init__(self, stm: AssignmentAST | ReturnAST):
      self.stm = stm
      
   def codeGenerate(self, builder: ll.IRBuilder, var_ptr_symbolTBL):
      return self.stm.codeGenerate(builder, var_ptr_symbolTBL)


class BlockAST(BaseAST):
   def __init__(self):
      self.ast_list: list[StatementAST] = []
      
   def codeGenerate(self, builder: ll.IRBuilder, var_ptr_symbolTBL):
      for ast in self.ast_list:
         ast.codeGenerate(builder, var_ptr_symbolTBL)
         
   def pushAST(self, ast):
      self.ast_list.append(ast)
      