# 程序说明

## 整体逻辑实现

![](docs/framework.png)

程序整体分为两个接口（测试接口除外），包括配置接口和用户交互接口（http协议）

配置接口没有编写前端，所以所有配置均采用postman发送脚本语言，将解析的结果返回。

用户交互接口与微信公众号相连，通过解析xml文件解析出来发送用户信息和信息内容，随后通过哈希映射，获取当前用户的状态，然后进行interprete的操作。

在interpret的操作过程中，首先调用了jieba这个中文分词的库，将关键词提取出来，然后对translation中的词进行查找，如果查找到了就进行二次映射，将返回给用户的信息返回出来，然后传回去；如果没有找到，则直接返回我不知道你在说什么。

## config接口逻辑说明

fastapi接受信息解码后把脚本语言传入parser中的parse函数，在parser.py中，使用pyparsing框架定义了脚本语言的文法和文法翻译方案，只需要通过一行``instruction.parse_string(shell)``即可完成建立数据结构的过程。


## 用户交互接口说明

fastapi接收信息解码后转换为包括来源方和内容等信息的结构体，随后提取出内容后放进解释器中得到应答文本，再包装为xml格式文本返回给微信进行信息交互。

## 脚本语言逻辑的数据结构说明

脚本语言的数据结构为拓扑图结构，有三类外链指针，分别是branch, default, goto，前两个为条件跳转边，用于在某一条件下跳转状态；goto为无条件跳转边，用于叶子结点返回根节点的无条件转移逻辑。除此之外，还有节点行为列表，用于在解释的过程中方便识别（目前只设置有PRINT和WAIT）。

## 解释器逻辑说明

解释器中首先定义了两个静态文件，分别为dict.txt和translation.txt，前者用于输出内容的映射，key为配置脚本中的PRINT后的值，value为真正应该打印的内容，项目维护者可以通过修改这个静态文件来实现内容的迭代。

在输入内容传进来时，首先通过splitWord把关键词提取出来并且在translation.txt中进行匹配，如果匹配到了则把英文关键词映射到dict.txt中，从而拿到输出的内容；而如果没有匹配，就返回一个我不知道你在说什么。

## 测试结果

### 压力测试(远程测试remote)

书写了一个随机生成带有关键词的字符串作为输出内容，另一随机字符串作为用户名代码，多线程并发发送post请求的一个python脚本(test_remote.py), 设置的参数为10个并发线程，每个线程500个发送任务，每次发送间隔0.1s。

最后的结果如下，QPS可以达到71W（这个是理论最优值，因为没有跑内部的interpreter逻辑）

![](docs/pressuretest.png)


### 测试桩(本机测试local)

这个部分一开始的时候忘记考虑了，但是在我翻阅我的debug日志时候发现我是有写符合老师要求的测试桩的程序的(test_local.py)，这是我用于测试parser时候打的测试桩，把parser模块剥离出来进行单独测试。

#### class test-parser parser测试桩

该类中根据已经定义好的BNF，自顶向下递归生成满足检测要求的测试脚本。

``` python
# BNF:
# instruction := step*
# step        := begin detail* end
# begin       := "step" stepname
# stepname    := "Proc:" + name(only alphnum)
# detail      := branch_detail | wait_detail | print_detail | default_detail | goto_detail
# end         := "end step"

def begin():
    salt = "step Proc:" + ''.join(random.sample(string.ascii_letters, 8)) + "\n"
    return salt

def end():
    return "end step\n"

def detail():
    return "PRINT hello\n"

def step():
    t = random.randint(1, 5)
    det = ""
    for i in range(t):
        det += detail()
    return begin() + det + end() + "\n"

def inst():
    t = random.randint(1, 5)
    res = ""
    for i in range(t):
        res += step()
    return res
```

#### class test_split 分词模块测试桩

这个模块测试的是interpreter中的分词系统，随机生成一个带有目标关键词的语言，传入后经过二次映射(translation.txt, dict.txt)传出应该返回的内容，并将其打印出来