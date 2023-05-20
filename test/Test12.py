import my_utils.str_util
from my_utils import file_util
from my_utils import str_util

print(my_utils.str_util.str_reverse("黑马程序员"))
print(str_util.substr("itheima", 0, 4))

file_util.append_to_file("./aaa.txt", "123")
file_util.print_file_info("./aaa")
