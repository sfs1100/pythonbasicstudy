# !/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    作者：sfs
    功能：AQI计算
    版本：6.0
    日期：2017-11-27
    2.0增加读取和写入json文件
    3.0读取json文件保存成csv
    4.0读取文件并判断文件是json还是CSV格式并进行相应处理（需要引入os包）
    5.0通过网络实时爬取最新的空气质量aqi的数据
    6.0通过beautifulsoup获得空气质量数据
'''

import requests
from bs4 import BeautifulSoup
from lxml import etree

def get_city_aqi(city_pinyin):
    '''
        获取城市的空气质量数据 
    '''

    url = 'http://pm25.in/' + city_pinyin
    r = requests.get(url, timeout=30).text
    soup = BeautifulSoup(r, 'lxml')
    div_list = soup.find_all('div', {'class':'span1'})

    city_aqi = []
    for i in range(8):
        div_content = div_list[i]
        caption = div_content.find('div',{'class':'caption'}).text.strip()
        value = div_content.find('div',{'class':'value'}).text.strip()

        city_aqi.append((caption, value))
    # s = etree.HTML(r)
    # div_list = s.xpath('//div[@class="span1"]')
    # city_aqi = []
    # for i in div_list:
    #     caption = i.xpath('div[@class="caption"]/text()')[0].strip()
    #     value = i.xpath('div[@class="value"]/text()')[0].strip()
    #     city_aqi.append((caption,value))
    return city_aqi


def main():
    '''
        主函数 
    '''

    city_pinyin = input('请输入城市拼音')
    city_aqi = get_city_aqi(city_pinyin)
    print(city_aqi)

if __name__ == '__main__':
    main()