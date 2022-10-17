# 列表元素的添加操作
# 1）在列表的末尾添加一个元素：append()
# 2）在列表的末尾至少添加一个元素：extend()
# 3）在列表的任意位置添加一个元素：insert()
# 4）在列表的任意位置至少添加一个元素：切片


lst = [10, 20, 30]
print('添加之前：', lst)
lst.append(40)
print('添加之后：', lst)
lst2 = ['hello', 'word']
# lst.append(lst2)#将lst2作为一个元素添加到列表的末尾
# 向列表的末尾一次性添加多个元素
lst.extend(lst2)  # 在列表的末尾拓展，把lst2中的每一个数据分别添加到lst的末尾
print(lst)


print('{:-^48}'.format('利用insert添加一个元素'))
# 在任意位置上添加一个元素
lst.insert(1, 100)
print(lst)

# 在任意的位置添加N个元素
lst3 = [True, False, 'hello']
lst[1:] = lst3  #把索引值 <= 1 的元素切掉，用新的内容来替换
print(lst)
