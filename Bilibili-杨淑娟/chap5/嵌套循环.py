for i in range(0,3):#表示行，执行三次
    for j in range(0,4):#不换行输出四个‘*’
        print('*', end='\t')  # 不换行输出
    print()#换行

#输出直角三角形
for i in range(0,10):
    for j in range(0,i):
        print('*',end='')
    print()

#输出9*9乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(i,'*',j,'=',i*j,end='\t')
    print()