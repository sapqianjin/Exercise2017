#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Dorian Wang 2017.09.06
# lesson: List Comprehensions
# 这个逻辑显然是不合理的，因为假设两个人对话，那么每个人都是单独的一行，这一行中并没有提到对方。
# 但事实上应该是两个人的对话表明相互交互，应该+1才对。
# 而且分词系统有问题，移除该文件

import os, sys
import jieba, codecs, math
import jieba.posseg

userList = []
names = {}  # 姓名词典
relationships = {}  # 关系词典
lineNames = []  # 每段内人物关系

with codecs.open("dict.txt", "r", encoding="utf-8") as f:
    for lineName in f.readlines():
        userList.append(lineName.split('\t')[0])

print(userList)

jieba.load_userdict("dict.txt")
with codecs.open("busan.txt", "r", encoding="utf-8") as f:
    for lineTxt in f.readlines():
        for i in range(0,len(lineTxt)):
            lineWord.append(lineTxt[:i])

        for lineWord
        poss = jieba.posseg.cut(lineTxt)
        # 分词系统有问题，珍熙这个词并没有分出来
        lineNames.append([])
        for w in poss:
            if w.word in userList:
                if w.flag != "nr" or len(w.word) < 2:
                    continue
                lineNames[-1].append(w.word)
                if names.get(w.word) is None:
                    names[w.word] = 0
                    relationships[w.word] = {}
                names[w.word] += 1

for name, times in names.items():
    print(name, times)

# print(lineNames)
for i in range(0, len(lineNames) ):
    # for i in range(0,20):
    # print(lineNames[i - 1:i + 1])
    for name1 in lineNames[i]:  # name1只在本行
        for name2 in lineNames[i]:  # 比较本行的name2
            # print(name1, name2)
            if name1 == name2:
                continue
            if relationships[name1].get(name2) is None:
                relationships[name1][name2] = 1
            else:
                relationships[name1][name2] = relationships[name1][name2] + 1

        if (i >=1) and (i <=len(lineNames) -1):
            for name2 in lineNames[i - 1]:  # 比较前面一行的name2
                # print(name1, name2)
                if name1 == name2:
                    continue
                if relationships[name1].get(name2) is None:
                    relationships[name1][name2] = 0.5
                else:
                    relationships[name1][name2] = relationships[name1][name2] + 0.5

for name, edges in relationships.items():
    for v, w in edges.items():
        if w > 3:
            print(name + " " + v + " " + str(w) + "\r\n")

# # create relationship for each two name
# for lineName in lineNames:
#     for name1 in lineName:
#         for name2 in lineName:
#             if name1 == name2:
#                 continue
#             if relationships[name1].get(name2) is None:
#                 relationships[name1][name2] = 1
#             else:
#                 relationships[name1][name2] = relationships[name1][name2] + 1
# # create node and edge file for gephi
# with codecs.open("busan_node.txt", "w", encoding="utf-8") as f:
#     f.write("Id Label Weight\r\n")
#     for name, times in names.items():
#         f.write(name + " " + name + " " + str(times) + "\r\n")
#
# with codecs.open("busan_edge.txt", "w", encoding="utf-8") as f:
#     f.write("Source Target Weight\r\n")
#     for name, edges in relationships.items():
#         for v, w in edges.items():
#             if w > 3:
#                 f.write(name + " " + v + " " + str(w) + "\r\n")
