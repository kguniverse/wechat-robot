stepMap = {}

class stepNode:
    steps = []
    next = {}
    name:str
    def __init__(self, name:str):
        self.name = name
    
    def addNode(self, stepName: str, condition: str):
        newNode = stepMap.get(stepName, None)
        if newNode is None:
            newNode = stepNode(stepName)
            stepMap.update({stepName: newNode})
        self.next.update({condition: newNode})
