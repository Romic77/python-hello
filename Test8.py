def main(name):
    print(f"{name}，您好，欢迎来到黑马银行ATM，请选择操作：")
    print(f"查询余额\t[输入1]")
    print(f"存款\t[输入2]")
    print(f"取款\t[输入3]")
    print(f"退出\t[输入4]")
    return int(input("请输入您的选择:"))

while True:
    name="zhangsan"
    switch_num =main(name)
    if switch_num == 1:
        print(f"{name},查询余额：50000元成功")
    elif switch_num == 2:
        print(f"{name},存款：存入50000元成功")
    elif switch_num == 3:
        print(f"{name},取款：取款50000元成功")
    elif switch_num == 4:
        print(f"{name},退出")
        break

