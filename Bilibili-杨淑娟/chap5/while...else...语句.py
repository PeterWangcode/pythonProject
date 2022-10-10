a=0
while a<3:
    pwd=input("输入密码：")
    if pwd=='8888':
        print('密码正确。')
        break
    else:
        print('输入错误')
    a+=1
else:
    print("对不起，三次均输入错误。")