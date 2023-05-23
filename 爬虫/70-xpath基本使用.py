from lxml import etree
from lxml.etree import _ElementTree

"""
xpath解析
1.本地文件
2. 服务响应的数据 response.read().decode('utf-8') 推荐
"""

# 解析本地文件
tree = etree.parse("./xpath基本使用.html")
print(tree)
assert isinstance(tree, _ElementTree)

# //查找所有子孙节点，不考虑层级关系
# /查找直接子节点

# 查找body下面的所有子孙节点 -> ul下面的子节点 li
li_list = tree.xpath('//body/ul/li')

# 查找所有有id属性的li标签
id_list = tree.xpath('//ul/li[@id]/text()')
print(id_list)

# 查找所有有id属性为深圳的
id_list = tree.xpath('//ul/li[@id="shenzhen"]/text()')
print(id_list)

# 属性查询，获取所有ul下面的li class为北京  多个条件可以用and 或者or
id_list = tree.xpath('//ul/li[@class="beijing" or @class="shanghai"]/text()')
print(id_list)

# 获取所有ul下面的li，li的id属性中包含1的
id_list = tree.xpath('//ul/li[contains(@id,"1")]/text()')
print(id_list)

# 获取所有ul下面的li，li的id属性以hu开头
id_list = tree.xpath('//ul/li[starts-with(@id,"hu")]/text()')
print(id_list)

# 查询 id为shenzhen class为shanghai的li标签
id_list = tree.xpath('//ul/li[@id="shenzhen" or @class="shanghai"]/text()')
print(id_list)
