class Phone:
    # 序列号
    IMEI = None
    # 厂商
    producer = None

    # 私有成员变量 电压
    __current_voltage = 0.5

    # 私有成员方法
    def __keep_single_core(self):
        print("让cpu单核运行节省电量")

    def call_by_5g(self):
        if self.__current_voltage >= 1:
            print("5G通话已开启")
        else:
            self.__keep_single_core()


ph = Phone()
ph.call_by_5g()
