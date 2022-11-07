# 条件表达式是if...else的缩写
# 语法结构：if  X:
#        else Y
# 运算规则：如果判断条件的布尔值为Ture,条件表达式返回值为X，否则条件表达式的返回值为False

'''从键盘录入两个整数，比较两个整数的大小'''
num_a = int(input('请输入整数a:'))
num_b = int(input('请输入整数b:'))

# if num_a>=num_b:
#    print(num_a,'大于或等于',num_b)
# else:
#    print(num_b,'大于',num_a)

print('----------------使用条件表达式进行比较----------------')
#              执行体1<----------True -------- 判断体 --------False-------> 执行体2
print(str(num_a) + '大于' + str(num_b) if num_a >= num_b else str(num_b) + '大于' + str(num_a))
