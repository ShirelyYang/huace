"""
2：写代码，有如下列表，利用切片实现每一个功能

    li = [1, 3, 2, "a", 4, "b", 5,"c"]

    通过对li列表的切片形成新的列表 [1,3,2]
    通过对li列表的切片形成新的列表 [“a”,4,”b”]
    通过对li列表的切片形成新的列表 [1,2,4,5]
    通过对li列表的切片形成新的列表 [3,”a”,”b”]
    通过对li列表的切片形成新的列表 [3,”a”,”b”,”c”]
    通过对li列表的切片形成新的列表 [“c”]
    通过对li列表的切片形成新的列表 [“b”,”a”,3]
"""
li = [1, 3, 2, "a", 4, "b", 5,"c"]
print(li)
# 通过对li列表的切片形成新的列表 [1,3,2]
li1 = li[:3]
print(li1)
#     通过对li列表的切片形成新的列表 [“a”,4,”b”]
li2 = li[3:-2]
print(li2)
#     通过对li列表的切片形成新的列表 [1,2,4,5]
li3 = li[::2]
print(li3)
#     通过对li列表的切片形成新的列表 [3,”a”,”b”]
li4 = li[1:-2:2]
print(li4)
#     通过对li列表的切片形成新的列表 [3,”a”,”b”,”c”]
li5 = li[1::2]
print(li5)
#     通过对li列表的切片形成新的列表 [“c”]
li6 = li[-1:]
print(li6)
#     通过对li列表的切片形成新的列表 [“b”,”a”,3]
li7 = li[5:-2]+li[3:4]+li[1:2]
print(li7)