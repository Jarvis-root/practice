import tkinter as tk

root = tk.Tk()
root.title('音乐下载器')
root.geometry('300x100')
l1 = tk.Label(root, text='歌曲：')
l1.pack()
e1 = tk.Entry(root)
e1.pack()

tk.Button(root, text='下载')

root.mainloop()