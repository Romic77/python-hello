class Student:
    # 不定义成员变量的时候，self没有提示
    def __int__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address


stu_list = []

i = 1
while i <= 3:
    stu = Student()
    stu.name = input("请输入学生的姓名:")
    stu.age = input("请输入学生的年龄:")
    stu.address = input("请输入学生的地址:")
    print(f"当前学生的姓名是{stu.name},年龄:{stu.age},地址是:{stu.address}")
    i += 1
    stu_list.append(stu)

for stu in stu_list:
    print(f"学生的姓名是{stu.name},年龄:{stu.age},地址是:{stu.address}")
