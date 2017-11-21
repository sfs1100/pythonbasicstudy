# !/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    作者：sfs
    功能：AQI计算
    版本：2.0
    日期：2017-11-21
    2.0增加读取和写入json文件
'''

import json


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
    top5_list = city_list[:5]

    f = open('top5_aqi.json', mode='w', encoding='utf-8')
    json.dump(top5_list, f, ensure_ascii=False) #如果 不加 ensure_ascii=False  输出的如果有汉字的话都默认给转换成一堆编码 如果加上的话 就都能正常显示变成了汉字
    f.close()

if __name__ == '__main__':
    main()