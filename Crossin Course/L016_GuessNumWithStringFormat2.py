#-*- coding: utf-8 -*
# lesson 16: String Format2
from random import randint

number = randint(1,100)

name = input("Hi, what's your name?\n")

answer = int(input("Please guess which number I think?\n"))

while answer!=number:
    if answer < number:
        print("Your answer %d is too small, %s." % (answer,name))
    else:
        print("Your answer %d is too big, %s." % (answer,name))
    answer = int(input("Guess it again?\n"))

print("Bingo! %s, you guess it, it's %d." % (name,answer))