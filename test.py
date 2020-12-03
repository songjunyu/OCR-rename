from tkinter import *
from tkinter.filedialog import askdirectory


def selectPath():
    path_ = askdirectory()
    path.set(path_)


def show():
    print('目标路径：%s' % path.get())

    e.delete(0, END)  # 获取完信息，清楚掉输入框的


root = Tk()
root.title('pdf合并')
root.geometry('500x450')
path = StringVar()
photo = PhotoImage(file='logo.png')
Label(root, image=photo).grid(row=0, column=0, rowspan=4, columnspan=2,ipadx=500,ipady=180)
Label(root, text="目标路径:").grid(row=3, column=0)
e = Entry(root, textvariable=path)
e.grid(row=3, column=1, ipadx=60)

Button(root, text="路径选择", command=selectPath).grid(row=3, column=2)
Button(root, text='获取信息', width=10, command=show).grid(row=4, column=0)
Button(root, text='退出', width=10, command=root.quit).grid(row=4, column=2)
root.mainloop()
