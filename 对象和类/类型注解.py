# 基础数据类型注解
age: int = 18
name: str = "zhangsan"
gender: bool = False


class Student:
    pass


stu: Student = Student()

# 基础容器注解
my_list: list[int] = [1, 2, 3]
my_tuple: tuple[int, str, bool] = (1, "张三", False)
my_set: set[int] = {1, 2, 3}
my_dict: dict[int, str] = {1: "zz", 2: "cc"}
