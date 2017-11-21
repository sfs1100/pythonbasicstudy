'''
    作者：sfs
    功能：52周存钱挑战
    版本：2.0
    日期：2017-11-13
    2.0增加功能：记录每周的存款数 用到了list
'''

import math

def main():
    '''
        主函数
    '''

    money_per_week = 10
    i = 1
    increase_money = 10
    total_week = 52
    saving = 0

    money_list = []

    while i <= total_week:
        money_list.append(money_per_week)
        saving = math.fsum(money_list)
        print('第{}周，存入{}元，账户累计{}元'.format(i, money_per_week, saving))
        money_per_week += increase_money
        i += 1

if __name__ == '__main__':
    main()