#-*- coding: utf-8 -*
# lesson 14: String Format
from random import randint

number = randint(1,100)

answer = int(input("Please guess which number I think?\n"))

while answer!=number:
    if answer < number:
        print("Your answer %d is too small." %answer)
    else:
        print("Your answer %d is too big." %answer)
    answer = int(input("Guess it again?\n"))

print("Bingo! You guess it, it's %d." %number)