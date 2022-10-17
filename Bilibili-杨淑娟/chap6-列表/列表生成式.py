print('{:*^48}'.format('利用列表生成式生成列表'))
lst = [i for i in range(1, 10)]
print(f'利用列表生成式生成的列表：{lst}')

#  生成列表元素为2、4、6、8、10的列表对象
lst2 = [i * 2 for i in range(1, 6)]
print(f'生成的列表对象：{lst2}')
