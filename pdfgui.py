from tkinter import *
from tkinter.filedialog import askdirectory
from pdf import BatchSM

def selectPath(p_):
    path_ = askdirectory()
    p_.set(path_)


def show():
    # print('目标路径：%s' % p_.get())
    demo = BatchSM(path1.get(), path2.get())  # 构建合并文件类，参数为源文件夹和目标文件夹

    demo.rem()



#     e.delete(0, END)  # 获取完信息，清楚掉输入框的


root = Tk()
root.title('pdf合并')
root.geometry('500x450')
path1 = StringVar()
path2 = StringVar()
photo = PhotoImage(file='logo.png')
# ,ipadx=500,ipady=180 设置logo
Label(root, image=photo).grid(row=0, column=0, rowspan=2, columnspan=3)
# 第3行，获取原路径
Label(root, text="原始路径:").grid(row=3, column=0)
e = Entry(root, textvariable=path1)  # 输入框，内容和path1绑定
e.grid(row=3, column=1, ipadx=60)
Button(root, text="路径选择", command=lambda: selectPath(path1)).grid(row=3, column=2)
# 第四行，获取目标路径
Label(root, text="目标路径:").grid(row=4, column=0)
e = Entry(root, textvariable=path2)  # 输入框，内容和path2绑定
e.grid(row=4, column=1, ipadx=60)
Button(root, text="路径选择", command=lambda: selectPath(path2)).grid(row=4, column=2)

# 第5行，开始按钮
Button(root, text='获取信息', command=show).grid(row=5, column=0)
# Button(root, text='开始pdf合并', command=lambda:(demo.rem())).grid(row=5, column=1)

# weight 设置宽度
Button(root, text='退出程序', command=root.quit).grid(row=5, column=2)
root.mainloop()
