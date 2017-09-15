#-*- coding: utf-8 -*
# Dorian Wang 2017.08.31
# lesson 34 & 35: Break and Continue

i = 0
while i <5:
    i = i + 1
    for j in range(3):
        print(j)
        if j == 2:
            break
    for k in range(3):
        if k == 2:
            continue
        print(k)
    if i >3:
        break
    print(i)

