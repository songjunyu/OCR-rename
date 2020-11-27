import pdfplumber
from PyPDF2 import PdfFileReader, PdfFileWriter
import re
import os
import collections
import time

start = time.process_time()
# 学籍卡PDF分割
学籍卡 = r"C:\Users\Kevin\Desktop\pdf\2016自动化学籍卡.pdf"
pdf_0 = PdfFileReader(学籍卡)
学籍卡字典 = {}
# 学位证PDF分割
学位证 = r"C:\Users\Kevin\Desktop\pdf\2016自动化学位证明打印.pdf"
pdf_1 = PdfFileReader(学位证)
学位证字典 = {}
# 成绩表PDF分割
成绩表 = r"C:\Users\Kevin\Desktop\pdf\2016自动化成绩表.pdf"
pdf_2 = PdfFileReader(成绩表)
成绩表字典 = collections.defaultdict(list)

with pdfplumber.open(学籍卡) as pdf:
    page_count = len(pdf.pages)
    print('学籍卡文件包含%d页PDF' % page_count)
    n = -1
    for page in pdf.pages:
        n += 1
        print('---------- 学籍卡第[%d]页 ----------' % page.page_number)
        str_0 = page.extract_text()
        reg = re.compile(r'学号：\d+\.*?\d')
        match = reg.search(str_0)
        student_number = match.group(0)[3:15]
        学籍卡字典[student_number] = pdf_0.getPage(n)
        print(student_number)
print('-----------------学籍卡扫描已完成--------------')
with pdfplumber.open(学位证) as pdf:
    page_count = len(pdf.pages)
    print('学位证文件包含%d页PDF' % page_count)
    i = -1
    for page in pdf.pages:
        i += 1
        print('---------- 学位证第[%d]页 ----------' % page.page_number)
        # print(page.extract_text())
        str_0 = page.extract_text()
        reg = re.compile(r'学号：\d+\.*?\d')
        match = reg.search(str_0)
        student_number = match.group(0)[3:15]
        学位证字典[student_number] = pdf_1.getPage(i)
        print(student_number)
print('--------------学位证扫描已完成------------------')
with pdfplumber.open(成绩表) as pdf:
    page_count = len(pdf.pages)
    print('成绩表文件包含%d页PDF' % page_count)
    j = -1
    for page in pdf.pages:
        j += 1
        print('---------- 成绩表第[%d]页 ----------' % page.page_number)
        str_0 = page.extract_text()
        reg = re.compile(r'学号：\d+\.*?\d')
        match = reg.search(str_0)
        student_number = match.group(0)[3:15]
        成绩表字典[student_number].append(pdf_2.getPage(j))
        print(student_number)
print('-----------------成绩表扫描已完成--------------')

for student_number in 学籍卡字典.keys():
    pdf_writer = PdfFileWriter()

    # 写入学籍卡
    个人学籍卡 = 学籍卡字典[student_number]
    pdf_writer.addPage(个人学籍卡)
    # 写入学位证
    个人学位证 = 学位证字典[student_number]
    pdf_writer.addPage(个人学位证)
    # 写入成绩表
    for item in 成绩表字典[student_number]:
        pdf_writer.addPage(item)

    outputFilename = r"C:\Users\Kevin\Desktop\pdf\2016自动化\\" + student_number + ".pdf"
    with open(outputFilename, "wb") as out:
        pdf_writer.write(out)
        print("成功生成目标文件", outputFilename)
end = time.process_time()
print('运行时间%d分%f秒' % (((end - start) // 60), (((end - start) / 60 - (end - start) // 60) * 60)))
