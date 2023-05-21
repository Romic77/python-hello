"""
数据容器有5种
列表、元祖、字符串、集合、字典
"""

name_list=['张三',3,True]
print(len(name_list))

# 通过[下标]来获取元素
print(name_list[2])
for i in name_list:
    print(type(i))


# 定义一个嵌套列表
name_list=[[1,2,3],[3,4,5]]
# 1 2 3
# 3 4 5 
print(name_list[0][1])
