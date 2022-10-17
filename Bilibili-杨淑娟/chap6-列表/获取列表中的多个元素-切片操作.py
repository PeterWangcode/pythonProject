# 切片操作
# 列表名[start:stop:step)
# 1）切片的结果 ---> 原列表片段的拷贝(切出来之后形成一个新的列表）
# 2）切片的范围 ---> [star:stop)
# 3）step默认为1 ---> 简写为 [start,stop)

lst = [10, 20, 30, 40, 50, 60, 70, 80]
# star=1,stop=6,step=1
lst2 = print(lst[1:6:1])
print('原列表：', id(lst))
print('切片之后的列表：', id(lst2))
# 两个列表的id不同，表示两个列表为不同的列表

print(lst[1:6])  # 默认步长为1
print(lst[1:6:])  # 默认步长为1

# star=1,stop=6,step=2
print(lst[1:6:2])

# star采取默认,stop=6,step=2
print(lst[:6:2])  # star默认为0

# star=1,stop采取默认,step=2
print(lst[1::2])  # stop默认读取整个列表

print('------------------------ step步长为负数的时候 ------------------------')
print('原列表：', lst)
print(lst[::-1])  # 若步长为负数，则列表的第一个元素，为原列表的最后一个元素
# start=7,stop 默认,step=1
print(lst[7::-1])

# start=6,stop=0,step=-2
print(lst[6:0:-2])
