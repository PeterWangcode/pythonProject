# 格式化字符串的两种操作
#   1） % 做占位符
#       a) %s ---> 字符串
#       b) %d/%i ---> 整形
#       c）%f ---> 浮点数
#   2） {} 做占位符

'''% 占位符'''
name = '王炸'
age = 20
print('我叫%s今年%d岁.' % (name, age))

'''{} 占位符'''
print('我叫{0}今年{1}岁.'.format(name, age))

'''f-string'''
print(f'我叫{name}今年{age}岁.')
