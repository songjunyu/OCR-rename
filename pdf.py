# 调用PDFread接口进行pdf合并
# 源文件命名需分别包含学籍卡，成绩表，学位证字符串
import tkinter as tk
from tkinter.filedialog import askdirectory
from PDFread import *
import os
import sys


# 遍历文件，将文件拆分，按照学号合并
class BatchSM:
    def __init__(self,dirpath_,tarpath_):
        self.学籍卡 = ''
        self.成绩表 = ''
        self.学位证 = ''
        self.dirpath_ = dirpath_
        self.tarpath_ = tarpath_
        print(dirpath_,tarpath_)
    def rem(self):  # 表示需要重新合并的文件夹

        i = -1
        for rootd, dirs, files in os.walk(self.dirpath_):
            if i==-1:
                dir = dirs
                i = i + 1
                continue

            for item in files:
                pdfpath=os.path.abspath(os.path.join(rootd,item))


                if "学籍卡" in item:
                    self.学籍卡 = pdfpath
                elif "成绩表" in item:
                    self.成绩表 = pdfpath
                elif "学位证" in item:
                    self.学位证 = pdfpath
            if self.学籍卡 == '':
                print("没有学籍卡或命名错误")
                sys.exit()
            if self.成绩表 == '':
                print("没有成绩表或命名错误")
                sys.exit()
            if self.学位证 == '':
                print("没有学位证或命名错误")
                sys.exit()

            # parent_path = os.path.abspath(os.path.join(dirpath_,"A-2020-JX14附件"))
            parent_path = os.path.abspath(os.path.join(self.tarpath_,dir[i] ))
            i = i + 1
            if not os.path.exists(parent_path):
                os.makedirs(parent_path)
            pdfread = PDF(self.学籍卡, self.成绩表, self.学位证, parent_path)
            pdfread.PDFread()
            # t.kill()


if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    dirpath = askdirectory(title=u'选择源文件夹')
    tarpath = askdirectory(title=u'选择目标文件夹')
    # tarpath= askdirectory(title=u'选择目标文件夹')
    demo = BatchSM(dirpath,tarpath)
    demo.rem()
