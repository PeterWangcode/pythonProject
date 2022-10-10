#python一切皆对象，所有对象都有一个bool值
  #获取对象的布尔值
    #使用内置函数bool
#以下对象的布尔值为False
#False
#数值0
#None
#空字符串
#空列表
#空元组
#空字典
#空集合

print('----------------以下对象的布尔值均为False----------------')
#测试对象的bool值
print(bool(False))#False
print(bool(0))#False
print(bool(0.0))#False
print(bool(None))#False
print(bool(''))#False
print(bool(""))#False
print(bool([]))#空链表
print(bool(list()))#空链表
print(bool(()))  #空元组
print(bool(tuple()))#空元组
print(bool([]))#空字典
print(bool(dict()))#空字典
print(bool(set()))#空集合


print('----------------其他对象的布尔值均为Ture----------------')
print(bool(185))
print(bool(True))
print(bool('hello word'))