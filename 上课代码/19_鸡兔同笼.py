for i in range(1, 35):  # i 为兔
    j = 35 - i  # j 为鸡
    if i * 4 + j * 2 == 94:
        print(f'有{i}只兔子\n有{j}只鸡')
