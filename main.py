from typing import Text
from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse

import hashlib
import uvicorn
import receive, reply
from parser import parse

app = FastAPI()


# handler chat
@app.post("/wx")
async def chatHandler(rq: Request):
    try:
        webData = await rq.body()
        print ("Handle Post webdata is ", webData)
        recMsg = receive.parse_xml(webData)
        if isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'text':
            toUser = recMsg.FromUserName
            fromUser = recMsg.ToUserName
            # if bytes.decode(recMsg.Content) == '王乾凱是傻子':
            content = "张裕是傻子"
            # else:
            content = bytes.decode(recMsg.Content)
            replyMsg = reply.TextMsg(toUser, fromUser, content)
            return PlainTextResponse(replyMsg.send())
        else:
            print ("暂且不处理")
            return PlainTextResponse("success")
    except Exception as ep:
        return ep.args


# handler config
@app.post("/config")
async def configHandler(rq: Request):
    webData = await rq.body()
    webStr = bytes.decode(webData)
    print("config shell is", webStr)
    parse(str(webStr))
    return PlainTextResponse("parse success")
    pass

if __name__ == '__main__':
    uvicorn.run(app)
