import urllib.request
import urllib.parse
import re
import time


def get_html(url, header):
    request = urllib.request.Request(url, headers=header)
    response = urllib.request.urlopen(request)
    html = response.read().decode("gbk")

    return html


def getaddressofpic(html):
    r_key = "<img alt=\"(.*?)\" src=\"(.*?)\" />"
    key = re.compile(r_key)

    piclist = re.findall(key, html)

    return piclist


def saving(piclist):
    for each in piclist:
        address = each[1]
        name = each[0]
        print(name)
        print(address)
        urllib.request.urlretrieve(address, "d://pachong/%s.jpg" % name)


def spider():
    for num in range(5550, 5580):
        if num % 10 != 3:
            url = "http://www.meizitu.com/a/" + str(num) + ".html"

            header = {"User-Agent":
                      "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                      " Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134"}

            html = get_html(url, header)

            piclist = getaddressofpic(html)

            saving(piclist)

        else:
            url = "http://www.meizitu.com/a//" + str(num) + ".html"

            header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134"}

            html = get_html(url, header)

            pic_list = getaddressofpic(html)

            saving(pic_list)

        time.sleep(60)


if __name__ == "__main__":
    spider()

print("爬取成功！")
