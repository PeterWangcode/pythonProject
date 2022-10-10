# 读取的字符是字母表的第几个字母
import string

s = input('请输入字母:')

idx = string.ascii_lowercase.find(s)
if idx != -1:
    print('第{}个小写字母。'.format(idx + 1))
else:
    idx = string.ascii_uppercase.find(s)
    if idx != -1:
        print('第{}个大写字母。'.format(idx+1))
    else:
        print('错误字符')
