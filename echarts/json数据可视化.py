import json

data = [{"name": "张三", "age": 11}, {"name": "李四", "age": 50}, ]
# 将字典data转为json
json_str = json.dumps(data, ensure_ascii=False)
print(type(json_str))
print(json_str)

# 将json转为data
l = json.loads(json_str)
print(type(l))
