# 两个集合是否相等
#   可以使用运算符 == 和 ！= 进行判断
# 一个集合是否是另一个集合的子集
#   可以调用方法issubset进行判断
# 一个集合是否是另一个集合的 超集
#   可以调用方法issuperset进行判断
#   A是B的的超集
# 两个集合是否没有交集
#   可以调用方法isdisjoint进行判断

'''判断两个集合是否相等(元素相同，就相等)'''
s = {10, 20, 30, 40, }
s0 = {40, 30, 20, 10, }
print(s == s0)  # True , 集合中的元素是无序的
print(s != s0)  # False
print()

'''一个集合是否是另一个集合的子集'''
s1 = {10, 20, 30, 40, 50, 60, }
s2 = {10, 20, 30, 40 , }
s3 = {10, 20, 90}
print(s2.issubset(s1))  # True
print(s3.issubset(s1))  # False
print()

'''一个集合是否是另一个集合的超集'''
print(s1.issuperset(s2))  # True
print(s1.issuperset(s3))  # False
print()

'''两个集合是否没有交集'''
s4 = {100, 200, 300, }
print(s1.isdisjoint(s2))  # False , 有交集为False
print(s1.isdisjoint(s4))  # True , 没有交集为True
