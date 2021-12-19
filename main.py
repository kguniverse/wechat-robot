#router

import hashlib
from parser import parse
from typing import Text

import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
from interpreter import interpreter

import receive
import reply

app = FastAPI()


# handler message
@app.post("/wx")
async def chatHandler(rq: Request):
    try:
        webData = await rq.body()
        print ("Handle Post webdata is ", webData)
        recMsg = receive.parse_xml(webData)
        if isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'text':
            toUser = recMsg.FromUserName
            fromUser = recMsg.ToUserName
            content = interpreter(toUser, bytes.decode(recMsg.Content))
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

#test interface
@app.post("/test")
async def gotest(rq: Request):
    webData:str = await rq.body()
    replyMsg = interpreter("123", bytes.decode(webData.Content))
    return PlainTextResponse(replyMsg)

# for debug
if __name__ == '__main__':
    uvicorn.run(app)
