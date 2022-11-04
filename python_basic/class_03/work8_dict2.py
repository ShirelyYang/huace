"""
2：根据需求写代码

     dic1 = {
      'name':['alex',2,3,5],
      'job':'teacher',
      'oldboy':{'alex':['python1','python2',100]}
      }
     1，将name对应的列表追加一个元素’wusir’。
     2，将name对应的列表中的alex首字母大写。
     3，oldboy对应的字典加一个键值对’老男孩’,’linux’。
     4，将oldboy对应的字典中的alex对应的列表中的python2删除
"""
dic1 = {
    'name': ['alex', 2, 3, 5],
    'job': 'teacher',
    'oldboy': {'alex': ['python1', 'python2', 100]}
}
print(dic1)
# 1，将name对应的列表追加一个元素’wusir’。
dic1["name"].append("wusir")
print(dic1)
# 2，将name对应的列表中的alex首字母大写。
# 要把改变后的值重新赋值回来
dic1["name"][0] = dic1["name"][0].capitalize()
print(dic1)

# 3，oldboy对应的字典加一个键值对’老男孩’,’linux’。
dic1["oldboy"]["老男孩"] = "linux"
print(dic1)
# 4，将oldboy对应的字典中的alex对应的列表中的python2删除
# del方法用索引值删除
del dic1["oldboy"]["alex"][1]
print(dic1)
