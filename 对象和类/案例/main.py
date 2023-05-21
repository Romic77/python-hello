from pyecharts.charts import Bar
from pyecharts.globals import ThemeType
from pyecharts.options import InitOpts, LabelOpts, TitleOpts

from file_define import TextFileReader, JSONFileReader
from data_define import Record

text_data_list: list[Record] = TextFileReader("./2011年1月销售数据.txt").read_data()
json_data: list[Record] = JSONFileReader("./2011年2月销售数据JSON.txt").read_data()

all_data_list: list[Record] = text_data_list + json_data

data_dict = {}
# 进行数据计算
for record in all_data_list:
    # 当前日期已经有记录了
    if record.date in data_dict.keys():
        data_dict[record.date] += record.money
    else:
        data_dict[record.date] = record.money

print(data_dict)

bar = Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))

# 取出字典的所有keys，然后转为list类型
bar.add_xaxis(list(data_dict.keys()))
bar.add_yaxis("销售额", list(data_dict.values()), label_opts=LabelOpts(is_show=False))
bar.set_global_opts(title_opts=TitleOpts(title="每日销售额"))

bar.render("每日销售柱状图.html")
