'''
    作者：sfs
    功能：BMR计算器
    版本：5.0
    日期：2017-11-12
    3.0 增加功能：用户可以在一行输入所有信息，带单位的信息输出
    4.0 增加功能：处理异常操作
    5.0 增加功能: 增加一个计算函数
'''

def bmr_computer(input_str):
    try:
        str_list = input_str.split(' ')
        gender = str_list[0]
        weight = float(str_list[1])
        height = float(str_list[2])
        age = int(str_list[3])

        if gender == '男':
            bmr = (13.7 * weight) + (5.0 * height) - (6.8 * age) + 66
        elif gender == '女':
            bmr = (9.6 * weight) + (1.8 * height) - (4.7 * age) + 655
        else:
            bmr = -1

        if bmr != -1:
            print('您的性别：{}，体重：{}公斤，身高：{}厘米，年龄：{}岁'.format(gender, weight, height, age))
            print('您的基础代谢率：{}大卡'.format(bmr))
        else:
            print('暂不支持该性别')

    except ValueError:
        print('请输入正确的信息！')
    except IndexError:
        print('输入的信息过少！')
    except:
        print('程序异常！')

def main():
    '''
        主函数 
    '''
    y_or_n = input('是否退出程序(y/n)?')

    while y_or_n != 'y':
        print('请输入以下信息，用空格分割')
        input_str = input('性别 体重(kg) 身高(cm) 年龄:')
        bmr_computer(input_str)
        print()  # 输出空行
        y_or_n = input('是否退出程序(y/n)？')

    print('程序已退出！')

if __name__ == '__main__':
    main()