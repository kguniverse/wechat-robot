# 程序设计实践作业

## 解析器

框架：pyparsing

## example

```
step welcome
PRINT "hello"
BRANCH "作业" hwProc
BRANCH "课程信息" CourseInfoProc
BRANCH "
end welcome
```

BNF:
instruction := steps*
steps       := begin detail end {validate begin.name == end.name}
begin       := "step" stepname {begin.name = stepname.name}
stepname    := \[((a~z) + (A~Z))+\] "Proc"
detail      := function branchInput stepname {if stepname doesn't exsist, build one} 
end         := "end" stepname {end.name = stepname.name}
function    := \[A~Z\]+
branchInput := " string "