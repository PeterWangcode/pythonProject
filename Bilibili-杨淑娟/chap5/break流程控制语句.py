#brek流程控制语句
#用与结束循环结构，通常与分支结构if一起使用

print('----------------从键盘录入密码，最多输入3次，如果正确就结束循环----------------')
for item in range(3):
    pwd=input('输入密码：')
    if pwd=='8888':
        print('密码正确。')
        break
    else:
        print('密码错误。')