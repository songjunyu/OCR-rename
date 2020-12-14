# 文件夹重命名
import os
import tkinter as tk
from tkinter.filedialog import askdirectory


class BatchRename:
    def __init__(self):
        pass
    def rename(self, dirpath_):  # 表示需要命名处理的大文件夹
        dirname =  os.listdir(dirpath_)
        i = 0
        for dir in dirname:
            i+=1
            # newname = f"A-2020-JX14-Y-{str(i).zfill(3)}"
            src = os.path.join(dirpath_, dir)  # path   os.path.abspath是绝对路径
            dst = os.path.join(dirpath_,f"A-2020-JX14-Y-{str(i).zfill(3)}")  # 处理后的格式也为jpg格式的，当然这里可以改成png格式


            try:
                os.rename(src, dst)  # 改名
                print('converting %s to %s !' % (dir,f"A-2020-JX14-Y-{str(i).zfill(3)}"))
            except:
                continue

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    dirpath = askdirectory(title=u'选择成绩表文件夹')
    demo = BatchRename()
    demo.rename(dirpath)