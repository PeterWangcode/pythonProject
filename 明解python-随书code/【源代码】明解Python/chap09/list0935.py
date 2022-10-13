"""打印输出乘法表（内部函数）""" 

upper = int(input('从1到几：')) 

def multiplication_table(n: int) -> bool: 
    """打印输出数字1～n的乘法表""" 
    
    def put_bar(n: int) -> None: 
        """连续打印输出n个'-'并换行"""
        print('-' * n)

    if    1 <= n <=  3: w = 2
    elif  4 <= n <=  9: w = 3
    elif 10 <= n <= 31: w = 4
    else              : return False

    f = '{{:{}d}}'.format(w)
    put_bar(n * w)
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f.format(i * j), end='')
        print()
    put_bar(n * w)
    return True

multiplication_table(upper)
