from common import *
from spiltWord import *

# multi-user control
nowMap = {}

def interpreter(username:str, message:str):
    global dic
    global nowMap
    now = nowMap.get(username, None)
    message = spiltWord(message)
    # get to next stepNode
    if now is None:
        now = stepMap.get('Proc:welcome')
    now = now.next.get(message, now.default)
     # iter every step
    for step in now.steps:
            actions = str(step).split()
            if actions[0] == 'WAIT':
                second = int(actions[1])
            elif actions[0] == 'PRINT':
                mess = dic.get(str(actions[1]))

    #directly go back to root & record user status(leaf node)
    now = now.goto
    #roll back to datamap
    nowMap.update({username:now})
    return mess