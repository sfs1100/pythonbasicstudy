"""
    作者：sfs
    功能：判断密码强度
    版本：6.0
    日期：2017-11-17
    2.0新增功能：循环的终止
    3.0新增功能：保存密码及强度到文件中
    4.0新增功能：读取文件中的密码
    5.0新增功能：定义一个password工具类
    6.0新增功能：定义一个文件工具类
"""

class PasswordTool:
    '''
        密码工具类
    '''

    def __init__(self,password):
        #类的属性
        self.password = password
        self.strength_level = 0

    def process_password(self):
        if len(self.password) >= 8:
            self.strength_level += 1
        else:
            print('密码长度要求至少8位')

        if self.check_number_exist():
            self.strength_level += 1
        else:
            print('密码要求包含数字！')

        if self.check_letter_exist():
            self.strength_level += 1
        else:
            print('密码要求包含字母！')

    def check_number_exist(self):
        '''
            判断字符串中是否含有数字
        '''

        has_number = False

        for c in self.password:
            if c.isnumeric():
                has_number = True
                break
        return has_number

    def check_letter_exist(self):
        '''
            判断字符串中是否含有字母
        '''

        has_letter = False

        for c in self.password:
            if c.isalpha():
                has_letter = True
                break
        return has_letter

class FileTool:
    '''
        文件工具类
    '''
    def __init__(self, filepath):
        self.filepath = filepath

    def write_to_file(self, line):
        f = open(self.filepath, 'a')
        f.write(line)
        f.close()

    def read_from_file(self):
        f = open(self.filepath, 'r')
        lines = f.readlines()
        f.close()
        return lines

def main():
    '''
        主函数
    '''

    try_times = 5
    filepath = 'password_6.0.txt'
    file_tool = FileTool(filepath)

    while try_times >=0:
        password = input('请输入密码：')

        password_tool = PasswordTool(password)
        password_tool.process_password()


        # f = open('password_3.0.txt','a')
        # f.write('密码：{}，强度：{} \n'.format(password, password_tool.strength_level))
        # f.close()
        if password_tool.strength_level == 1:
            line = '密码：{}，强度：{} \n'.format(password, '弱')
        elif password_tool.strength_level == 2:
            line = '密码：{}，强度：{} \n'.format(password, '中')
        elif password_tool.strength_level == 3:
            line = '密码：{}，强度：{} \n'.format(password, '强')

        file_tool.write_to_file(line)

        if password_tool.strength_level == 3:
            print('恭喜！密码强度合格！')
            break
        else:
            print('密码强度不合格！')
            try_times -= 1

        print()

    if try_times <= 0:
        print('尝试次数过多，密码设置失败！')

    lines = file_tool.read_from_file()
    print(lines)

    # #读取文件
    # f = open('password_3.0.txt', 'r')
    #
    # #1. read()
    # # content = f.read()
    # # print(content)
    # # 2.readline()
    # # line = f.readline()
    # # print(line)
    # # line = f.readline()
    # # print(line)
    # #3. readlines()
    # for line in f:
    #     print('read: {}'.format(line))
    #
    # f.close()


if __name__ == '__main__':
    main()