# 转义字符
print('hello\nword')  # \ +转义功能的首字母  n--->newline的首字符表示换行
print('hello\tword')
print('hello\tword')  # \t是制表位转义字符，四个位置为一个制表位
print('helloooo\tword')
print('hello\rword')  # \r是回车转义字符，‘word’经过回车之后占了'hello'的位置
print('hello\bword')  # \b是退格转义字符，将’o'退没了

print('http:\\\\www.baidu.com')  # 打印字符'\'需要使用转义字符'\\'
print('老师说：\'大家好\'')  # 打印'''(单引号),需要使用转义字符''\'

# 原字符：不希望字符串中的转义字符起作用，就使用原字符，就是在字符串之前加上r，或者R
print(r'hello\n word')
# 注意事项，最后一个字符不能是 单个反斜杠
# print(r' hello\n word\')
print(r'hello\n word\\')
