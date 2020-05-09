"""
使用webdriver和requests，利用http://www.douqq.com/qqmusic/的api来下载qq音乐
# parse = 'http://www.douqq.com/qqmusic/'   # <title>QQ音乐无损接口api</title>
# driver.get(parse)
# driver.execute_script("return document.querySelector('#mid')").send_keys(url)  # 通过执行js来定位元素，等同于下面的
# # driver.find_element_by_xpath('//*[@id="mid"]').send_keys()
# driver.execute_script("return document.querySelector('#sub')").click()
# music = driver.execute_script("return document.getElementById('mp3_l').text")  # 狗日的写了个js把text给老子清空了，
# # webdriver获取不到text，又不会破解js，操，放弃使用webdriver，使用requests试试
#
# print(music)
"""
from selenium import webdriver, common
import requests
import json
from sys import exit
from urllib.request import urlretrieve
from urllib.error import HTTPError
# import tkinter as tk


class DownloadMusic(object):

    def __init__(self, name):
        """

        Parameters
        ----------
        name
        """
        self.url_search = f'https://y.qq.com/portal/search.html#page=1&searchid=1&' \
            f'remoteplace=txt.yqq.top&t=song&w={name}'
        self.api = 'http://www.douqq.com/qqmusic/qqapi.php'

    def get_qq_url(self):
        """
        获取播放链接
        :return:
        """

        option = webdriver.ChromeOptions()
        option.add_argument('--headless')
        driver = webdriver.Chrome(options=option)  # 让浏览器无界面运行
        driver.implicitly_wait(10)
        driver.get(self.url_search)
        try:
            url = driver.find_element_by_xpath('//*[@id="song_box"]/div[2]/ul[2]/li[1]/div/div[2]/span'
                                               ).find_element_by_tag_name('a').get_attribute('href')  # 先找到上一级的，成功率高
            song_title = driver.find_element_by_xpath('//*[@id="song_box"]/div[2]/ul[2]/li[1]/div/div[2]/span'
                                                      ).find_element_by_tag_name('a').get_attribute('title').strip()
            singer = driver.find_element_by_xpath('//*[@id="song_box"]/div[2]/ul[2]/li[1]/div/div[3]'
                                                  ).get_attribute('title')
        except common.exceptions.NoSuchElementException:
            print('没找到这首歌')
            print(self.url_search)
            return
        finally:
            driver.quit()
        print('歌曲链接：' + url)
        print('获取歌曲：' + song_title)
        print('歌手：' + singer)
        # 处理song_title中间有'|'字符的情况，有命名会报错：
        return {'mid': url, 'song_title': song_title if '|' not in song_title else song_title[0:song_title.index('|')]}

    def get_qq_music(self, data):
        """
        调用解析api
        :param data: get_qq_url的返回值
        :return:
        """

        data_url = {}
        for k, v in data.items():
            if k == 'mid':
                data_url[k] = v
        response = requests.post(self.api, data_url).content
        return response

    def go(self):
        song_dict = self.get_qq_url()
        if song_dict:
            music = self.get_qq_music(song_dict)
            # print(music)
            deserialize = json.loads(music)  # 反序列化
            rep = deserialize.replace(r'\/\/', '//').replace(r'\/', '/')  # url不区分正反斜杠
            dic = json.loads(rep)  # 再反序列化就变成了字典了
            print(dic)
            if dic['mp3_l'] == '' and dic['mv'] == '':
                print('这首歌下载不了，乖乖充钱吧。')
                return
            elif dic['mv'] != '暂无MV' and dic['mv'] != '':
                if dic['mp3_l'] != '':
                    print('这首歌有MV可以下载。')
                else:
                    print('这首歌只有MV可以下载，歌曲需付费下载！')
                ask = input('是否下载MV（输入任意字符开始下载，按回车跳过)?')
                if ask:
                    try:
                        print('开始下载MV...')
                        urlretrieve(dic['mv'], filename=song_dict['song_title'] + '.mp4')
                        print('下载MV成功：' + song_dict['song_title'] + ' 路径：本工具所在路径')
                    except HTTPError as e:
                        print(e)
                        print('下载MV失败')
            if dic['mp3_l'] != '':
                try:
                    print('开始下载歌曲...')
                    urlretrieve(dic['mp3_l'], filename=song_dict['song_title'] + '.mp3')
                    print('下载歌曲成功：' + song_dict['song_title'] + ' 路径：本工具所在路径')
                    return True
                except HTTPError as e:
                    print(e)
                    print('由于版权原因这首歌必须付费下载')
            else:
                print('由于未知原因这首歌不能下载！')
        else:
            print('由于没有找到这首歌，下载失败')


if __name__ == '__main__':

    while True:
        i = input('输入要下载的歌名，或者按回车退出：')
        s = DownloadMusic(i)
        print(s.__doc__)
        print(s.__dict__)
        if i:
            print(i)
            print('开始获取信息：' + i)
            DownloadMusic.go(s)
        else:
            exit()

    # root = tk.Tk()
    # root.title('音乐下载器')
    # root.geometry('300x100')
    # l1 = tk.Label(root, text='歌曲：')
    # l1.pack()
    # e1 = tk.Entry(root)
    # e1.pack()
    #
    # tk.Button(root, text='下载', command=lambda: DownloadMusic(e1.get()).go).pack()
    #
    # root.mainloop()
