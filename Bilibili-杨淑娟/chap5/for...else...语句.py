print('----程序开始----')
for item in range(0,3):
    pwd=input('输入密码：')
    if pwd=='8888':
        print('密码正确')
        break
    else:
        print('密码错误')
else:
    print('对不起，三次密码均输入错误')