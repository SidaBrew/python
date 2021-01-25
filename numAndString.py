# 单行注释
"""
多行注释
再来一行
CTRL+/注释的快捷键
"""
# print(2+2)
# 除法运算 (/) 永远返回浮点数类型。如果要做 floor division 得到一个整数结果（忽略小数部分）你可以使用 // 运算符；如果要计算余数，可以使用 %
print(17/3)
print(17//3)
print(17 % 3)
print(5 * 3 +2)
# 使用 ** 运算符来计算乘方
print(5 ** 2)
print(2 ** 7)
width = 20
height = 5*9
print(width * height)
# 包含多种混合类型运算数的运算会把整数转换为浮点数:
print(4 * 3.75 -1)
# 字符串 ==================================
print('doesn\'t')
print("doesn't")
print('"Isn\'t", they said.')
s = "First line. \nSecond line"
print(s)
print(s)
print('c:\some\name')
print(r'c:\some\name')
# 字符串字面值可以跨行连续输入。一种方式是用三重引号："""...""" 或 '''...'''。字符串中的回车换行会自动包含到字符串中，如果不想包含，在行尾添加一个 \ 即可
print("""\
Usage: thingy[OPTIONS]
    -h              Display this usage message
    -H hostname     Hostname to connect to
""")
# 字符串可以用 + 进行连接（粘到一起），也可以用 * 进行重复:
print(3 * 'un' +'ium')
# 相邻的两个或多个 字符串字面值 （引号引起来的字符）将会自动连接到一起.
print('py' 'thon')
# 如果你想连接变量，或者连接变量和字面值，可以用 + 号:
prefix = 'py'
print(prefix+'thon')
word = 'python'
print(word[0])
print(word[5])
# 索引也可以用负数，这种会从右边开始数:
print(word[-1])
print(word[-2])
print(word[-6])
print(word[0:2])
print(word[2:5])
print(word[:2]+word[2:])
print(word[:4]+word[4:])
# 切片的索引有默认值；省略开始索引时默认为0，省略结束索引时默认为到字符串的结束:
print(word[:2])
print(word[:4])
print(word[-2:])
# Python 中的字符串不能被修改，它们是 immutable 的。因此，向字符串的某个索引位置赋值会产生一个错误:
print('j'+word[2:])
s = 'sdfasfasfsdfsfsdfsdfsdfsdf'
print(len(s))
