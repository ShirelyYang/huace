"""
作业二
完成一个简易的计算器
用户可以先输入第一个数字，然后输入运算符号，最后输入第二个数字。
最后打印出计算结果
"""
num1 = int(input("请输入第一个数字："))
symbol = input("请输入运算符号：")
num2 = int(input("请输入第二个数字："))
result = 0
while True:
    if symbol == "/":
        if num2 == 0:
            num2 = int(input("除法运算下第二个数字不能为0，请重新输入："))
        else:
            result = num1/num2
            break
        continue
    elif symbol == "+":
        result = num1 + num2
        break
    elif symbol == "-":
        result = num1 - num2
        break
    elif symbol == "*":
        result = num1 * num2
        break
    else:
        symbol = input("您输入的运算符号不合法，请重新输入:")
        continue
print("计算结果为:{}".format(result))