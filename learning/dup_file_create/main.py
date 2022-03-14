from tkinter import Tk, Label, Entry, Button, IntVar, Checkbutton, Frame, Radiobutton, StringVar, messagebox
from tkinter.constants import TOP, END, HORIZONTAL, LEFT, DISABLED, NORMAL
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import Separator

from dup_file_create import *


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

        self.frame1 = Frame(self.tk)
        self.frame_text_file_create_ui = Frame(self.tk)
        self.frame_copy_file_ui = Frame(self.tk)
        self.text_file_create_ui()
        self.copy_file_ui()
        tag = IntVar()
        Radiobutton(self.frame1, text="指定大小创建", command=lambda: self.change_tab(0), width=11, variable=tag, value=0,
                    bd=1, indicatoron=False).pack(side=LEFT)
        Radiobutton(self.frame1, text="拷贝多份文件", command=lambda: self.change_tab(1), width=10, variable=tag, value=1,
                    bd=1, indicatoron=False).pack(side=LEFT)
        Radiobutton(self.frame1, text="其他", command=lambda: self.change_tab(2), width=10, variable=tag, value=2,
                    bd=1, indicatoron=False).pack(side=LEFT)
        self.frame1.pack(padx=10, fill='x')
        Separator(self.tk, orient=HORIZONTAL).pack(padx=13, pady=8, fill='x', side=TOP)
        self.frame_text_file_create_ui.pack()
        # self.frame_copy_file_ui.pack()
        self.tk.mainloop()

    def change_tab(self, tag):

        self.frame_text_file_create_ui.pack_forget()
        self.frame_copy_file_ui.pack_forget()
        if tag == 0:
            self.frame_text_file_create_ui.pack()
        elif tag == 1:
            self.frame_copy_file_ui.pack()
        elif tag == 2:
            self.frame_text_file_create_ui.pack_forget()
            self.frame_copy_file_ui.pack_forget()

    def text_file_create_ui(self):
        # Label(self.frame_text_file_create_ui, text="<创建指定大小的文本文件>").grid(row=0, column=1)
        Label(self.frame_text_file_create_ui, text="文件个数：").grid(row=2, column=0)
        Label(self.frame_text_file_create_ui, text="文件大小（字节）：").grid(row=4, column=0)
        Label(self.frame_text_file_create_ui, text="头部相同字节数：").grid(row=6, column=0)
        Label(self.frame_text_file_create_ui, text="文件存放基础路径：").grid(row=8, column=0)
        ext_label = Label(self.frame_text_file_create_ui, text="扩展名：")
        ext_label.grid(row=10, column=0)

        extension = StringVar()
        extension.set(EXTENSION)
        count_entry = Entry(self.frame_text_file_create_ui, width=30)
        size_entry = Entry(self.frame_text_file_create_ui, width=30)
        same_bytes_entry = Entry(self.frame_text_file_create_ui, width=30)
        path_entry = Entry(self.frame_text_file_create_ui, width=30)
        ext_entry = Entry(self.frame_text_file_create_ui, width=30, textvariable=extension)
        count_entry.grid(row=2, column=1, pady=3)
        size_entry.grid(row=4, column=1, pady=3)
        same_bytes_entry.grid(row=6, column=1, pady=3)
        path_entry.grid(row=8, column=1, pady=3)
        ext_entry.grid(row=10, column=1, pady=3)

        path_entry.insert(0, BASE_PATHS)
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
                    command=click_random_ext).grid(row=12, column=0)

        def check_input():
            text1.delete(1.0, END)
            count = count_entry.get()
            try:
                count = int(count)
            except ValueError:
                messagebox.showinfo(title='温馨提示', message='输入文件个数错误！')
                return
            size = size_entry.get()
            same_bytes = same_bytes_entry.get()
            if not same_bytes:
                same_bytes = 0
            try:
                same_bytes = int(same_bytes)
            except ValueError:
                messagebox.showinfo(title='温馨提示', message='输入头部相同字节数错误！')
                return
            try:
                size = int(size)
            except ValueError:
                messagebox.showinfo(title='温馨提示', message='输入文件大小错误！')
                return
            base_paths = path_entry.get()
            if random_ext_check.get() == 1:
                ext = 'random'
            else:
                ext = ext_entry.get()
            if ':' not in base_paths:
                messagebox.showinfo(title='温馨提示', message='基础路径错误！')
                return
            try:
                ret = create_duplicate_files(count, size, same_bytes, base_paths=base_paths, extension=ext)
                s = ''
                for i in ret:
                    s = s + i + '\n'
                text1.insert(END, s)
                messagebox.showinfo(title='温馨提示', message='执行成功')
            except Exception as e:
                s = str(e)
                text1.insert(END, s)

        Button(self.frame_text_file_create_ui, text='执行', bg='white', width=8, height=1, command=check_input).grid(
            row=6, column=5, padx=4)

        text1 = ScrolledText(self.frame_text_file_create_ui, width=75, height=9)
        text1.grid(row=18, column=0, columnspan=10)

    def copy_file_ui(self):
        Label(self.frame_copy_file_ui, text="<拷贝多份指定文件>").grid(row=14, column=1)
        label1 = Label(self.frame_copy_file_ui, text="源文件绝对路径：")
        label2 = Label(self.frame_copy_file_ui, text="复制数量：")
        label3 = Label(self.frame_copy_file_ui, text="文件存放基础路径：")
        Label(self.frame_copy_file_ui, text="是否修改文件名：").grid(row=22)
        label1.grid(row=16)
        label2.grid(row=18)
        label3.grid(row=20)

        def check_input():
            text1.delete(1.0, END)
            path = entry1.get()
            if ':' not in path:
                messagebox.showinfo(title='温馨提示', message='路径错误！')
                return
            count = entry2.get()
            try:
                count = int(count)
            except ValueError:
                messagebox.showinfo(title='温馨提示', message='复制数量错误！')
                return
            base_dir = entry3.get()
            if ':' not in base_dir:
                messagebox.showinfo(title='温馨提示', message='文件存放基础路径错误！')
                return
            try:
                ret = copy_file(path, count, base_dir, True) if v1.get() else copy_file(path, count, base_dir, False)
                if not ret:
                    return
                s = ''
                for i in ret:
                    s = s + i + '\n'
            except Exception as e:
                s = str(e)
            text1.insert(END, s)
            messagebox.showinfo(title='温馨提示', message='执行成功')

        entry1 = Entry(self.frame_copy_file_ui, width=30)
        entry2 = Entry(self.frame_copy_file_ui, width=30)
        entry3 = Entry(self.frame_copy_file_ui, width=30)
        entry1.grid(row=16, column=1, pady=3)
        entry2.grid(row=18, column=1, pady=3)
        entry3.grid(row=20, column=1, pady=3)
        entry3.insert(0, BASE_PATHS)

        v1 = IntVar()
        v1.set(0)
        v2 = IntVar()
        v2.set(0)

        radio_button1 = Checkbutton(self.frame_copy_file_ui, text='是', variable=v1, onvalue=1, offvalue=0,
                                    command=lambda: radio_button2.deselect() if v2.get() == 1 else 0)
        radio_button2 = Checkbutton(self.frame_copy_file_ui, text='否', variable=v2, onvalue=1, offvalue=0,
                                    command=lambda: radio_button1.deselect() if v1.get() == 1 else 0)
        radio_button1.grid(row=22, column=1)
        radio_button2.grid(row=22, column=2)
        radio_button2.select()

        Button(self.frame_copy_file_ui, text='执行', bg='#7CCD7C', width=8, height=1, command=check_input).grid(
            row=18, column=5, padx=4)

        text1 = ScrolledText(self.frame_copy_file_ui, width=75, height=9)
        text1.grid(row=25, column=0, columnspan=10)


if __name__ == '__main__':
    UI()
