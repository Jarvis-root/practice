import json
import mitmproxy.http
from mitmproxy import ctx, http


class CapturedRequest(object):
    def __init__(self, hostname: str):
        self.hostname = hostname

    def request(self, flow: mitmproxy.http.HTTPFlow):  # (Called when) 来自客户端的 HTTP 请求被成功完整读取。
        ctx.log.info("flow.request.host: %s" % flow.request.host)
        if flow.request.host == self.hostname:
            d = {}
            with open('request_info.txt', 'a') as f:
                for k, v in flow.request.headers.items():
                    d[k] = v
                f.write(json.dumps(d) + '\n')
            with open('request_body.txt', 'a') as f:
                f.write(flow.request.content.decode('utf-8') + '\n')
                
                
addons = [
    CapturedRequest('fanyi.youdao.com')
]

# chrome.exe --proxy-server=127.0.0.1:8080 --ignore-certificate-errors 设置代理地址并强制忽略掉证书错误
# mitmweb -s addons.py
# mitmdump -s addons.py
