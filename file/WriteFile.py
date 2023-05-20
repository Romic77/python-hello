with open('./write.txt', 'w', encoding="UTF-8") as f:
    f.write("hello world")

    # 把缓冲区的数据刷新到硬盘中
    f.flush()

with open('./write.txt', 'w', encoding="UTF-8") as f:
    f.write("777")
    # 把缓冲区的数据刷新到硬盘中
    f.flush()

with open('./write.txt', 'a', encoding="UTF-8") as f:
    f.write(" 999")
    # 把缓冲区的数据刷新到硬盘中
    f.flush()
