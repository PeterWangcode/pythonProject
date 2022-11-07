# 元组的创建方式
#   1）直接使用小括号（半角）：
#       t = ('python', 'hello', 90)
#   2）使用内置函数tuple():
#        t = tuple(('python', 'hello', 90))
#   3）只包含一个元素的元组需要使用 ’,‘ 和 ’()‘
#       t = (10, )
print('{:%^48}'.format(' 第一种 使用小括号 '))
t = ('python', 'hello', 98,)
print(f'元组t：{t}\t元组t的类型：{type(t)}')
print()

t2 = 'python', 'hello', 98  # 省略了小括号
print(f'元组t2：{t2}\t元组t2的类型：{type(t2)}')
print()

t3 = ('python')  # 元组只有一个元素时，省略 逗号 不会创建成元组类型
print(f't3：{t3}\tt3的类型：{type(t3)}')
print()

t4 = ('python',)  # 元组元素只有一个元素时， 逗号 不可以省略
print(f'元组t4：{t4}\t元组t4的类型：{type(t4)}')
print()

print('{:%^48}'.format(' 第二种 使用内置函数tuple '))
k = tuple(('python', 'hello', 100))
print(f'元组k：{k}\t元组k的类型：{type(k)}')
print()

print('{:%^48}'.format(' 空元组的创建 '))

# 空列表
lst = []
lst_1 = list()
print(f'空列表 lst:{lst},lst_1{lst_1}\nlst数据类型：{type(lst)},lst_1数据类型：{type(lst_1)}')
print()

# 空字典
dict_1 = {}
dict_2 = dict()
print(f'空字典 dict_1:{dict_1},dict_2{dict_2}\ndict_1数据类型：{type(dict_1)},dict_2数据类型：{type(dict_2)}')
print()

# 空元组
tuple_1 = ()
tuple_2 = tuple()
print(f'空元组 tuple_1:{tuple_1},tuple_2{tuple_2}\ntuple_1数据类型：{type(tuple_1)},tuple_2数据类型：{type(tuple_2)}')
print()
