# 调用PDFread接口进行pdf合并
# 源文件命名需分别包含学籍卡，成绩表，学位证字符串
import tkinter as tk
from tkinter.filedialog import askdirectory
from PDFread import *
import os
import sys

root = tk.Tk()
root.withdraw()
dirpath = askdirectory(title=u'选择源文件夹')
tarpath = askdirectory(title=u'选择目标文件夹')


class BatchSM:
    def __init__(self):
        学籍卡 = ''
        成绩表 = ''
        学位证 = ''

    # 遍历文件，将文件拆分，按照学号合并
    def rem(self, dirpath_, parentpath=tarpath):  # 表示需要重新合并的文件夹
        count = 0
        dirs_names = []
        for root, dirs, files in os.walk(dirpath_):
            if dirs:
                for i in dirs:
                    dirs_names.append(i)
                    dirs_path = os.path.abspath(os.path.join(parentpath, '.', i))
                    if not os.path.exists(dirs_path):
                        os.makedirs(dirs_path)
                        print("目标文件{}已生成".format(dirs_path))
            elif files:
                for item in files:
                    if "学籍卡" in item:
                        学籍卡 = os.path.abspath(os.path.join(dirpath_, '.', dirs_names[count], '.', item))
                    elif "成绩表" in item:
                        成绩表 = os.path.abspath(os.path.join(dirpath_, '.', dirs_names[count], '.', item))
                    elif "学位证" in item:
                        学位证 = os.path.abspath(os.path.join(dirpath_, '.', dirs_names[count], '.', item))
                if 学籍卡 == '':
                    print("没有学籍卡或命名错误")
                    sys.exit()  # 通过引发SystemExit异常来退出Python程序。
                if 成绩表 == '':
                    print("没有成绩表或命名错误")
                    sys.exit()
                if 学位证 == '':
                    print("没有学位证或命名错误")
                    sys.exit()
                parent_path = os.path.abspath(os.path.join(parentpath, '.', dirs_names[count]))
                pdfread = PDF()
                pdfread.PDFread(学籍卡, 成绩表, 学位证, parent_path)
                count += 1


if __name__ == '__main__':
    demo = BatchSM()
    demo.rem(dirpath)
