# codeing=utf-8
'''
    作者：sfs
    功能：五角星的绘制
    版本：3.0
    日期：2017-11-09
    新增功能：加入循环操作绘制重复不同大小的图形
    新增功能：使用迭代函数绘制重复不同大小的图形
'''

import turtle


def draw_recursize_pentagram(size):
    """
        迭代绘制五角星
    """
    count = 1
    while count <=5:
        turtle.forward(size)
        turtle.right(144)
        count += 1
    #五角星绘制完毕，更新参数
    size += 10
    if size <=100:
        draw_recursize_pentagram(size)

def main():
    '''
        主函数
    '''

    turtle.penup()
    turtle.backward(100)
    turtle.pendown()
    turtle.pensize(2)
    turtle.pencolor('red')

    size = 50
    draw_recursize_pentagram(size)


    turtle.exitonclick()

if __name__ == '__main__':
    main()

