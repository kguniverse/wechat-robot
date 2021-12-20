import parser
from common import *
from spiltWord import *
import random
import string

# stepName = Combine("Proc:" + Word(alphas))
# branchInput = Word(alphas)
# branch_detail = ("BRANCH" + branchInput.setResultsName("condition") + stepName.setResultsName("sonName")).setParseAction(stepBranch)
# wait_detail = ("WAIT" + Word(nums).setResultsName("wait_time")).setParseAction(stepWait)
# print_detail = ("PRINT" + Word(alphanums).setResultsName("print_str")).setParseAction(stepPrint)
# default_detail = ("DEFAULT" + stepName.setResultsName("sonName")).setParseAction(stepDefault)
# goto_detail = ("GOTO" + stepName.setResultsName("sonName")).setParseAction(stepGoto)
# detail = branch_detail | wait_detail | print_detail | default_detail | goto_detail
# begin = ("step" + stepName.setResultsName("fatherName")).setParseAction(stepCheck)
# end = Literal("end") + Literal("step")
# step = begin + OneOrMore(detail) + end
# instruction = OneOrMore(step)
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

class test_split:
    def __init__(self):
        self.word = "老子的作业是什么"
    
    def test(self):
        return spiltWord(self.word)







if __name__ == '__main__':
    tp = test_parser()
    tp.test()
    # ts = test_split()
    # aws = ts.test()
    # print(aws)
    pass