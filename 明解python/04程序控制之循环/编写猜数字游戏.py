'''
1)数字范围是1~1000
2)必须在10次以内猜中
3)输入小于1或大于1000的数字时，程序不会将其计入猜测的次数
'''

print('-' * 16, '猜数字游戏的实现', '-' * 16)

import random  # 调用函数模块

stage = 1  # 输入的次数
MAX_STAGE = 10  # 最多可以输入的次数
MAX = 1000  # 数字的最大范围
print('请在{}次以内猜中范围在1~{}的数字。'.format(MAX_STAGE, MAX))

answer = random.randint(1, MAX)  # 随机生成1~MAX之间的数字

while (stage <= MAX_STAGE):
    print('第{}次，正确的数字是：'.format(stage), end='')
    n = int(input(''))  # 录入自己猜测的数值

    if (n < 1 or n > MAX):
        print('数值的范围出错，不会计入猜测次数，请重新输入\a')
        continue  # 如果输入规定范围外的数字则重新输入
    if (n == answer):
        print('正解，第{}次猜中。'.format(stage))
        break
    elif (n > answer):
        print('正确数字要小一些')
    else:
        print('正确数字要打一些')

    stage += 1  # 调整次数的值

else:
    print('真可惜。正确数字是{}。'.format(answer))
