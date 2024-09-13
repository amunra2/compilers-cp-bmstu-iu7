; ModuleID = "course"
target triple = "unknown-unknown-unknown"
target datalayout = ""

define i32 @"main"()
{
entry:
  %"x" = alloca i32
  %"y" = alloca i32
  %".2" = mul i32 20, 2
  %".3" = add i32 10000, %".2"
  store i32 %".3", i32* %"x"
  %".5" = load i32, i32* %"x"
  ret i32 %".5"
}
