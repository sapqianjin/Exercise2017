#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Dorian Wang 2017.09.05
# lesson: Recursion

import time

def fact(n):
    if n == 1:
        return 1
    else:
        print("%d * fact(%d)" % (n,n - 1))
        return n * fact(n - 1)


def fact2(n):
    f2 = 1
    while n > 1:
        f2 = n * f2
        n = n - 1
    return f2
#我是觉得最好不要用递归，虽然程序逻辑看起来清晰明了，但调用到999的时候就会出错。

# print(fact(998))
# print(fact2(998))


def hanoiTower(n, a, b, c):
    global count
    if n==1:
        print("%s ---> %s" % (a,c))
        count = count +1
    else:
        hanoiTower(n - 1,a,c,b)
        print("%s ---> %s" % (a,c))
        count = count + 1
        hanoiTower(n - 1,b,a,c)

count = 0
startTime = time.time()
hanoiTower(20,'A','B','C')
print(count)
endTime = time.time()
print('time: %f' % (endTime - startTime))