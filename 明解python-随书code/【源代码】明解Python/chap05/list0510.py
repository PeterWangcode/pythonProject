# 以十进制数的形式输出整数左右移位后的值

x = int(input('整数：')) 
n = int(input('移动的位数：')) 

print('x << n = {:d}'.format(x << n)) 
print('x >> n = {:d}'.format(x >> n))