import asyncio
from time import time

import aiohttp

COLLECT = []
URLS = [
    'https://cn.bing.com/',
    'https://cn.bing.com/',
    'https://cn.bing.com/',
    'https://cn.bing.com/',
]


async def fetch(client, url):
    async with client.get(url) as resp:
        assert resp.status == 200
        return await resp.text()


async def do_job(session, url):
    html = await fetch(session, url)
    COLLECT.append(html[0:15])


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in URLS:
            tasks.append(do_job(session, url))
        coroutines = asyncio.as_completed(tasks)
        for coroutine in coroutines:
            await coroutine

t1 = time()
# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())
r = asyncio.run(main())
print(COLLECT)
t2 = time()

print(t2 - t1)

import requests
t1 = time()
l = []
for u in URLS:
    res = requests.get(u)
    assert 200 == res.status_code
    l.append(res.text[0:15])
print(l)
t2 = time()
print(t2 - t1)


