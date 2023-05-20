my_str = "itheima and itcast"

print(my_str[8])

# 获取and的索引
print(my_str.index("and"))

print(my_str.replace("and", "666"))

str1 = my_str.split(" ")
print(str1)

print(my_str.count("a"))

str1 = "iteima itcast boxuegu"
# 统计字符串内有多少个it字符
print(str1.count("it"))

# 将字符串内的空格全部替换为字符串|
print(str1.replace(" ", "|"))

# 按照|进行字符串分隔，得到列表
st1 = str1.split("|")
print(str1)
