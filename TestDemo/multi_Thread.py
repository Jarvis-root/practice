import threading
import time


# def run():
#     print("run started! at {}".format(time.ctime()))
#     time.sleep(3)
#     print("run finished! at {}".format(time.ctime()))
#
#
# for n in range(3):
#     mythread = threading.Thread(target=run)  # 创建线程
#     mythread.start()
#     # mythread.join()  # 等待线程终止
#     time.sleep(1)



# exitFlag = 0
#
#
# class myThread (threading.Thread):
#     def __init__(self, threadID, name, counter):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.counter = counter
#
#     def run(self):
#         print ("开始线程：" + self.name)
#         print_time(self.name, self.counter)
#         print ("退出线程：" + self.name)
#
#
# def print_time(threadName, delay, count=5):
#     while count:
#         if exitFlag:
#             threadName.exit()
#         time.sleep(delay)
#         print ("%s: %s" % (threadName, time.ctime(time.time())))
#         count -= 1
#
# # 创建新线程
# thread1 = myThread(1, "Thread-1", 1)
# thread2 = myThread(2, "Thread-2", 2)
#
# # 开启新线程
# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()
# print ("退出主线程")


# 创建线程类,假装多线程播放
class MyThread(threading.Thread):
    def __init__(self, func, arg1, arg2, name=''):
        threading.Thread.__init__(self)
        self.name=name
        self.func=func
        self.arg1=arg1
        self.arg2=arg2

    def run(self):
        self.func(self.arg1, self.arg2)


def super_play(file1, time1):
    for i in range(2):
        print ('Start playing： %s! %s' %(file1, time.ctime()))
        time.sleep(time1)


dic = {'爱情买卖.mp3':3,'阿凡达.mp4':5}
# 创建线程
threads = []
files = range(len(dic))
for f, t in dic.items():
    thread = MyThread(super_play, f, t, super_play.__name__)
    threads.append(thread)
if __name__ == '__main__':
    # 启动线程
    for i in files:
        threads[i].start()
    for i in files:
        threads[i].join()
    # 主线程
    print('end:%s' % time.ctime())
