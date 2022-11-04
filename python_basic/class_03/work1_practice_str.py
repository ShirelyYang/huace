"""
一、字符串练习题：
1：有变量name = "aleX leNb " 完成如下操作：
    移除 name 变量对应的值两边的空格,并输出处理结果
    判断 name 变量是否以”Nb”结尾,并输出结果（用切片）
    将 name 变量对应的值中的 所有的”l” 替换为 “p”,并输出结果
    将 name 变量对应的值中的第一个”l”替换成”p”,并输出结果
    将 name 变量对应的值根据 所有的”l” 分割,并输出结果
    将 name 变量对应的值根据第一个”l”分割,并输出结果
    将 name 变量对应的值变小写,并输出结果
    请输出 name 变量对应的值的第 2 个字符?
    请输出 name 变量对应的值的前 3 个字符?

2：有字符串s = "123a4b5c"
    通过对s切片形成新的字符串 "a4b"
    通过对s切片形成新的字符串 "2abc"
"""
name = "aleX leNb "
# 移除 name 变量对应的值两边的空格,并输出处理结果
name1 = name.strip()
print(name1)

# 判断 name 变量是否以”Nb”结尾,并输出结果（用切片）
if name.endswith("Nb ",):
    print(name[len(name)-3:])
else:
    print("不是以”Nb”结尾")

# 将 name 变量对应的值中的 所有的”l” 替换为 “p”,并输出结果
name2 = name.replace("l", "p")
print(name2)

# 将 name 变量对应的值中的第一个”l”替换成”p”,并输出结果
name3 = name.replace("l", "p", 1)
print(name3)

# 将 name 变量对应的值根据 所有的”l” 分割,并输出结果
name4 = name.split("l")
print(name4)

# 将 name 变量对应的值根据第一个”l”分割,并输出结果
name5 = name.split("l",1)
print(name5)

# 将 name 变量对应的值变小写,并输出结果
name6 = name.lower()
print(name6)

# 请输出 name 变量对应的值的第 2 个字符?
print(name[1:2])

# 请输出 name 变量对应的值的前 3 个字符?
print(name[:3])