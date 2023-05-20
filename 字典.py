"""
字典就是key-value
set集合底层是数组类似java hashSet
"""

map = {}
map = {1: "张三", 2: "李四"}

# 获取单个元素
print(map[1])

# 定义嵌套字典

stu_score_dict = {
    1: {
        "名称": "张三",
        "语文": 77,
        "数学": 88,
    },
    2: {
        "名称": "李四",
        "语文": 99,
        "数学": 11,
    }
}

print(stu_score_dict)

print(f"{stu_score_dict[1]['名称']},{stu_score_dict[1]['语文']},{stu_score_dict[1]['数学']}的成绩")

my_dict = {"周杰伦": 99, "林俊杰": 88, "张学友": 77}
# 修改张学友的值
my_dict["张学友"] = 66
# 新增元素
my_dict["李白"] = 100

# 删除元素
my_dict.pop("周杰伦")
print(my_dict)

# 清空元素
# my_dict.clear()
# print(my_dict)

# 获取全部的key
print("全部的key是", my_dict.keys())

# 遍历字典的所有选项
for key in my_dict:
    print(f"字典的key是{key}")
    print(f"字典的value是{my_dict[key]}")

# 遍历字典的所有的值
for item in my_dict.values():
    print(item)

print(len(my_dict))
