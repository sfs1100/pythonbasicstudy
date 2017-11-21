# codeing=utf-8
'''
    作者：sfs
    功能：利用递归函数绘制分形树
    版本：2.0
    日期：2017-11-10
    新增功能：绘制彩色树，让最后一个数组是绿色的
'''

import turtle


def draw_branch(branch_length):
    """
        迭代绘制分型树
    """

    if branch_length > 5 :
        #绘制右侧树枝
        turtle.forward(branch_length)
        turtle.right(20)
        if branch_length <= 20:
            turtle.pencolor('green')
        else:
            turtle.pencolor('red')
        draw_branch(branch_length-10)


       #绘制左侧树枝
        turtle.left(40)
        if branch_length <= 20:
            turtle.pencolor('green')
        else:
            turtle.pencolor('red')
        draw_branch(branch_length-10)

        #返回之前的树枝
        turtle.right(20)
        if branch_length <= 20:
            turtle.pencolor('green')
        else:
            turtle.pencolor('red')
        turtle.backward(branch_length)







def main():
    '''
        主函数
    '''
    turtle.left(90)
    turtle.penup()
    turtle.backward(100)
    turtle.pendown()
    turtle.pensize(2)
    turtle.pencolor('red')

    size = 90
    draw_branch(size)


    turtle.exitonclick()

if __name__ == '__main__':
    main()

