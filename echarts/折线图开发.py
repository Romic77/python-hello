import json

from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts


def common_method(file_name):
    with open(file_name, "r", encoding="UTF-8") as f:
        content = f.read()
        # 去除开头的不规则json数据
        content = content.replace("jsonp_1629344292311_69436(", "")
        # 去除结尾的);
        content = content[:-2]
        return content


data_us = common_method("./美国.txt")
data_jp = common_method("./日本.txt")
data_in = common_method("./印度.txt")

trend_data_us = json.loads(data_us)['data'][0]['trend']
trend_data_jp = json.loads(data_jp)['data'][0]['trend']
trend_data_in = json.loads(data_in)['data'][0]['trend']

# 设置X轴的数据
line = Line()
line.add_xaxis(trend_data_us["updateDate"][:314])
line.add_yaxis("美国确诊人数", trend_data_us["list"][0]['data'][:314])

line.add_xaxis(trend_data_jp["updateDate"][:314])
line.add_yaxis("日本确诊人数", trend_data_jp["list"][0]['data'][:314])

line.add_xaxis(trend_data_in["updateDate"][:314])
line.add_yaxis("印度确诊人数", trend_data_in["list"][0]['data'][:314])

# 设置全局配置项
line.set_global_opts(
    title_opts=TitleOpts(title="2020年美日印三国确诊人数对比折线图", pos_left="center", pos_bottom="1%"),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True)
)

# 通过render()渲染
line.render()
