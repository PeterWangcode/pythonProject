#  1)remove()
#       a)一次删除一个元素
#       b)重复元素只删除第一个
#       c)元素不存在抛出 ValueError
#  2)POP()
#       a)删除一个指定索引位置上的元素
#       b)指定索引不存在抛出IndexError
#       c)不指定索引，删除列表最后一个元素
#  3)切片
#       一次至少删除一个元素
#  clean()
#       清空列表
#  del()
#       删除列表

print('{:-^48}'.format('remove()删除操作'))
lst = [10, 20, 30, 40, 50, 60, 30, ]
lst.remove(30)  # 从列表中移除一个元素，如果有重复元素只移出第一个出现的
print(f'删除‘30’之后的列表{lst}')
#    lst.remove(100)  # list.remove(x): x not in list
print()

print('{:-^48}'.format('pop()根据索引移除元素'))
lst.pop(1)
print(f'删除索引值为‘1’之后的列表{lst}')
# lst.pop(5)  # IndexError: pop index out of range  如果指定的索引位置不存在，将抛出异常
lst.pop()  # 如果不指定参数（索引），将删除列表中最后一个元素
print(f'不指定参数（索引）之后的列表{lst}')
print()

print('{:-^48}'.format('切片操作-删除至少一个元素，将产生一个新的列表内容'))
new_lst = lst[1:3]
print(f'原列表：{lst}')
print(f'切片之后的列表：{new_lst}')  # 切片之后产生一个新的列表
print('---------------不取出列表对象，而是删除列表对象---------------')
lst[1:3] = []  # 实质使用空列表替换切片的对象
print(f'用空列表替换切片对象，之后的列表{lst}')

print('{:-^48}'.format('lst.claen()-清空列表中的元素'))
lst.clear()
print(f'使用clean清空列表元素之后的列表{lst}')
print()

print('{:-^48}'.format('del语句将列表对象删除'))
del lst
# print(f'使用del语句删除列表对象之后的结果{lst}')#  NameError: name 'lst' is not defined
