"""
元组练习题：判断是否可以实现，如果可以请写代码实现。
    li = ["alex",[11,22,(88,99,100,),33], "WuSir", ("ritian", "barry",), "wenzhou"]
    - 请将 "WuSir" 修改成 "吴彦祖"
    - 请将 ("ritian", "barry",) 修改为 ['日月','星辰']
    - 请将 88 修改为 87
    - 请将 "wenzhou" 删除，然后再在列表第0个索引位置插入 "周周"
"""
li = ["alex", [11, 22, (88, 99, 100,), 33], "WuSir", ("ritian", "barry",), "wenzhou"]
print(li)
# - 请将 "WuSir" 修改成 "吴彦祖"
li[2] = "吴彦祖"
print(li)
# - 请将 ("ritian", "barry",) 修改为 ['日月','星辰']
li[-2] = ['日月', '星辰']
print(li)
# - 请将 88 修改为 87
li[1][2] = (87, 99, 100)
print(li)
# - 请将 "wenzhou" 删除，然后再在列表第0个索引位置插入 "周周"
del li[-1]
li.insert(0, "周周")
print(li)
