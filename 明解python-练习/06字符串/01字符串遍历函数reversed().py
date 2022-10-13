s = input('输入字符串：')

# 生成正向遍历字符串
for i, char in enumerate(s, 1):
    print('第{}个字符：{}'.format(i, char))

print('-' * 32)
# 生成反向遍历字符串
for i, char in enumerate(reversed(s), 1):
    print('第{}个字符：{}'.format(i, char))

# 不使用函数来完成字符串的遍历（正向）
s = input('输入字符串：')

for i in s:
    print(i)

# 不使用函数来完成字符串的遍历（正向）
s = input('输入字符串：')

for i in s[::-1]:
    print(i)