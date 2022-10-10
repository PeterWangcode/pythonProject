#多分支结构
#语法结构：
# if 条件表达式1：
#       条件执行体1
# elif 条件表达式2：
#       条件执行体2
# elif 条件表达式3：
#       条件执行体3：
#elif  条件表达式n：
#        条件执行体n
#[else]：            #（可省略）
#        条件执行体n+1

'''
多分支结构，多选一执行
从键盘录入一个整数 成绩
90-100 A
80-89 B
70-79 C
60-69 D
0-59 E
小于0或者大于100为非法数据（不是成绩的有限范围）
'''

score=int(input('请输入你的成绩：'))
if score>=90 and score<=100:
    print('A级')
elif score>=80 and score<90:
    print('B级')
elif score>=70 and score <80:
    print('C级')
elif score>=0 and score<60:
    print('E级')
else:
    print('您输入了错误的值！！！\a')