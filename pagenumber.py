# -*- encoding: utf-8 -*-
"""
@File    : test.py
@Time    : 2021/1/11 19:12
@Author  : SJY
@Email   : 1434508535@qq.com
@Software: PyCharm
@function: 获取每个学生pdf文件页数，写入一个空白Excel中，同时查看小于4页的、
            有可能是写的年份有错误，最后合并到卷内Excel中
"""


import os
import tkinter as tk
from tkinter.filedialog import askdirectory
from PyPDF2 import PdfFileReader
import xlwt  # 写Excel
class BatchRename:


    def __init__(self):
        pass
    '''
    根据文件路径，获取pdf页数并返回
    '''
    def getPDF_pages(self,pathfile):
        reader = PdfFileReader(pathfile)
        return reader.getNumPages()


    def rename(self, dirpath_):  # 表示需要命名处理的文件夹
        f = xlwt.Workbook(encoding='utf-8', style_compression=0)  # 新建一个Excel
        sheet = f.add_sheet('sheet1')  # 新建一个sheet，开始著录行
        i = 0
        for rootd, dirs, files in os.walk(dirpath_):
            for file in files:
                self.number =self.getPDF_pages(os.path.join(rootd,file))
                print(self.number)
                sheet.write(i, 0, self.number)
                i+=1
        f.save('pdfnumber.xls')  # 保存






if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    dirpath = askdirectory(title=u'选择附件文件夹')
    demo = BatchRename()
    demo.rename(dirpath)