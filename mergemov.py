# -*- encoding: utf-8 -*-
"""
@File    : test.py
@Time    : 2021/1/11 19:12
@Author  : SJY
@Email   : 1434508535@qq.com
@Software: PyCharm
@function: 将相应的学籍卡，成绩表，学位证明合并到一个文件夹

"""
import os,shutil

import tkinter as tk
from tkinter.filedialog import askdirectory


class BatchRename:


    def __init__(self):
        pass
    def rename(self, dirpath_,dirpath_1,dirpath_2):  # 表示需要命名处理的文件夹
        i = 4
        for rootd, dirs, files in os.walk(dirpath_):

            for file in files:
                # print(file[:-7])
                # print(os.path.join(dirpath_2,f"{file[:-7]}学籍卡.pdf"))
                i+=1
                # 根据成绩表设定要建立的文件夹
                parent_path = os.path.abspath(os.path.join(dirpath_, "..","原件",f"A-2020-JX14-Y-{str(i).zfill(3)}"))
                if not os.path.exists(parent_path):
                    os.makedirs(parent_path)
                # 移动成绩表
                try:
                    shutil.move(os.path.join(rootd,file), parent_path)  # 移动文件
                    # print(file+f"->A-2020-JX14-Y-{str(i).zfill(4)}")
                except:
                    print(file+"无法移动")
                # 移动学籍卡
                try:
                    shutil.move(os.path.join(dirpath_1,f"{file[:-7]}学籍卡.pdf"), parent_path)  # 移动文件
                    # print(file+f"->A-2020-JX14-Y-{str(i).zfill(4)}")
                except:
                    print(f"A-2020-JX14-Y-{str(i).zfill(4)}{file[:-7]}学籍卡.pdf 缺失")
                # 移动学位证明
                try:
                    shutil.move(os.path.join(dirpath_2,f"{file[:-7]}学位证明.pdf"), parent_path)  # 移动文件
                    # print(file+f"->A-2020-JX14-Y-{str(i).zfill(4)}")
                except:
                    print(f"A-2020-JX14-Y-{str(i).zfill(3)} {file[:-7]}学位证明.pdf 缺失")



if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    dirpath = askdirectory(title=u'选择成绩表文件夹')
    dirpath1 = askdirectory(title=u'选择学籍卡文件夹')
    dirpath2 = askdirectory(title=u'选择学位证明文件夹')
    demo = BatchRename()
    demo.rename(dirpath,dirpath1,dirpath2)