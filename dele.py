# -*- encoding: utf-8 -*-
"""
@File    : test.py
@Time    : 2021/1/11 19:12
@Author  : SJY
@Email   : 1434508535@qq.com
@Software: PyCharm
@function: 删除成绩单，（删除包含指定文本内容的图片）
           图片文件夹可以嵌套
           文件夹可以迭代
           参数为最外层文件夹

"""
#删除包含学生两个字的文件
#import cv2
import re
import os
import pytesseract    #谷歌字符识别库，需要先安装软件，此为python调用接口
from PIL import Image
import tkinter as tk
from tkinter.filedialog import askdirectory   #python 获取文件夹路径

left = 60
top = 0
right = 225
bottom = 140
list1 = [ '学', '生']
class BatchRename():
    def __init__(self):
        pass

    def rename(self,path):
        self.path = path
        filelist = os.listdir(self.path)  # 列出所有文件
        total_num = len(filelist)  # 文件个数
        print(total_num)
        for item in filelist:
            try:
                item_path = os.path.join(path, item)  # 拼接路径
                if os.path.isdir(item_path):  # 判断是否是文件夹
                    self.rename(item_path)  # 如果是文件夹就迭代
                # else:
                #     print(item_path)
                #     extension_name = os.path.splitext(item_path)  # ?????????????????????????????
                #     print(extension_name)
            except:
                continue
            if item.endswith('.jpg'):  # 只识别后缀名为jpg的文件
                path : str = os.path.join(os.path.abspath(self.path), item)
                # print(path)
                im = Image.open(path)
                im = im.crop((0, 0, im.size[0] * 2 / 3, im.size[1] / 2)) # 只获取图片中的一部分
                #image = im.crop((left, top, right, bottom))  # ???????????
                #code = pytesseract.image_to_string(im, lang="eng",
                                                   #config="--psm 6")  # lang?????????????????????????????????????????????????????????
                code = pytesseract.image_to_string(im, lang="chi_sim",
                                                   config="--psm 6")  # 文本识别

                code_str = list(code)

                for i in code_str:
                    if ' ' in code_str:
                        code_str.remove(' ')

                no_exist = [False for a in list1 if a not in code_str]
                if no_exist:
                    print('成绩单') #如果字符串存在，则说明是成绩单（图片中包含学生两个字），删除
                    os.remove(path)
                else:
                    print("学籍卡")
                    continue
              
if __name__ == '__main__':
    tk.Tk().withdraw()
    path = askdirectory()
    demo = BatchRename()
    demo.rename(path)