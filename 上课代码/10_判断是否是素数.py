num = int(input('请输入一个整数：'))

i = 2
while i < num:
    if num % i == 0:
        print(f'{num}不是素数！！！')
        break
    else:
        print(f'{num}是素数！！！')
        break
    i += 1