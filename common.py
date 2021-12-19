# serve as model layer to store data structure


stepMap = {}

class stepNode:
    def __init__(self, name:str):
        self.name = name
        self.steps = []
        self.next = {}
        self.default: stepNode = self
        self.goto: stepNode = self
    
    def addNode(self, stepName: str, condition: str):
        newNode = stepMap.get(stepName, None)
        if newNode is None:
            newNode = stepNode(stepName)
            stepMap.update({stepName: newNode})
        self.next.update({condition: newNode})
    
    def addDefault(self, stepName: str):
        newNode = stepMap.get(stepName, None)
        if newNode is None:
            newNode = stepNode(stepName)
            stepMap.update({stepName: newNode})
        self.default = newNode
        pass

    def addGoto(self, stepName: str):
        newNode = stepMap.get(stepName, None)
        if newNode is None:
            newNode = stepNode(stepName)
            stepMap.update({stepName: newNode})
        self.goto = newNode
        pass

# a map data structure from key value to detail message
class dictionary:
    def __init__(self):
        self.dic = {}
        state:int = 0
        first:str = ""
        second:str = ""
        with open("dict.txt") as fp:
            line = fp.readline().strip()
            while line:
                if state == 0:
                    first = line
                    state = 1
                else:
                    if line == "end":
                        state = 0
                        self.dic.update({first: second})
                        first = ""
                        second = ""
                    else:
                        second = second + line + "\n"
                line = fp.readline().strip()
        pass

    def get(self, key:str):
        return self.dic.get(key, "管理员很懒，还未更新相关内容")

dic = dictionary()


