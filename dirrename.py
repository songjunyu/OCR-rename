# -*- encoding: utf-8 -*-
"""
@File    : test.py
@Time    : 2021/1/11 19:12
@Author  : SJY
@Email   : 1434508535@qq.com
@Software: PyCharm
@function:文件夹批量重命名
          对大文件夹下的子文件夹进行批量重命名
          新文件夹格式名：A-2020-JX14-Y-{str(i).zfill(3)}
          参数为大文件夹
"""




import os
import tkinter as tk
from tkinter.filedialog import askdirectory


class BatchRename:
    def __init__(self):
        pass
    def rename(self, dirpath_):  # 表示需要命名处理的大文件夹
        dirname =  os.listdir(dirpath_) #列出所有子文件夹
        i = 0
        for dir in dirname:
            i+=1
            # newname = f"A-2020-JX14-Y-{str(i).zfill(3)}"
            src = os.path.join(dirpath_, dir)  # path   os.path.abspath是绝对路径
            dst = os.path.join(dirpath_,f"A-2020-JX14-Y-{str(i).zfill(3)}")


            try:
                os.rename(src, dst)  # 改名
                print('converting %s to %s !' % (dir,f"A-2020-JX14-Y-{str(i).zfill(3)}"))
            except:
                continue

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    dirpath = askdirectory(title=u'选择成绩表文件夹')
    demo = BatchRename()
    demo.rename(dirpath)