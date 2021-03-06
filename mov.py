# -*- encoding: utf-8 -*-
"""
@File    : test.py
@Time    : 2021/1/11 19:12
@Author  : SJY
@Email   : 1434508535@qq.com
@Software: PyCharm
@function: 移动文件到上层目录，将个人文件夹图片复制到上层班级目录，参数为整个大文件夹

"""
#移动文件到上层目录，将个人文件夹图片复制到班级
import re
import os,shutil
# import pytesseract
# from PIL import Image
import tkinter as tk
from tkinter.filedialog import askdirectory
# from tqdm import tqdm
# pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR'

class BatchRename:


    def __init__(self):
        pass
    def rename(self, dirpath_):  # 表示需要命名处理的文件夹
        # print(dirpath_)
        filelist = os.listdir(dirpath_)  # 获取文件列表
        global flag
        for item in filelist:
            # print(item)
            imgpath = os.path.join(os.path.abspath(dirpath_), item)
            if os.path.isdir(imgpath):
                self.rename(imgpath)
                continue

            parent_path = os.path.abspath(os.path.join(dirpath_, ".."))
            try:
                shutil.move(imgpath, parent_path)  # 移动文件
                flag = True
            except:
                flag= False
        if  flag:
            os.rmdir(dirpath_)
            flag = False
            # if item.endswith('.jpg'):
            #     continue
            # # if flag:
            # #     pbar.update(1)
            # # print(imgpath)
            # try:
            #     txtf = open(imgpath,encoding='gbk')
            # except:
            #     txtf = open(imgpath,encoding='utf-8')
            #
            # # print(type(txtf))
            # lines = txtf.read(40)
            # txtf.close()
            # # print(lines)
            #
            #
            # # flines = len(lines)
            # #(?<=学号: )
            # reg = re.compile(r"\d+\.*?\d")
            # match = reg.search(lines)
            # if not match:
            #     os.remove(imgpath)
            #     # print("未识别出来学号，跳过")
            #     continue
            # # print("识别出学号{}".format(match.group(0)))
            #
            # reg0 = re.compile(r"学籍卡")
            # match0 = reg0.search(lines)
            #
            # if not match0:
            #     # print("其他: ")
            #     os.remove(imgpath)
            #     # print("删除txt")
            #     portion = os.path.splitext(imgpath)  # 分离文件名字和后缀
            #     # print(portion)
            #     newname = portion[0] + ".jpg"  # 要改的新后缀
            #     os.remove(newname)
            #     # print("删除jpg")
            #     continue
            # print(match0.group(0))
            # os.remove(imgpath)
            # # print("删除学籍卡txt")
            # dst = os.path.join(os.path.abspath(dirpath_),
            #                     '' + match.group(0) + '.jpg')  # 处理后的格式也为jpg格式的，当然这里可以改成png格式
            # portion = os.path.splitext(imgpath)  # 分离文件名字和后缀
            # # print(portion)
            # newname = portion[0] + ".jpg"  # 要改的新后缀
            # try:
            #     os.rename(newname, dst)
            #     print('改名')
            # except:
            #     # print("跳过 %s" % src)
            #     continue

            # os.remove(imgpath)

            # image = im.crop((self.left, self.top, im.size[0]/3, im.size[1]/3))  # 对截图进行裁剪
            # image.show()
            # code_str = pytesseract.image_to_string(image, lang="eng",
            #                                    config="--psm 6")  # lang的值可以根据安装的语言选择，也不是都可以用，一般看的是验证码类型就可以了。
            # code_str = "".join(code)  # 字符串
            # print(code_str)
            # code_str = re.findall(r"\d+\.*?\d", code_str)  # 正则  遇到开始和结束就进行截取
            # code_str = "".join(code_str)
            # print("识别出", code_str)
            # src = imgpath
            # if code_str.strip() == '':
            #     os.remove(src)
            #     # print("删除 %s" % src)
            #     continue
            # dst = os.path.join(os.path.abspath(dirpath_),
            #                     '' + match.group(0) + '.jpg')  # 处理后的格式也为jpg格式的，当然这里可以改成png格式
            # try:
            #     os.rename(src, dst)
            #     print('converting %s to %s!' % (src, dst))
            # except:
            #     # print("跳过 %s" % src)
            #     continue
        # if flag:
        #     pbar.close()


if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    dirpath = askdirectory()
    flag = False
    demo = BatchRename()
    demo.rename(dirpath)
