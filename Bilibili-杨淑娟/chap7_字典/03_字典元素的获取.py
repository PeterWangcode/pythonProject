# 一、获取字典元素的方法
#   1）[]--->举例：scores['张三’]
#   2）get()方法--->举例：scores.get('张三‘)
# 二、[]取值与get()取值的区别
#       1)[]如果字典中不存在指定的key，抛出keyError异常
#       2）get()方法取值，如果字典中不存在指定的key,并不会抛出keyError而是返回None，可以通过参数设置默认的value，以便指定的key不存在时返回

print('{:%^48}'.format(' 第一种 使用[] '))
scores = {'张三': 100, '李四': 98, '王五': 45}
print(scores['张三'])
# print(scores['陈六']) # KeyError: '陈六'

print('{:%^48}'.format(' 第二种 使用get方法 '))
print(scores.get('王五'))
print(scores.get('陈六'))  # None
print(scores.get('麻七', 666))  # 当查找的键不存在时，用get方法刻意指定默认值
