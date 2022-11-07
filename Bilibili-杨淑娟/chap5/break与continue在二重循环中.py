# 流程控制语句break与continue在二重循环中的使用
print('----------------break----------------')
for i in range(5):  # 外层循环代表执行五次
    for j in range(1, 11):
        j % 2 == 0  # j的值是2的倍数就跳出
        break
    print(j)

print('----------------continue----------------')
for i in range(5):  # 外层循环代表执行五次
    for j in range(1, 11):
        if j % 2 == 0:
            continue
        print(j, end='\t')
    print()
