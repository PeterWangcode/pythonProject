# 字符串的比较操作
#   1)运算符：> , >= , < , <= , ==,!=
#   2)比较规则：首先比较两个字符串的中的第一个字符，如果相等则继续比较下一个字符，
#     依次比较下去，直到两个字符中的字符不相等时，其比较结果就是两个字符串的比较
#      结果，两个字符串中的所有后续字符将不再被比较。
#    3）比较原理：两个字符进行比较时，比较的是其 ordinal value(原始值），调用内置函数ord
#       可以得到指定字符的ordinal value. 与内置函数ord对应的是内置函数chr，调用内置函数
#       chr时指定ordinal value. 可以得到其对应的字符

print('apple' > 'app')  # Ture
print('apple' > 'banana')  # False(相当于97 > 98)
print(ord('a'), ord('b'))
print(ord('杨'))

print(chr(97), chr(98))
print(chr(26472))
print('----------------------------')

'''
 == 与is的区别
 1）==判断的时 value 是否相等
 2）is 比较的是 id 是否相等
 '''
a = b = 'Python'
c = 'Python'

print(a == b)  # True
print(b == c)  # True

print(a is b)  # True
print(a is c)  # True

print(id(a))  # 1683030124464
print(id(b))  # 1683030124464
print(id(c))  # 1683030124464
