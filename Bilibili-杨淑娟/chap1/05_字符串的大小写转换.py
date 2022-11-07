# 字符串大小写转换的操作方法
#   1）upper() 把字符串中的所有字符都转换成大写字母
#   2）lower() 把字符串中的所有字符都转换成小写字母
#   3）swapcase() 把字符串中的所有大写字母转换成小写字母，把所有小写字母转换成大写字母
#   4）capitalize() 把第一个字符转换为大写，其余字符转换成小写
#   5）title() 把每一个单词的第一个字符转换为大写，其余字符转换为小写

s = 'hello word'
a = s.upper()
# 转换为大写
print(f'\t原字符串：{s}，id:{id(s)}\n新产生的字符串：{a},id:{id(a)}')  # 转换之后，会产生一个新的字符串对象
print()
# 转换为小写
b = s.lower()
print(f'\t原字符串：{s},id:{id(s)}\n新产生的字符串：{b},id{id(b)}')  # 转换之后，会产生一个新的字符串对象
print()
print(b == s)  # True , 内容相等
print(b is s)  # False , 地址不相同

#  交换字母大小写
s1 = 'Hello Python'
a1 = s1.swapcase()  # 大写的转换为小写的，小写的转换为大写的
print(a1)
print()

# 每个单词的首字母为大写，其余的为小写
b2 = s1.title()
print(b2)
print()
