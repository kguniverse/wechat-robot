import parser
from common import *
from spiltWord import *
class test_parser:
    def __init__(self):
        self.shell: str = """
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
"""
        pass
    
    def test(self):
        shelling = parser.parse(self.shell)
        print(shelling)

class test_split:
    def __init__(self):
        self.word = "老子的作业是什么"
    
    def test(self):
        return spiltWord(self.word)


if __name__ == '__main__':
    # tp = test_parser()
    # tp.test()
    ts = test_split()
    aws = ts.test()
    print(aws)
    pass