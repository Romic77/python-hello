"""
函数的定义：
def 函数名(传入参数):
    函数体
    return 返回值
"""

str1 = "hello"
str2 = "world1"
str3 = "my bro"


def my_length(str):
    count = 0
    for i in str:
        count += 1
    print(count)


my_length(str1)
my_length(str2)
my_length(str3)


def hello():
    print("欢迎来到 编程世界")


print(type(hello()))


def count(num1, num2):
    return num1 + num2


print(count(1, 2))


def checkTheTemperature(temp):
    if temp < 37.5:
        print("可以进入")
    else:
        print("滚")


checkTheTemperature(38)


def check_age(age):
    """
    check_age 检查年龄
    :param age: 年龄
    :return: 超过18岁返回成功，否则返回None
    """
    if age > 18:
        return "SUCCESS"
    return None


print(check_age(10))

# None可以用来定义变量 ，用来作为方法的返回值
name = None

num = 200


def test_a():
    print(f"{num}")


def test_b():
    # 将num声明为全局变量，然后修改num的值为500，那么test_c的调用的时候发现num变为500了
    global num
    num = 500
    print(f"{num}")


def test_c():
    print(f"{num}")


test_a()
test_b()
test_c()
