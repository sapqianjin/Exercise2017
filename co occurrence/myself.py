#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Dorian Wang 2017.09.06
# lesson: co occurrence
# 改用自己想的逻辑

import codecs

nameList = []  # 姓名列表
nameCount = {}  # 姓名在每一行的出现次数
relationships = {}  # 两个姓名之间的关系词典

# 从指定文件中读取nameList
# 增加姓名的变体，在同一行
with codecs.open("nameList.txt", "r", encoding="utf-8") as f:
    for lineName in f.readlines():
        nameList.append(lineName.split())
print(nameList)

# 遍历全文，依次得到每个姓名在每一行的出现次数
with codecs.open("busan.txt", "r", encoding="utf-8") as f:
    for lineTxt in f.readlines():
        for name in nameList:
            for i in range(0, len(name)):
                if i == 0:
                    if nameCount.get(name[0]) is None:
                        nameCount[name[0]] = []
                        relationships[name[0]] = {}
                    nameCount[name[0]].append(lineTxt.count(name[0]))
                else:
                    # 增加变体姓名的检查，计入在第一个名字的Count中
                    # 所以这里不能用append，而要用+=，增量为变体姓名找到的数量
                    # 因为必然是最后一个元素，所以使`用-1定位
                    nameCount[name[0]][-1] += lineTxt.count(name[i])

# print('%s\n' % str(line) for line in nameCount.items())
for line in nameCount.items():
    print(line)
    # print(sum(line[1]))

# 检查每两个姓名是否出现在同一行+1，上一行+0.5
for name1, count1 in nameCount.items():
    for name2, count2 in nameCount.items():
        if name1 == name2:
            continue
        else:
            for i in range(0, len(count1)):
                if int(count1[i]) > 0:  # name1只在本行
                    try:
                        if int(count2[i]) > 0:  # 比较本行的name2
                            if relationships[name1].get(name2) is None:
                                relationships[name1][name2] = 1
                            else:
                                relationships[name1][name2] += 1
                        if int(count2[i - 1]) > 0:  # 比较前面一行的name2
                            if relationships[name1].get(name2) is None:
                                relationships[name1][name2] = 0.5
                            else:
                                relationships[name1][name2] += 0.5
                    except:
                        print(name1, name2, i)
                        print(count1, count2)

# 结果输出，过滤掉小于3的内容
for n1, edges in relationships.items():
    for n2, relation in edges.items():
        if relation > 3:
            print(n1, n2, str(relation))
