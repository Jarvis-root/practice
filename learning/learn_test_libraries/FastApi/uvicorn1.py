async def app(scope, receive, send):
    assert scope['type'] == 'http'
    await send({
        'type': 'http.response.start',
        'status': 200,
        'headers': [
            [b'content-type', b'text/plain'],
            ['Access-Control-Allow-Origin', 'https://postwoman.io/']
        ]
    })
    await send({
        'type': 'http.response.body',
        'body': b'suck a dick!',
    })
import pymysql

# 运行： uvicorn uvicorn1:app
