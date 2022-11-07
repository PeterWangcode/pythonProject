import random

bj = 100  # 本金

# 外层循环控制游戏运行和退出
while True:

    # 控制输入
    while True:
        xz = float(input("请下注："))
        p = input("请玩家押大小，请输入大或小：")
        if xz > bj and p not in ("大", "小"):
            continue
        else:
            break

    # 利用生成的数字来控制大小
    num = random.randint(3, 18)

    # 判断胜负
    if (3 <= num <= 9 and p == "小") or (10 <= num <= 18 and p == "大"):
        print("恭喜你，押中！")
        bj = bj + xz
    else:
        print("很遗憾，未押中！")
        bj = bj - xz

    # 退出机制
    flag = input("是否继续游戏，结束按0，继续按任意键：")
    if flag == "0":
        print("游戏结束，您的本金为：", bj)
        break
