"""
五：集合练习题
	1：[‘taobao’,'jingdong','alibaba','baidu','taobao']对元素去重复
	2：分别有两个集合{1,2,1,3,4,5,6,7}，{1,2,3,8,9,7,10}，求两个集合的差集、并集、交集
"""

# 1：[‘taobao’, 'jingdong', 'alibaba', 'baidu', 'taobao']对元素去重复
lis = ["taobao", 'jingdong', 'alibaba', 'baidu', 'taobao']
print(lis)
lis2 = list(set(lis))
print(lis2)
# 2：分别有两个集合
# {1, 2, 1, 3, 4, 5, 6, 7}，{1, 2, 3, 8, 9, 7, 10}，求两个集合的差集、并集、交集
set1 = {1, 2, 1, 3, 4, 5, 6, 7}
set2 = {1, 2, 3, 8, 9, 7, 10}
print(set1)
print(set2)
set3 = set1.intersection(set2)
print(set3)
