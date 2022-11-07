def fun(a, b, c, ):  # a, b, c在函数的定义处，所以是形式参数
    print('a=', a)
    print('b=', b)
    print('c=', c)


# 函数的调用
fun(10, 20, 30, )
lst = [11, 22, 33, ]
fun(*lst)  # 在函数调用时，将列表中的每个元素都转换为位置实参传入

print('------------------------------------------------')

fun(c=100, b=200, a=300, )
dic = {'a': 111, 'b': 222, 'c': 333}
fun(**dic)  # 在函数调用时，将字典中的键值对都转换为关键字实参传入

'''函数的默认参数'''


def c_fun(a, b=10):  # b 是在函数的定义处，所以b是形参，而且进行了赋值，所以b称为默认值形参
    print('a=', a)
    print('b=', b)


def c_fun2(*args):  # 个数可变的位置形参
    print(args)


def c_fun3(**args2):  # 个数可变的关键字形参
    print(args2)


c_fun2(10, 20, 30, 40, )
c_fun3(a=110, b=120, c=119)


def c_fun4(a, b, c, d, ):
    print('a=', a)
    print('b=', b)
    print('c=', c)
    print('d=', d)


c_fun4(10, 20, 30, 40)  # 位置实参传递
c_fun4(a=10, b=20, c=30, d=40)  # 关键字实参传递
c_fun4(10, 20, c=30, d=40)
