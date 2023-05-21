class Phone:
    # 序列号
    IMEI = None
    # 厂商
    producer = "华为"

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


class PhoneXr(Phone):
    face_id = "1001"

    def call_by_5g(self):
        print("xr优化之后的5g功能")


class NFCReader:
    nfc_type = "第五代"
    producer = "HM"

    def read_card(self):
        print("nfc读卡")

    def write_card(self):
        print("cfc写卡")


class RemoteControl:
    rc_type = "红外遥控"

    def control(self):
        print("红外遥控开启了")


class MyPhone(Phone, NFCReader, RemoteControl):
    producer = "romic制造"

    def call_by_5g(self):
        # print("假5G")
        # 调用父类(推荐使用这种方式调用父类的变量或者方法)
        super().call_by_5g()

        # 这一行会报错，以为子类没有rc_type的成员变量
        # super().rc_type = "aa"

        RemoteControl.rc_type = "Romic工场生产"
        RemoteControl.control(self)

    pass


# 子类复写父类的属性或者方法
myPhone = MyPhone()
print(myPhone.producer)
myPhone.call_by_5g()
