# 元组元素的获取方式


print('{:%^48}'.format(' 使用索引元组方式 '))
t = (10, [20, 30], 9)
print(t[0])
print(t[1])
print(t[2])
# print(t[3])  # IndexError: tuple index out of range
print()

print('{:%^48}'.format(' 使用遍历元组方式 '))
t = (10, [20, 30], 9)
for item in t:
    print(item)
