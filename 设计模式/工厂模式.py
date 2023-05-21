class Person:
    pass


class Worker(Person):
    pass


class Student(Person):
    pass


class Teacher(Person):
    pass


class PersonFactory:
    def get_person(self, person_type):
        if person_type == 'w':
            return Worker()
        elif person_type == 't':
            return Teacher()
        else:
            return Student()


f = PersonFactory()
print(f.get_person("w"))
print(f.get_person("t"))
