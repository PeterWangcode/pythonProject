# 集合的数学操作
#   1）交集：
#           a) intersection()方法
#           b) 求交集操作符 &
#   2）并集:
#           a) union方法
#           b)并集操作符 |
#   3）差集
#   4）对称差集

'''1) 交集'''
s1 = {10, 20, 30, 40, }
s2 = {20, 30, 40, 50, 60, }
print(s1.intersection(s2))  # intersection()方法 与 & 等价
print(s1 & s2)
print()

'''并集操作'''
print(s1.union(s2))  # union方法 与 | 等价
print(s1 | s2)
print()

'''差集操作'''
print(s1.difference(s2))  # difference方法 与 - 等价
print(s1 - s2)
print()

'''对称差集'''
print(s1.symmetric_difference(s2))  # symmetric_difference()方法 与 ^ 等价
print(s1 ^ s2)
print()