# 调用PDFread接口进行pdf合并

import os,shutil

import tkinter as tk
from tkinter.filedialog import askdirectory
from PDFread import *

class BatchRename:


    def __init__(self):
        pass
    def rename(self, dirpath_):  # 表示需要命名处理的文件夹
        filelist = os.listdir(dirpath_)  # 获取文件列表
        for item in filelist:
            imgpath = os.path.join(os.path.abspath(dirpath_), item)
            if os.path.isdir(imgpath):
                self.rename(imgpath)
                continue
            if "学籍卡" in item:
                学籍卡 = imgpath
            elif "成绩表" in item:
                成绩表 = imgpath
            elif "学位证" in item:
                学位证 = imgpath
            parent_path = os.path.abspath(os.path.join(dirpath_, ".."))
        pdfread=PDF()
        pdfread.PDFread(学籍卡,成绩表,学位证,parent_path)




if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    dirpath = askdirectory()
    demo = BatchRename()
    demo.rename(dirpath)
