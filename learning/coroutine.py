"""
协程学习
首先consumer函数是一个generator,在开始执行之后：

调用next(c)启动生成器；
进入do_work，这是一个递归调用，其内部将url传递给consumer，由consumer来发出请求，获取到html信息，返回给produce,
produce解析html，获取url数据，继续生产url，
当所有的url都在history_urls中，也就是说我们已经爬取了所有的url地址，结束递归调用
调用c.close()，关闭consumer，整个过程结束。
可以看到，我们的整个流程无锁，由一个线程执行，produce和consumer协作完成任务，所以称为“协程”，而非线程的抢占式多任务。
"""

from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse


start_url = 'https://www.cnblogs.com'
trust_host = 'www.cnblogs.com'
ignore_path = []
history_urls = []


def parse_html(html):
    soup = BeautifulSoup(html, "lxml")
    print(soup.title)
    links = soup.find_all('a', href=True)
    return (a['href'] for a in links if a['href'])


def parse_url(url):
    url = url.strip()

    if url.find('#') >= 0:
        url = url.split('#')[0]
    if not url:
        return None
    if url.find('javascript:') >= 0:
        return None

    for f in ignore_path:
        if f in url:
            return None
    if url.find('http') < 0:
        url = start_url + url
        return url
    parse = urlparse(url)
    if parse.hostname == trust_host:
        return url


def consumer():
    html = ''
    while True:
        url = yield html
        if url:
            print('[CONSUMER] Consuming %s...' % url)
            rsp = requests.get(url)
            html = rsp.content


def produce(c):
    next(c)

    def do_work(urls):
        for u in urls:
            if u not in history_urls:
                history_urls.append(u)
                print('[PRODUCER] Producing %s...' % u)
                html = c.send(u)
                results = parse_html(html)
                work_urls = (x for x in map(parse_url, results) if x)
                do_work(work_urls)

    do_work([start_url])
    c.close()


if __name__ == '__main__':
    cons = consumer()
    produce(cons)
    print(len(history_urls))
