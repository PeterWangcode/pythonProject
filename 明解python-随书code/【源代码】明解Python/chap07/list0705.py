# 使用enumerate函数遍历列表的所有元素（从1开始计数） 

x = ['John', 'George', 'Paul', 'Ringo'] 

for i, name in enumerate(x, 1): 
    print('第{}个元素 = {}'.format(i, name))