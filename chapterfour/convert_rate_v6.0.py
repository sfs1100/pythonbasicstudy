'''
    作者：sfs
    版本：v4.0
    时间：2017-11-08
    功能：自由判断币种然后进行换算
    3.0 增加功能：程序可以一直运行，直到用户选择退出
    4.0 增加功能：将汇率兑换功能封装到函数中
    5.0 增加功能：(1) 使程序结构化 
    6.0 增加功能：(2) 简单函数的定义 lambda
'''


def main():
    '''
        主函数
    '''

    USD_VS_RMB = 6.77

    currency_str_value = input('请输入带单位的货币金额：')


    # 获得货币单位
    unit = currency_str_value[-3:]

    if unit == 'CNY':
        exchange_rate = 1 / USD_VS_RMB

    elif unit == 'USD':
        exchange_rate = USD_VS_RMB

    else:
        exchange_rate = -1

    if exchange_rate != -1:
        in_money = eval(currency_str_value[:-3])

        # 使用lambda定义函数
        convert_currency2 = lambda money: money * exchange_rate

        #调用lambda函数
        out_money = convert_currency2(in_money)
        print('转换后的金额：',out_money)
    else:
        print('目前版本尚不支持该种货币！')

    print('程序已退出！')

if __name__ == '__main__':
    main()


