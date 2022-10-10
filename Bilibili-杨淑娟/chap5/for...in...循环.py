for item in 'python':#第一次取出来的是p，将p赋值给item
    print(item)#将item的值输出

#range()产生一个序列，--->也是一个可迭代的对象
for i in range(10):
    print(i)

#如果在循环体中，不需要自定义变量，可将自定义变量写为‘_’
for _ in range(5):
    print('人生苦短，我用python.')

print('----------------使用for循环，计算1到100之间的偶数和----------------')
'''
1)
sum=0#存储偶数和
for i in range(1,101,2):
    sum+=i
print(sum)
'''
#2)
sum=0
for i in range(1,101):
    if i%2==0:
        sum+=i
print(sum)