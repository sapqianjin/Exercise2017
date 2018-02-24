#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Dorian Wang 2018.01.23
# Chinese remainder theorem
# https://zh.wikipedia.org/wiki/%E4%B8%AD%E5%9B%BD%E5%89%A9%E4%BD%99%E5%AE%9A%E7%90%86

m1 = int(input("Please input m1:"))
x1 = int(input("Please input x1:"))
m2 = int(input("Please input m2:"))
x2 = int(input("Please input x3:"))
m3 = int(input("Please input m3:"))
x3 = int(input("Please input x3:"))

for t1 in range(0, m1):
    M1 = m2 * m3 * t1
    if M1 % m1 == 1:
        print("M1=", M1, "t1=", t1)
        break

for t2 in range(0, m2):
    M2 = m1 * m3 * t2
    if M2 % m2 == 1:
        print("M2=", M2, "t2=", t2)
        break

for t3 in range(0, m3):
    M3 = m1 * m2 * t3
    if M3 % m3 == 1:
        print("M3=", M3, "t3=", t3)
        break

for k in range(-10, 10):
    result = M1 * x1 + M2 * x2 + M3 * x3 + m1 * m2 * m3 * k
    print("n=", k, "result=", result)
