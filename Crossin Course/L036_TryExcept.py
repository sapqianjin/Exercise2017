#-*- coding: utf-8 -*
# Dorian Wang 2017.08.31
# lesson 36: Try Except

try:
    f = open('L036_Data.txt')
    print("file %s is opened." % f.name)
    f.close()
except:
    print("file is not exist.")
print("Done.")