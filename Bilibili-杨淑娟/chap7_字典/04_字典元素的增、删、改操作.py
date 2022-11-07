# 字典的常用操作
# 一、key的判断
#   1）   in--->指定的key在字典中，则返回True
#   2)not in--->指定的key不在字典中，则返回True
# 二、字典元素的删除
#       del scores['张三’]
# 三、字典元素的新增
#       scores['jake'] = 90
# 四、获取字典元素视图的三种方法
#   1）keys()--->获取字典中所有的key
#   2）values()--->获取字典中的所有value
#   3）items()--->获取字典中的 key-value 对
# 五、字典元素的遍历
#       for item in scores:
#           print(item)

print('{:*^48}'.format('字典元素的判断'))
scores = {'张三': 100, '李四': 98, '王二麻子': 45, }
print('张三' in scores)  # True
print('张三' not in scores)  # False
print()

print('{:*^48}'.format('字典元素的删除'))
del scores['王二麻子']  # 删除指定的 key-value
print(scores)  # {'张三': 100, '李四': 98} 将指定键值对删除
scores.clear()  # 清空字典的元素
print(scores)  # {} 将列表的所有元素清空
print()

print('{:*^48}'.format('字典元素的添加操作'))
scores = {'张三': 100, '李四': 98, '王二麻子': 45, }
print(f'\t 原列表：{scores}')
scores['陈六'] = 101  # 新增元素
print(f'添加之后的列表：{scores}')
print()

scores['陈六'] = 666  # 修改元素
print(f'更改之后的元素：{scores}')
print()

print('{:*^48}'.format('字典元素的三种视图'))
scores = {'张三': 100, '李四': 98, '王二麻子': 45, }
keys = scores.keys()  # 获取所有的 key 并存储到变量 keys 中
print(f'键值对：{keys}\t类型：{type(keys)}')
print(list(keys))  # 将所有 key 组成的视图转换成列表
print()

values = scores.values()  # 获取字典中所有的 value 并存储到变量 values 中
print(f'字典元素的所有值：{values}\tvalues的数据类型：{type(values)}')
print(list(values))  # 将字典的所有 值 转换成 list 类型
print()

items = scores.items()  # 获取字典中所有的 key-value
print(f'字典的键值对：{items}\t 数据类型：{type(items)}')
print(list(items))  # 转换之后的列表元素是由 元组 构成的
print()

print('{:*^48}'.format('字典元素的遍历'))
scores = {'张三': 100, '李四': 98, '王二麻子': 45, }
for items in scores:
    print(items, scores.get(items))  # items 变量可以获取 key 而 scores.get() 方法可以获取 value
