class Student:
    # 可以省略成员变量的定义
    # name: None
    # age: None
    # tel: None

    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel
        print("Student创建了一个类对象")


stu = Student("张三", 12, "13822222222")
print(f"{stu.name}:{stu.age}:{stu.tel}")
