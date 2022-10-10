# 浮点类型
# (1)浮点数由整数部分和小数部分
# (2)浮点数存储不精确
a = 3.14159
print(a, type(a))

# 使用浮点数进行计算时，可能会出现小数位不确定的情况
n1 = 1.1
n2 = 2.2
print(n1 + n2)
# 解决方案；导入 Decimal 模块
from decimal import Decimal

print(Decimal('1.1') + Decimal('2.2'))
