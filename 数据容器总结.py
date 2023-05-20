"""
列表list、元组tuple、字符串str 有序
集合set、字典dict  无序、不可重复

"""

# 定义数组
my_list = [1, 2, 3, 4, 5]
# 定义元组
my_tuple = (1, 2, 3, 4, 5)
# 定义字符串
my_str = "abcdefg"
# 定义集合
my_set = {1, 2, 3, 4, 5}
# 定义字典
my_dict = {"key1": 1, "key2": 2}

print(f"数组有{len(my_list)}")
print(f"元组有{len(my_tuple)}")
print(f"字符串{len(my_str)}")
print(f"集合有{len(my_set)}")
print(f"字典有{len(my_dict)}")

# max最大元素
print(f"最大元素有{max(my_list)}")
print(f"最大元素有{max(my_tuple)}")
print(f"最大元素串{max(my_str)}")
print(f"最大元素有{max(my_set)}")
print(f"最大元素有{max(my_dict)}")

# min最小元素
print(f"最大元素有{min(my_list)}")
print(f"最大元素有{min(my_tuple)}")
print(f"最大元素串{min(my_str)}")
print(f"最大元素有{min(my_set)}")
print(f"最大元素有{min(my_dict)}")

# 容器转为列表
print(f"数组转为列表{list(my_list)}")
print(f"元组转为列表{list(my_tuple)}")
print(f"字符转为列表{list(my_str)}")
print(f"集合转为列表{list(my_set)}")
print(f"字典转为列表{list(my_dict)}")

# 容器转为元组
print(f"数组转为元组{tuple(my_list)}")
print(f"元组转为元组{tuple(my_tuple)}")
print(f"字符转为元组{tuple(my_str)}")
print(f"集合转为元组{tuple(my_set)}")
print(f"字典转为元组{tuple(my_dict)}")

# 容器转为字符串
print(f"数组转为字符串{str(my_list)}")
print(f"元组转为字符串{str(my_tuple)}")
print(f"字符转为字符串{str(my_str)}")
print(f"集合转为字符串{str(my_set)}")
print(f"字典转为字符串{str(my_dict)}")

# 容器转集合
print(f"数组转为集合{set(my_list)}")
print(f"元组转为集合{set(my_tuple)}")
print(f"字符转为集合{set(my_str)}")
print(f"集合转为集合{set(my_set)}")
print(f"字典转为集合{set(my_dict)}")

# sorted排序
print(sorted(my_list, reverse=True))
print(sorted(my_tuple, reverse=True))
print(sorted(my_str, reverse=True))
print(sorted(my_set, reverse=True))
print(sorted(my_dict, reverse=True))
