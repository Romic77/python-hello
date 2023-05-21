class Student:
    name = None
    age = None

    # 成员方法访问成员变量通过self才能访问,
    def getName(self):
        print(self.name)

    def sayHello(self):
        print("hello world")

    def newStudent(self, name, age):
        self.name = name
        self.age = age


stu = Student()
stu.name = "张三"
stu.age = 12
stu.getName()
print(f"学生姓名是{stu.name},学生年龄是:{stu.age},{stu.getName()}")

stu.newStudent("李四", 55)
print(f"学生姓名是{stu.name},学生年龄是:{stu.age},{stu.getName()}")
