import random

num = random.randint(1, 10)
print("随机数是:", num)
gress_num = int(input("请输入数字"))

if num == gress_num:
    print("猜对了，你是天选之子")
else:
    if gress_num > num:
        print("太大了")
    elif gress_num < num:
        print("太小了")
    else:
        print("第二次就猜中了")

    gress_num = int(input("请输入数字"))
    if num == gress_num:
        print("第三次猜对了")
    else:
        if gress_num > num:
            print("太大了")
        elif gress_num < num:
            print("太小了")
        else:
            print("fw")
    gress_num = int(input("请输入数字"))
    if num == gress_num:
        print("第三次猜对了")
    else:
        if gress_num > num:
            print("太大了")
        elif gress_num < num:
            print("太小了")
        else:
            print("fw")
