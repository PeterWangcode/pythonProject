#内置函数 range()
#range函数的优点：
#   不管range对象表示的整数序列有多长，所有range对象占用的内存空间都是相同的，因为
#仅仅需要存储start,stop,step,只有当用到range对象时，才会去计算序列中的相关元素
#作用：用于生成一个整数序列
#创建 range 函数的三种方法

print('----------------range函数的第一种创建方法----------------')
#range(stop)---->创建一个[0,stop)之间的整数序列   #小括号中指定了1个参数
r=range(10)#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]，从0开始，默认相差1
print(r)#返回值是一个迭代器对象  range(0,10)
print(list(r))#想查看range对象中的整数序列，需要调用'list'     list---->是列表的意思

print('----------------range函数的第二种创建方法----------------')
#range(start,stop)---->创建一个[start,stop)之间的序列，步长为1   #小括号中指定了2个参数：
r=range(2,10)#指定了从2开始，到10结束
print(list(r))#[2, 3, 4, 5, 6, 7, 8, 9]

print('----------------range函数的第三种创建方法----------------')
#range(start,stop,step)---->创建一个[start,stop)之间的整数序列，步长为step    #小括号中指定了3个参数：起始值、结束值、步长
r=range(2,10,2)#指定了从2开始，到10结束，步长为2
print(list(r))#[2, 4, 6, 8]

#判断指定的整数 在序列中是否存在（可以使用in,not in)
print(6 in r)#True  6在这个序列中
print(10 in r)#False  10不在这个序列中

print(6 not in r)#False  6在这个序列中
print(10 not in r)#True  10不在这个序列中

