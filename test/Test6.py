# 次数
import random

count = 0

# 随机数
random_number = random.randint(1, 100)
print(random_number)
flag = True
while flag:
    gress_number = int(input("请输入数字："))
    count += 1
    if gress_number > random_number:
        print("太大了")
    elif gress_number < random_number:
        print("太小了")
    else:
        flag = False
        break
print(f"总共猜测了{count}次")