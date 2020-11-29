'''
   # 将指定文件夹下文件名存储到Excel中
'''
import os
import xlwt
import tkinter as tk
from tkinter.filedialog import askdirectory

class BatchRename:


    def __init__(self):
        pass
    def rename(self, dirpath_):  # 表示需要命名处理的文件夹
        parent_path = os.path.abspath(os.path.join(dirpath_, ".."))
        f = xlwt.Workbook(encoding='utf-8', style_compression=0)  # 新建一个Excel
        sheet = f.add_sheet('sheet1')  # 新建一个sheet
        i=1
        for root,dirs,files in os.walk(dirpath_):
            for file in files:
                print("'"+file.split('.')[0])
                sheet.write(i,0,"'"+file.split('.')[0])
                i = i+1
        f.save(parent_path+'\\filename.xls')




if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    dirpath = askdirectory()
    flag = False
    demo = BatchRename()
    demo.rename(dirpath)

