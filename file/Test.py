# 方式1 获取所有内容 使用count统计 关键字  出现的次数
with open('./word.txt', 'r', encoding="UTF-8") as f:
    content = f.read()
    count = content.count("itheima")
    print(f"itheima在文件中出现了{count}次")

# 方式2 遍历每一行累加
count = 0
with open('./word.txt', 'r', encoding="UTF-8") as f:
    for line in f:
        rows = line.strip().split(" ")
        for row in rows:
            if row == "itheima":
                count += 1

    print(f"itheima在文件中出现了{count}次")
