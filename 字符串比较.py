# 字符串比较是一个字符一个字符比较，只要有一个大就整体打
print(f"abd大于abd的结果{'abd' > 'abc'}")

print(f"a2大于a1的结果{'a2' > 'a1'}")


def uesr_info(name, age, gender="男"):
    print(f"姓名是{name},年龄是:{age},性别是：{gender}")


uesr_info("张三", 12, "男")

uesr_info(name="zz", gender="女", age=11)

# 通过函数设置默认的参数，如果不传递这个参数默认是男
uesr_info("张三", 12)


# *args表示不固定的参数 类似java...
# 参数是存在元组中，根据元组处理
def user_info2(*args):
    # 通过元组进行操作元素,元组里面的元素是不允许修改的，修改会报错
    # args[0] = 3
    print(f"args参数类型是：{type(args)}，内容是：{args}")


user_info2(1, 2, 3, 4, 5, 6, 7)


# **kwargs 是keyvalue args，表示键值对参数
def user_info3(**kvargs):
    # 通过dict操作字典
    kvargs["name"] = "哈哈"
    print(f"args参数的类型是：{type(kvargs)}，内容是：{kvargs}")


user_info3(name="张三", age=11)
