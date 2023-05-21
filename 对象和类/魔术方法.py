class Student:
    # 可以省略成员变量的定义
    # name: None
    # age: None
    # tel: None

    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel

    # 类似java对象的toString()方法，不覆盖就是打印内存地址，覆盖这个str这个模式方法就可以指定格式化输出
    def __str__(self):
        return f"name:{self.name}  age:{self.age}"

    # 这个就类似java的对象比较，需要实现接口Comparable，然后覆盖compareTo的方法
    # python是使用lt的魔术方法，用来设置比较的格式，完成2个对象的比较
    def __lt__(self, other):
        return self.age < other.age

    def __le__(self, other):
        return self.age <= other.age

    # 类似java的equals python实现eq魔术方法，如果两个对象的电话相等就相等
    def __eq__(self, other):
        return self.tel == other.tel


stu1 = Student("张三", 11, 138222222)
print(stu1)
stu2 = Student("李四", 11, 138222222)
print(stu2)
print(stu1 <= stu2)
print("对象是否相等：", stu1 == stu2)
