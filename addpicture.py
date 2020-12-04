import tkinter as tk
from tkinter.filedialog import askdirectory

import os

import fitz
def pdf2pic(dirpath_, pic_path_):
    for rootd, dirs, files in os.walk(dirpath_):
        for item in files:
            pdffile=os.path.join(rootd,item)
            doc = fitz.open(pdffile)  # 打开pdf文件
            imgdoc = fitz.open("2.jpg")  # 打开图片
            pdfbytes = imgdoc.convertToPDF()  # 使用图片创建单页的 PDF
            imgpdf = fitz.open("1610120129.pdf", pdfbytes)
            doc.insertPDF(imgpdf)  # 将当前页插入文档
            doc.save("1601601.pdf")
            doc.close()


if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    dirpath = askdirectory(title=u'选择源文件夹')
    pic_path = askdirectory(title=u'选择源文件夹')
    pdf2pic(dirpath,pic_path)

