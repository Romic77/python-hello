# 定义一个空集合,集合类似map 值不能重复
a = set()

a = {1, 2, 3, 4}

a.add(5)
print(a)
a.remove(5)
print(a)

# 随机取出一个元素
item = a.pop()
print(item)

# 清空集合
a.clear()

set1 = {1, 2, 3}
set2 = {1, 5, 6}
# 集合set1与set2的差集
# set3 = set1.difference(set2)
# print(set3)

# 消除差集 集合set1消除和set2相同的元素。
set1.difference_update(set2)
print(set1, set2)

# 集合合并
print(set1.union(set2))

print(len(set1.union(set2)))

for i in set1.union(set2):
    print(f"元素为{i}")
