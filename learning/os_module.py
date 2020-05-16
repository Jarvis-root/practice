import os


# os.rename(r'file_backup.py', r'D:\PycharmProjects\practice\learning\file_backup.py')  # 不仅可以改名字还可以移动

# os.remove('温柔[备份].mp3')  # 删了就找不到了，不会放到回收站

# os.mkdir('A')
# os.rmdir('A')

print(os.getcwd())
os.chdir(r'/\learning')  # cd
print(os.getcwd())

print(os.listdir(r'D:\PycharmProjects'))
print(os.path.isdir(r'D:\PycharmProjects'))