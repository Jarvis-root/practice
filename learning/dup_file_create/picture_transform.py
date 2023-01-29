import os

import numpy as np
import cv2


def calc():
    img = cv2.imread(r'D:\DupPhoto\iCloud1\iCloud1\IMG_0404.JPG')

    # 分通道计算每个通道的直方图
    hist_b = cv2.calcHist([img], [0], None, [256], [0, 256])
    hist_g = cv2.calcHist([img], [1], None, [256], [0, 256])
    hist_r = cv2.calcHist([img], [2], None, [256], [0, 256])


# 定义Gamma矫正的函数
def gamma_trans(filename, output_path, gamma=0.5):
    # 具体做法是先归一化到1，然后gamma作为指数值求出新的像素值再还原
    gamma_table = [np.power(x / 255.0, gamma) * 255.0 for x in range(256)]
    gamma_table = np.round(np.array(gamma_table)).astype(np.uint8)
    img = cv2.imread(filename)
    file_name = os.path.basename(filename)
    # 实现这个映射用的是OpenCV的查表函数
    img_corrected = cv2.LUT(img, gamma_table)
    f = f'{output_path}/{"-[GAMMA_TRANS].".join(file_name.split("."))}'
    print(f)
    cv2.imwrite(f, img_corrected)
    return f


# 变绿，变灰，变暗
def convert_image(filename, method='greener', output_path=None):
    img = cv2.imread(filename)
    # 通过cv2.cvtColor把图像从BGR转换到HSV
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    file_name = os.path.basename(filename)
    if not output_path:
        output_path = os.path.dirname(filename)
    f = ''
    if method == 'greener':
        # H空间中，绿色比黄色的值高一点，所以给每个像素+15，黄色的树叶就会变绿
        turn_green_hsv = img_hsv.copy()
        turn_green_hsv[:, :, 0] = (turn_green_hsv[:, :, 0] + 15) % 180
        turn_green_img = cv2.cvtColor(turn_green_hsv, cv2.COLOR_HSV2BGR)
        f = f'{output_path}/{"-[GREENER].".join(file_name.split("."))}'
        print(f)
        cv2.imwrite(f, turn_green_img)
    elif method == 'gery':
        # 减小饱和度会让图像损失鲜艳，变得更灰
        colorless_hsv = img_hsv.copy()
        colorless_hsv[:, :, 1] = 0.5 * colorless_hsv[:, :, 1]
        colorless_img = cv2.cvtColor(colorless_hsv, cv2.COLOR_HSV2BGR)
        f = f'{output_path}/{"-[GERY].".join(file_name.split("."))}'
        print(f)
        cv2.imwrite(f, colorless_img)
    else:
        # 减小明度为原来一半
        darker_hsv = img_hsv.copy()
        darker_hsv[:, :, 2] = 0.5 * darker_hsv[:, :, 2]
        darker_img = cv2.cvtColor(darker_hsv, cv2.COLOR_HSV2BGR)
        f = f'{output_path}/{"-[DARKER].".join(file_name.split("."))}'
        print(f)
        cv2.imwrite(f, darker_img)
    return f


# 裁切放大，旋转
def rotate_image(filename, method='1', output_path=None):
    img = cv2.imread(filename)
    file_name = os.path.basename(filename)
    if not output_path:
        output_path = os.path.dirname(filename)
    theta = 15 * np.pi / 180
    shape = img.shape
    x = shape[0]
    y = shape[1]
    if method == '0':
        rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
        f = f'{output_path}/{"-[6666666].".join(file_name.split("."))}'
        print(f)
        cv2.imwrite(f, rotated)

        rotated = cv2.rotate(img, cv2.ROTATE_180)
        f = f'{output_path}/{"-[ROTATE_180].".join(file_name.split("."))}'
        print(f)
        cv2.imwrite(f, rotated)

        rotated = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
        f = f'{output_path}/{"-[ROTATE_90_COUNTERCLOCKWISE].".join(file_name.split("."))}'
        print(f)
        cv2.imwrite(f, rotated)
    elif method == '1':
        # 沿着横纵轴放大1.1倍，然后平移(0,0)，最后沿原图大小截取，等效于裁剪并放大
        m_crop = np.array([
            [1.1, 0, 0],
            [0, 1.1, 0]
        ], dtype=np.float32)

        img_1 = cv2.warpAffine(img, m_crop, (y-200, x-200))
        f = f'{output_path}/{"-[LOOM].".join(file_name.split("."))}'
        print(f)
        cv2.imwrite(f, img_1)
    elif method == '2':
        # x轴的剪切变换，角度15°
        m_shear = np.array([
            [1, np.tan(theta), 0],
            [0, 1, 0]
        ], dtype=np.float32)
        f = f'{output_path}/{"-[ROTATE1].".join(file_name.split("."))}'
        print(f)
        img_sheared = cv2.warpAffine(img, m_shear, (0, 0))
        cv2.imwrite(f, img_sheared)
    elif method == '3':
        # 顺时针旋转，角度15°
        m_rotate = np.array([
            [np.cos(theta), -np.sin(theta), 0],
            [np.sin(theta), np.cos(theta), 0]
        ], dtype=np.float32)
        f = f'{output_path}/{"-[ROTATE2].".join(file_name.split("."))}'
        print(f)
        img_rotated = cv2.warpAffine(img, m_rotate, (0, 0))
        cv2.imwrite(f, img_rotated)
    else:
        # 某种变换，具体旋转+缩放+旋转组合可以通过SVD分解理解
        m = np.array([
            [1, 1.5, -400],
            [0.5, 2, -100]
        ], dtype=np.float32)
        f = f'{output_path}/{"-[ROTATE3].".join(file_name.split("."))}'
        print(f)
        img_transformed = cv2.warpAffine(img, m, (0, 0))
        cv2.imwrite(f, img_transformed)
    return f


def resize_image(filename, length=200, width=200, output_path=None):
    img = cv2.imread(filename)
    file_name = os.path.basename(filename)
    if not output_path:
        output_path = os.path.dirname(filename)
    img_1 = cv2.resize(img, (length, width))
    img_2 = cv2.resize(img_1, (0, 0), fx=0.5, fy=0.5,
                       interpolation=cv2.INTER_NEAREST)
    # img_3 = cv2.copyMakeBorder(img_2, 50, 50, 0, 0, cv2.BORDER_CONSTANT, value=(0, 0, 0))
    f = f'{output_path}/{"-[RESIZE].".join(file_name.split("."))}'
    print(f)
    cv2.imwrite(f, img_2)
    return f


if __name__ == '__main__':
    # convert_image(r'D:\DupPhoto\iCloud1\iCloud1\IMG_0766.JPEG', '111')
    # resize_image(r'D:\DupPhoto\iCloud1\iCloud1\IMG_0336.JPG')
    rotate_image(r'D:\DupPhoto\iCloud1\iCloud1\IMG_0336.JPG', '0', output_path=r'D:\DupPhoto\same')
