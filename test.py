"""
本代码是展示变量的写法

"""

# 打印hello world
print("hello world ")
# 打印数字类型
print(11)
# 打印浮点类型
print(11.11)

# 定义一个变量记录钱包余额50元
money = 50
print("钱包还剩下", money)

money = money - 10
print("买了一个冰淇淋还剩下：", money)

print("money的数据类型：", type(money))

print("数据类型式：", type(545.112))

# 将int转为string
print("数据有类型，变量无类型：", type(str(11)))

# float转string
print("浮点类型转为字符串：", type(str(11.11)))

# string转int
print("字符串转为int类型：", type(int("11")), int("11"))

# 浮点数转int
print("浮点数据转换:", type(int(11.11)), int(11))

# int转为浮点数
print("int数据类型转为浮点:", type(float(11)), float(11))

# 变量的定义
name = "张三"
age = 12
address = "深圳是南山区"

# 变量的运算符
print("1+1")

# java %是取模，就是 python% 是取余数
print(5 % 2)

# 5除以3
print(5 / 3)

# 2的3次方 **是指数
print(2 ** 3)

# 字符串定义的三种方式
name = '单引号定义字符串'
name = "双引号定义字符串"
name = """三引号定义字符串，如果三个引号有变量接收就是字符串，没有变量接受就是注释"""

# 字符串包含双引号
name = '"双引号字符串变量"'
print(name)
name = "'单引号字符串'"
print(name)
name = "\"我是字符串\""
print(name)

# python 字符串只能拼接字符串，不能拼接其他的类型，会报错
# print(name + age)

# 字符串占位符%s 是将其他类型转为string进行拼接
des = "我的名字是%s,我的年龄是%s"
print(name, age)

# 字符串占位符
message = "我的名字是%s,我的年龄是%s" % (name, age)
print(message)

# python多个单词使用下划线进行拼接
home_address = "我的家庭住址"
print(home_address)

# %d整数占位符 %f浮点占位符
name = "二次元"
year = 2006
gupiao = 11.115
message = "%s,成立于%d,股票价格是%f" % (name, year, gupiao)
print(message)

# %.2f .后面的2是精度控制 代表保留2为小数，并且会进行四舍五入
message = "%s,成立于%d,股票价格是%.2f" % (name, year, gupiao)
print(message)


# 字符串格式化 使用f"{站位}"
print(f"我是{name},年龄是{age},股价是{gupiao}")
