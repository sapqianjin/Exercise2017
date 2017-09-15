#-*- coding: utf-8 -*

minInt = int(input("Please input the min int?\n"))
maxInt = int(input("Please input the max int?\n"))

summy = 0

for i in range(minInt,maxInt+1):
    summy = summy + i


print(minInt, "+", maxInt, "=", summy)