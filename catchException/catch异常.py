# 没有abc.txt文件，会抛出异常
try:
    f = open("./abc.txt", "r", encoding="UTF-8")
# 这个是捕获全局异常
except:
    print("出现了异常，因为文件不存在，我们捕获了异常，改为w模式去创建打开他")
    f = open("./abc.txt", "w", encoding="UTF-8")

# 捕获指定异常
try:
    1 / 0
# 这个是捕获全局异常
except NameError as e:
    print("出现了变量未定义的异常")
except ZeroDivisionError as e1:
    print(e1)
    print("0不能作为被除数")
except:
    print("全局异常捕获")
finally:
    print("就算进入了异常，这里也能进去")
