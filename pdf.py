# 调用PDFread接口进行pdf合并
# 源文件命名需分别包含学籍卡，成绩表，学位证字符串
# 最终要生成镜像文件夹
import tkinter as tk
from tkinter.filedialog import askdirectory
from PDFread import *
import os
import sys

root = tk.Tk()
root.withdraw()
dirpath = askdirectory(title=u'选择源文件夹')
tar_dir_path = askdirectory(title=u'选择目标文件夹')


# 遍历文件，将文件拆分，按照学号合并
class BatchSM:
    def __init__(self):
        学籍卡 = ''
        成绩表 = ''
        学位证 = ''

    def rem(self, dirpath_, tarpath=tar_dir_path):  # 表示需要重新合并的文件夹
        filelist = os.listdir(dirpath_)  # 获取文件列表
        for item in filelist:
            pdfpath = os.path.join(os.path.abspath(dirpath_), item)  # 文件路径
            if os.path.isdir(pdfpath):
                # dirs = item
                self.rem(pdfpath)
                continue
            if "学籍卡" in item:
                学籍卡 = pdfpath
            elif "成绩表" in item:
                成绩表 = pdfpath
            elif "学位证" in item:
                学位证 = pdfpath
        if 学籍卡 == '':
            print("没有学籍卡或命名错误")
            sys.exit()  # 通过引发SystemExit异常来退出Python程序。
        if 成绩表 == '':
            print("没有成绩表或命名错误")
            sys.exit()
        if 学位证 == '':
            print("没有学位证或命名错误")
            sys.exit()

        # parent_path = os.path.abspath(os.path.join(dirpath_,"A-2020-JX14附件"))
        parent_path = os.path.abspath(os.path.join(tarpath, '.', "A-2020-JX14附件"))
        if not os.path.exists(parent_path):
            os.makedirs(parent_path)
            print("目标文件{}已生成".format(parent_path))
        pdfread = PDF()
        pdfread.PDFread(学籍卡, 成绩表, 学位证, parent_path)


if __name__ == '__main__':
    demo = BatchSM()
    demo.rem(dirpath)
