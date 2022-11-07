# while 循环的语法结构
# while 条件表达式:        #Ture执行，False跳出
#      条件执行体（循环体）

a = 1
while a < 10:  # 判断会比循环多一次，因为最后一次判断是False，不会执行
    print(a)
    a += 1
