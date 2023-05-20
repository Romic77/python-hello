"""
数组可以修改里面的值 list

元组固定里面的值，不能修改 tuple


"""

# 可以通过tuple方法获取空的元组
my_list = tuple()
my_list = (1, 2, 3, 4)

print(type(my_list))

for i in my_list:
    print(i)

# 定义单个元素
t4 = ("hell",)

# 元组嵌套
t5 = ((1, 2, 3), (3, 3, 3))
print(f"t5的类型是:{type(t5)}")

# 获取元素
print("获取元素：", t5[1][2])

# index查找某个数据
my_list = (1, 2, 3, 4, 2)
item = my_list.index(2)
print(item)

# count获取元素出现的次数
print(my_list.count(2))

