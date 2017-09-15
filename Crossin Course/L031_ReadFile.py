#-*- coding: utf-8 -*
# Dorian Wang 2017.08.30
# lesson 31: Read File

f = open('L031_Data.txt')
data1 = f.read()
print("read:\n",data1,"\n")

f.seek(0)
#文件指针位置归零，即回到文件头。
#否则如果指针仍旧在文件结尾，读到的数据会是空。
data2 = f.readline()
print("readline:\n",data2,"\n")

f.seek(0)
data3 = f.readlines()
print("readlines:\n",data3,"\n")
f.close()



