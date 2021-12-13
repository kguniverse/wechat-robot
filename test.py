import parser
from common import *
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


if __name__ == '__main__':
    tp = test_parser()
    tp.test()
    pass