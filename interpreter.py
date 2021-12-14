from common import *

now = stepMap.get('Proc:welcome')

def interpreter(message:str):
    global now
    now = stepMap.get('Proc:welcome')
    if message == 'begin':
        pass
    else:
        now = now.next.get(message)
    for step in now.steps:
            actions = str(step).split()
            if actions[0] == 'WAIT':
                second = int(actions[1])
            elif actions[0] == 'PRINT':
                mess = str(actions[1])
    return mess