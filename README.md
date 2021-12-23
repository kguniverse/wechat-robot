# 程序设计实践作业

## BUPT2019211504 王乾凱

## github链接说明

[link](https://github.com/kguniverse/wechat-robot)

由于我在校外走读，Linux服务器没法做校园网内网穿透（global protect），所以就先把服务器里的项目暂存在github上，防止服务器宕掉。每一次来学校上课都把我的笔记本作为一个转发服务器，把我的项目push到gitlab上。

## 详细模块说明

## [link](asset/README.md)

## git提交日志标准

我在这门课过程中还学习了如何规范书写git提交日志并自己写出了一篇博客[link](https://blog.kger.io/2021/12/21/git-commit-format/)

但是因为学习的时候已经基本完成了这个工程，只有最后一次提交是参照着学习的规范写的。

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

## DSL脚本格式

```
BNF:

instruction := step*

step        := begin detail* end

begin       := "step" stepname

stepname    := "Proc:" + name(only alphnum)

detail = branch_detail | wait_detail | print_detail | default_detail | goto_detail

end         := "end step"
```

### 对标准范式的说明

instruction涵盖了整个脚本，由若干个子步骤(step)组成。每一个step中都由begin块，detail块和end块，其中begin块就是step加上以Proc:开头的步骤名，end块就是“end step”（这两个单词的分隔符随意）。

detail模块是由若干个重复detail组成的，即功能块，包括了``branch，wait，print，default，goto``功能，详细见example。