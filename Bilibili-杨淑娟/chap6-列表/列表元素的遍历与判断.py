#判断指定元素在列表是否存在
#1）元素  in 列表名
#2）元素  not in  列表名

#列表元素的遍历
#for  迭代变量 in 列表名

print('---------------- 判断 ----------------')
print('p' in 'python')#True
print('k' not in 'python')#True

lst=[10,20,'python','hello']
print(10 in lst)
print(100 in lst)
print(10 not in lst)
print(100 not in lst)

print('---------------- 遍历 ----------------')
for item in lst:
    print(item)