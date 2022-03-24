import datetime
import time

import win32timezone  # 这个不能去掉，否则pyinstaller打的包有问题
from win32file import *
from dup_file_create import F


def modify_file_time(file_path, create_time=None, modify_time=None, access_time=None):
    """
    用来修改任意文件的相关时间属性，时间格式：YYYY-MM-DD HH:MM:SS 例如：2019-02-02 00:01:02
    :param file_path: 文件路径名
    :param create_time: 创建时间
    :param modify_time: 修改时间
    :param access_time: 访问时间
    """
    fh = CreateFile(file_path, GENERIC_READ | GENERIC_WRITE, 0, None, OPEN_EXISTING, 0, 0)
    c_time_t = get_time_struct(create_time)
    m_time_t = get_time_struct(modify_time)
    a_time_t = get_time_struct(access_time)
    if c_time_t:
        SetFileTime(fh, datetime.datetime(*c_time_t[:6]), None, None)
    if m_time_t:
        SetFileTime(fh, None, None, datetime.datetime(*m_time_t[:6]))
    if a_time_t:
        SetFileTime(fh, None, datetime.datetime(*a_time_t[:6]), None)
    # createTimes, accessTimes, modifyTimes = GetFileTime(fh)
    # print(createTimes, accessTimes, modifyTimes)
    CloseHandle(fh)
    return True


def random_file_time(file_path, random_create_time=False, random_modify_time=False, random_access_time=False):
    fh = CreateFile(file_path, GENERIC_READ | GENERIC_WRITE, 0, None, OPEN_EXISTING, 0, 0)
    if random_create_time:
        SetFileTime(fh, F.date_time_this_century(), None, None)
    if random_modify_time:
        SetFileTime(fh, None, F.date_time_this_century(), None)
    if random_access_time:
        SetFileTime(fh, None, None, F.date_time_this_century())
    CloseHandle(fh)
    return True


def get_time_struct(times, format_="%Y-%m-%d %H:%M:%S"):
    if not times:
        return
    return time.strptime(times, format_)
