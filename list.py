squares = [1, 3, 5, 9]
print(squares)
print(squares[0])
print(squares[-1])
print(squares[-3:])
# 所有的切片操作都返回一个新列表，这个新列表包含所需要的元素。就是说，如下的切片会返回列表的一个新的(浅)拷贝:
print(squares[:])
print(squares + [11, 13, 15, 17])
# 与 immutable 的字符串不同, 列表是一个 mutable 类型，就是说，它自己的内容可以改变:
cubes = [1, 8, 27, 65, 125]
print(4 ** 3)
cubes[0] = 64
print(cubes)
# 给切片赋值也是可以的，这样甚至可以改变列表大小，或者把列表整个清空:
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
letters[2:5] = ['C', 'D', 'E']
print(letters)
letters[2:5] = []
print(letters)
letters[:]= []
print(letters)
letters = ['a', 'b', 'c', 'd']
print(len(letters))
# 也可以嵌套列表 (创建包含其他列表的列表), 比如说:
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
print(x[0])
print(x[0][1])

# 整数：结果去除小数点
a = 9
b = 2
print(a // b)
