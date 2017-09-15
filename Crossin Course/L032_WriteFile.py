#-*- coding: utf-8 -*
# Dorian Wang 2017.08.30
# lesson 32: Write File

f = open('L032_Data.txt', 'w')
data1 = "I will be writen to one file.\nThe file's name is %s.\nCool!\n" % f.name
f.write(data1)
f.write(str(input("The last line is:\n")))
f.close()

f = open('L032_Data.txt')
data2 = f.read()
print(data2)
f.close()
