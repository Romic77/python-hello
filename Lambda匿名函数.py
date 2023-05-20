def test_func(compute):
    result = compute(1, 2)
    print(result)


# lambda匿名函数语法：
# lambda 参数:函数体(一行代码)
test_func(lambda x, y: x * y)
