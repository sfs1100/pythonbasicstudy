"""
    作者：sfs
    功能：判断密码强度
    版本：2.0
    日期：2017-11-15
    2.0新增功能：循环的终止
"""

def check_number_exist(password_str):
    '''
        判断字符串中是否含有数字
    '''

    has_number = False

    for c in password_str:
        if c.isnumeric():
            has_number = True
            break
    return has_number

def check_letter_exist(password_str):
    '''
        判断字符串中是否含有字母
    '''

    has_letter = False

    for c in password_str:
        if c.isalpha():
            has_letter = True
            break
    return has_letter

def main():
    '''
        主函数
    '''

    try_times = 5

    while try_times >=0:
        password = input('请输入密码：')
        strength_level = 0

        if len(password) >= 8:
            strength_level += 1
        else:
            print('密码长度要求至少8位')

        if check_number_exist(password):
            strength_level += 1
        else:
            print('密码要求包含数字！')

        if check_letter_exist(password):
            strength_level += 1
        else:
            print('密码要求包含字母！')

        if strength_level == 3:
            print('恭喜！密码强度合格！')
            break
        else:
            print('密码强度不合格！')
            try_times -= 1

        print()

    if try_times <= 0:
        print('尝试次数过多，密码设置失败！')

if __name__ == '__main__':
    main()