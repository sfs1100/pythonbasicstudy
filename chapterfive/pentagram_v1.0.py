# codeing=utf-8
'''
    作者：sfs
    功能：五角星的绘制
    版本：1.0
    日期：2017-11-09
'''

import turtle

def main():
    '''
        主函数
    '''
    count = 1

    while count <= 5:
        turtle.forward(200)
        turtle.right(144)
        count = count + 1


    turtle.exitonclick()


if __name__ == '__main__':
    main()

