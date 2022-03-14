import os
import random
import shutil
from string import ascii_letters
from faker import Faker

F = Faker()
# Faker.seed(0)
# print(F.pystr(5, 5))
BASE_PATHS = 'D:\\TEST'
EXTENSION = 'test-duplicate'


def mkdir(path: str):
    if not path:
        return path
    if not os.path.exists(path):
        os.mkdir(path)
    return path


def write_content(file, content: bytes):
    with open(file, 'wb') as f:
        f.write(content)


def yield_base_path(base_paths: str):
    p = base_paths.split(',')
    while True:
        yield random.choice(p)


def yield_letter():
    for n in ascii_letters:
        yield n


def create_duplicate_files(file_count,
                           file_size_bytes,
                           head_same_bytes=0,
                           base_paths=BASE_PATHS,
                           extension: str = EXTENSION):
    files = []
    gen_letter = yield_letter()
    gen_base_path = yield_base_path(base_paths)
    one_mb = 1048576

    # 生成文件名：
    for _ in range(file_count):
        if extension == 'random':
            file_path = F.file_path(depth=random.randint(1, 5))
        else:
            file_path = F.file_path(depth=random.randint(1, 5), extension=extension)
        file_name = f'{next(gen_base_path)}{file_path}'.replace('/', '\\')
        d = os.path.dirname(file_name)
        if not os.path.exists(d):
            os.makedirs(d)
        files.append(file_name)

    text_one_mb = F.pystr(one_mb, one_mb)
    size_n = file_size_bytes // one_mb
    size_m = file_size_bytes % one_mb
    # 创建第一个文件，后面的文件拷贝第一个
    if file_size_bytes > one_mb:  # 大于1MB，使用a模式写，避免占用大量内存
        with open(files[0], 'a') as f:
            for _ in range(size_n):
                f.write(text_one_mb)
            if size_m:
                f.write(text_one_mb[:size_m])
    else:
        text = F.pystr(file_size_bytes, file_size_bytes)
        with open(files[0], 'w') as f:
            f.write(text)

    text_same_head = ''
    if 0 < head_same_bytes < file_size_bytes:
        with open(files[0]) as f0:
            text_same_head = f0.read(head_same_bytes)
            text_same_head = text_same_head.replace(text_same_head[-1], next(gen_letter))
    for i, file_name in enumerate(files):
        if i == 0:
            continue
        if 0 < head_same_bytes < file_size_bytes:  # 支持头字节相同，其他不同
            assert 52 >= file_count, '指定头部字节相同时，每次最大只能创建52个文件'
            assert one_mb >= head_same_bytes, f'头部相同字节最大支持{one_mb}字节'
            if file_size_bytes > one_mb:
                with open(file_name, 'a') as f:
                    f.write(text_same_head)
                    left = file_size_bytes - len(text_same_head)
                    size_n = left // one_mb
                    size_m = left % one_mb
                    text_one_mb = F.pystr(one_mb, one_mb)
                    for n in range(size_n):
                        f.write(text_one_mb)
                    if size_m:
                        f.write(text_one_mb[:size_m])
            else:
                text = F.pystr(file_size_bytes, file_size_bytes)
                text_same_head = text_same_head + text
                with open(files[0], 'w') as f:
                    f.write(text)
        else:
            shutil.copy2(files[0], file_name)

    with open(files[0]) as f, open(files[1]) as f1:
        r1 = f.read(head_same_bytes+1)
        r2 = f1.read(head_same_bytes+1)
        if r1[:head_same_bytes] == r2[:head_same_bytes] :
            print(111)
        if r1[-1] != r2[-1]:
            print(222)
    return files


def copy_file(abs_filename,
              count,
              base_paths=BASE_PATHS,
              change_file_name=False):
    gen_base_path = yield_base_path(base_paths)
    if not os.path.exists(abs_filename):
        return
    files = []
    for _ in range(count):
        new_file_path = F.file_path(depth=random.randint(1, 5)).replace('/', '\\')
        file_name = os.path.basename(abs_filename)
        dir_name = f'{next(gen_base_path)}{os.path.dirname(new_file_path)}'
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
        if not change_file_name:
            d = shutil.copy2(abs_filename, f'{dir_name}\\{file_name}')
        else:
            ext = file_name.split('.')[-1]
            new_name = F.file_name(extension=ext)
            d = shutil.copy2(abs_filename, f'{dir_name}\\{new_name}')
        files.append(d)

    return files


if __name__ == '__main__':
    create_duplicate_files(2, 1024, 512, extension='random')
