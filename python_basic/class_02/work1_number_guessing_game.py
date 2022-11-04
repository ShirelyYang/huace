"""
# 课后作业：
作业一
完成一个猜数字游戏
# 进入程序后
# 提示用户输入 要猜的数字
# 其他人输入时，提示数字大了，或者小了
# 猜到正确的数字为止,提示恭喜猜对了
# (选做：可以控制每位玩家的猜数字次数，例如，一个人只能猜3次，3次猜错结束程序,显示正确的数字后，重新开始)
# (选做: 猜数字的游戏中的数字尝试让系统生成，提示：random.randint(n,m) 可以让python在n-m之间生成一个随机数)

"""
from numpy import random

print("欢迎来到猜数字游戏！")
answer = random.randint(1, 10)  # 随机获取一个答案
# print(answer)
n = 3  # 猜数字次数
while n > 0:
    num = int(input("请输入要猜的数字："))
    if num > answer:
        print("大了大了")
        n -= 1
        continue
    elif num < answer:
        print("小了小了")
        n -= 1
        continue
    else:
        print("恭喜您猜对啦~")
        break
print("游戏结束！")