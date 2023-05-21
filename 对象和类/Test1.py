class Phone:
    __is_5g_enable = True

    def __check_5g(self):
        if self.__is_5g_enable:
            print("5g开启")
        else:
            print("5g关闭,使用4G通话中")

    def call_by_5g(self):
        self.__check_5g()
        print("正在通话中")


ph = Phone()
ph.call_by_5g()
