import imghdr
import pathlib
from typing import Iterable, List, Union

import cv2
import numpy


def fix_image_size(image: numpy.array, expected_pixels: float = 2E6):
    ratio = numpy.sqrt(expected_pixels / (image.shape[0] * image.shape[1]))
    return cv2.resize(image, (0, 0), fx=ratio, fy=ratio)


def estimate_blur(image: numpy.array, threshold: int = 100):
    if image.ndim == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    blur_map = cv2.Laplacian(image, cv2.CV_64F)
    score = numpy.var(blur_map)
    return blur_map, score, bool(score < threshold)


def pretty_blur_map(blur_map: numpy.array, sigma: int = 5, min_abs: float = 0.5):
    abs_image = numpy.abs(blur_map).astype(numpy.float32)
    abs_image[abs_image < min_abs] = min_abs

    abs_image = numpy.log(abs_image)
    cv2.blur(abs_image, (sigma, sigma))
    return cv2.medianBlur(abs_image, sigma)


def find_images(image_paths: List[Union[str, pathlib.Path]]):
    for path in image_paths:
        if not isinstance(path, pathlib.Path):
            path = pathlib.Path(path)
        if path.is_file():
            absolute = str(path.absolute())
            if imghdr.what(absolute):
                yield absolute
        elif path.is_dir():
            yield from find_images(list(path.iterdir()))


def main(image_paths: list, threshold: int = 100):
    for p in find_images(image_paths):
        try:
            image = fix_image_size(cv2.imread(p))
            m, s, f = estimate_blur(image, threshold)
            print(f'file: {p}, score: {s}, result: {f}')
        except Exception as e:
            print(f'不支持中文路径：{p}')
            print(e)


if __name__ == '__main__':
    # image1 = fix_image_size(cv2.imread(r'D:\TEST1\t01106799eb6ad5611c.jpg'))
    # m, s, f = estimate_blur(image1)
    # print(m)
    # print(s)
    # print(f)
    # p = pretty_blur_map(m)
    # print(p)
    # print(s)
    # cv2.imshow('result', m)
    # cv2.imshow('result', p)
    # cv2.waitKey(0)
    main([r'D:\DupPhoto\john lennon'])