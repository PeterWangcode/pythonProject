# 向文件写入两行字符串（writelines方法）

f = open('hello.txt', 'w') # 打开（文本＋写入模式）

f.writelines(['Hello!\n', 'How are you?\n'])

f.close()                  # 关闭