import os
import random
import time

import cv2
import pyautogui

# import win32con
# import win32gui
# import win32print
# import win32ui

STOP_FLAG = False


def screenshot1(path, pic_format='jpg'):
    img = pyautogui.screenshot()
    nowtime = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(time.time()))
    path = f'{path}/{nowtime}_{random.randint(0, 9999)}.{pic_format}'
    img.save(path)
    return path


# def screenshot2(path):
#     # 获取桌面
#     hdesktop = win32gui.GetDesktopWindow()
#     # 分辨率适应
#     hDC = win32gui.GetDC(0)
#     # 横向分辨率
#     width = win32print.GetDeviceCaps(hDC, win32con.DESKTOPHORZRES)
#     # 纵向分辨率
#     height = win32print.GetDeviceCaps(hDC, win32con.DESKTOPVERTRES)
#     # 创建设备描述表
#     desktop_dc = win32gui.GetWindowDC(hdesktop)
#     img_dc = win32ui.CreateDCFromHandle(desktop_dc)
#     # 创建一个内存设备描述表
#     mem_dc = img_dc.CreateCompatibleDC()
#     # 创建位图对象
#     screenshot = win32ui.CreateBitmap()
#     screenshot.CreateCompatibleBitmap(img_dc, width, height)
#     mem_dc.SelectObject(screenshot)
#     # 截图至内存设备描述表
#     mem_dc.BitBlt((0, 0), (width, height), img_dc, (0, 0), win32con.SRCCOPY)
#     # 将截图保存到文件中
#     nowtime = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(time.time()))
#     path = f'{path}/{nowtime}_{random.randint(0, 9999)}.jpg'
#     screenshot.SaveBitmapFile(mem_dc, path)
#     # 内存释放
#     mem_dc.DeleteDC()
#     win32gui.DeleteObject(screenshot.GetHandle())


def start_screenshot(func, save_path, durations, interval=0.5, pic_format='jpg'):
    print('start_screenshot')
    assert isinstance(durations, float)
    assert durations <= 600
    assert interval < durations
    global STOP_FLAG
    while durations > 0:
        durations = durations - interval
        print(durations)
        time.sleep(interval)
        if not STOP_FLAG:
            func(screenshot1(save_path, pic_format))
        else:
            STOP_FLAG = False
            break


def stop_screenshot():
    global STOP_FLAG
    STOP_FLAG = True


class Video:

    def __init__(self) -> None:
        self.execute_flag = False

    def to_picture(self, func, filepath, save_path, frame_interval, pic_format='jpg'):
        if self.execute_flag:
            return
        self.execute_flag = True
        cap = cv2.VideoCapture()
        # VideoCapture::open函数可以从文件获取视频
        cap.open(filepath)
        # 获取视频帧数
        n_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        file_name = os.path.basename(filepath)
        try:
            for i in range(n_frames):
                if not self.execute_flag:
                    return
                ret, frame = cap.read()
                # 每隔frame_interval帧进行一次截屏操作
                if i % frame_interval == 0:
                    imagename = '{}/{}_{:0>6d}.{}'.format(save_path, file_name, i, pic_format)
                    func(imagename)
                    print(imagename)
                    cv2.imwrite(imagename, frame)
        except Exception as e:
            print(e)
            raise
        finally:
            # 执行结束释放资源
            cap.release()
            self.execute_flag = False

    def stop_executing_task(self):
        print('stop_executing_task')
        if not self.execute_flag:
            return
        self.execute_flag = False


def cap_picture(filepath, save_path, frame_interval, pic_format='jpg'):
    cap = cv2.VideoCapture()
    # VideoCapture::open函数可以从文件获取视频
    cap.open(filepath)
    # 获取视频帧数
    n_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    file_name = os.path.basename(filepath)
    try:
        for i in range(n_frames):
            ret, frame = cap.read()
            # 每隔frame_interval帧进行一次截屏操作
            if i % frame_interval == 0:
                imagename = '{}/{}_{:0>6d}.{}'.format(save_path, file_name, i, pic_format)
                cv2.imwrite(imagename, frame)
    except Exception as e:
        print(e)
        raise
    finally:
        # 执行结束释放资源
        cap.release()



def stop_executing_task(self):
    print('stop_executing_task')
    if not self.execute_flag:
        return
    self.execute_flag = False


if __name__ == '__main__':
    Video().to_picture(print, r'D:\DupPhoto\HDRSample.mkv', r'D:\DupPhoto\测试', 10)
