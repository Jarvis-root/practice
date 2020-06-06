import mitmproxy.http
from mitmproxy import ctx, http


class CapturedRequest(object):
    def __init__(self, hostname: str):
        self.hostname = hostname

    def request(self, flow: mitmproxy.http.HTTPFlow):  # (Called when) 来自客户端的 HTTP 请求被成功完整读取。
        ctx.log.info("flow.request.host: %s" % flow.request.host)
        if flow.request.host == self.hostname:

            with open('request_info.txt', 'a') as f:
                f.write(flow.request.get_text())


        # if "wd" not in flow.request.query.keys():
        #     ctx.log.warn("can not get search word from %s" % flow.request.pretty_url)
        #     return
        #

        # flow.request.query.set_all("wd", ["360搜索"])
