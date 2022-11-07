# 字符串的替换
#   1）replace() 第一个参数指定被替换的子串，第二个参数指定替换子串的字符串，该方法返回替换后得到的字符串，
#                替换前的字符串不发生变化，调用该方法时可以通过第三个参数指定最大替换次数
# 字符串的合并
#   2）join() 将列表或元组中的字符串合并成一个字符串

# 两个参数
s = 'hello word'
print(s)  # 原字符串
print(s.replace('word', 'python'))  # 替换后的字符串

# 三个参数
s1 = 'hello word word word'
print(s1.replace('word', 'python', 2))

print('---------------------------------------')
# join() 方法

# 连接列表
lst = ['hello', 'word', 'java', 'python']
print('|'.join(lst))
print(''.join(lst))
print()
# 连接元组
tup = ('hello', 'word', 'java', 'python')
print(''.join(tup))
# 连接字符串
print('*'.join('python'))