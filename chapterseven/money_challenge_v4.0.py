'''
    作者：sfs
    功能：52周存钱挑战
    版本：4.0
    日期：2017-11-13
    2.0增加功能：记录每周的存款数 用到了list
    3.0增加功能：使用循环直接计数 用到for循环
    3.0增加功能：使用循环直接计数
    4.0增加功能：灵活设置每周的存款数，增加的存款数及存款周数
'''

import math

def save_money_in_n_weeks(money_per_week,increase_money,total_week):
    '''
        计算n周内的存款金额
    '''
    money_list = []

    for i in range(total_week): #注意for循环是从0到51 所以下面i要加一
        money_list.append(money_per_week)
        saving = math.fsum(money_list)
        money_per_week += increase_money
    return saving

def main():
    '''
        主函数
    '''

    money_per_week = float(input('请输入每周的存入的金额：'))     # 每周的存入的金额
    increase_money = float(input('请输入每周的递增金额：'))     # 递增的金额
    total_week = int(input('请输入总共的周数：'))         # 总共的周数

    # 调用函数
    saving = save_money_in_n_weeks(money_per_week,increase_money,total_week)
    print('总存款金额',saving)


if __name__ == '__main__':
    main()