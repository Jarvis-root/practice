from threading import Thread
from tkinter import Tk, Button, IntVar, Checkbutton, Radiobutton, StringVar, messagebox
from tkinter.constants import END, LEFT, DISABLED, NORMAL
from tkinter.filedialog import askdirectory, askopenfilename
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import Entry, LabelFrame, Spinbox, Label, Progressbar

from dup_file_create import *
from file_time import *


class TextFileCreateUI:

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

        self.extension = StringVar()
        self.extension.set(EXTENSION)
        self.ext_entry = Entry(master, width=30, textvariable=self.extension)

        self.count_entry = Spinbox(master, width=28, validate='focusout',
                                   validatecommand=self.check_count_entry_input, from_=1, to=100)
        self.size_entry = Spinbox(master, width=28, validate='focusout', validatecommand=self.check_size_entry_input,
                                  from_=ONE_MB, to=ONE_GB, increment=ONE_MB)
        self.same_bytes_entry = Spinbox(master, validate='focusout', validatecommand=self.check_same_bytes_entry_input,
                                        width=28, from_=0, to=ONE_MB, increment=512)
        self.path_entry = Entry(master, width=30, validate='focusout', validatecommand=self.check_path_entry_input)
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

        self.desc2 = '格式：2019-02-02 00:01:02'
        # path_entry.insert(0, BASE_PATHS)
        self.file_create_time_entry.insert(0, self.desc2)
        self.file_modify_time_entry.insert(0, self.desc2)
        self.file_access_time_entry.insert(0, self.desc2)
        self.random_ext_check = IntVar()
        self.random_ext_check.set(0)
        Checkbutton(master, text="随机扩展名", variable=self.random_ext_check, onvalue=1, offvalue=0,
                    command=self.click_random_ext).grid(row=20, column=0)

        self.exe_button1 = Button(master, text='执行', bg='#f0f0f0', width=8, height=1,
                                  command=lambda: Thread(target=self.check_input_and_execute, daemon=True).start())
        self.exe_button1.grid(row=10, column=5, padx=4)

        Button(master, text='选择目录', bg='#f0f0f0', width=8, height=1,
               command=self.select_dir).grid(row=8, column=5, padx=4)
        self.text1 = ScrolledText(master, width=75, height=15)
        self.text1.grid(row=26, column=0, columnspan=10)

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
            int(self.dir_level_entry.get())
            return True
        except ValueError:
            # messagebox.showinfo(title='温馨提示', message='文件目录层级输入错误')
            self.dir_level_entry.delete(0, END)
            return False

    def check_path_entry_input(self):
        v = self.path_entry.get()
        if not v:
            messagebox.showwarning(title='温馨提示', message='请选择或输入基础路径')
            return False
        if ':' not in v:
            messagebox.showerror(title='温馨提示', message='基础路径错误！')
            self.path_entry.delete(0, END)
            return False
        return True

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

    def select_dir(self):
        selected_path = self.path_entry.get()
        directory = askdirectory()
        if directory:
            self.path_entry.delete(0, END)
            selected_path = selected_path + ';' + directory
            self.path_entry.insert(0, selected_path.lstrip(';'))

    def executing(self):
        self.exe_button1['state'] = DISABLED
        self.exe_button1['text'] = '执行中'

    def done(self):
        self.exe_button1['state'] = NORMAL
        self.exe_button1['text'] = '执行'

    def check_input_and_execute(self):
        if not self.check_path_entry_input():
            return
        if not self.check_file_create_time_entry_input():
            return
        if not self.check_file_access_time_entry_input():
            return
        if not self.check_file_modify_time_entry_input():
            return

        self.executing()
        self.text1.delete(1.0, END)
        count = int(self.count_entry.get())
        size = int(self.size_entry.get())
        same_bytes = int(self.same_bytes_entry.get())
        dir_level = int(self.dir_level_entry.get())
        file_create_time = self.file_create_time_entry.get()
        file_modify_time = self.file_modify_time_entry.get()
        file_access_time = self.file_access_time_entry.get()
        if file_create_time == self.desc2:
            file_create_time = None
        if file_modify_time == self.desc2:
            file_modify_time = None
        if file_access_time == self.desc2:
            file_access_time = None
        if not same_bytes:
            same_bytes = 0
        base_paths = self.path_entry.get()
        if self.random_ext_check.get() == 1:
            ext = 'random'
        else:
            ext = self.ext_entry.get()
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
                    modify_file_time(file, file_create_time, file_modify_time, file_access_time)
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
        self.text1 = ScrolledText(master, width=75, height=25)
        self.text1.grid(row=25, column=0, columnspan=10)

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
        self.text1 = ScrolledText(master, width=75, height=15)
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


class MainUI:

    def __init__(self, master):
        self.tk = master
        self.width = 550
        self.height = 560
        self.tk.title("重复文件创建v1.0")

        # 放到屏幕中央
        self.ws = self.tk.winfo_screenwidth()
        self.hs = self.tk.winfo_screenheight()
        x = (self.ws / 2) - (self.width / 2)
        y = (self.hs / 2) - (self.height / 2)
        self.tk.geometry('%dx%d+%d+%d' % (self.width, self.height, x, y))

        self.frame1 = LabelFrame(self.tk)
        self.frame_text_file_create_ui = LabelFrame(self.tk)
        self.frame_copy_file_ui = LabelFrame(self.tk)
        self.frame_attr_ui = LabelFrame(self.tk)
        TextFileCreateUI(self.frame_text_file_create_ui)
        CopyFileUI(self.frame_copy_file_ui)
        ModifyFileAttrUI(self.frame_attr_ui)

        tag = IntVar()
        Radiobutton(self.frame1, text="指定大小创建", command=lambda: self.change_tab(0), width=11, variable=tag, value=0,
                    bd=1, indicatoron=False).pack(side=LEFT)
        Radiobutton(self.frame1, text="拷贝多份文件", command=lambda: self.change_tab(1), width=10, variable=tag, value=1,
                    bd=1, indicatoron=False).pack(side=LEFT)
        Radiobutton(self.frame1, text="修改文件属性", command=lambda: self.change_tab(2), width=10, variable=tag, value=2,
                    bd=1, indicatoron=False).pack(side=LEFT)
        self.frame1.pack(padx=10, fill='x')
        # Separator(self.tk, orient=HORIZONTAL).pack(padx=13, pady=8, fill='x', side=TOP)
        self.frame_text_file_create_ui.pack()
        self.tk.mainloop()

    def change_tab(self, tag):

        self.frame_text_file_create_ui.pack_forget()
        self.frame_copy_file_ui.pack_forget()
        self.frame_attr_ui.pack_forget()
        if tag == 0:
            self.frame_text_file_create_ui.pack()
        elif tag == 1:
            self.frame_copy_file_ui.pack()
        elif tag == 2:
            self.frame_attr_ui.pack()


if __name__ == '__main__':
    MainUI(Tk())
