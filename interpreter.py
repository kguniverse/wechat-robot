from common import *

now:stepNode = stepMap.get('Proc:welcome')

# multi-user control
nowMap = {}

def interpreter(username:str, message:str):
    global dic
    global now
    global nowMap
    # now = stepMap.get('Proc:welcome')
    now = nowMap.get(username, None)
    if now is None:
        now = stepMap.get('Proc:welcome')
    now = now.next.get(message, now.default)
    for step in now.steps:
            actions = str(step).split()
            if actions[0] == 'WAIT':
                second = int(actions[1])
            elif actions[0] == 'PRINT':
                mess = dic.get(str(actions[1]))

    #directly go back to root & record user status
    now = now.goto
    nowMap.update({username:now})
    return mess