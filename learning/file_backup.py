import sys


def back_up():
    old_name: str = input('input filename:')
    index = old_name.rfind('.')
    if index > 0:
        postfix = old_name[index:]
        filename = old_name[:index]
    else:
        print('Windows上需要后缀名')
        sys.exit()

    f1 = open(old_name, 'rb')
    # print(f1.seekable())
    # f1.seek(0, 2)  # 改变文件指针，比如a模式可以改到起始位置

    with open(filename + "[备份]" + postfix, 'wb') as f2:
        while True:
            a = f1.read(1024)

            if len(a) == 0:
                break
            f2.write(a)

    f1.close()
    print('Done')


back_up()
