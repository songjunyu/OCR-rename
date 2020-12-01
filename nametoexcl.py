'''
   # 将指定文件夹下文件名存储到Excel中
'''
import os
import xlwt
import xlrd
import tkinter as tk
from tkinter.filedialog import askdirectory

class BatchRename:


    def __init__(self):
        pass
    def rename(self, dirpath_):  # 表示需要命名处理的文件夹
        parent_path = os.path.abspath(os.path.join(dirpath_, ".."))
        source_path = r"C:\Users\sjy\Desktop\2020½ì.xls"
        sourcexls = xlrd.open_workbook(source_path)
        sourcesheet = sourcexls.sheet_by_index(0)
        学号 = sourcesheet.col_values(5,1,None)
        姓名 = sourcesheet.col_values(6,1,None)
        身份证号 = sourcesheet.col_values(9,1,None)
        证书号 = sourcesheet.col_values(10,1,None)
        学位证号 = sourcesheet.col_values(11,1,None)
        学院 = sourcesheet.col_values(12,1,None)
        专业 = sourcesheet.col_values(13,1,None)

        # print(学号)  # 取第1行，第6~10列（不含第10表）

        f = xlwt.Workbook(encoding='utf-8', style_compression=0)  # 新建一个Excel
        sheet = f.add_sheet('sheet1')  # 新建一个sheet
        sheet.write(0,0,"档号")
        sheet.write(0,1,"全宗号")
        sheet.write(0,2,"年度")
        sheet.write(0,3,"实体分类号")
        sheet.write(0,4,"案卷号")
        sheet.write(0,5,"件号")
        sheet.write(0,6,"页号")
        sheet.write(0,7,"文件题名")
        sheet.write(0,8,"学号")
        sheet.write(0,9,"学位证号")
        sheet.write(0,10,"证书号")
        sheet.write(0,11,"归档单位")
        sheet.write(0,12,"文件时间")
        sheet.write(0,13,"保管期限")
        sheet.write(0,14,"页数")
        sheet.write(0,15,"密级")
        sheet.write(0,16,"身份证号")
        sheet.write(0,17,"责任者")
        i=1
        for root,dirs,files in os.walk(dirpath_):
            for file in files:

                xh=file.split('.')[0]
                if xh in 学号:
                    xm = 姓名[学号.index(xh)]
                    sfzh = 身份证号[学号.index(xh)]
                    zsh = 证书号[学号.index(xh)]
                    xwzh = 学位证号[学号.index(xh)]
                    xy = 学院[学号.index(xh)]
                    zy = 专业[学号.index(xh)]
                    # print(xh,xm,xfzh,zsh,xwzh,xy,zy)
                    sheet.write(i,9,xwzh)
                    sheet.write(i,10,zsh)
                    sheet.write(i,16,sfzh)
                    sheet.write(i,7,f"2020年河南大学【{xy}（{zy}）】学生学籍表：{xm}")
                sheet.write(i,8,xh)
                sheet.write(i,0,"A-2020-JX14-004")
                sheet.write(i,1,"A")
                sheet.write(i,2,"2020")
                sheet.write(i,3,"JX14")
                sheet.write(i,4,"004")
                sheet.write(i,5,f"A-2020-JX14-004-{xh}")
                sheet.write(i,6,f"{3*(i-1)+1}")
                sheet.write(i,11,"档案馆")
                sheet.write(i,13,"Y")
                sheet.write(i,15,"内部")
                sheet.write(i,17,"宋俊玉")


                i = i+1
        f.save(parent_path+'\\filename.xls')




if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    dirpath = askdirectory()
    demo = BatchRename()
    demo.rename(dirpath)

