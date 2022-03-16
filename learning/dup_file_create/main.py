import traceback
from threading import Thread
from tkinter import Tk, Label, Entry, Button, IntVar, Checkbutton, Frame, Radiobutton, StringVar, messagebox
from tkinter.constants import TOP, END, HORIZONTAL, LEFT, DISABLED, NORMAL
from tkinter.filedialog import askdirectory, askopenfilename
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import Separator

from dup_file_create import *
from file_time import *


class UI:

    def __init__(self):
        self.tk = Tk()
        self.width = 550
        self.height = 560
        self.tk.title("重复文件创建v0.1")

        # 放到屏幕中央
        self.ws = self.tk.winfo_screenwidth()
        self.hs = self.tk.winfo_screenheight()
        x = (self.ws / 2) - (self.width / 2)
        y = (self.hs / 2) - (self.height / 2)
        self.tk.geometry('%dx%d+%d+%d' % (self.width, self.height, x, y))

        self.exe_button1 = None
        self.exe_button2 = None

        self.frame1 = Frame(self.tk)
        self.frame_text_file_create_ui = Frame(self.tk)
        self.frame_copy_file_ui = Frame(self.tk)
        self.frame_modify_file_attr_ui = Frame(self.tk)
        self.text_file_create_ui()
        self.copy_file_ui()
        self.modify_file_attr_ui()
        tag = IntVar()
        Radiobutton(self.frame1, text="指定大小创建", command=lambda: self.change_tab(0), width=11, variable=tag, value=0,
                    bd=1, indicatoron=False).pack(side=LEFT)
        Radiobutton(self.frame1, text="拷贝多份文件", command=lambda: self.change_tab(1), width=10, variable=tag, value=1,
                    bd=1, indicatoron=False).pack(side=LEFT)
        Radiobutton(self.frame1, text="修改文件属性", command=lambda: self.change_tab(2), width=10, variable=tag, value=2,
                    bd=1, indicatoron=False).pack(side=LEFT)
        self.frame1.pack(padx=10, fill='x')
        Separator(self.tk, orient=HORIZONTAL).pack(padx=13, pady=8, fill='x', side=TOP)
        self.frame_text_file_create_ui.pack()

        self.tk.mainloop()

    def change_tab(self, tag):

        self.frame_text_file_create_ui.pack_forget()
        self.frame_copy_file_ui.pack_forget()
        self.frame_modify_file_attr_ui.pack_forget()
        if tag == 0:
            self.frame_text_file_create_ui.pack()
        elif tag == 1:
            self.frame_copy_file_ui.pack()
        elif tag == 2:
            self.frame_modify_file_attr_ui.pack()

    def text_file_create_ui(self):
        # Label(self.frame_text_file_create_ui, text="<创建指定大小的文本文件>").grid(row=0, column=1)
        Label(self.frame_text_file_create_ui, text="文件个数：").grid(row=2, column=0)
        Label(self.frame_text_file_create_ui, text="文件大小（字节）：").grid(row=4, column=0)
        Label(self.frame_text_file_create_ui, text="头部相同字节数：").grid(row=6, column=0)
        Label(self.frame_text_file_create_ui, text="文件存放基础路径：").grid(row=8, column=0)
        Label(self.frame_text_file_create_ui, text="文件目录层级：").grid(row=10, column=0)
        Label(self.frame_text_file_create_ui, text="文件创建时间：").grid(row=12, column=0)
        Label(self.frame_text_file_create_ui, text="文件修改时间：").grid(row=14, column=0)
        Label(self.frame_text_file_create_ui, text="文件访问时间：").grid(row=16, column=0)
        ext_label = Label(self.frame_text_file_create_ui, text="扩展名：")
        ext_label.grid(row=18, column=0)

        extension = StringVar()
        extension.set(EXTENSION)
        count_entry = Entry(self.frame_text_file_create_ui, width=30)
        size_entry = Entry(self.frame_text_file_create_ui, width=30)
        same_bytes_entry = Entry(self.frame_text_file_create_ui, width=30)
        path_entry = Entry(self.frame_text_file_create_ui, width=30)
        dir_level_entry = Entry(self.frame_text_file_create_ui, width=30)
        file_create_time_entry = Entry(self.frame_text_file_create_ui, width=30)
        file_modify_time_entry = Entry(self.frame_text_file_create_ui, width=30)
        file_access_time_entry = Entry(self.frame_text_file_create_ui, width=30)
        ext_entry = Entry(self.frame_text_file_create_ui, width=30, textvariable=extension)
        count_entry.grid(row=2, column=1, pady=3)
        size_entry.grid(row=4, column=1, pady=3)
        same_bytes_entry.grid(row=6, column=1, pady=3)
        path_entry.grid(row=8, column=1, pady=3)
        dir_level_entry.grid(row=10, column=1, pady=3)
        file_create_time_entry.grid(row=12, column=1, pady=3)
        file_modify_time_entry.grid(row=14, column=1, pady=3)
        file_access_time_entry.grid(row=16, column=1, pady=3)
        ext_entry.grid(row=18, column=1, pady=3)

        desc1 = '默认1到5之间随机，最大10'
        desc2 = '格式：2019-02-02 00:01:02'
        # path_entry.insert(0, BASE_PATHS)
        dir_level_entry.insert(0, desc1)
        file_create_time_entry.insert(0, desc2)
        file_modify_time_entry.insert(0, desc2)
        file_access_time_entry.insert(0, desc2)
        random_ext_check = IntVar()
        random_ext_check.set(0)

        def click_random_ext():
            if random_ext_check.get() == 1:
                extension.set('')
                ext_entry['state'] = DISABLED
            elif random_ext_check.get() == 0:
                extension.set(EXTENSION)
                ext_entry['state'] = NORMAL

        Checkbutton(self.frame_text_file_create_ui, text="随机扩展名", variable=random_ext_check, onvalue=1, offvalue=0,
                    command=click_random_ext).grid(row=20, column=0)

        def check_input_and_execute():

            def executing():
                self.exe_button1['state'] = DISABLED
                self.exe_button1['text'] = '执行中'

            def done():
                self.exe_button1['state'] = NORMAL
                self.exe_button1['text'] = '执行'

            executing()
            text1.delete(1.0, END)
            count = count_entry.get()
            size = size_entry.get()
            same_bytes = same_bytes_entry.get()
            dir_level = dir_level_entry.get()
            file_create_time = file_create_time_entry.get()
            file_modify_time = file_modify_time_entry.get()
            file_access_time = file_access_time_entry.get()
            if file_create_time == desc2:
                file_create_time = None
            if file_modify_time == desc2:
                file_modify_time = None
            if file_access_time == desc2:
                file_access_time = None

            try:
                count = int(count)
            except ValueError:
                messagebox.showinfo(title='温馨提示', message='输入文件个数错误！')
                done()
                return
            if not same_bytes:
                same_bytes = 0
            try:
                same_bytes = int(same_bytes)
            except ValueError:
                messagebox.showinfo(title='温馨提示', message='输入头部相同字节数错误！')
                done()
                return
            try:
                size = int(size)
            except ValueError:
                messagebox.showinfo(title='温馨提示', message='输入文件大小错误！')
                done()
                return
            try:
                get_time_struct(file_create_time)
            except ValueError:
                messagebox.showinfo(title='温馨提示', message='文件创建时间格式错误！')
                done()
                return
            try:
                get_time_struct(file_modify_time)
            except ValueError:
                messagebox.showinfo(title='温馨提示', message='文件修改时间格式错误！')
                done()
                return
            try:
                get_time_struct(file_access_time)
            except ValueError:
                messagebox.showinfo(title='温馨提示', message='文件访问时间格式错误！')
                done()
                return
            try:
                if dir_level == desc1:
                    dir_level = None
                else:
                    dir_level = int(dir_level)
            except ValueError:
                messagebox.showinfo(title='温馨提示', message='文件目录层级输入错误')
                done()
                return
            base_paths = path_entry.get()
            if random_ext_check.get() == 1:
                ext = 'random'
            else:
                ext = ext_entry.get()
            if ':' not in base_paths:
                messagebox.showinfo(title='温馨提示', message='基础路径错误！')
                done()
                return
            try:
                if not same_bytes:
                    ret = create_duplicate_files(count, size, base_paths=base_paths,
                                                 extension=ext, dir_depth=dir_level)
                else:
                    ret = create_same_head_files(count, size, same_bytes, base_paths=base_paths,
                                                 extension=ext, dir_depth=dir_level)
                s = ''
                for file in ret:
                    s = s + file + '\n'
                    if any([file_create_time, file_modify_time, file_access_time]):
                        try:
                            modify_file_time(file, file_create_time, file_modify_time, file_access_time)
                        except Exception as e:
                            traceback.print_exc()
                            s = s + str(e) + '\n'
                text1.insert(END, s)
                # messagebox.showinfo(title='温馨提示', message='执行成功')
            except Exception as e:
                s = str(e)
                text1.insert(END, s)
            done()

        self.exe_button1 = Button(self.frame_text_file_create_ui, text='执行', bg='#f0f0f0', width=8, height=1,
                                  command=lambda: Thread(target=check_input_and_execute, daemon=True).start())
        self.exe_button1.grid(row=10, column=5, padx=4)

        def select_dir():
            directory = askdirectory()
            path_entry.delete(0, END)
            path_entry.insert(0, directory)

        Button(self.frame_text_file_create_ui, text='选择目录', bg='#f0f0f0', width=8, height=1,
               command=select_dir).grid(row=8, column=5, padx=4)
        text1 = ScrolledText(self.frame_text_file_create_ui, width=75, height=15)
        text1.grid(row=26, column=0, columnspan=10)

    def copy_file_ui(self):
        # Label(self.frame_copy_file_ui, text="<拷贝多份指定文件>").grid(row=14, column=1)
        Label(self.frame_copy_file_ui, text="源文件绝对路径：").grid(row=16)
        Label(self.frame_copy_file_ui, text="复制数量：").grid(row=18)
        Label(self.frame_copy_file_ui, text="文件存放基础路径：").grid(row=20)
        Label(self.frame_copy_file_ui, text="文件存放目录层级：").grid(row=22)
        Label(self.frame_copy_file_ui, text="是否修改文件名：").grid(row=24)

        entry1 = Entry(self.frame_copy_file_ui, width=38)
        entry2 = Entry(self.frame_copy_file_ui, width=38)
        entry3 = Entry(self.frame_copy_file_ui, width=38)
        entry4 = Entry(self.frame_copy_file_ui, width=38)
        entry1.grid(row=16, column=1, pady=5)
        entry2.grid(row=18, column=1, pady=5)
        entry3.grid(row=20, column=1, pady=5)
        entry3.insert(0, BASE_PATHS)
        entry4.grid(row=22, column=1, pady=5)

        v1 = IntVar()
        v1.set(0)
        v2 = IntVar()
        v2.set(0)

        radio_button1 = Checkbutton(self.frame_copy_file_ui, text='是', variable=v1, onvalue=1, offvalue=0,
                                    command=lambda: radio_button2.deselect() if v2.get() == 1 else 0)
        radio_button2 = Checkbutton(self.frame_copy_file_ui, text='否', variable=v2, onvalue=1, offvalue=0,
                                    command=lambda: radio_button1.deselect() if v1.get() == 1 else 0)
        radio_button1.grid(row=24, column=1)
        radio_button2.grid(row=24, column=2)
        radio_button2.select()

        def check_input_and_execute():
            self.exe_button2['state'] = DISABLED
            self.exe_button2['text'] = '执行中'

            def done():
                self.exe_button2['state'] = NORMAL
                self.exe_button2['text'] = '执行'

            text1.delete(1.0, END)
            path = entry1.get()
            if ':' not in path:
                messagebox.showinfo(title='温馨提示', message='路径错误！')
                done()
                return
            count = entry2.get()
            try:
                count = int(count)
            except ValueError:
                messagebox.showinfo(title='温馨提示', message='复制数量错误！')
                done()
                return
            base_dir = entry3.get()
            if ':' not in base_dir:
                messagebox.showinfo(title='温馨提示', message='文件存放基础路径错误！')
                done()
                return
            depth = entry4.get()
            try:
                ret = copy_file(path, count, base_dir, True, depth
                                ) if v1.get() else copy_file(path, count, base_dir, False, depth)
                if not ret:
                    return
                s = ''
                for i in ret:
                    s = s + i + '\n'
                # messagebox.showinfo(title='温馨提示', message='执行成功')
            except Exception as e:
                s = str(e)
            text1.insert(END, s)
            done()

        self.exe_button2 = Button(self.frame_copy_file_ui, text='执行', bg='#f0f0f0', width=8, height=1,
                                  command=lambda: Thread(target=check_input_and_execute, daemon=True).start())
        self.exe_button2.grid(row=18, column=5, padx=4)

        def select_file():
            file = askopenfilename()
            entry1.delete(0, END)
            entry1.insert(0, file)

        def select_path():
            directory = askdirectory()
            entry3.delete(0, END)
            entry3.insert(0, directory)

        Button(self.frame_copy_file_ui, text='选择文件', bg='#f0f0f0', width=8, height=1,
               command=select_file).grid(row=16, column=5, padx=4)
        Button(self.frame_copy_file_ui, text='选择路径', bg='#f0f0f0', width=8, height=1,
               command=select_path).grid(row=20, column=5, padx=4)
        text1 = ScrolledText(self.frame_copy_file_ui, width=75, height=25)
        text1.grid(row=25, column=0, columnspan=10)

    def modify_file_attr_ui(self):
        Label(self.frame_modify_file_attr_ui, text="文件绝对路径：").grid(row=2, column=0)
        Label(self.frame_modify_file_attr_ui, text="文件创建时间：").grid(row=4, column=0)
        Label(self.frame_modify_file_attr_ui, text="文件修改时间：").grid(row=6, column=0)
        Label(self.frame_modify_file_attr_ui, text="文件访问时间：").grid(row=8, column=0)

        file_entry = Entry(self.frame_modify_file_attr_ui, width=30)
        file_create_time_entry = Entry(self.frame_modify_file_attr_ui, width=30)
        file_modify_time_entry = Entry(self.frame_modify_file_attr_ui, width=30)
        file_access_time_entry = Entry(self.frame_modify_file_attr_ui, width=30)
        file_entry.grid(row=2, column=1, pady=3)
        file_create_time_entry.grid(row=4, column=1, pady=3)
        file_modify_time_entry.grid(row=6, column=1, pady=3)
        file_access_time_entry.grid(row=8, column=1, pady=3)

        desc2 = '格式：2019-02-02 00:01:02'
        file_create_time_entry.insert(0, desc2)
        file_modify_time_entry.insert(0, desc2)
        file_access_time_entry.insert(0, desc2)

        def execute():
            text1.delete(1.0, END)
            file = file_entry.get()
            file_create_time = file_create_time_entry.get()
            file_modify_time = file_modify_time_entry.get()
            file_access_time = file_access_time_entry.get()
            if file_create_time == desc2:
                file_create_time = None
            if file_modify_time == desc2:
                file_modify_time = None
            if file_access_time == desc2:
                file_access_time = None
            if not file:
                messagebox.showinfo(title='温馨提示', message='请输入文件')
            if not any([file_create_time, file_modify_time, file_access_time]):
                text1.insert(END, '未填写时间')
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
                text1.insert(END, '成功')
            else:
                text1.insert(END, '失败')

        Button(self.frame_modify_file_attr_ui, text='执行', bg='#f0f0f0', width=8, height=1,
               command=execute).grid(row=6, column=2, padx=4)
        text1 = ScrolledText(self.frame_modify_file_attr_ui, width=75, height=15)
        text1.grid(row=26, column=0, columnspan=10)


if __name__ == '__main__':
    UI()
