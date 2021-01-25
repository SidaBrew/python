# if预约
# x = int(input("Please enter an integer:"))
# if x <0:
#     x = 0
#     print('Negative changed to zero')
# elif x == 0:
#     print('Zero')
# elif x == 1:
#     print('Single')
# else:
#     print('More')

# for语句
# words = ['cat', 'window', 'defenestrate']
# for w in words:
#     print(w, len(w))
#
# left_num = input('请输入第一个数字：')
# right_num = input('请输入第二个数字：')
# # print(type(left_num), type(right_num))
# # 类型转换
# # int(val) 将变量val转换为int类型
# left_num_int = int(left_num)
# print(type(left_num), type(left_num_int))
# right_num_int = int(right_num)
# result = left_num_int + right_num_int
# print('%d + %d 的结果是 %d' % (left_num_int, right_num_int, result))
# ===============================================================
# a = 10
# b = 20
# if a > b:
#     ret = a + b
# else:
#     ret = a - b
# print('ret = %d' % ret)
# # ==========================================
# input_username = input('请输入您的用户名：')
# input_password = input('请输入您的密码：')

# correct_name = 'admin'
# correct_pass = '123'

# if input_username == correct_name:
#     if input_password == correct_pass:
#         print('欢迎 %s 登录系统！' % input_username)
#     else:
#         print('您的用户名或密码错误！')
# else:
#     print('您的用户名或密码错误！')

# and or ===========================
a = 10
b = 20
ret = a > b and a or b
# if a >b:
#     print(a)
# else:
#     ret = b
print(ret)

# not ==============
ret = not (a > b)
print(ret)

# while ==================================
# * 重复输出字符串 a * 2 aa
i = 1
while i <= 5:
    print('*' * i)
    i += 1


def my_add(num1, num2):
    result = num1 + num2
    print('num1 + num2 =', result)


my_add(10, 20)


def my_add(num1, num2, num3, num4):
    result = num1 + num2 + num3 + num4
    print("num1:" + str(num1))
    print(result)
    return result


# my_add(100, 200, 300, num4=400)
# my_add( num2=200, num3=300, num4=400, num1=1)

total_value = 100


def my_function():
    total_value = 200
    print('total_value:', total_value)


my_function()


# 带有默认值的参数一定要位于参数列表的最后面.
def my_function(a, b=20, c=30):
    return a + b + c


print(my_function(10))
my_function(10, 100)
print(my_function(10, 100, 1000))

my_string = '我叫做司马狗剩,我今年10岁了!'
# i = 0
# while i < len(my_string):
#     print(my_string[i], end=' ')
#     i += 1
# print(len(my_string))

# for ch in my_string:
#     print(ch, end=' ')

poetry = '远看泰山黑乎乎, 上头细来下头粗. 茹把泰山倒过来, 下头细来上头粗茹.'
# 将所有的 '茹' 替换为 '如'
right_poetry = poetry.replace('茹', '如')
print(right_poetry)
# 只替换第一次出现的 '茹'
right_poetry = poetry.replace('茹', '如', 1)
print(right_poetry)
# 从 10 位置开始查找 '上'的索引
position = poetry.find('上', 10, 100)
print(position)
print(len(poetry))
# 从0开始到7之间：步长, 每隔2个字符选取一个字符, 组成一个序列
print(poetry[0:7:2])

