'''
   读取案卷内pdf文件名，文件名为学生学号；
   在学生信息表中查找对用信息，著录卷内Excel表；
   信息表中没有信息的通过pdf文件直接获取
'''
import pdfplumber  # 读取pdf文件，转换为文本
import re  # 正则化
import os
import xlwt  # 写Excel
import xlrd  # 读Excel
import tkinter as tk
from tkinter.filedialog import askdirectory  # 获取文件路径
from tqdm import tqdm
import time
class Rcord:
    def __init__(self,ry,tmpath):
        self.y=''
        self.ry=ry
        self.dir_str=''
        self.srrq=time.strftime('%Y%m%d')
        self.ajh=''
        self.xy=''
        self.zy=''
        self.tmpath=tmpath
        if not os.path.exists(self.tmpath):
            os.makedirs(self.tmpath)
    '''
        正则函数，输入参数为正则规则，pdf源文件路径
    '''
    def setStyle(self,color):
        style = xlwt.XFStyle()  # 初始化样式
        font = xlwt.Font()  # 为样式创建字体
        # 字体类型：比如宋体、仿宋也可以是汉仪瘦金书繁
        font.colour_index = color
        alignment = xlwt.Alignment()
        # 0x01(左端对齐)、0x02(水平方向上居中对齐)、0x03(右端对齐)
        alignment.horz = 0x02
        # 0x00(上端对齐)、 0x01(垂直方向上居中对齐)、0x02(底端对齐)
        alignment.vert = 0x01
        style.alignment = alignment
        # 字体大小
        style.font = font
        return style
    def xre(self, xreg, pdfpath):  # 正则，参数为匹配规则
        with pdfplumber.open(pdfpath) as pdf:
            page = pdf.pages[0]  # 获取首页
            str = page.extract_text()  # 转文本
            reg = re.compile(xreg)
            match = reg.search(str)
            return match

    '''
        著录信息
    '''

    def rcord(self, dirpath_):  # 表示需要著录处理的文件夹
        # parent_path = os.path.abspath(os.path.join(dirpath_, "..", "A-2020-JX14条目"))  # 著录Excel的存放路径
        source_path = r"学生信息.xlsx"
        sourcexls = xlrd.open_workbook(source_path)  # 打开学生信息
        sourcesheet = sourcexls.sheet_by_index(0)  # 第一个工作表
        学号 = sourcesheet.col_values(5, 1, None)  # 获取列值，用作查找
        姓名 = sourcesheet.col_values(6, 1, None)
        身份证号 = sourcesheet.col_values(9, 1, None)
        证书号 = sourcesheet.col_values(10, 1, None)
        学位证号 = sourcesheet.col_values(11, 1, None)
        学院 = sourcesheet.col_values(12, 1, None)
        专业 = sourcesheet.col_values(13, 1, None)

        f = xlwt.Workbook(encoding='utf-8', style_compression=0)  # 新建一个Excel
        g = xlwt.Workbook(encoding='utf-8', style_compression=0)  # 新建一个案卷Excel
        sheet = f.add_sheet('sheet1')  # 新建一个sheet，开始著录行
        tabel = g.add_sheet('sheet1')  # 新建一个tabel，开始著录行
        # 卷内首行
        sheet.write(0, 0, "档号", self.setStyle(2))
        sheet.write(0, 1, "分类号", self.setStyle(2))
        sheet.write(0, 2, "年度", self.setStyle(2))
        sheet.write(0, 3, "件号", self.setStyle(2))
        sheet.write(0, 4, "保管期限", self.setStyle(2))
        sheet.write(0, 5, "题名", self.setStyle(2))
        sheet.write(0, 6, "总页数", self.setStyle(2))
        sheet.write(0, 7, "密级", self.setStyle(2))
        sheet.write(0, 8, "输入员", self.setStyle(2))
        sheet.write(0, 9, "输入时间", self.setStyle(2))
        sheet.write(0, 10, "归档单位", self.setStyle(2))
        sheet.write(0, 11, "学号", self.setStyle(2))
        sheet.write(0, 12, "学位证号", self.setStyle(2))
        sheet.write(0, 13, "证书号", self.setStyle(2))
        sheet.write(0, 14, "身份证号", self.setStyle(2))
        # 案卷首行
        tabel.write(0, 0, "全宗号", self.setStyle(2))
        tabel.write(0, 1, "档号", self.setStyle(2))
        tabel.write(0, 2, "分类号", self.setStyle(2))
        tabel.write(0, 3, "年度", self.setStyle(2))
        tabel.write(0, 4, "案卷号", self.setStyle(2))
        tabel.write(0, 5, "题名", self.setStyle(2))
        tabel.write(0, 6, "总件数", self.setStyle(2))
        tabel.write(0, 7, "保管期限", self.setStyle(2))
        tabel.write(0, 8, "密级", self.setStyle(2))
        tabel.write(0, 9, "立卷责任者", self.setStyle(2))
        tabel.write(0, 10, "立卷时间", self.setStyle(2))
        tabel.write(0, 11, "输入员", self.setStyle(2))
        tabel.write(0, 12, "输入时间", self.setStyle(2))
        tabel.write(0, 13, "归档单位", self.setStyle(2))

        i = 1
        j = 0
        for root, dirs, files in os.walk(dirpath_):
            if len(files) != 0:
                j+=1
                counter = 1
                tabel.write(j,6,len(files))
                pbar = tqdm(desc='卷著录', total=len(files), ascii=' =')
                for file in files:
                    xh = file.split('.')[0]  # 分离学号
                    pbar.update(1)
                    if xh in 学号:  # 查找
                        xm = 姓名[学号.index(xh)]
                        sfzh = 身份证号[学号.index(xh)]
                        zsh = 证书号[学号.index(xh)]
                        xwzh = 学位证号[学号.index(xh)]
                        xy = 学院[学号.index(xh)]
                        zy = 专业[学号.index(xh)]
                    else:  # 查找不到，采用正则表达式从pdf中获取
                        match = self.xre(r'\b姓名 .*? \b', os.path.join(root, file))
                        if match:
                            xm = match.group(0)[3:]
                        else:
                            xm=''
                        match = self.xre(r'身份证号 \d+\.*?\w', os.path.join(root, file)) # \W表示字母或者数字
                        if match:
                            sfzh = match.group(0)[5:]
                        else:
                            sfzh=''
                        match = self.xre(r'\b院系：.*? \b', os.path.join(root, file))
                        if match:
                            xy = match.group(0)[3:]
                        else:
                            xy=''
                        match = self.xre(r'\b专业：.*? \b', os.path.join(root, file))
                        if match:
                            zy = match.group(0)[3:]
                        else:
                            zy=''
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
                    self.xy=xy
                    self.zy=zy
                    dir_str = root.split('\\')[-1]  # 如果不需要加Y就不要以下的dir_str了
                    self.dir_str = dir_str
                    dir_str = dir_str.split(r'-')
                    self.y=dir_str[1]
                    self.ajh=dir_str[-1]
                    # dir_str.insert(3, 'Y')
                    # self.dir_str = '-'.join(dir_str)

                    # print(dir_str)
                    sheet.write(i, 0, self.dir_str)
                    sheet.write(i, 1, "JX14")
                    sheet.write(i, 2, f"{self.y}")
                    sheet.write(i, 3, f"{str(counter).zfill(4)}")
                    sheet.write(i, 4, "Y")
                    sheet.write(i, 5, f"{self.y}年河南大学【{xy}（{zy}）】学生学籍表：{xm}")
                    sheet.write(i, 6, "4")
                    sheet.write(i, 7, "内部")
                    sheet.write(i, 8, f"{self.ry}")
                    sheet.write(i, 9, f"{self.srrq}")
                    sheet.write(i, 10, "档案馆")
                    sheet.write(i, 11, xh)
                    sheet.write(i, 12, xwzh)  # 开始著录列
                    sheet.write(i, 13, zsh)
                    sheet.write(i, 14, sfzh)
                    i = i + 1
                    counter+=1
                tabel.write(j,0,"A")
                tabel.write(j,1,f"{self.dir_str}")
                tabel.write(j,2,f"JX14")
                tabel.write(j,3,f"{self.y}")
                tabel.write(j,4,f"{self.ajh}")
                tabel.write(j,5,f"{self.y}年河南大学【{self.xy}（{self.zy}）】学生学籍表")
                tabel.write(j,7,f"Y")
                tabel.write(j,8,f"内部")
                tabel.write(j,11,f"{self.ry}")
                tabel.write(j,12,f"{self.srrq}")
                tabel.write(j, 13, f"档案馆")
        f.save(f'{self.tmpath}/{self.y}年普通高校学籍表卷内.xls')  # 保存
        g.save(f'{self.tmpath}/{self.y}年普通高校学籍表案卷.xls')  # 保存
        # print("著录完成")
        return f"{self.tmpath}/{self.y}年普通高校学籍表卷内.xls"

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    dirpath = askdirectory()
    demo = Rcord("李开放","D:/条目")
    demo.rcord(dirpath)
