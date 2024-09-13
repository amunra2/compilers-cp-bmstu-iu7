from ast.ASTBuilder import buildAST, compile_and_run
import sys

def main():
  try:
    src_fname = sys.argv[1]
    astb = buildAST(src_fname)
  except:
    astb = buildAST()

  llvm_code = astb.generateLLVMCode(printCode=True)
  compile_and_run(llvm_code)


if __name__ == '__main__':
  main()
