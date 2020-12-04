'''
   # 将pdf文件拼接上其问价夹名
'''
import os
import tkinter as tk
from tkinter.filedialog import askdirectory

class BatchRename:


    def __init__(self):
        pass
    def rename(self, dirpath_):  # 表示需要命名处理的文件夹
        for root,dirs,files in os.walk(dirpath_):
            i=0
            for file in files:
                i=i+1
                srcname = os.path.abspath(os.path.join(root,file))
                # print(srcname)
                newname = root+'/'+f"{str(i).zfill(4)}.pdf"
                print(file+"->"+newname)
                os.rename(srcname,newname)

# 新测试

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    dirpath = askdirectory()
    flag = False
    demo = BatchRename()
    demo.rename(dirpath)

