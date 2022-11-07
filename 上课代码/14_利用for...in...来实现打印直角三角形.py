# 利用 for...in... 打印输出直角在 左下角 的直角三角形

n = int(input('腰长：'))

for i in range(1, n + 1):
    for _ in range(i):
        print('*', end='')
    print()

# 利用 for...in... 打印输出直角在 右下角 的直角三角形

n = int(input('腰长：'))

for i in range(1, n + 1):
    for _ in range(n - i):  # 打印空格
        print(' ', end='')
    for k in range(i):  # 打印‘*’号
        print('*', end='')
    print()
