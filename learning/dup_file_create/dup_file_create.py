import os
import random
import shutil

from faker import Faker

F = Faker()
# Faker.seed(0)
# print(F.pystr(5, 5))
BASE_PATHS = 'C:\\TEST,D:\\TEST'
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


def create_duplicate_files(file_count,
                           file_size_bytes,
                           abs_dir=None,
                           base_paths=BASE_PATHS,
                           extension=EXTENSION):
    abs_dir = mkdir(abs_dir)
    text = F.pystr(file_size_bytes, file_size_bytes)
    files = []
    for _ in range(file_count):
        if abs_dir:
            file_name = f'{abs_dir}{os.sep}{F.file_name(extension=extension)}'.replace('/', '\\')
            with open(file_name, 'w') as f:
                f.write(text)
            files.append(file_name)
        else:
            for base_path in base_paths.split(','):
                file_name = f'{base_path}{F.file_path(depth=random.randint(1, 5), extension=extension)}' \
                    .replace('/', '\\')
                d = os.path.dirname(file_name)
                if not os.path.exists(d):
                    os.makedirs(d)
                with open(file_name, 'w') as f:
                    f.write(text)
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
