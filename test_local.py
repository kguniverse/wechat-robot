import parser
from common import *
from spiltWord import *
import random
import string

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

# for parser test
class test_parser:
    def __init__(self):

#         self.shell: str = """
# step Proc:welcome
# PRINT hello
# BRANCH homework Proc:hw
# BRANCH CourseInfo Proc:CourseInfo
# end step
# step Proc:hw
# WAIT 5
# BRANCH homework Proc:hw
# BRANCH CourseInfo Proc:CourseInfo
# end step
# """ 

        self.shell = inst()
        pass
    
    def test(self):
        print(self.shell)
        shelling = parser.parse(self.shell)
        print(shelling)


# for interpreter test
class test_split:
    def __init__(self):
        self.word = "我的作业是什么"
    
    def test(self):
        return spiltWord(self.word)







if __name__ == '__main__':
    tp = test_parser()
    tp.test()
    # ts = test_split()
    # aws = ts.test()
    # print(aws)
    pass