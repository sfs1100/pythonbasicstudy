'''
    作者：sfs
    功能：52周存钱挑战
    版本：3.0
    日期：2017-11-13
    2.0增加功能：记录每周的存款数 用到了list
    3.0增加功能：使用循环直接计数 用到for循环
'''

import math

def main():
    '''
        主函数
    '''

    money_per_week = 100
    increase_money = 50
    total_week = 52
    saving = 0

    money_list = []

    for i in range(total_week): #注意for循环是从0到51 所以下面i要加一
        money_list.append(money_per_week)
        saving = math.fsum(money_list)
        print('第{}周，存入{}元，账户累计{}元'.format(i+1, money_per_week, saving))
        money_per_week += increase_money


if __name__ == '__main__':
    main()