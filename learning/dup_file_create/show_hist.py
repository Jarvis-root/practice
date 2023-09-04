# 画直方图
import cv2
from matplotlib import pyplot as plt


def plot_demo(image):
    plt.hist(image.ravel(), 256, [0, 256])  # numpy的ravel函数功能是将多维数组降为一维数组
    plt.show()


def show_image_hist(file_path1, file_path2):  # 画三通道图像的直方图
    image1 = cv2.imread(file_path1)
    image2 = cv2.imread(file_path2)
    plt.figure(figsize=(16, 8))
    plt.xlim([0, 256])
    # plt.ylim([0, 350000])
    colors = ('b', 'g', 'r')  # 这里画笔颜色的值可以为大写或小写或只写首字母或大小写混合
    plt.subplot(1, 2, 1)  # 子图
    plt.title(file_path1)
    for i, color in enumerate(colors):
        hist = cv2.calcHist([image1], [i], None, [256], [0, 256])  # 计算直方图
        plt.plot(hist, color)
    plt.subplot(1, 2, 2)
    plt.title(file_path2)
    for i, color in enumerate(colors):
        hist = cv2.calcHist([image2], [i], None, [256], [0, 256])
        plt.plot(hist, color)
    plt.show()


# def main(file_path):
#     src = cv2.imread(file_path)
#     cv2.namedWindow('input_image', cv2.WINDOW_NORMAL)
#     cv2.imshow('input_image', src)
#     plot_demo(src)
#     image_hist(src)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()


if __name__ == '__main__':
    show_image_hist(r'F:\ss\DSC00832.JPG', r'F:\ss\DSC00833.JPG')
    # main(r'D:\DupPhoto\STScI-01GA6K5N0X9R63BK72VXVHBTVM.jpg')
