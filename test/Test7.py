import random

money = 10000
for i in range(1, 21):
    score = random.randint(1, 10)
    if score < 5:
        print(f"绩效分数是{score},不发工资")
        continue
    money -= 1000

    if money > 0:
        print(f"员工{i},发放工资1000,还剩余{money}")
    elif money < 0:
        print(f"员工{i}，公司没钱啦")
        break
