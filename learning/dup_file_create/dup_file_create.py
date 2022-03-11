import os
import random
import shutil

from faker import Faker

F = Faker('zh-CN')
# Faker.seed(0)
# print(F.pystr(5, 5))
BASE_PATHS = 'C:\\TEST,D:\\TEST'
EXTENSION = 'test-duplicate'
HEAD_SAME_BYTES = '512'


def mkdir(path: str):
    if not path:
        return path
    if not os.path.exists(path):
        os.mkdir(path)
    return path


def write_content(file, content: bytes):
    with open(file, 'wb') as f:
        f.write(content)


def create_duplicate_files(file_count,
                           file_size_bytes,
                           head_same_bytes=0,
                           base_paths=BASE_PATHS,
                           extension: str = EXTENSION):
    # assert file_size_bytes >= head_same_bytes, '文件大小必须大于或等于头部相同字节数'
    text = F.pystr(file_size_bytes, file_size_bytes)
    files = []
    other_bytes = 0
    if file_size_bytes > head_same_bytes:
        text = text[:int(head_same_bytes)]
        other_bytes = file_size_bytes - head_same_bytes
    for _ in range(file_count):
        for base_path in base_paths.split(','):
            if extension == 'random':
                file_path = F.file_path(depth=random.randint(1, 5))
            else:
                file_path = F.file_path(depth=random.randint(1, 5), extension=extension)
            file_name = f'{base_path}{file_path}'.replace('/', '\\')
            d = os.path.dirname(file_name)
            if not os.path.exists(d):
                os.makedirs(d)
            with open(file_name, 'w') as f:
                if file_size_bytes > head_same_bytes:
                    new_str = text + F.pystr(other_bytes, other_bytes)
                    f.write(new_str)
                else:
                    f.write(text)
                print(new_str)
            files.append(file_name)
    return files


def copy_file(abs_filename,
              count,
              base_paths=BASE_PATHS,
              change_file_name=False):
    if not os.path.exists(abs_filename):
        return
    files = []
    for _ in range(count):
        for base_path in base_paths.split(','):
            new_file_path = F.file_path(depth=random.randint(1, 5)).replace('/', '\\')
            file_name = os.path.basename(abs_filename)
            dir_name = f'{base_path}{os.path.dirname(new_file_path)}'
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
    create_duplicate_files(1,15,10, extension='random')