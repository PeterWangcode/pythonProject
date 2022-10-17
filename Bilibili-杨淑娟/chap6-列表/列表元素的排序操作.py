#  列表元素排序常见的两种方式
#   1）调用sort()方法，列表中的所有元素默认按照从小到大的顺序进行排序，可以指定reverse() = True ，进行降序排序
#   2）调用内置函数sorted()，可以指定 reverse = True，进行降序排序，原列表不发生改变

print('{:*^48}'.format(' sort()方法 '))
lst = [10, 20, 30, 40, 50, 60, ]
print(f'排序前的列表：{lst},id:{id(lst)}')
#  开始排序，调用列表对象的sort方法，升序排序(sort方法是在原列表的基础上排序的，不会改变列表对象）
lst.sort()
print(f'排序后的列表：{lst},id:{id(lst)}')

#  通过指定关键字参数，将列表中的元素进行降序排序
lst.sort(reverse=True)  # reverse=True 表示降序排序，reverse = False就是降序排序
print(f'利用reverse = True之后的列表：{lst}')
lst.sort(reverse=False)
print(f'利用reverse = False之后的列表：{lst}')

print('{:*^48}'.format(' 调用内置函数sorted() '))
#  注意：使用sorted()函数将会产生一个新的列表对象
lst = [10, 20, 30, 40, 50, 60, ]
print(f'原列表：{lst}')
#  开始排序
new_lst = sorted(lst)
print(f'排序之后的列表：{new_lst}')

#  指定关键字参数，实现列表元素的降序排序
dect_lst = sorted(lst, reverse=True)
print(f'排序之后的列表：{dect_lst}')
