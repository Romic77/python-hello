class Clock:
    id = None
    price = None

    def ring(self):
        """
        mac没有winsound模块，运行会报错
        :return:
        """
        import winsound
        winsound.Beep(2000, 3000)


# 构建2个闹钟独享
clock1 = Clock()
clock1.id = "1"
clock1.price = 19.99
print(f"{clock1.id},{clock1.price}")
clock1.ring()
