#双分支结构if……else……，二选一执行
#语法结构
#if 条件表达式：
#     条件执行体1
#else：
#     条件执行体2

#从键盘录入一个整数，编写程序让计算机判断是奇数还是偶数
print('----------------单分支结构----------------')
a=int(input('请输入一个整数：'))
if a%2==0:
    print(a,'为偶数')
else:
    print(a,'为奇数')