#-*- coding: utf-8 -*
# lesson 15: Loop

for i in range(0,6):
    for j in range(0,i+1):
        print('*', end='')
    print()

print("5*5")
for i in range(0,6):
    for j in range(0,6):
        print('*', end='')
    print()

#  Show all probroblity  in Zelda Breath of the Wild
# A = ("E","F","G","H")
# B = ("Q", "R", "S", "T")
# C = ("A", "B", "C", "D")
#
# for a in A:
#     for b in B:
#         for c in C:
#             print (a+b+c)
