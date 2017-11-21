'''
    作者：sfs
    功能：52周存钱挑战
    版本：1.0
    日期：2017-11-13
'''


def main():
    '''
        主函数
    '''

    money_per_week = 10
    i = 1
    increase_money = 10
    total_week = 52
    saving = 0

    while i <= total_week:
        saving += money_per_week
        print('第{}周，存入{}元，账户累计{}元'.format(i, money_per_week, saving))
        money_per_week += increase_money
        i += 1

if __name__ == '__main__':
    main()