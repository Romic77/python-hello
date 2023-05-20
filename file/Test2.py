file = open('./bill.txt', 'r', encoding="UTF-8")
file1 = open('./bill.txt.bak', 'w', encoding="UTF-8")
for row in file.readlines():
    if row.count("测试") > 0:
        continue
    else:
        file1.write(row)

file.close()
file1.close()
