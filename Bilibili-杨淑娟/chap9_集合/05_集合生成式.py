# 用于生成集合的公式
# { i*i for i in range(1, 10) }
# i*i：表示集合元素的表达式；i ：自定义变量； range(1, 10):可迭代对象
# 将{}改成[]就是列表生成式
# 没有元组生成式

'''列表生成式'''
lst = [i * i for i in range(1, 10)]
print(lst)

'''集合生成式'''
lst = {i * i for i in range(1, 10)}
print(lst)