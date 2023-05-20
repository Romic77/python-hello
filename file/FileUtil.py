# encoding的顺序不是第三位，所以只能使用关键字参数直接指定
# mode常用模式 r-read默认模式 读取 w-write写入模式，文件不存在会创建文件 a-append将新的内容追加到当前内容中


# 打开文件
f = open('./file.txt', 'r', encoding="UTF-8")
# 读取文件-read()
print(f.read())
f.close()

# 读取文件-readLine() 按照行的方式读取返回的是列表 每一行为一个元素
f = open('./file.txt', 'r', encoding="UTF-8")
rows = f.readlines()
print(rows)
f.close()

# with open 语法  可以自动关闭文件流
with open('./file.txt', 'r', encoding="UTF-8") as f:
    for line in f:
        print(f"每一行的数据是:{line}")
