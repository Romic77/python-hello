import json

import jsonpath as jsonpath

obj = json.load(open('73_爬虫_解析_jsonpath.json', 'r', encoding='utf-8'))

# 书店所有书的作者
author_list = jsonpath.jsonpath(obj, '$.store.book[*].author')
print(author_list)

# 所有作者
author_list = jsonpath.jsonpath(obj, '$..author')
print(author_list)

# 获取store下面的所有的元素
store_list = jsonpath.jsonpath(obj, '$.store.*')
print(store_list)

# 获取store下面的所有价格
price_list = jsonpath.jsonpath(obj, '$.store..price')
print(price_list)

# 第三本书
book = jsonpath.jsonpath(obj, '$.store.book[2]')
print(book)

# 最后一本书
book = jsonpath.jsonpath(obj, '$..book[(@.length-1)]')
print(book)

# 前面两本书
book_list = jsonpath.jsonpath(obj, '$..book[0,1]')
print(book_list)

# 过滤出所有包含isbn的书
book_list = jsonpath.jsonpath(obj, '$..book[?(@.isbn)]')
print(book_list)

# 过滤出价格低于10元的书
price_list = jsonpath.jsonpath(obj, '$..book[?(@.price<10)]')
print(price_list)

# 所有元素
all = jsonpath.jsonpath(obj, '$..*')
print(all)
