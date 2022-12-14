# 驻留机制的几种情况（交互模式）
#   1）字符串长度为0或1时
#   2）符合标识符的字符串
#   3）字符串只在编译时进行驻留，而非运行
#   4）[-5, 256]之间的整数数字
# sys中的intern方法强制两个字符串指向同一个对象
# PyCharm对字符串进行了优化处理

# 字符转驻留机制的特点
#   1）当需要值相同的字符串时，可以直接从字符串池里拿来使用，避免频繁的创建和销毁，
#      提升效率和节约内存，因此拼接字符串和修改字符串是会比较影响性能的.
#   2) 在需要进行字符串拼接时建议使用str类型的Join()方法是先计算出所有字符中的长度，
#       然后再拷贝，只新一次对象，效率要比“+”效率高
