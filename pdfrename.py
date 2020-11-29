'''
   # 将pdf文件拼接上其问价夹名
'''
import os
import xlwt
import tkinter as tk
from tkinter.filedialog import askdirectory

class BatchRename:


    def __init__(self):
        pass
    def rename(self, dirpath_):  # 表示需要命名处理的文件夹
        for root,dirs,files in os.walk(dirpath_):
            for file in files:
                srcname = os.path.join(root,file)
                # print(srcname)
                newname = root+'/'+root.split("/")[-1]+'-'+file
                print(file)
                os.rename(srcname,newname)

# 测试

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    dirpath = askdirectory()
    flag = False
    demo = BatchRename()
    demo.rename(dirpath)

