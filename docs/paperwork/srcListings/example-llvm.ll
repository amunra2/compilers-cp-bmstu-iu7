@.str_1 = private unnamed_addr constant [12 x i8] c"Hello World\00", align 1
declare i32 @printf(i8*, ...)
declare i32 @scanf(i8*, ...)
define i32 @main() {
%1 = getelementptr inbounds [12 x i8], [12 x i8]* @.str_1, i64 0, i64 0
%2 = ptrtoint i8* %1 to i99
%3 = inttoptr i99 %2 to i8*
%4 = call i32 (i8*, ...) @printf(i8* %3)
ret i32 0
ret i32 zeroinitializer
}
