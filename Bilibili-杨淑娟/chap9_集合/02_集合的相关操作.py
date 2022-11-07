# 集合元素的判断操作
#   1）in或not in
# 集合元素的新增操作
#   2）调用add（）方法，一次添加一个操作
#   3）调用update()方法，至少添加一个元素
# 集合元素的删除操作
#   1）调用remove()方法，一次删除一个指定元素，如果指定的元素不存在抛出 keyError
#   2) 调用discord()方法，一次删除一个指定元素，若指定的元素不存在，也不抛出异常
#   3）调用pop()方法，一次删除一个任意元素
#   4）调用clear()方法，清空集合

print("{:%^48}".format(' 集合的判断操作 '))
s = {10, 20, 30, 40, 50, 60}
print(10 in s)  # True
print(100 in s)  # False
print(10 not in s)  # False
print(100 not in s)  # True
print()

print("{:%^48}".format(' 集合元素的新增操作 '))
s = {10, 20, 30, 40, 50, 60}
s.add(70)  # 一次添加一个
print(s)
s.update([80, 90])  # 一次至少添加一个元素
s.update({100, 110})
s.update((120, 130))
print(s)
print()

print("{:%^48}".format(' 集合元素的删除操作 '))
print(f'原列表:{s}')
s.remove(100)
# s.remove(500)  # KeyError: 500 , 元素不存在会报错
s.discard(500)  # 集合中有该元素会删除，没有也不会报错
print(s)
s.pop()  # r任意删除一个元素
# s.pop(10)  # TypeError: set.pop() takes no arguments (1 given), 该函数是没有参数的，写入参数会报错
s.clear()  # 清空所有元素
print(s)
