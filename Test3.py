num = 7
if int(input("请输入一次猜想的数字")) == num:
    print("恭喜第一次就猜对了呢")
elif int(input("猜错了，再猜一次：")) == num:
    print("猜对了")
elif int(input("猜错了，再猜一次：")) == num:
    print("猜对了")
else:
    print("sorry 都不对")

