# -*- encoding: utf-8 -*-
"""
@File    : test.py
@Time    : 2021/1/11 19:12
@Author  : SJY
@Email   : 1434508535@qq.com
@Software: PyCharm
@function: 查找打不开的PDF文件，以及缺失的PDF文件

"""

import os
import tkinter as tk
from tkinter.filedialog import askdirectory
from PyPDF2 import PdfFileReader

class BatchRename:


    def __init__(self):
        pass

    def isValidPDF_pathfile2(self,pathfile):
        bValid = True
        try:
            reader = PdfFileReader(pathfile)
            if reader.getNumPages() < 1:  # 进一步通过页数判断。
                bValid = False
        except:
            bValid = False
        return bValid

    def rename(self, dirpath_):  # 表示需要命名处理的文件夹
        for rootd, dirs, files in os.walk(dirpath_):
            if len(files) != 3:
                print(rootd,"缺失",3-len(files))

            for file in files:
                if not self.isValidPDF_pathfile2(os.path.join(rootd,file)):
                    print(rootd,file)




if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    dirpath = askdirectory(title=u'选择成绩表文件夹')
    demo = BatchRename()
    demo.rename(dirpath)