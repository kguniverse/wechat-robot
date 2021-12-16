from common import *

now:stepNode = stepMap.get('Proc:welcome')

def interpreter(message:str):
    global dic
    global now
    now = stepMap.get('Proc:welcome')
    if message == 'begin':
        pass
    else:
        now = now.next.get(message, now.default)
    for step in now.steps:
            actions = str(step).split()
            if actions[0] == 'WAIT':
                second = int(actions[1])
            elif actions[0] == 'PRINT':
                mess = dic.get(str(actions[1]))
    now = now.goto
    return mess