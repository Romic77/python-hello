# import time
#
# time.sleep(2)
#

# 从time包里面导入sleep函数， 那么就只能使用sleep。
# from time import sleep
# sleep(2)


# 这种写法与import time一样
from time import *

sleep(1)

# as 给具体的功能改名 不建议使用
from time import sleep as s

s(1)
