# 字典的创建方法
#   1）使用花括号：
#       scores = { '张三':100, '李四’：98， ‘王五’：45 }
#   2）使用内置函数：( 采用赋值的方式，等号右边不加引号，右侧加不加双引号由数据类型来定）
#       dict( name = 'jack', age = 20)

print('{:%^48}'.format(' 一使用{}创建 '))
scores = {'张三': 100, '李四': 98, '王五': 45}
print(f'字典scores元素:{scores}\n字典scores类型:{type(scores)}')

print('{:%^48}'.format(' 二使用内置函数dict创建 '))
student = dict(name='jake', age=20)
print(f'字典scores元素:{student}\n字典scores类型:{type(student)}')

print('{:%^48}'.format(' 空字典 '))
d = {}
print(d)



