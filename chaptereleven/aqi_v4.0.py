# !/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    作者：sfs
    功能：AQI计算
    版本：4.0
    日期：2017-11-23
    2.0增加读取和写入json文件
    3.0读取json文件保存成csv
    4.0读取文件并判断文件是json还是CSV格式并进行相应处理（需要引入os包）
'''

import json
import csv
import os


def process_json_file(filepath):
    '''
        解码json文件
    '''
    # f = open(filepath, mode='r', encoding='utf-8')
    # city_list = json.load(f)
    # return city_list

    with open(filepath, mode='r', encoding='utf-8') as f:
        city_list = json.load(f)
    print(city_list)

def process_csv_file(filepath):
    '''
        处理csv文件
    '''
    with open(filepath, mode='r', encoding='utf-8', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            print('|'.join(row)) #数据之间以（|）进行分割

def main():
    '''
        主函数 
    '''

    filepath = input('请输入json文件名称：')
    filename, file_ext = os.path.splitext(filepath)

    if file_ext == '.json': #这里file_ext得出的数据是.加文件类型（.json)字符串
        process_json_file(filepath)
    elif file_ext == '.csv':
        process_csv_file(filepath)
    else:
        print('不支持的文件格式')


if __name__ == '__main__':
    main()