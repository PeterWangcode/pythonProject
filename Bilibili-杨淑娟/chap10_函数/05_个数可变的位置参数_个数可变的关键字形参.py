# 个数可变的位置参数
#   定义函数时，可能无法事先确定传递的位置实参的个数时，使用可变的位置参数
#   使用 * 定义个数可变的位置形参
#   结果为一个元组
# 个数可变的关键字形参
#   定义函数时，无法事先确定传递的关键字实参的个数时，使用可变的关键字形参
#   使用 ** 定义个数可变的关键字形参
#   结果为一个字典

def fun(*args):
    print(args)


fun(10)
fun(10, 20, )
fun(10, 20, 30, )


def fun1(**args):
    print(args)


fun1(a=10, )
fun1(a=10, b=20, )
fun1(a=10, b=20, c=30, )

'''
def fun2(*args, **args):
        pass
    以上代码会报错，个数可变的位置参数，只能是一个
'''

'''
def fun2(**args, **args):
        pass
    以上代码会报错，个数可变的位置参数，只能是一个
'''


def fun2(*args1, **args2):
    pass


'''
def fun3(**args1, *args2):
    pass
在一个函数的定义过程中，既有个数可变的关键字参数，也有个数可变的位置形参，要求，个数可变的位置形参，放在个数可变的关键字形参之前
'''