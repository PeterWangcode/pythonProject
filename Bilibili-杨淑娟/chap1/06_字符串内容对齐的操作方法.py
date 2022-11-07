# 字符串内容对齐的操作方法
#  1）center() 居中对齐，第一个参数指定宽度，第二个参数指定填充符（可省略，默认为空格），如果设置宽度小于字符串宽度，则返回原字符串
#  2）l just() 左对齐，第一个参数指定宽度，第二个参数指定填充符（可省略，默认为空格），如果设置宽度小于字符串宽度，则返回原字符串
#  3）r just() 右对齐，第一个参数指定宽度，第二个参数指定填充符（可省略，默认为空格），如果设置宽度小于字符串宽度，则返回原字符串
#  4）zfill() 右对齐，左边用0填充，该方法只接收一个参数，用于指定字符串的宽度，如果指定的宽度小于等于字符串的长度，返回字符串本身

s = 'hello word'

# center()方法
print(s.center(20, '*'))
print()

# l just()方法
print(s.ljust(20, '*'))
print(s.ljust(20))  # 默认填充10个空格
print(s.ljust(10))  # 返回原字符
print()

# r just() 方法
print(s.rjust(20, '*'))
print(s.rjust(20))  # 默认填充空格
print(s.rjust(10))  # 小于字符串宽度，返回原字符

# zfill() 方法，接收一个参数，用0填充
print(s.zfill(20))
print(s.zfill(10))
print('-8910'.zfill(8))
