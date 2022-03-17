from pywintypes import Time  # 可以忽视这个 Time 报错（运行程序还是没问题的）
from win32file import *
from win32file import *
import time


def modify_file_time(filePath, createTime=None, modifyTime=None, accessTime=None):
    """
    用来修改任意文件的相关时间属性，时间格式：YYYY-MM-DD HH:MM:SS 例如：2019-02-02 00:01:02
    :param filePath: 文件路径名
    :param createTime: 创建时间
    :param modifyTime: 修改时间
    :param accessTime: 访问时间
    """
    fh = CreateFile(filePath, GENERIC_READ | GENERIC_WRITE, 0, None, OPEN_EXISTING, 0, 0)
    cTime_t = get_time_struct(createTime)
    mTime_t = get_time_struct(modifyTime)
    aTime_t = get_time_struct(accessTime)
    if cTime_t:
        createTimes = Time(cTime_t)
        SetFileTime(fh, createTimes, None, None)
    if mTime_t:
        modifyTimes = Time(mTime_t)
        SetFileTime(fh, None, None, modifyTimes)
    if aTime_t:
        accessTimes = Time(aTime_t)
        SetFileTime(fh, None, accessTimes, None)
    # createTimes, accessTimes, modifyTimes = GetFileTime(fh)
    # print(createTimes, accessTimes, modifyTimes)
    CloseHandle(fh)
    return True


def get_time_struct(times, format="%Y-%m-%d %H:%M:%S"):
    if not times:
        return
    return time.mktime(time.strptime(times, format))


# if __name__ == '__main__':
#     cTime = "2015-12-22 22:51:22"  # 创建时间
#     mTime = "2015-02-22 22:01:22"  # 修改时间
#     aTime = "2015-02-22 22:01:22"  # 访问时间
#     fName = r"D:\TEST\deep\threat\which.mp3"
#
#     offset = (0, 0, 2)
#     r = modify_file_time(fName, cTime, mTime, aTime)
#     if r:
#         print('修改完成')
#     else:
#         print('修改失败')
