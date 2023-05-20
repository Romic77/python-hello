def list_while():
    my_list = ["1", "2", "3"]
    index = 0
    while index < len(my_list):
        item = my_list[index]
        print(f"列表的元素{item}")
        index += 1


list_while()


def list_for():
    my_list = [1, 2, 3, 4, 5]
    for i in my_list:
        print(f"for列表的元素{i}")


list_for()
