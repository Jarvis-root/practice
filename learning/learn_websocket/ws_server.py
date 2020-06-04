"""
WebSocket的出现打破了HTTP请求和响应只能一对一通信的模式，也改变了服务器只能被动接受客户端请求的状况
目前有很多Web应用是需要服务器主动向客户端发送信息的，例如股票信息的网站可能需要向浏览器发送股票涨停通知，
社交网站可能需要向用户发送好友上线提醒或聊天信息。

WebSocket的特点如下所示：

建立在TCP协议之上，服务器端的实现比较容易。
与HTTP协议有着良好的兼容性，默认端口是80（WS）和443（WSS），通信握手阶段采用HTTP协议，能通过各种 HTTP 代理服务器（不容易被防火墙阻拦）。
数据格式比较轻量，性能开销小，通信高效。
可以发送文本，也可以发送二进制数据。
没有同源策略的限制，客户端（浏览器）可以与任意服务器通信。
"""

import asyncio
import datetime
import random
import websockets


# async def hello(websocket, path):
#     name = await websocket.recv()
#     print(f"< {name}")
#
#     greeting = f"Hello {name}!"
#
#     await websocket.send(greeting)
#     print(f"> {greeting}")
#
# start_server = websockets.serve(hello, 'localhost', 8765)
#
# asyncio.get_event_loop().run_until_complete(start_server)
# asyncio.get_event_loop().run_forever()


async def time(websocket, path):
    while True:
        now = datetime.datetime.utcnow().isoformat() + "Z"
        await websocket.send(now)
        await asyncio.sleep(random.random() * 3)

start_server = websockets.serve(time, "127.0.0.1", 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()