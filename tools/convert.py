
# 读取每行数据，在其前后添加引号，在后面添加逗号，用于查询SQL中使用in语法
# example:
#         aaaaa
#         tt
#         tt
#         ddd
# 转换之后：
#         'aaaaa',
#         'tt',
#         'tt',
#         'ddd'
# 备注：将需要转换的文件放到当前目录下，命名为a.txt，执行python convert.py

# def alter(file,old_str,new_str):
#     file_data = ""
#     with open(file, "r", encoding="utf-8") as f:
#         for line in f:
#             if old_str in line:
#                 line = line.replace(old_str,new_str)
#             file_data += line
#     with open(file,"w",encoding="utf-8") as f:
#         f.write(file_data)
#
# alter("a.txt", "dddd", "python")

#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys, getopt

def convert(file, file2):
    data_text = ''
    with open(file, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            line = ('\'' + line).strip() + '\'' +',\r\n'
            data_text += line
    with open(file2, 'w', encoding='utf-8') as f2:
        data_text2 = data_text[:-3]
        print(data_text2)
        f2.write(data_text2)

convert('a.txt', 'a_1.txt')

