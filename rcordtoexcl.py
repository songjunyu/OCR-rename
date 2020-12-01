'''
   读取案卷内pdf文件名，文件名为学生学号；
   在学生信息表中查找对用信息，著录卷内Excel表；
   信息表中没有信息的通过pdf文件直接获取
'''
import pdfplumber # 读取pdf文件，转换为文本
import re         # 正则化
import os
import xlwt       #写Excel
import xlrd       #读Excel
import tkinter as tk
from tkinter.filedialog import askdirectory  # 获取文件路径

class Rcord:
    def __init__(self):
        pass
    '''
        正则函数，输入参数为正则规则，pdf源文件路径
    '''
    def xre(self,xreg,pdfpath): # 正则，参数为匹配规则
        with pdfplumber.open(pdfpath) as pdf:
            page = pdf.pages[0] #  获取首页
            str = page.extract_text() # 转文本
            reg = re.compile(xreg)
            match = reg.search(str)
            return match
    '''
        著录信息
    '''

    def rcord(self, dirpath_):  # 表示需要著录处理的文件夹
        parent_path = os.path.abspath(os.path.join(dirpath_, "..")) # 著录Excel的存放路径
        source_path = r"C:\Users\sjy\Desktop\学生信息.xlsx"
        sourcexls = xlrd.open_workbook(source_path) # 打开学生信息
        sourcesheet = sourcexls.sheet_by_index(0)   # 第一个工作表
        学号 = sourcesheet.col_values(5,1,None)      # 获取列值，用作查找
        姓名 = sourcesheet.col_values(6,1,None)
        身份证号 = sourcesheet.col_values(9,1,None)
        证书号 = sourcesheet.col_values(10,1,None)
        学位证号 = sourcesheet.col_values(11,1,None)
        学院 = sourcesheet.col_values(12,1,None)
        专业 = sourcesheet.col_values(13,1,None)



        f = xlwt.Workbook(encoding='utf-8', style_compression=0)  # 新建一个Excel
        sheet = f.add_sheet('sheet1')  # 新建一个sheet，开始著录行
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
                xh=file.split('.')[0]           # 分离学号
                if xh in 学号:                   # 查找
                    xm = 姓名[学号.index(xh)]
                    sfzh = 身份证号[学号.index(xh)]
                    zsh = 证书号[学号.index(xh)]
                    xwzh = 学位证号[学号.index(xh)]
                    xy = 学院[学号.index(xh)]
                    zy = 专业[学号.index(xh)]


                else:                           # 查找不到，采用正则表达式从pdf中获取
                    match = self.xre(r'\b姓名 .*? \b', os.path.join(root, file))
                    xm = match.group(0)[3:]
                    match = self.xre(r'身份证号 \d+\.*?\d', os.path.join(root, file))
                    sfzh=match.group(0)[5:]
                    match = self.xre(r'\b院系：.*? \b', os.path.join(root, file))
                    xy=match.group(0)[3:]
                    match = self.xre(r'\b专业：.*? \b', os.path.join(root, file))
                    zy=match.group(0)[3:]
                    match = self.xre(r'证书号 \d+\.*?\d', os.path.join(root, file))
                    if match:
                        zsh = match.group(0)[4:]
                    else:
                        zsh = ''
                    match = self.xre(r'学位证书号 \d+\.*?\d', os.path.join(root, file))
                    if match:
                        xwzh = match.group(0)[6:]
                    else:
                        xwzh = ''
                # print(xh,xm,xfzh,zsh,xwzh,xy,zy)
                sheet.write(i, 9, xwzh)             # 开始著录列
                sheet.write(i, 10, zsh)
                sheet.write(i, 16, sfzh)
                sheet.write(i, 7, f"2020年河南大学【{xy}（{zy}）】学生学籍表：{xm}")

                sheet.write(i,8,xh)
                sheet.write(i,0,"A-2020-JX14-004")
                sheet.write(i,1,"A")
                sheet.write(i,2,"2020")
                sheet.write(i,3,"JX14")
                sheet.write(i,4,"004")
                sheet.write(i,5,f"{str(i).zfill(4)}")
                sheet.write(i,6,f"{3*(i-1)+1}")
                sheet.write(i,11,"档案馆")
                sheet.write(i,13,"Y")
                sheet.write(i,15,"内部")
                sheet.write(i,17,"宋俊玉")


                i = i+1
        f.save(parent_path+'\\rcord.xls')     # 保存




if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    dirpath = askdirectory()
    demo = Rcord()
    demo.rcord(dirpath)

