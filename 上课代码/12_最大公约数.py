# 录入信息
num1, num2 = int(input('num1:')), int(input('num2:'))

# 升序排列输入的值
num1, num2 = sorted([num1, num2])

# 递减变量
n = num1

# 求取值
while n >= 1:
    if num1 % n == 0 and num2 % n == 0:
        print(f'{num1}和{num2}的最大公约数：{n}')
        break
    n -= 1
