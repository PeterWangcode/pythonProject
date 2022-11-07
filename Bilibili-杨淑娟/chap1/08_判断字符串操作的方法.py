# 判断字符操作的方法
#   1）isidentifier() 判断指定的字符串是不是合法的标识符
#   2）isspace() 判断指定的字符串是否全部由空白字符组成（回车、换行、水平制表符）
#   3）isalpha() 判断指定的字符串是不是全部由字母组成
#   4）isdecimal() 判断指定字符串是否全部由十进制的数字组成
#   5）isnumeric() 判定指定的字符串是否全部由数字组成
#   6）isalnum() 判断指定的字符串是否全部由数字和字母组成

'''isidentifier() 判断指定的字符串是不是合法的标识符'''
s = 'hello,word'
print('1.', s.isidentifier())  # False,字符串中含有’，’
print('2.', 'hello'.isidentifier())  # True
print('3.', '张三_'.isidentifier())  # True
print('4.', '张三_123'.isidentifier())  # True
print('-----------------------------------')

'''isspasce() 判断指定的字符串是否全部由空白字符组成'''
print('\t'.isspace())  # Ture
print('-----------------------------------')

'''isalpha() 判断指定的字符串是不是全部由字母组成'''
print('1.', 'abc'.isalpha())  # True
print('2.', '张三'.isalpha())  # True
print('3.', '张三1'.isalpha())  # False
print('-----------------------------------')

'''isdecimal() 判断指定的字符串是否全部由十进制的数字组成'''
print('1.', '123'.isdecimal())  # True
print('2.', '123四'.isdecimal())  # False
print('3.', 'Ⅱ Ⅱ Ⅱ'.isdecimal())  # False
print('-----------------------------------')

'''isnumeric() 判断指定的字符串是否全部由数字组成'''
print('1.', '123'.isnumeric())  # True
print('2.', '123四'.isnumeric())  # True
print('3.', 'Ⅱ Ⅱ Ⅱ'.isnumeric())  # True
print('-----------------------------------')

'''isalnum() 判断指定的字符串是否全部由字母和数字组成'''
print('1.', 'abc1'.isalnum())  # True
print('2.', '张三123'.isalnum())  # True
print('3.', 'abc!'.isalnum())  # False

