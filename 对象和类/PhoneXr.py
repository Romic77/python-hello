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
    pass


xr = PhoneXr()
xr.call_by_5g()
# xr能访问父类的变量和方法
print(xr.IMEI, xr.face_id, xr.producer)

myphone = MyPhone()
myphone.read_card()
myphone.call_by_5g()
