# 布尔运算符

print('----------------and 并且 ----------------')
a, b = 1, 2
print(a == 1 and b == 2)  # True         Ture and Ture --->Ture
print(a == 1 and b < 2)  # False         True and False --->False
print(a != 1 and b == 2)  # False        False and True --->False
print(a != 1 and b != 2)  # False        False and False --->False

print('---------------- or 或者 ----------------')
print(a == 1 or b == 2)  # Ture        Ture and Ture --->Ture
print(a == 1 or b < 2)  # Ture         True and False --->True
print(a != 1 or b == 2)  # Ture        False and True --->Ture
print(a != 1 or b != 2)  # False       False and False --->False

# not非
print('---------------- not 对Bool类型操作数进行取反 ----------------')
f = True
f2 = False
print(not f)

print('---------------- in 与 not in  ----------------')
s = 'hello word'
print('w' in s)  # 'w'这个字符在 s 中
print('k' in s)  # ’k‘这个字符在 s 中
print('w' not in s)  # 'w'这个字符不在 s 中
print('k' not in s)  # ’k‘这个字符不在 s 中
