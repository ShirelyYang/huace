"""
写代码，有如下列表，按照要求实现每一个功能。

    li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]

    计算列表的长度并输出
    请通过步长获取索引为偶数的所有值，并打印出获取后的列表
    列表中追加元素”seven”,并输出添加后的列表
    请在列表的第1个位置插入元素”Tony”,并输出添加后的列表
    请修改列表第2个位置的元素为”Kelly”,并输出修改后的列表
    请将列表的第3个位置的值改成 “太白”，并输出修改后的列表
    请将列表 l2=[1,”a”,3,4,”heart”] 的每一个元素追加到列表li中，并输出添加后的列表
    请将字符串 s = “qwert”的每一个元素添加到列表li中，一行代码实现，不允许循环添加。
    请删除列表中的元素”ritian”,并输出删除元素后的列表
    请删除列表中的第2个元素，并输出删除元素后的列表
    请删除列表中的第2至第4个元素，并输出删除元素后的列表
"""
li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
# 计算列表的长度并输出
len_li = len(li)
print(len_li)
# 请通过步长获取索引为偶数的所有值，并打印出获取后的列表
li2 = li[0:len_li:2]
print(li2)
# 列表中追加元素”seven”,并输出添加后的列表
li.append("seven")
print(li)
# 请在列表的第1个位置插入元素”Tony”,并输出添加后的列表
li.insert(0, "Tony")
print(li)
#     请修改列表第2个位置的元素为”Kelly”,并输出修改后的列表
li[1] = "Kelly"
print(li)
#     请将列表的第3个位置的值改成 “太白”，并输出修改后的列表
li[2] = "太白"
print(li)
#     请将列表 l2=[1,”a”,3,4,”heart”] 的每一个元素追加到列表li中，并输出添加后的列表
l2 = [1, "a", 3, 4, "heart"]
li.extend(l2)
print(li)
#     请将字符串 s = “qwert”的每一个元素添加到列表li中，一行代码实现，不允许循环添加。
s = "qwert"
li.extend(s)
print(li)
#     请删除列表中的元素”ritian”,并输出删除元素后的列表
li.remove("ritian")
print(li)
#     请删除列表中的第2个元素，并输出删除元素后的列表
li.pop(1)
print(li)
#     请删除列表中的第2至第4个元素，并输出删除元素后的列表
li3 = li[1:4]
print(li3)
for i in li3:
    li.remove(i)
print(li)