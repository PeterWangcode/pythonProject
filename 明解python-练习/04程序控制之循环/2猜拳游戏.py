print('---------------- 猜拳游戏 ----------------')

import random

# 胜利次数、失败次数、平局次数
win = lose = draw = 0

while True:
    AI = random.randint(0, 2)  # 电脑随机出拳
    while True:
        print('0:石头/1：剪刀/2：布')
        human = int(input('我出：'))  # 玩家出拳
        if 0 <= human <= 2:  # r若不符合范围，则重新出拳
            break  # 符合范围，出拳成功，跳出循环
    # 电脑出拳
    print('AI的是：', end='')
    if AI == 0:
        print('石头')
    elif AI == 1:
        print('剪刀')
    elif AI == 2:
        print('布')
    # 评判胜负
    judge = abs(human - AI) % 3
    if judge == 0:
        print('平局')
        draw += 1
    elif judge == 1:
        print('很遗憾,您输了！！！')
        lose += 1
    elif judge == 2:
        print('您取得了胜利！！！')
        win += 1

    retry = int(input('再玩一局（0：是/1：否）'))
    if retry == 1:
        print('----------------游戏结束----------------')
        break

print('成绩:')
print(win, '次胜利')
print(lose, '次失败')
print(draw, '次平局')
