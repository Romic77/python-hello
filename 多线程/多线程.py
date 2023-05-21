import threading
import time


def sing(msg):
    while True:
        print(f"{msg}")
        time.sleep(1)


def dance(type):
    while True:
        print(f"{type}")
        time.sleep(1)


if __name__ == '__main__':
    # args 可以给函数传递参数
    sing_thread = threading.Thread(target=sing, args=("荷塘月色",))
    dance_thread = threading.Thread(target=dance, kwargs={"type": "lock"})
    sing_thread.start()
    dance_thread.start()
