print('{:%^48}'.format('计算矩阵的和'))

h = int(input('行：'))
l = int(input('列：'))

a = [None] * h

for i in range(h):
    a[i] = [None] * l
    for j in range(l):
        a[i][j] = int(input('a[{}][{}]:'.format(i, j)))

b = [None] * h
for i in range(h):
    b[i] = [None] * l
    for j in range(l):
        b[i][j] = int(input('b[{}][{}]:'.format(i, j)))

c = [None] * h
for i in range(h):
    c[i] = [None] * l
    for j in range(l):
        c[i][j] = a[i][j] + b[i][j]

for i in range(h):
    for j in range(l):
        print('c[{}][{}] = {}'.format(i, j, c[i][j]))