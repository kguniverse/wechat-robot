from typing import Text
from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse

import hashlib
import uvicorn
import receive, reply

app = FastAPI()


# handler
@app.post("/wx")
async def handler(rq: Request):
    try:
        webData = await rq.body()
        print ("Handle Post webdata is ", webData)
        recMsg = receive.parse_xml(webData)
        if isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'text':
            toUser = recMsg.FromUserName
            fromUser = recMsg.ToUserName
            content = "test"
            replyMsg = reply.TextMsg(toUser, fromUser, content)
            return PlainTextResponse(replyMsg.send())
        else:
            print ("暂且不处理")
            return PlainTextResponse("success")
    except Exception as ep:
        return ep.args

if __name__ == '__main__':
    uvicorn.run(app)
