'''
    作者：sfs
    版本：v3.0
    时间：2017-11-08
    功能：自由判断币种然后进行换算
    3.0 增加功能：程序可以一直运行，直到用户选择退出
'''

USD_VS_RMB = 6.77

currency_str_value = input('请输入带单位的货币金额：(是否要退出！退出请输入Q)')

i = 0

while currency_str_value != 'Q':

    i = i + 1
    print('循环次数', i)
    # 获得货币单位
    unit = currency_str_value[-3:]

    if unit == 'CNY':
        rmb_str_value = currency_str_value[:-3]
        rmb_value = eval(rmb_str_value)
        usd_value = rmb_value / USD_VS_RMB
        print('美元(USD)金额是：',usd_value)
    elif unit == 'USD':
        usd_str_value = currency_str_value[:-3]
        usd_value = eval(usd_str_value)
        rmb_value = usd_value * USD_VS_RMB
        print('人民币(CNY)金额是：', rmb_value)
    else:
        print('目前版本尚不支持该种货币！')

    print('*********************************************************')
    currency_str_value = input('请输入带单位的货币金额：(是否要退出！退出请输入Q)')

print('程序已退出！')


