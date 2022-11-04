"""
选做题目：
根据老师上课讲的打工人一天案例，扩展一下
打工人一天早上9点上班 中午休息两个小时。 晚上18-19点 公司有免费晚餐，
# 22点才下班 break contniue  if elif
"""
input_time = int(input("请输入现在的时间："))
while True:
    if input_time < 9:
        print("还没开始上班呐！")
        input_time = int(input("请输入现在的时间："))
        continue
    elif input_time >= 9 and input_time < 12:
        print("现在是上班时间~")
        input_time = int(input("请输入现在的时间："))
        continue
    elif input_time >= 12 and input_time < 14:
        print("现在是午休时间！")
        input_time = int(input("请输入现在的时间："))
        continue
    elif input_time >= 14 and input_time <= 18:
        print("现在是下午上班时间！")
        input_time = int(input("请输入现在的时间："))
        continue
    elif input_time > 18 and input_time <= 19:
        print("现在是晚餐时间！")
        input_time = int(input("请输入现在的时间："))
        continue
    elif input_time > 19 and input_time <= 22:
        print("现在是加班时间！")
        input_time = int(input("请输入现在的时间："))
        continue
    else:
        print("下班啦！！！")
        break
