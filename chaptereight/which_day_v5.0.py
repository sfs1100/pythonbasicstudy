"""
    作者：sfs
    版本：4.0
    日期：2017-11-14
    功能：输入某年某月某日，判断这一天是这一年的第几天？
    2.0增加功能：用列表替换元组
    3.0增加功能：将月份划分为不同的集合再操作
    4.0增加功能：将月份及其对应天数通过字典表示
"""

from datetime import datetime

def is_leep_year(year):
    '''
        判断year是否为闰年
        是，返回true
        否，返回false
    '''

    is_leep = False

    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        is_leep = True

    return is_leep

def main():
    '''
        主函数
    '''

    input_date_str = input('请输入日期(yyyy/mm/dd)')
    input_date = datetime.strptime(input_date_str, '%Y/%m/%d')
    print(input_date)

    year = input_date.year
    month = input_date.month
    day = input_date.day

    month_day_dict = {1: 31,
                      2: 28,
                      3: 31,
                      4: 30,
                      5: 31,
                      6: 30,
                      7: 31,
                      8: 31,
                      9: 30,
                      10: 31,
                      11: 30,
                      12: 31}

    day_month_dict = {30:{4,6,9,11},
                      31:{1,3,5,7,8,10,12}}

    days = 0
    days += day

    for i in range(1, month):
        days += month_day_dict[i]

    for i in range(1, month):
        for key in day_month_dict.keys():
            if i in day_month_dict.values():
                days += key

    if is_leep_year(year) and month>2:
        days += 1

    print('这是{}年的第{}天'.format(year, days))


if __name__ == '__main__':
    main()