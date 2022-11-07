# 比较运算符的结果为bool类型
print('-----------比较运算符-----------')
a, b = 10, 20
print('a>b吗？', a > b)  # False
print('a<b吗？', a < b)  # Ture
print('a<=b吗？', a <= b)  # Ture
print('a>=b吗？', a >= b)  # False
print('a==b吗？', a == b)  # False
print('a!=b吗？', a != b)  # Ture

'''
   一个 ‘=’ 称为赋值运算符 ， ‘==’称为比较运算符
   一个变量由三部分组成：表示、类型、值
   ‘==’比较的是值还是标识呢？  比较的是值！
   如何来比较对象的标识呢？    使用‘is’！
'''

print('--------比较判断运算符‘==’与‘is’的区别--------')
a, b = 10, 10
print(a == b)  # Ture   #说明a与b的值相同
print(a is b)  # Ture  #说明a与b的id标识相同

list1 = [11, 22, 33, 44]
list2 = [11, 22, 33, 44]
print(list1 == list2)
print(list1 is list2)
print(id(list1))
print(id(list2))
# 结论：判断运算符‘==’比较的是值（value)
#     运算符   ‘is’比较的是标识（id）

print(a is not b)  # False     #‘is not’的意思是‘他们的地址是不相等的吗？’
print(list1 is not list2)  # Ture      #list1的id与list2的id是不相等的吗？
