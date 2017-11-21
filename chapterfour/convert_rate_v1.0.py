'''
    作者：sfs
    版本：v1.0
    时间：2017-11-08
    功能：人民币兑换美元
'''


rmb_str_value = input('请输入人民币(CNY)金额：')

rmb_value = eval(rmb_str_value) #把输入的数值字符串转换成数字

usd_va_rmb = 6.77

usd_value = rmb_value/usd_va_rmb

print('美元(USD)金额是:', usd_value)