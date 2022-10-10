#  & 按位与  对应数位都是 1 ，结果才为 1 ，否则为0
#  | 按位或  对应数位都是 0 ，结果才为 0 ，否则为1
#  左移运算符 <<  高位溢出舍去，低位补0 ， 每移一位，就乘2
#  右移运算符 >>  低位溢出舍去，高位补0 ， 每移一位，就除2

print('----------------按位与 & 运算和按位或 | 运算----------------')
print(4 & 8)#按位与&，同为1时结果为0
print(4 | 8)#按位或|，同为0时结果为0

print('---------------- 左移运算符 << 和 右移运算符 >> ----------------')
print(4 << 1)#向左移动一位（移动一个位置）  相当于乘2
print(4 << 2)#向左移动两位（移动两个位置）  相当于乘4

print(4 >> 1)#向右移动一位，相当于除以2
print(4 >> 2)#向右移动两位，相当于除以4