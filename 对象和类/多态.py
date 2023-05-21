# 多态是多种状态，完成某个行为 使用不同的对象的到不同的状态

class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        print("汪汪汪")


class Cat(Animal):
    def speak(self):
        print("喵喵喵")


# 这就是根据传入的对象不同调用不用的speak()函数
def make_noise(animal: Animal):
    animal.speak()


dog = Dog()
cat = Cat()

make_noise(dog)
make_noise(cat)


class AC:
    def cool_wind(self):
        """制冷"""

    pass

    def hot_wind(self):
        """制热"""
        pass

    def swing_l_r(self):
        """摆风"""
        pass


class Midea_AC(AC):
    def cool_wind(self):
        print("美的空调制冷")

    def hot_wind(self):
        print("美的空调制热")

    def swing_l_r(self):
        print("美的空调摆风")


class Green_AC(AC):
    def cool_wind(self):
        print("格力空调制冷")

    def hot_wind(self):
        print("格力空调制热")

    def swing_l_r(self):
        print("格力空调摆风")


def make_cool(ac: AC):
    ac.cool_wind()


def make_hot(ac: AC):
    ac.hot_wind()


make_cool(Midea_AC())
make_cool(Green_AC())
