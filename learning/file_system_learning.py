import chardet
import pysnooper


def convert_to_big_endian(little_endian: str):
    lst = [little_endian[i:i + 2] for i in range(0, len(little_endian), 2)]
    lst.reverse()
    return ''.join(lst)


def int_from_bytes(bytes_):
    return int.from_bytes(bytes_, 'little')  # 可以指定字节序


def convert_to_bin_num(big_endian_hex: str):
    return bin(int(big_endian_hex, 16))


def convert_to_hex_num(big_endian_hex: str):
    return hex(int(big_endian_hex, 16))


def hex_to_chars(hex_str: str):
    s = ''
    for i in range(0, len(hex_str), 2):
        n = hex_str[i: i + 2]
        s += chr(int(n, 16))
    return s


def normal_str_to_hex_str(normal_str: str):
    return normal_str.encode('utf-8').hex()


def hex_str_to_normal_str(hex_str: str):
    import codecs
    return codecs.decode(hex_str.encode('utf-8'), 'hex').decode('utf-8')


def read_disk_one_sector_in_hex(disk_num: str, absolute_lba_address: int,
                                bytes_per_sep=16, sep='\n', sector_size=512):
    device_name = f'\\\\.\\PHYSICALDRIVE{disk_num}'
    with open(device_name, 'rb') as disk:
        disk.seek(absolute_lba_address * sector_size, 0)
        data = disk.read(sector_size)
        return data.hex(sep, bytes_per_sep)


def read_disk_one_sector_in_bytes(disk_num: str, absolute_lba_address: int, sector_size=512):
    device_name = f'\\\\.\\PHYSICALDRIVE{disk_num}'
    with open(device_name, 'rb') as disk:
        disk.seek(absolute_lba_address * sector_size, 0)
        data = disk.read(sector_size)
        return data


def find_root_dir_file_fat(disk_num, fat_root_dir_1st_sector, find_removed_file=True, sector_size=512):
    device_name = f'\\\\.\\PHYSICALDRIVE{disk_num}'
    with open(device_name, 'rb') as disk:
        disk.seek(fat_root_dir_1st_sector * sector_size, 0)
        res = {}
        _find_removed_file_fat(disk, res, sector_size, find_removed_file)
        return res


# @pysnooper.snoop()
def _find_removed_file_fat(disk, result, sector_size, find_removed_file=True):
    bytes_ = disk.read(sector_size)
    if int.from_bytes(bytes_, 'little') == 0:
        return
    for i in range(0, len(bytes_), 32):
        b = bytes_[i: i+32]
        hex_str = b.hex()
        if int.from_bytes(b, 'little') == 0:
            break
        if hex_str[23] == 'f'.casefold():  # 排除长文件名
            continue
        if find_removed_file:
            if hex_str.startswith('e5'):  # E5第一字节为删除
                result[b] = hex_str
        else:
            if not hex_str.startswith('e5'):
                result[b[:8].decode('GBK')] = hex_str
    _find_removed_file_fat(disk, result, sector_size, find_removed_file)


if __name__ == '__main__':
    # print(hex_to_chars('4E4557'))
    # print(int_from_bytes(b'\x00\x08\x00\x00'))
    # print(hex_str_to_normal_str(normal_str_to_hex_str('哈哈啦啦啦啊as')))
    # print((read_disk_one_sector_in_hex('3', 8413304)))
    # print((read_disk_one_sector_in_bytes('3', 8413288)).decode())
    print(find_root_dir_file_fat('3', 8413240, find_removed_file=False))  # fat32
    print(find_root_dir_file_fat('2', 1562023, find_removed_file=False))  # fat16
