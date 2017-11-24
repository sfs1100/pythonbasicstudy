# !/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    作者：sfs
    功能：AQI计算
    版本：3.0
    日期：2017-11-22
    2.0增加读取和写入json文件
    3.0读取json文件保存成csv
'''

import json
import csv


def process_json_file(filepath):
    '''
        解码json文件
    '''
    f = open(filepath, mode='r', encoding='utf-8')
    city_list = json.load(f)
    return city_list

def main():
    '''
        主函数 
    '''

    filepath = input('请输入json文件名称：')
    city_list = process_json_file(filepath)
    city_list.sort(key=lambda city: city['aqi']) #正序排列（1，2，3....)
    #city_list.sort(key=lambda city: city['aqi'], reverse=True) # 倒序排列(4,3,2,1)

    lines = []
    #列名
    lines.append(list(city_list[0].keys())) #取出第一个值中的key作为列的表头
    for city in city_list:
        lines.append(list(city.values())) #循环city_list列表取value

    f = open('aqi.csv', 'w', encoding='utf-8', newline='')
    writer = csv.writer(f)
    for line in lines:
        writer.writerow(line)
    f.close()

if __name__ == '__main__':
    main()