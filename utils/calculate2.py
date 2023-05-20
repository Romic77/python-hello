def add(x, y):
    """
    加法
    :param x:
    :param y:
    :return:
    """
    return x + y


def sub(x, y):
    """
    减法
    :param x:
    :param y:
    :return:
    """
    return x - y


# 可以测试单个函数，外部使用函数的时候也不会执行这个函数
if __name__ == '__main__':
    print(add(1, 2))
