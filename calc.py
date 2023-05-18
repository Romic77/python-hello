# 名称
name = "传智播客"
# 股票价格
stock_price = 19.99
# 股票号码
stock_code = "003032"
# 股票每日增长系数，浮点数类型
stock_price_daily_growth_factor = 1.2
# 增长天数
growth_days = 7

print(f"公司:{name},股票代码:{stock_code},当日股价:{stock_price}")

message = "每日增长系数是%s,经过%d天增长后,股价达到了%.2f" % (stock_price_daily_growth_factor, growth_days,
                                                              stock_price_daily_growth_factor ** growth_days * stock_price)
print(message)
