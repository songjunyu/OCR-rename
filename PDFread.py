"""给三出一"""
import pdfplumber
from PyPDF2 import PdfFileReader, PdfFileWriter
import re
import collections
import time
from tqdm import tqdm


class PDF:
    def __init__(self):
        pass

    def PDFread(self, roll, score, degree, parent_path):
        self.学籍卡 = roll
        self.成绩表 = score
        self.学位证 = degree
        start = time.process_time()
        # 学籍卡PDF分割
        # 学籍卡 = r"C:\Users\Kevin\Desktop\pdf\2016自动化学籍卡.pdf"
        pdf_0 = PdfFileReader(self.学籍卡)
        dict = {}
        # 学位证PDF分割
        # 学位证 = r"C:\Users\Kevin\Desktop\pdf\2016自动化学位证明打印.pdf"
        pdf_1 = PdfFileReader(self.学位证)
        学位证字典 = {}
        # 成绩表PDF分割
        # 成绩表 = r"C:\Users\Kevin\Desktop\pdf\2016自动化成绩表.pdf"
        pdf_2 = PdfFileReader(self.成绩表)
        成绩表字典 = collections.defaultdict(list)

        with pdfplumber.open(self.学籍卡) as pdf:
            page_count = len(pdf.pages)
            # print('学籍卡文件包含%d页PDF' % page_count)
            pbar = tqdm(desc='学籍卡扫描', total=page_count, ascii=' =')
            n = -1
            for page in pdf.pages:
                n += 1
                # print('---------- 学籍卡第[%d]页 ----------' % page.page_number)
                str_0 = page.extract_text()
                reg = re.compile(r'学号：\d+\.*?\d')
                match = reg.search(str_0)
                if not match:
                    continue
                student_number = match.group(0)[3:15]
                dict[student_number] = pdf_0.getPage(n)
                pbar.update(1)
                # print(student_number)
        # print('-----------------学籍卡扫描已完成--------------')
        pbar.close()

        with pdfplumber.open(self.成绩表) as pdf:
            page_count = len(pdf.pages)
            pbar = tqdm(desc='成绩表扫描', total=page_count, ascii=' =')
            # print('成绩表文件包含%d页PDF' % page_count)
            j = -1
            for page in pdf.pages:
                j += 1
                # print('---------- 成绩表第[%d]页 ----------' % page.page_number)
                str_0 = page.extract_text()
                reg = re.compile(r'学号：\d+\.*?\d')
                match = reg.search(str_0)
                if not match:
                    continue
                student_number = match.group(0)[3:15]
                成绩表字典[student_number].append(pdf_2.getPage(j))
                # print(student_number)
                pbar.update(1)
        pbar.close()
        # print('-----------------成绩表扫描已完成--------------')
        with pdfplumber.open(self.学位证) as pdf:
            page_count = len(pdf.pages)
            pbar = tqdm(desc='学位证扫描', total=page_count, ascii=' =')
            print('学位证文件包含%d页PDF' % page_count)
            i = -1
            for page in pdf.pages:
                i += 1
                # print('---------- 学位证第[%d]页 ----------' % page.page_number)
                # print(page.extract_text())
                str_0 = page.extract_text()
                reg = re.compile(r'学号：\d+\.*?\d')
                match = reg.search(str_0)
                if not match:
                    continue
                student_number = match.group(0)[3:15]
                学位证字典[student_number] = pdf_1.getPage(i)
                # print(student_number)
                pbar.update(1)
        pbar.close()
        # print('--------------学位证扫描已完成------------------')

        pbar = tqdm(desc='合并', total=page_count, ascii=' =')
        for student_number in dict.keys():
            pdf_writer = PdfFileWriter()

            # 写入学籍卡
            个人学籍卡 = dict[student_number]
            pdf_writer.addPage(个人学籍卡)
            # 写入成绩表
            if f'{student_number}' in 成绩表字典.keys():
                for item in 成绩表字典[student_number]:
                    pdf_writer.addPage(item)
            # 写入学位证
            if f'{student_number}' in 学位证字典.keys():
                个人学位证 = 学位证字典[student_number]
                pdf_writer.addPage(个人学位证)

            outputFilename = parent_path + '\\' + student_number + ".pdf"
            with open(outputFilename, "wb") as out:

                pdf_writer.write(out)
                # print("成功生成目标文件", outputFilename)
            pbar.update(1)
        pbar.close()
        end = time.process_time()
        print('运行时间%d分%f秒' % (((end - start) // 60), (((end - start) / 60 - (end - start) // 60) * 60)))
