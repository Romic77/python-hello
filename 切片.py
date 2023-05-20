"""
对列表、元组、字符串进行切片操作

序列[起始下标:结束下标:步长]
"""

my_list = [1, 2, 3, 4, 5]
# 步长默认是1可以省略
result1 = my_list[1:4:1]
print(result1)

# 对tuple进行切片，从头开始，到最后结束，步长为1
list2 = (1, 2, 3, 4, 5, 6)
print(list2[:])

# 对str进行切片，从头开始，到最后结束，步长为2
str1 = "123456"
print(str1[::2])

# 对str进行切片，从头开始，到最后结束，步长为-1
str2 = "123456"
print(str2[::-1])

# 对列表进行切片，从3开始到1结束，步长-1
my_list = [1, 2, 3, 4, 5]
print(my_list[3:1:-1])

# 对元组进行切片，从头开始 到尾结束，步长-2

my_tuple = (1, 2, 3, 4)
print(my_tuple[::-2])

str3 = "万过薪月，员序程马黑来，nohtyp学"
# 正序排列
str3 = str3[5:10:1][::-1]
print(str3)

str4 = "万过薪月，员序程马黑来，nohtyp学"

print(str4.split("，")[1].replace("来", "")[::-1])
