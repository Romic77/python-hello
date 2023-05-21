my_list = ["it1", "aaa", "ccc"]
index = my_list.index("aaa")
print(f"index('值')返回索引的值{index}")

# 通过索引修改值
my_list[1] = 555
print(my_list[1])

# 指定索引添加值
my_list.insert(len(my_list), "666")
print(my_list)

# list尾部追加
my_list.append("777")
print(my_list)

# extend追加容器
my_list.extend([1, 2, 3])
print(my_list)

# 删除列表索引元素
del my_list[1]
print(my_list)

ele = my_list.pop(1)
print(ele)
print(my_list)

# 删除单个元素
my_list.remove("666")

count=my_list.count("aaa")
print(f"列表中aaa的数量{count}")

# 清空列表的所有数据
my_list.clear()
