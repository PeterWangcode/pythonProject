# 字典的生成式
#   1）{ item.upper() : price  for item, price in zip(items, prices)}
#     { 表示字典key的表达式：表示字典value的表达式 for 自定义key的变量， 自定义value的变量 in 可迭代对象 }
#   2）内置函数zip()
#       用于将可迭代的对象作为参数，将列表中对应的元素打包成一个元组，然后返回由这些元组组成的列表

items = {'Fruits', 'Books', 'others'}
prices = {96, 78, 45}

# 生成原列表
d = {item: price for item, price in zip(items, prices)}
print(d)
# 把键转换为大写字母
d = {item.upper(): price for item, price in zip(items, prices)}
print(d)
