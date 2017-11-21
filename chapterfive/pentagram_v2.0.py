# codeing=utf-8
'''
    作者：sfs
    功能：五角星的绘制
    版本：2.0
    日期：2017-11-09
    新增功能：加入循环操作绘制重复不同大小的图形
'''

import turtle

def draw_pemtagram(size):
    count = 1
    while count <= 5:
        turtle.forward(size)
        turtle.right(144)
        count += 1

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
    while size <= 200:
        draw_pemtagram(size)
        size += 10

    # for size in range(50,200,10):
    #     draw_pemtagram(size)

    turtle.exitonclick()

if __name__ == '__main__':
    main()

