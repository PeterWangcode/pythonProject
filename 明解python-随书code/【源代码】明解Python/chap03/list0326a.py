# 计算并输出较小的数字和较大的数字（其三：各代码块用一行代码编写） 

a = int(input('整数a：'))
b = int(input('整数b：'))

if a < b: min2 = a; max2 = b;
else: min2 = b; max2 = a;

print('较小的数字是', min2, '。') 
print('较大的数字是', max2, '。')
