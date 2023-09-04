import traceback
from threading import Thread
from tkinter import Tk, Button, IntVar, Checkbutton, StringVar, messagebox
from tkinter.constants import END, DISABLED, NORMAL, HORIZONTAL
from tkinter.filedialog import askdirectory, askopenfilename
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import Entry, LabelFrame, Spinbox, Label, Progressbar, Notebook

import imghdr

from dup_file_create import *
from file_time import *
from dup_picture_create import start_screenshot, Video, stop_screenshot
import picture_transform
from calculate_samilirity import compare_similarity, stop_task
from show_hist import show_image_hist


class DupFileCreateUI:

    def __init__(self, master):
        Label(master, text="文件个数*：").grid(row=2, column=0)
        Label(master, text="文件大小（字节）*：").grid(row=4, column=0)
        Label(master, text="头部相同字节数：").grid(row=6, column=0)
        Label(master, text="文件存放基础路径*：").grid(row=8, column=0)
        Label(master, text="文件目录层级*：").grid(row=10, column=0)
        Label(master, text="文件创建时间：").grid(row=12, column=0)
        Label(master, text="文件修改时间：").grid(row=14, column=0)
        Label(master, text="文件访问时间：").grid(row=16, column=0)
        ext_label = Label(master, text="扩展名：")
        ext_label.grid(row=18, column=0)
        filename_label = Label(master, text="文件名：")
        filename_label.grid(row=20, column=0)

        self.extension = StringVar()
        self.extension.set(EXTENSION)
        self.ext_entry = Entry(master, width=30, textvariable=self.extension)
        self.filename_entry = Entry(master, width=30)

        self.count_entry = Spinbox(master, width=28, validate='focusout',
                                   validatecommand=self.check_count_entry_input, from_=1, to=100)
        self.size_entry = Spinbox(master, width=28, validate='focusout', validatecommand=self.check_size_entry_input,
                                  from_=ONE_MB, to=ONE_GB, increment=ONE_MB)
        self.same_bytes_entry = Spinbox(master, validate='focusout', validatecommand=self.check_same_bytes_entry_input,
                                        width=28, from_=0, to=ONE_MB, increment=512)
        self.path_entry = Entry(master, width=30)
        self.dir_level_entry = Spinbox(master, width=28, from_=1, to=10, validate='focusout',
                                       validatecommand=self.check_dir_level_entry_input)
        self.file_create_time_entry = Entry(master, width=30, validate='focusout',
                                            validatecommand=self.check_file_create_time_entry_input)
        self.file_modify_time_entry = Entry(master, width=30, validate='focusout',
                                            validatecommand=self.check_file_modify_time_entry_input)
        self.file_access_time_entry = Entry(master, width=30, validate='focusout',
                                            validatecommand=self.check_file_access_time_entry_input)

        self.count_entry.grid(row=2, column=1, pady=3)
        self.size_entry.grid(row=4, column=1, pady=3)
        self.same_bytes_entry.grid(row=6, column=1, pady=3)
        self.path_entry.grid(row=8, column=1, pady=3)
        self.dir_level_entry.grid(row=10, column=1, pady=3)
        self.file_create_time_entry.grid(row=12, column=1, pady=3)
        self.file_modify_time_entry.grid(row=14, column=1, pady=3)
        self.file_access_time_entry.grid(row=16, column=1, pady=3)
        self.ext_entry.grid(row=18, column=1, pady=3)
        self.filename_entry.grid(row=20, column=1, pady=3)

        self.desc2 = '默认当前时间'
        self.desc3 = '格式：2019-02-02 00:01:02'

        self.file_create_time_entry['state'] = DISABLED
        self.file_modify_time_entry['state'] = DISABLED
        self.file_access_time_entry['state'] = DISABLED
        self.random_dir_level = IntVar()
        self.random_dir_level.set(0)
        Checkbutton(master, text="随机", variable=self.random_dir_level, onvalue=1, offvalue=0,
                    command=self.click_random_dir_level).grid(row=10, column=2)
        self.random_ext_check = IntVar()
        self.random_ext_check.set(1)
        self.click_random_ext()
        Checkbutton(master, text="随机", variable=self.random_ext_check, onvalue=1, offvalue=0,
                    command=self.click_random_ext).grid(row=18, column=2)
        self.random_filename_check = IntVar()
        self.random_filename_check.set(1)
        self.click_filename_ext()
        Checkbutton(master, text="随机", variable=self.random_filename_check, onvalue=1, offvalue=0,
                    command=self.click_filename_ext).grid(row=20, column=2)
        self.random_create_time = IntVar()
        self.random_create_time.set(1)
        Checkbutton(master, text="随机", variable=self.random_create_time, onvalue=1, offvalue=0,
                    command=self.click_random_create_time).grid(row=12, column=2)
        self.random_modify_time = IntVar()
        self.random_modify_time.set(1)
        Checkbutton(master, text="随机", variable=self.random_modify_time, onvalue=1, offvalue=0,
                    command=self.click_random_modify_time).grid(row=14, column=2)
        self.random_access_time = IntVar()
        self.random_access_time.set(1)
        Checkbutton(master, text="随机", variable=self.random_access_time, onvalue=1, offvalue=0,
                    command=self.click_random_access_time).grid(row=16, column=2)

        self.exe_button1 = Button(master, text='执行', bg='#f0f0f0', width=8, height=1,
                                  command=lambda: Thread(target=self.check_input_and_execute, daemon=True).start())
        self.exe_button1.grid(row=10, column=5, padx=4)

        Button(master, text='选择', bg='#f0f0f0', width=4, height=1,
               command=self.select_dir).grid(row=8, column=2, padx=4)
        self.text1 = ScrolledText(master, width=62, height=15)
        self.text1.grid(row=30, column=0, columnspan=10)
        self.progress_bar = Progressbar(master, length=500, orient=HORIZONTAL, mode='determinate')
        self.progress_bar.grid(row=26, column=0, columnspan=10)

    def check_count_entry_input(self):
        try:
            int(self.count_entry.get())
            return True
        except ValueError:
            # messagebox.showerror(title='温馨提示', message='输入文件个数错误！')
            self.count_entry.delete(0, END)
            return False

    def check_size_entry_input(self):
        try:
            int(self.size_entry.get())
            return True
        except ValueError:
            # messagebox.showerror(title='温馨提示', message='输入文件大小错误！')
            self.size_entry.delete(0, END)
            return False

    def check_same_bytes_entry_input(self):
        try:
            int(self.same_bytes_entry.get())
            return True
        except ValueError:
            # messagebox.showinfo(title='温馨提示', message='输入头部相同字节数错误！')
            self.same_bytes_entry.delete(0, END)
            return False

    def check_dir_level_entry_input(self):
        try:
            n = int(self.dir_level_entry.get())
            if n > 10:
                self.dir_level_entry.set(10)
            return True
        except ValueError:
            # messagebox.showinfo(title='温馨提示', message='文件目录层级输入错误')
            self.dir_level_entry.delete(0, END)
            return False

    def check_file_create_time_entry_input(self):
        v = self.file_create_time_entry.get()
        if v == self.desc2:
            return True
        try:
            get_time_struct(v)
            return True
        except ValueError:
            messagebox.showinfo(title='温馨提示', message='文件创建时间格式错误！')
            return False

    def check_file_modify_time_entry_input(self):
        v = self.file_modify_time_entry.get()
        if v == self.desc2:
            return True
        try:
            get_time_struct(v)
            return True
        except ValueError:
            messagebox.showinfo(title='温馨提示', message='文件修改时间格式错误！')
            return False

    def check_file_access_time_entry_input(self):
        v = self.file_access_time_entry.get()
        if v == self.desc2:
            return True
        try:
            get_time_struct(v)
            return True
        except ValueError:
            messagebox.showinfo(title='温馨提示', message='文件访问时间格式错误！')
            return False

    def click_random_ext(self):
        if self.random_ext_check.get() == 1:
            self.extension.set('')
            self.ext_entry['state'] = DISABLED
        elif self.random_ext_check.get() == 0:
            self.extension.set(EXTENSION)
            self.ext_entry['state'] = NORMAL

    def click_filename_ext(self):
        if self.random_filename_check.get() == 1:
            self.filename_entry['state'] = DISABLED
        elif self.random_filename_check.get() == 0:
            self.filename_entry['state'] = NORMAL

    def click_random_create_time(self):
        if self.random_create_time.get() == 1:
            self.file_create_time_entry.delete(0, END)
            self.file_create_time_entry['state'] = DISABLED
        elif self.random_create_time.get() == 0:
            self.file_create_time_entry['state'] = NORMAL
            self.file_create_time_entry.insert(0, self.desc2)

    def click_random_modify_time(self):
        if self.random_modify_time.get() == 1:
            self.file_modify_time_entry.delete(0, END)
            self.file_modify_time_entry['state'] = DISABLED
        elif self.random_modify_time.get() == 0:
            self.file_modify_time_entry['state'] = NORMAL
            self.file_modify_time_entry.insert(0, self.desc2)

    def click_random_access_time(self):
        if self.random_access_time.get() == 1:
            self.file_access_time_entry.delete(0, END)
            self.file_access_time_entry['state'] = DISABLED
        elif self.random_access_time.get() == 0:
            self.file_access_time_entry['state'] = NORMAL
            self.file_access_time_entry.insert(0, self.desc2)

    def click_random_dir_level(self):
        if self.random_dir_level.get() == 1:
            self.dir_level_entry.set('')
            self.dir_level_entry['state'] = DISABLED
        elif self.random_dir_level.get() == 0:
            self.dir_level_entry['state'] = NORMAL

    def select_dir(self):
        selected_path = self.path_entry.get()
        directory = askdirectory()
        if directory:
            self.path_entry.delete(0, END)
            selected_path = selected_path + ';' + directory
            self.path_entry.insert(0, selected_path.lstrip(';'))

    def executing(self):
        self.progress_bar.start()
        self.exe_button1['state'] = DISABLED
        self.exe_button1['text'] = '执行中'

    def done(self):
        self.progress_bar.stop()
        self.exe_button1['state'] = NORMAL
        self.exe_button1['text'] = '执行'

    def check_input_and_execute(self):
        self.executing()
        self.text1.delete(1.0, END)
        count = self.count_entry.get()
        size = self.size_entry.get()
        same_bytes = self.same_bytes_entry.get()
        dir_level = self.dir_level_entry.get()
        random_create_time = self.random_create_time.get()
        random_modify_time = self.random_modify_time.get()
        random_access_time = self.random_access_time.get()
        file_create_time = self.file_create_time_entry.get()
        file_modify_time = self.file_modify_time_entry.get()
        file_access_time = self.file_access_time_entry.get()
        if file_create_time == self.desc2:
            file_create_time = None
        if file_modify_time == self.desc2:
            file_modify_time = None
        if file_access_time == self.desc2:
            file_access_time = None

        try:
            count = int(count)
        except ValueError:
            messagebox.showinfo(title='温馨提示', message='输入文件个数错误！')
            self.done()
            return
        if not same_bytes:
            same_bytes = 0
        try:
            same_bytes = int(same_bytes)
        except ValueError:
            messagebox.showinfo(title='温馨提示', message='输入头部相同字节数错误！')
            self.done()
            return
        try:
            size = int(size)
        except ValueError:
            messagebox.showinfo(title='温馨提示', message='输入文件大小错误！')
            self.done()
            return
        # try:
        #     get_time_struct(file_create_time)
        # except ValueError:
        #     messagebox.showinfo(title='温馨提示', message='文件创建时间格式错误！')
        #     self.done()
        #     return
        # try:
        #     get_time_struct(file_modify_time)
        # except ValueError:
        #     messagebox.showinfo(title='温馨提示', message='文件修改时间格式错误！')
        #     self.done()
        #     return
        # try:
        #     get_time_struct(file_access_time)
        # except ValueError:
        #     messagebox.showinfo(title='温馨提示', message='文件访问时间格式错误！')
        #     self.done()
        #     return
        if self.random_dir_level.get():
            dir_level = None
        else:
            try:
                dir_level = int(dir_level)
            except ValueError:
                messagebox.showinfo(title='温馨提示', message='文件目录层级输入错误')
                self.done()
                return
        base_paths = self.path_entry.get()
        if self.random_ext_check.get() == 1:
            ext = 'random'
        else:
            ext = self.ext_entry.get()
        if self.random_filename_check.get():
            filename = None
        else:
            filename = self.filename_entry.get()
        if ':' not in base_paths:
            messagebox.showinfo(title='温馨提示', message='基础路径错误！')
            self.done()
            return
        try:
            if not same_bytes:
                ret = create_duplicate_files(count, size, base_paths=base_paths,
                                             extension=ext, filename=filename, dir_depth=dir_level)
            else:
                ret = create_same_head_files(count, size, same_bytes, base_paths=base_paths,
                                             extension=ext, filename=filename, dir_depth=dir_level)
            s = ''
            for file in ret:
                s = s + file + '\n'
                if any([file_create_time, file_modify_time, file_access_time]):
                    modify_file_time(file, file_create_time, file_modify_time, file_access_time)
                if any([random_access_time, random_modify_time, random_create_time]):
                    random_file_time(file, random_create_time, random_modify_time, random_access_time)
            self.text1.insert(END, s)
            # messagebox.showinfo(title='温馨提示', message='执行成功')
        except Exception as e:
            s = str(e)
            self.text1.insert(END, s)
        self.done()


class CopyFileUI:

    def __init__(self, master):
        Label(master, text="源文件绝对路径：").grid(row=16)
        Label(master, text="复制数量：").grid(row=18)
        Label(master, text="文件存放基础路径：").grid(row=20)
        Label(master, text="文件存放目录层级：").grid(row=22)
        # Label(master, text="是否修改文件名：").grid(row=24)

        self.entry1 = Entry(master, width=38)
        self.entry2 = Entry(master, width=38)
        self.entry3 = Entry(master, width=38)
        self.entry4 = Entry(master, width=38)
        self.entry1.grid(row=16, column=1, pady=5)
        self.entry2.grid(row=18, column=1, pady=5)
        self.entry3.grid(row=20, column=1, pady=5)
        self.entry3.insert(0, BASE_PATHS)
        self.entry4.grid(row=22, column=1, pady=5)

        self.flag_modify_file_name = IntVar()
        self.flag_modify_file_name.set(0)
        Checkbutton(master, text='修改文件名', variable=self.flag_modify_file_name, onvalue=1, offvalue=0).grid(row=24,
                                                                                                           column=0)
        self.exe_button2 = Button(master, text='执行', bg='#f0f0f0', width=8, height=1,
                                  command=lambda: Thread(target=self.check_input_and_execute, daemon=True).start())
        self.exe_button2.grid(row=18, column=5, padx=4)
        Button(master, text='选择文件', bg='#f0f0f0', width=8, height=1,
               command=self.select_file).grid(row=16, column=5, padx=4)
        Button(master, text='选择路径', bg='#f0f0f0', width=8, height=1,
               command=self.select_path).grid(row=20, column=5, padx=4)
        self.text1 = ScrolledText(master, width=62, height=25)
        self.text1.grid(row=27, column=0, columnspan=10)
        self.progress_bar = Progressbar(master, length=500, orient=HORIZONTAL, mode='determinate')
        self.progress_bar.grid(row=25, column=0, columnspan=10)

    def select_file(self):
        file = askopenfilename()
        self.entry1.delete(0, END)
        self.entry1.insert(0, file)

    def select_path(self):
        directory = askdirectory()
        self.entry3.delete(0, END)
        self.entry3.insert(0, directory)

    def check_input_and_execute(self):
        self.exe_button2['state'] = DISABLED
        self.exe_button2['text'] = '执行中'

        def done():
            self.exe_button2['state'] = NORMAL
            self.exe_button2['text'] = '执行'

        self.text1.delete(1.0, END)
        path = self.entry1.get()
        if ':' not in path:
            messagebox.showinfo(title='温馨提示', message='路径错误！')
            done()
            return
        count = self.entry2.get()
        try:
            count = int(count)
        except ValueError:
            messagebox.showinfo(title='温馨提示', message='复制数量错误！')
            done()
            return
        base_dir = self.entry3.get()
        if ':' not in base_dir:
            messagebox.showinfo(title='温馨提示', message='文件存放基础路径错误！')
            done()
            return
        depth = self.entry4.get()
        try:
            ret = copy_file(path, count, base_dir, True, depth
                            ) if self.flag_modify_file_name.get() else copy_file(path, count, base_dir, False, depth)
            if not ret:
                return
            s = ''
            for i in ret:
                s = s + i + '\n'
            # messagebox.showinfo(title='温馨提示', message='执行成功')
        except Exception as e:
            s = str(e)
        self.text1.insert(END, s)
        done()


class ModifyFileAttrUI:

    def __init__(self, master):
        Label(master, text="文件绝对路径：").grid(row=2, column=0)
        Label(master, text="文件创建时间：").grid(row=4, column=0)
        Label(master, text="文件修改时间：").grid(row=6, column=0)
        Label(master, text="文件访问时间：").grid(row=8, column=0)

        self.file_entry = Entry(master, width=30)
        self.file_create_time_entry = Entry(master, width=30)
        self.file_modify_time_entry = Entry(master, width=30)
        self.file_access_time_entry = Entry(master, width=30)
        self.file_entry.grid(row=2, column=1, pady=3)
        self.file_create_time_entry.grid(row=4, column=1, pady=3)
        self.file_modify_time_entry.grid(row=6, column=1, pady=3)
        self.file_access_time_entry.grid(row=8, column=1, pady=3)

        self.desc2 = '格式：2019-02-02 00:01:02'
        self.file_create_time_entry.insert(0, self.desc2)
        self.file_modify_time_entry.insert(0, self.desc2)
        self.file_access_time_entry.insert(0, self.desc2)

        Button(master, text='执行', bg='#f0f0f0', width=8, height=1,
               command=self.execute).grid(row=6, column=2, padx=4)
        self.text1 = ScrolledText(master, width=62, height=28)
        self.text1.grid(row=26, column=0, columnspan=10)
        Button(master, text='选择文件', bg='#f0f0f0', width=8, height=1,
               command=self.select_file).grid(row=2, column=2, padx=4)

    def select_file(self):
        file = askopenfilename()
        if file:
            self.file_entry.delete(0, END)
            self.file_entry.insert(0, file)

    def execute(self):
        self.text1.delete(1.0, END)
        file = self.file_entry.get()
        file_create_time = self.file_create_time_entry.get()
        file_modify_time = self.file_modify_time_entry.get()
        file_access_time = self.file_access_time_entry.get()
        if file_create_time == self.desc2:
            file_create_time = None
        if file_modify_time == self.desc2:
            file_modify_time = None
        if file_access_time == self.desc2:
            file_access_time = None
        if not file:
            messagebox.showinfo(title='温馨提示', message='请输入文件')
            return
        if not any([file_create_time, file_modify_time, file_access_time]):
            self.text1.insert(END, '未填写时间')
            return
        try:
            get_time_struct(file_create_time)
        except ValueError:
            messagebox.showinfo(title='温馨提示', message='文件创建时间格式错误！')
            return
        try:
            get_time_struct(file_modify_time)
        except ValueError:
            messagebox.showinfo(title='温馨提示', message='文件修改时间格式错误！')
            return
        try:
            get_time_struct(file_access_time)
        except ValueError:
            messagebox.showinfo(title='温馨提示', message='文件访问时间格式错误！')
            return
        ret = modify_file_time(file, file_create_time, file_modify_time, file_access_time)
        if ret:
            self.text1.insert(END, '成功')
        else:
            self.text1.insert(END, '失败')


class ScreenShotUI:

    def __init__(self, master):
        Label(master, text="图片保存路径：").grid(row=16)
        Label(master, text="截屏持续时间（秒）：").grid(row=18)
        Label(master, text="截屏间隔（秒）：").grid(row=20)
        Label(master, text="图片格式：").grid(row=22)
        # Label(master, text="是否修改文件名：").grid(row=24)

        self.entry1 = Entry(master, width=38)
        self.entry2 = Entry(master, width=38)
        self.entry3 = Entry(master, width=38)
        self.entry4 = Entry(master, width=38)
        self.entry1.grid(row=16, column=1, pady=5)
        self.entry2.grid(row=18, column=1, pady=5)
        self.entry3.grid(row=20, column=1, pady=5)
        self.entry4.grid(row=22, column=1, pady=5)
        self.entry4.insert(0, 'jpg')

        self.exe_button2 = Button(master, text='执行', bg='#f0f0f0', width=8, height=1,
                                  command=lambda: Thread(target=self.check_input_and_execute, daemon=True).start())
        self.exe_button2.grid(row=18, column=4, padx=4)
        Button(master, text='选择路径', bg='#f0f0f0', width=8, height=1,
               command=self.select_path).grid(row=16, column=4, padx=4)
        self.text1 = ScrolledText(master, width=62, height=23)

        def show_end(event):
            self.text1.see(END)
            self.text1.edit_modified(0)

        self.text1.grid(row=27, column=0, columnspan=10)
        self.text1.bind('<<Modified>>', show_end)
        self.execute_flag = False

    def select_path(self):
        directory = askdirectory()
        self.entry1.delete(0, END)
        self.entry1.insert(0, directory)

    def insert_to_text(self, s):
        self.text1.insert(END, s + '\n')

    def check_input_and_execute(self):
        print('check_input_and_execute')
        self.exe_button2['text'] = '停止'

        def done():
            self.exe_button2['text'] = '执行'
            self.insert_to_text('执行结束。')

        try:
            if self.execute_flag:
                stop_screenshot()
                return
            self.execute_flag = True
            self.text1.delete(1.0, END)
            path = self.entry1.get()
            if ':' not in path:
                messagebox.showinfo(title='温馨提示', message='路径错误！')
                done()
                return
            if not os.path.exists(path):
                os.makedirs(path)
            duration = self.entry2.get()
            try:
                duration = float(duration)
            except ValueError:
                messagebox.showinfo(title='温馨提示', message='截屏持续时间错误！')
                done()
                return
            interval = self.entry3.get()
            try:
                interval = float(interval)
            except ValueError:
                messagebox.showinfo(title='温馨提示', message='截屏间隔错误！')
                done()
                return
            ext = self.entry4.get()
            try:
                start_screenshot(self.insert_to_text, path, duration, interval, ext)
                # messagebox.showinfo(title='温馨提示', message='执行成功')
            except Exception as e:
                s = str(e)
                self.insert_to_text(s)
            done()
        finally:
            self.execute_flag = False


class VideoToPicUI:

    def __init__(self, master):
        Label(master, text="图片保存路径：").grid(row=16)
        Label(master, text="源视频路径：").grid(row=18)
        Label(master, text="截取帧间隔：").grid(row=20)
        Label(master, text="图片格式：").grid(row=22)
        # Label(master, text="是否修改文件名：").grid(row=24)

        self.entry1 = Entry(master, width=38)
        self.entry2 = Entry(master, width=38)
        self.entry3 = Entry(master, width=38)
        self.entry4 = Entry(master, width=38)
        self.entry1.grid(row=16, column=1, pady=5)
        self.entry2.grid(row=18, column=1, pady=5)
        self.entry3.grid(row=20, column=1, pady=5)
        self.entry4.grid(row=22, column=1, pady=5)
        self.entry4.insert(0, 'jpg')

        self.exe_button2 = Button(master, text='执行', bg='#f0f0f0', width=8, height=1,
                                  command=lambda: Thread(target=self.check_input_and_execute, daemon=True).start())
        self.exe_button2.grid(row=20, column=4, padx=4)
        Button(master, text='选择路径', bg='#f0f0f0', width=8, height=1,
               command=self.select_path).grid(row=16, column=4, padx=4)
        Button(master, text='选择文件', bg='#f0f0f0', width=8, height=1,
               command=self.select_file).grid(row=18, column=4, padx=4)
        self.text1 = ScrolledText(master, width=62, height=23)

        def show_end(event):
            self.text1.see(END)
            self.text1.edit_modified(0)

        self.text1.grid(row=27, column=0, columnspan=10)
        self.text1.bind('<<Modified>>', show_end)
        self.execute_flag = False
        self.video = Video()

    def select_path(self):
        directory = askdirectory()
        self.entry1.delete(0, END)
        self.entry1.insert(0, directory)

    def select_file(self):
        file = askopenfilename()
        self.entry2.delete(0, END)
        self.entry2.insert(0, file)

    def insert_to_text(self, s):
        self.text1.insert(END, s + '\n')

    def check_input_and_execute(self):
        print('check_input_and_execute')

        def done():
            self.exe_button2['text'] = '执行'
            self.insert_to_text('执行结束。')

        try:
            if self.execute_flag:
                self.video.stop_executing_task()
                return
            self.execute_flag = True
            self.exe_button2['text'] = '停止'
            self.text1.delete(1.0, END)
            path = self.entry1.get()

            if ':' not in path:
                messagebox.showinfo(title='温馨提示', message='路径错误！')
                done()
                return
            if not os.path.exists(path):
                os.makedirs(path)
            file = self.entry2.get()
            if ':' not in path:
                messagebox.showinfo(title='温馨提示', message='源文件路径错误！')
                done()
                return
            frame = self.entry3.get()
            try:
                frame = int(frame)
            except ValueError:
                messagebox.showinfo(title='温馨提示', message='截取帧间隔错误！')
                done()
                return
            ext = self.entry4.get()
            try:
                self.video.to_picture(self.insert_to_text, file, path, frame, ext)
                # messagebox.showinfo(title='温馨提示', message='执行成功')
            except Exception as e:
                s = str(e)
                self.insert_to_text(s)
            done()
        finally:
            self.execute_flag = False


class PictureTransformUI:

    def __init__(self, master):
        Label(master, text="图片路径：").grid(row=16)
        Label(master, text="保存路径：").grid(row=18)
        Label(master, text="变换方式：").grid(row=20)
        # Label(master, text="图片格式：").grid(row=22)
        # Label(master, text="是否修改文件名：").grid(row=24)

        self.entry1 = Entry(master, width=38)
        self.entry2 = Entry(master, width=38)
        self.entry3 = Entry(master, width=38)
        self.entry1.grid(row=16, column=1, pady=5)
        self.entry2.grid(row=18, column=1, pady=5)
        self.entry3.grid(row=20, column=1, pady=5)
        self.entry3.insert(0, '按照支持的所有变换方式进行变换，不支持指定')
        self.entry3['state'] = DISABLED
        self.keep_exif = IntVar()
        self.keep_exif.set(0)
        Checkbutton(master, text="是否保留Exif", variable=self.keep_exif, onvalue=1, offvalue=0, takefocus=True
                    ).grid(row=22, column=0)

        self.exe_button2 = Button(master, text='执行', bg='#f0f0f0', width=8, height=1,
                                  command=lambda: Thread(target=self.check_input_and_execute, daemon=True).start())
        self.exe_button2.grid(row=20, column=4, padx=4)
        Button(master, text='选择路径', bg='#f0f0f0', width=8, height=1,
               command=self.select_path1).grid(row=16, column=4, padx=4)
        Button(master, text='选择路径', bg='#f0f0f0', width=8, height=1,
               command=self.select_path2).grid(row=18, column=4, padx=4)
        self.text1 = ScrolledText(master, width=62, height=23)

        def show_end(event):
            self.text1.see(END)
            self.text1.edit_modified(0)

        self.text1.grid(row=27, column=0, columnspan=10)
        self.text1.bind('<<Modified>>', show_end)
        self.execute_flag = False
        self.stop_flag = False

    def select_path1(self):
        directory = askdirectory()
        self.entry1.delete(0, END)
        self.entry1.insert(0, directory)

    def select_path2(self):
        file = askdirectory()
        self.entry2.delete(0, END)
        self.entry2.insert(0, file)

    def insert_to_text(self, s):
        self.text1.insert(END, s + '\n')

    def done(self):
        self.exe_button2['text'] = '执行'
        self.insert_to_text('执行结束。')

    def execute(self):
        output_path = self.entry2.get()
        keep_exif = False
        if self.keep_exif.get():
            keep_exif = True
        if ':' not in output_path:
            messagebox.showinfo(title='温馨提示', message='保存路径错误！')
            self.done()
            return
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        path = self.entry1.get()
        if not os.path.exists(path):
            messagebox.showinfo(title='温馨提示', message='图片路径错误！')
            self.done()
            return
        for root, dirs, files in os.walk(path):
            if self.stop_flag:
                self.stop_flag = False
                break
            for file in files:
                if self.stop_flag:
                    self.stop_flag = False
                    break
                f = f'{root}/{file}'
                what = imghdr.what(f)
                if what:
                    try:
                        picture_transform.gamma_trans(f, output_path, keep_exif=keep_exif, callback=self.insert_to_text)
                        picture_transform.rotate_image(f, '0', output_path=output_path, keep_exif=keep_exif,
                                                       callback=self.insert_to_text)
                        picture_transform.rotate_image(f, '1', output_path=output_path, keep_exif=keep_exif,
                                                       callback=self.insert_to_text)
                        picture_transform.rotate_image(f, '2', output_path=output_path, keep_exif=keep_exif,
                                                       callback=self.insert_to_text)
                        picture_transform.rotate_image(f, '3', output_path=output_path, keep_exif=keep_exif,
                                                       callback=self.insert_to_text)
                        picture_transform.rotate_image(f, '4', output_path=output_path, keep_exif=keep_exif,
                                                       callback=self.insert_to_text)
                        picture_transform.convert_image(f, 'greener', output_path=output_path, keep_exif=keep_exif,
                                                        callback=self.insert_to_text)
                        picture_transform.convert_image(f, 'gray', output_path=output_path, keep_exif=keep_exif,
                                                        callback=self.insert_to_text)
                        picture_transform.convert_image(f, 'no_color', output_path=output_path, keep_exif=keep_exif,
                                                        callback=self.insert_to_text)
                        picture_transform.convert_image(f, 'other', output_path=output_path, keep_exif=keep_exif,
                                                        callback=self.insert_to_text)
                        picture_transform.resize_image(f, output_path=output_path, keep_exif=keep_exif,
                                                       callback=self.insert_to_text)
                    except Exception as e:
                        s = str(e)
                        self.insert_to_text(f'文件执行报错：{f}')
                        traceback.print_exc()

    def check_input_and_execute(self):
        print('check_input_and_execute')
        if self.execute_flag:
            self.stop_flag = True
            return
        try:
            self.execute_flag = True
            self.exe_button2['text'] = '停止'
            self.text1.delete(1.0, END)
            self.execute()
        finally:
            self.done()
            self.execute_flag = False


class HistCompareUI:

    def __init__(self, master):
        Label(master, text="基准图片路径：").grid(row=16)
        Label(master, text="待对比图片路径：").grid(row=18)
        Label(master, text="说明：").grid(row=20)
        # Label(master, text="图片格式：").grid(row=22)
        # Label(master, text="是否修改文件名：").grid(row=24)

        self.entry1 = Entry(master, width=38)
        self.entry2 = Entry(master, width=38)
        self.entry3 = Entry(master, width=38)
        # self.entry4 = Entry(master, width=38)
        self.entry1.grid(row=16, column=1, pady=5)
        self.entry2.grid(row=18, column=1, pady=5)
        self.entry3.grid(row=20, column=1, pady=5)
        self.entry3.insert(0, '对比图片与基准图片的直方图差异和哈希值')
        self.entry3['state'] = DISABLED
        # self.entry4.grid(row=22, column=1, pady=5)
        # self.entry4.insert(0, 'jpg')

        self.exe_button2 = Button(master, text='执行', bg='#f0f0f0', width=8, height=1,
                                  command=lambda: Thread(target=self.check_input_and_execute, daemon=True).start())
        self.exe_button2.grid(row=20, column=4, padx=4)
        Button(master, text='选择文件', bg='#f0f0f0', width=8, height=1,
               command=self.select_file).grid(row=16, column=4, padx=4)
        Button(master, text='选择路径', bg='#f0f0f0', width=8, height=1,
               command=self.select_path2).grid(row=18, column=4, padx=4)
        self.text1 = ScrolledText(master, width=62, height=23)

        def show_end(event):
            self.text1.see(END)
            self.text1.edit_modified(0)

        self.text1.grid(row=27, column=0, columnspan=10)
        self.text1.bind('<<Modified>>', show_end)
        self.execute_flag = False

    def select_file(self):
        directory = askopenfilename()
        self.entry1.delete(0, END)
        self.entry1.insert(0, directory)

    def select_path2(self):
        file = askdirectory()
        self.entry2.delete(0, END)
        self.entry2.insert(0, file)

    def insert_to_text(self, s):
        self.text1.insert(END, s + '\n')

    def done(self):
        self.exe_button2['text'] = '执行'
        self.insert_to_text('执行结束。')

    def execute(self):
        compare_files = self.entry2.get()
        if not os.path.exists(compare_files):
            messagebox.showinfo(title='温馨提示', message='基准图片路径错误！')
            self.done()
            return
        base_file = self.entry1.get()
        if not os.path.exists(base_file):
            messagebox.showinfo(title='温馨提示', message='基准图片路径错误！')
            self.done()
            return
        compare_similarity(base_file, compare_files, callback=self.insert_to_text)

    def check_input_and_execute(self):
        print('check_input_and_execute')
        if self.execute_flag:
            stop_task()
            self.execute_flag = False
            return
        try:
            self.execute_flag = True
            self.exe_button2['text'] = '停止'
            self.text1.delete(1.0, END)
            try:
                self.execute()
                # messagebox.showinfo(title='温馨提示', message='执行成功')
            except Exception as e:
                s = str(e)
                self.insert_to_text(s)
                raise
            self.done()
        finally:
            self.execute_flag = False


class ShowHistUI:

    def __init__(self, master):
        Label(master, text="图片1：").grid(row=16)
        Label(master, text="图片2：").grid(row=18)
        Label(master, text="说明：").grid(row=20)
        # Label(master, text="图片格式：").grid(row=22)
        # Label(master, text="是否修改文件名：").grid(row=24)

        self.entry1 = Entry(master, width=48)
        self.entry2 = Entry(master, width=48)
        self.entry3 = Entry(master, width=48)
        # self.entry4 = Entry(master, width=38)
        self.entry1.grid(row=16, column=1, pady=5)
        self.entry2.grid(row=18, column=1, pady=5)
        self.entry3.grid(row=20, column=1, pady=5)
        self.entry3.insert(0, '对比图片的平面直方图')
        self.entry3['state'] = DISABLED
        # self.entry4.grid(row=22, column=1, pady=5)
        self.exe_button2 = Button(master, text='执行', bg='#f0f0f0', width=8, height=1,
                                  command=self.execute)
        self.exe_button2.grid(row=20, column=4, padx=4)
        Button(master, text='选择文件', bg='#f0f0f0', width=8, height=1,
               command=self.select_file1).grid(row=16, column=4, padx=4)
        Button(master, text='选择文件', bg='#f0f0f0', width=8, height=1,
               command=self.select_file2).grid(row=18, column=4, padx=4)
        self.text1 = ScrolledText(master, width=62, height=23)

    def select_file1(self):
        directory = askopenfilename()
        self.entry1.delete(0, END)
        self.entry1.insert(0, directory)

    def select_file2(self):
        directory = askopenfilename()
        self.entry2.delete(0, END)
        self.entry2.insert(0, directory)

    def execute(self):
        compare_file1 = self.entry1.get()
        if not os.path.exists(compare_file1):
            messagebox.showinfo(title='温馨提示', message='图片1路径错误！')
            return
        compare_file2 = self.entry2.get()
        if not os.path.exists(compare_file2):
            messagebox.showinfo(title='温馨提示', message='图片2路径错误！')
            return
        show_image_hist(compare_file1, compare_file2)


class MainUI:

    def __init__(self, master):
        self.tk = master
        self.width = 550
        self.height = 560
        self.tk.title("重复文件创建2.0")

        # 放到屏幕中央
        self.ws = self.tk.winfo_screenwidth()
        self.hs = self.tk.winfo_screenheight()
        x = (self.ws / 2) - (self.width / 2)
        y = (self.hs / 2) - (self.height / 2)
        self.tk.geometry('%dx%d+%d+%d' % (self.width, self.height, x, y))

        self.notebook = Notebook(self.tk)
        self.frame_text_file_create_ui = LabelFrame(self.tk)
        self.frame_copy_file_ui = LabelFrame(self.tk)
        self.frame_attr_ui = LabelFrame(self.tk)
        self.frame4 = LabelFrame(self.tk)
        self.frame5 = LabelFrame(self.tk)
        self.frame6 = LabelFrame(self.tk)
        DupFileCreateUI(self.frame_text_file_create_ui)
        # CopyFileUI(self.frame_copy_file_ui)
        ScreenShotUI(self.frame_copy_file_ui)
        # ModifyFileAttrUI(self.frame_attr_ui)
        VideoToPicUI(self.frame_attr_ui)
        PictureTransformUI(self.frame4)
        HistCompareUI(self.frame5)
        ShowHistUI(self.frame6)

        self.notebook.add(self.frame_text_file_create_ui, text=' 指定大小创建 ')
        # self.notebook.add(self.frame_copy_file_ui, text='拷贝多份文件')
        self.notebook.add(self.frame_copy_file_ui, text=' 截屏 ')
        # self.notebook.add(self.frame_attr_ui, text='修改文件属性')
        self.notebook.add(self.frame_attr_ui, text=' 视频截图 ')
        self.notebook.add(self.frame4, text=' 图片变换 ')
        self.notebook.add(self.frame5, text=' 图片相似度对比 ')
        self.notebook.add(self.frame6, text=' 查看直方图 ')
        self.notebook.pack(padx=10, fill='x')
        self.tk.mainloop()


if __name__ == '__main__':
    MainUI(Tk())
