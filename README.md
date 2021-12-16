# 程序设计实践作业

## 运行截图

![1](asset/docs/IMG_0412.PNG)

## 解析器

框架：pyparsing
交互框架：fastapi(处理http请求) + nginx(非root用户端口转发)

## 配置

nginx:
(转发微信公众号的post请求)
```
server {
    listen       80;
    server_name  localhost;

    location / {
            proxy_pass http://127.0.0.1:8000;
    }
}
```

## example

```
step Proc:welcome
PRINT hello
BRANCH homework Proc:hw
BRANCH CourseInfo Proc:CourseInfo
end step
step Proc:hw
WAIT 5
BRANCH homework Proc:hw
BRANCH CourseInfo Proc:CourseInfo
end step
```

BNF:

instruction := steps*

steps       := begin detail end {validate begin.name == end.name}

begin       := "step" stepname {begin.name = stepname.name}

stepname    := [((a~z) + (A~Z))+] "Proc"

detail      := function branchInput stepname {if stepname doesn't exsist, build one} 

end         := "end" stepname {end.name = stepname.name}

function    := \[A~Z]+

branchInput := " string "