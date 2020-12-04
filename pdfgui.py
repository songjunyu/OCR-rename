from tkinter import *
from tkinter.filedialog import askdirectory
from pdf import BatchSM
from rcordtoexcl import Rcord
from pdfaddimg import pdf2pic
from pdfrename import BatchRename
def selectPath(p_):
    path_ = askdirectory()
    p_.set(path_)


def sm():
    print("开始合并")
    demo = BatchSM(path1.get(), path2.get())  # 构建合并文件类，参数为源文件夹和目标文件夹
    demo.rem()
    print("完成合并")
    B1['command']=record
    B1['text']="附件pdf著录"
def record():
    print(path2.get(), "开始著录") # path2为合并后附件文件夹
    demo = Rcord()          # 著录实现
    demo.rcord(path2.get())
    print(path2.get(), "完成著录")
    L1['text']="毕业照片"
    L1['bg']="yellow"
    B1['command'] = addimg
    B1['text'] = "添加照片"

def addimg():
    print("添加照片")
    pdf2pic(path2.get(),path1.get())
    print("添加照片完成")
    B1['command'] = rename
    B1['text'] = "改名"
def rename():
    # print('目标路径：%s' % p_.get())
    # demo = BatchSM(path1.get(), path2.get())  # 构建合并文件类，参数为源文件夹和目标文件夹
    # print(path1.get(), "pdf附件路径")

    print("改名")
    demo = BatchRename() # 重命名类
    demo.rename(path2.get())
    print("改名完成")
    B1['command'] = root.quit
    B1['text'] = "退出程序"

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
L1=Label(root, text="原始路径:")
L1.grid(row=3, column=0)
e = Entry(root, textvariable=path1)  # 输入框，内容和path1绑定
e.grid(row=3, column=1, ipadx=60)
Button(root, text="路径选择", command=lambda: selectPath(path1)).grid(row=3, column=2)
# 第四行，获取目标路径
L2=Label(root, text="目标路径:")
L2.grid(row=4, column=0)
e = Entry(root, textvariable=path2)  # 输入框，内容和path2绑定
e.grid(row=4, column=1, ipadx=60)
Button(root, text="路径选择", command=lambda: selectPath(path2)).grid(row=4, column=2)

# 第5行，开始按钮
B1=Button(root, text='pdf合并', command=sm,bg='red')
B1.grid(row=8, column=1,ipadx=12,ipady=12)
# Button(root, text='著录', command=record).grid(row=5, column=1)
# Button(root, text='开始pdf合并', command=lambda:(demo.rem())).grid(row=5, column=1)

# weight 设置宽度
Button(root, text='退出程序', command=root.quit).grid(row=8, column=2)
root.mainloop()
