"""
计算利润 —— 一个烤鸭利润不得高于20元 （政府部门提出的要求）
一只烤鸭利润不得低于5元，低于5元不卖
利润计算器 —— 不退出，计算完利润，继续下一个
"""
print("烤鸭店计算器开始工作了~")
while True:
    price1 = int(input("请输入您的进货价："))
    price2 = int(input("请输入您的售卖价："))
    profits = price2 - price1
    if profits < 5 or profits >= 20:
        print("价格定价不合理，请重新输入！")
        continue
    num = int(input("请输入卖出的鸭子数量："))
    result = profits * num
    print("烤鸭店的利润为：{}".format(result))
    y_or_no = input("是否退出烤鸭店计算器？输入y为退出，否则继续：")
    if y_or_no == "y":
        print("您已退出烤鸭店计算器！")
        break
    else:
        continue