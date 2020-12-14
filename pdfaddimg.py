import os
import tkinter as tk
import img2pdf
import PyPDF2
import xlrd  # 读Excel
from tkinter.filedialog import askdirectory,askopenfilename




def pdf2pic(dirpath_, pic_path_,xpath):
    source_path = xpath
    sourcexls = xlrd.open_workbook(source_path)  # 打开学生信息
    sourcesheet = sourcexls.sheet_by_index(0)  # 第一个工作表
    学号 = sourcesheet.col_values(11, 1, None)  # 获取列值，用作查找
    身份证号 = sourcesheet.col_values(14, 1, None)
    for rootd, dirs, files in os.walk(dirpath_):
         for item in files:
            xh = item.split('.')[0]  # 分离学号
            if xh in 学号:
                sfzh = 身份证号[学号.index(xh)]
            file = os.path.join(rootd,item)   # 获得所有的pdf文件，附件文件夹
            try:
                with open("tmp.pdf", "wb") as f:    # 临时文件，获取照片到pdf
                    f.write(img2pdf.convert(f"{pic_path_}/{sfzh}.jpg"))
            except:
                continue
            pdfReader = PyPDF2.PdfFileReader(file) # 读取pdf源文件
            pdfWriter = PyPDF2.PdfFileWriter()  # 写对象
            for i in range(pdfReader.getNumPages()):
                pdfWriter.addPage(pdfReader.getPage(i)) # 重写原始pdf文件
            pdfReader1 = PyPDF2.PdfFileReader("tmp.pdf") # 读照片pdf文件
            pdfWriter.addPage(pdfReader1.getPage(0))    # 添加照片pdf文件
            with open(file, "wb") as out:               #覆盖原始pdf文件
                pdfWriter.write(out)
            print(rootd,"正在添加照片")




if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    dirpath = askdirectory(title="pdf文件夹")
    pic_path= askdirectory(title=u'毕业照片')
    pdf2pic(dirpath,pic_path,"D:/条目","2020")
