print('====================================')
for item in range(100, 1000):
    ge = item % 10          # 取个位
    shi = item // 10 % 10   # 取十位
    bai = item // 100 % 10  # 取百位

    #   print(bai,shi,ge)
    if ge ** 3 + shi ** 3 + bai ** 3 == item:
        print(f'{item}为水仙花数')
print('====================================')
