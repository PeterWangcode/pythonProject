import random

principal = 100  # 本金100元

while principal > 0:
    num = random.randint(3, 18)  # 生成大小
    if 3 <= num <= 9:
        num = '小'
    elif 9 < num < 19:
        num = '大'

    while True:  # 玩家选择‘大’或‘小’
        print('请选择大小：\n 1) 3~9为小\n 2) 10~18为大')
        choose = int(input('我选择：'))
        if 3 <= choose <= 18:
            break
        else:
            print('输入错误值！！！')

    if 3 <= choose <= 9:
        choose = '小'
    elif 9 < choose < 19:
        choose = '大'

    # 审判
    if choose == num:
        print('玩家获胜！！！')
        principal += 10
    elif choose != num:
        print('玩家失败！！！')
        principal -= 10
    print(principal)

    # 游戏退出机制