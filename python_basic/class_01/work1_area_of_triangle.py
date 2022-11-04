"""
用户输入三角形三边长度，并计算三角形的面积（海伦公式）
S=√p(p-a)(p-b)(p-c)
开平方：
方法1：import math

math.sqrt( x )

python
方法2：利用pow(a, b)函数即可。需要开a的r次方则pow(a, 1.0/r)

判断三角形是否成立：
a+b>c and a+c>b and b+c>a1
"""
print("三角形面积计算器")
a = float(input("请输入三角形的第一条边长："))
b = float(input("请输入三角形的第二条边长："))
c = float(input("请输入三角形的第三条边长："))
# e = int((a + b) > c) + int((a + c) > b) + int((c + b) > a)
e = ((a + b) > c) + ((a + c) > b) + ((b + c) > a)  # 布尔值在计算的时候当作0或1计算
if e == 3:
    p = (a + b + c) / 2
    s = pow(p * (p - a) * (p - b) * (p - c), 0.5)
    print("三角形的面积为：{}".format(s))
else:
    print("您输入的边长不能构成三角形，请重新输入~")
