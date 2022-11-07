# 字符串的劈分操作
# 1）split()
#       a)从字符串的左边开始劈分，默认的劈分字符是空格字符串，返回的值是一个列表
#       b)以通过参数set指定劈分字符串是的劈分符
#       c)通过参数maxsplit指定劈分字符串时的最大劈分次数，在经过最大劈分之后，剩余的子串会做为单独的一部分
# 2）rsplit()
#       a)从字符串的右边开始劈分，默认的劈分字符是空格字符，返回的值都是一个列表
#       b)以通过参数sep指定劈分字符串是的劈分符
#       c)通过参数maxsplit指定劈分字符串时的最大劈分次数，在经过最大劈分之后，剩余的子串会单独做为一部分
'''split方法'''
# 不指定分隔符，默认为 空格
s = 'hello word python'
lst = s.split()
print(lst)
# 使用set指定分隔符
s1 = 'hello|word|python'
lst1 = s1.split(sep="|")
print(lst1)
# 使用maxsplit指定最大劈分次数
lst1 = s1.split(sep="|", maxsplit=1)
print(lst1)

'''rsplit方法（从右侧开始劈分）'''
print(s.rsplit())
print(s1.rsplit(sep='|'))
print(s1.rsplit(sep='|', maxsplit=1))
