# 显示函数'print()'
# 显示函数可以输出的内容：（1）数字 （2）字符串 （3）含有运算符的表达式
# 显示函数可以输出到的目的地：（1）控制台 （2）指定文件中

# 可以输出数字
print(520)
print(98.5)

# 可以输出字符串
# 单引号和双引号之内的是字符串
print('hello word')
print('hello word')

# 含有运算符的表达式
print(3 + 1)  # 这其中‘3’和‘1‘是操作数，’+‘是运算符

# 将数据输出到指定文件中
# 注意：（1）所指定的盘符是存在的 （2）使用‘file’
char = open('D:/text.txt', 'a+')  # 第一个单引号中的内容为文件地址,第二个单引号内容('a+')为如果文件不存在就创建，存在就在文件内容之后继续追加
print('hello word', file=char)
char.close()

# 不进行换行输出（输出内容在一行当中）
print('hell', 'word', 'python')
