class Record:
    date = None  # 订单日期
    order_id = None  # 订单id
    money = None  # 订单金额
    province = None  # 销售省份

    def __init__(self, date, order_id, money, province):
        self.date = date
        self.order_id = order_id
        self.money = money
        self.province = province

    def __str__(self):
        return f"date:{self.date}  order_id:{self.order_id}  money:{self.money}  province:{self.province}"
