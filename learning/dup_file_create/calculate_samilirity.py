import imghdr
import os

import cv2
import numpy as np

STOP_FLAG = False


def a_hash(image1, image2):
    image1 = cv2.resize(image1, (8, 8))
    image2 = cv2.resize(image2, (8, 8))
    gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
    hash1 = get_hash(gray1)
    hash2 = get_hash(gray2)
    return hamming_distance(hash1, hash2)


def p_hash(image1, image2):
    image1 = cv2.resize(image1, (32, 32))
    image2 = cv2.resize(image2, (32, 32))
    gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
    # 将灰度图转为浮点型，再进行dct变换
    dct1 = cv2.dct(np.float32(gray1))
    dct2 = cv2.dct(np.float32(gray2))
    # 取左上角的8*8，这些代表图片的最低频率
    # 这个操作等价于c++中利用opencv实现的掩码操作
    # 在python中进行掩码操作，可以直接这样取出图像矩阵的某一部分
    dct1_roi = dct1[0:8, 0:8]
    dct2_roi = dct2[0:8, 0:8]
    hash1 = get_hash(dct1_roi)
    hash2 = get_hash(dct2_roi)
    return hamming_distance(hash1, hash2)


# 输入灰度图，返回hash
def get_hash(image):
    avg = np.mean(image)
    h = []
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if image[i, j] > avg:
                h.append(1)
            else:
                h.append(0)
    return h


# 计算汉明距离，越小越接近
def hamming_distance(hash1, hash2):
    num = 0
    for index in range(len(hash1)):
        if hash1[index] != hash2[index]:
            num += 1
    return num


def compare_similarity(base_file, compare_file_path, compare_method=cv2.HISTCMP_CORREL, callback=print):
    if what := imghdr.what(base_file):
        if what == 'gif':
            callback('不支持gif')
            return
    else:
        return

    base = cv2.imread(base_file)
    hsv_base = cv2.cvtColor(base, cv2.COLOR_BGR2HSV)
    h_bins = 50
    s_bins = 60
    hist_size = [h_bins, s_bins]
    h_ranges = [0, 180]
    s_ranges = [0, 256]
    ranges = h_ranges + s_ranges
    channels = [0, 1]

    hist_base = cv2.calcHist([hsv_base], channels, None, hist_size, ranges, accumulate=False)
    cv2.normalize(hist_base, hist_base, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
    callback(f'base_file: {base_file}')
    try:
        global STOP_FLAG
        for root, dirs, files in os.walk(compare_file_path):
            if STOP_FLAG:
                break
            for file in files:
                file_path = f'{root}/{file}'
                if what := imghdr.what(file_path):
                    if what == 'gif':
                        callback(f'不支持gif: {file_path}')
                        continue
                else:
                    continue
                callback('-------------------------------------------------------------')
                callback(f'file: {file_path}')
                if STOP_FLAG:
                    break

                test = cv2.imread(file_path)
                h = a_hash(base, test)
                callback(f'aHash = {h}')
                h = p_hash(base, test)
                callback(f'pHash = {h}')

                hsv_test = cv2.cvtColor(test, cv2.COLOR_BGR2HSV)
                hist_test = cv2.calcHist([hsv_test], channels, None, hist_size, ranges, accumulate=False)
                cv2.normalize(hist_test, hist_test, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
                result = cv2.compareHist(hist_base, hist_test, compare_method)
                callback(f'Hist = {round(result, 2)}')
    finally:
        STOP_FLAG = False


def stop_task():
    global STOP_FLAG
    STOP_FLAG = True


if __name__ == '__main__':
    compare_similarity(r'D:/DupPhoto/same/raw111.gif_000000.jpg', r'D:\DupPhoto\same')
