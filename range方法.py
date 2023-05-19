# range 返回1-10的所有数字 不包含10
# range(10) 返回0-9
# range(1,10) 返回1-9
# range(1,10,5)  1-9之间每隔5返回一次
# for i in range(1, 10, 5):
#     print(i)


for i in range(1, 101):
    print(f"今天是向小美表白的第{i}天，坚持")
    for j in range(1, 11):
        print(f"送给小美的第{j}朵玫瑰花")
    print(f"小美，我喜欢你，第{i}天结束")

print(f"第{i}天，表白成功")

for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}*{i}={i * j}\t", end='')
        j += 1
    i += 1
    print()


for i in range(1,6):
    print("语句1")
    for j in range(1,6):
        print("语句2")
        break

    print("语句4")