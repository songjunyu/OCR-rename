#可打开多个文件夹，全图识别，正确率高，无法删除非成绩单


import re
import os
import pytesseract    #光学字符识别引擎
from PIL import Image
import tkinter as tk
from tkinter.filedialog import askdirectory   #python 进行窗口视窗设计的模块

# left = 60
# top = 0
# right = 225
# bottom = 140
list1 = ['学','位']
list2 = ['档','案']



class BatchRename():

    def __init__(self):
        pass

    def rename(self,path):
        self.path = path
        filelist = os.listdir(self.path)  # 获取文件路径
        total_num = len(filelist)  # 获取文件长度（个数）
        print(total_num)
        for item in filelist:
            item_path = os.path.join(path, item)  # 获取绝对路径
            if os.path.isdir(item_path):  # 判断给出的路径是否是文件夹 是-->TRUE
                self.rename(item_path)  # 如果是文件夹，就递归调用自己
                continue
            if item.endswith('.jpg'):  # 初始的图片的格式为jpg格式的（或者源文件是png格式及其他格式，后面的转换格式就可以调整为自己需要的格式即可）判断字符串是否以指定后缀结尾
                path: str = os.path.join(os.path.abspath(self.path), item)
                # print(path)
                im = Image.open(path)
                im = im.crop((0, 0, im.size[0] * 2 / 3, im.size[1] / 5))
                # im.show()
                #image = im.crop((left, top, right, bottom))  # 对截图进行裁剪
                #code = pytesseract.image_to_string(im, lang="eng",
                                                   #config="--psm 6")  # lang的值可以根据安装的语言选择，也不是都可以用，一般看的是验证码类型就可以了。
                code = pytesseract.image_to_string(im, lang="chi_sim",
                                                   config="--psm 6")  # lang的值可以根据安装的语言选择，也不是都可以用，一般看的是验证码类型就可以
                #print("识别出",code)  #识别之后的乱码
                # code_str = "".join(code)  # 字符串
                code_str = list(code)
                # print(code_str)
                for i in code_str:
                    if ' ' in code_str:
                        code_str.remove(' ')
                #print(code_str)
                # if set(list1) < set(code_str) :
                #     print("移除")
                no_exist = [False for a in list1 if a not in code_str]
                # no_exist = [False for a in list2 if a not in code_str]


                # if no_exist:
                #     print('学籍卡')
                # else:
                #     print("成绩表")
                #     os.remove(path)
                #     continue
                no_exist = [False for a in list1 if a not in code_str]
                if no_exist:
                    # print('学籍卡')
                    pass
                else:
                    print("删除学位证")
                    os.remove(path)
                    continue
                no_exist1 = [False for b in list2 if b not in code_str]
                if no_exist1:
                    # print('学籍卡')
                    pass
                else:
                    print("删除成绩表")
                    os.remove(path)
                    continue
                code_str = "".join(code)  # 字符串
                # if code_str.find(str1, 0, len(code_str)):
                #     print("移除")
                code_str = re.findall(r"\d+\.*?\d", code_str)  # 正则  遇到开始和结束就进行截取
                #print(type(code_str))
                # print(code_str) #正则化后的列表
                code_str = list(filter(lambda s: isinstance(s, str) and 11 >= len(s) >= 7, code_str))

                if len(code_str) :
                    code_str = code_str.pop(0)
                else:
                    print("识别数字空")
                code_str = "".join(code_str)
                # print("识别出", code_str)

                if code_str.strip() == '':
                                        #shutil.move(path,newpos)
                    #os.remove(path)
                    print("识别错误")
                    continue
                src = os.path.join(os.path.abspath(self.path), item)  #path   os.path.abspath是绝对路径
                dst = os.path.join(os.path.abspath(self.path),
                                   '' + str(code_str) + '.jpg')  # 处理后的格式也为jpg格式的，当然这里可以改成png格式
                # dst = os.path.join(os.path.abspath(self.path), '0000' + format(str(i), '0>3s') + '.jpg')    这种情况下的命名格式为0000000.jpg形式，可以自主定义想要的格式

                try:
                    os.rename(src, dst)  #改名
                    print('converting %s to %s !' % (src, dst))
                except:
                    continue
            # print ('total %d to rename & converted %d jpgs' % (total_num, i))

if __name__ == '__main__':
    tk.Tk().withdraw()
    path = askdirectory()
    demo = BatchRename()
    demo.rename(path)