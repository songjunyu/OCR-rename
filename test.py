import tkinter as tk
from tkinter import filedialog
from PDFread import *

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.filePath = tk.StringVar()
        self.pack()
        # self.demo = BatchRename().rename()

        tk.Button(self,text = '源文件夹',bg = 'red',width = 20,height = 1,command = self._getFile).pack(side = 'top')
        self.dirpath = self.filePath
        tk.Button(self,text = '目标文件夹',bg = 'red',width = 20,height = 1,command = self._getFile).pack(side = 'top')
        self.dirpath1 = filepath
        self.demo = BatchRename().rename(str(self.dirpath))
        tk.Button(self,text = '运行',bg = 'yellow',width = 20,height = 1,command = self.demo).pack(side = 'top')

    # 打开文件并显示路径
    def _getFile(self):
        default_dir = r"文件夹路径"
        self.filePath = tk.filedialog.askdirectory(title=u'选择文件夹', initialdir=(os.path.expanduser(default_dir)))
        tag = tk.Entry(self,width = 60)
        tag.pack(side = 'top')
        tag.delete(0, "end")
        tag.insert(0, self.filePath)
        return self.filePath
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


root = tk.Tk()
root.title("学生档案归档")
root.geometry("400x300")
app = Application(master=root)
app.mainloop()