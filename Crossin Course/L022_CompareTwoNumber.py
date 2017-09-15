#-*- coding: utf-8 -*
# lesson 22: Function Example
from random import randint

number = randint(1,100)

name = input("Hi, what's your name?\n")

answer = int(input("Please guess which number I think?\n"))

def isEqual(name, num1, num2):
    if num1 < num2:
        print("Your answer %d is too small, %s." % (num1,name))
        return False
    elif num1 > num2:
        print("Your answer %d is too big, %s." % (num1,name))
        return False
    else:
        print("Bingo! %s, you guess it, it's %d." % (name, num2))
        return True



while not(isEqual(name,answer,number)):
    answer = int(input("Guess it again?\n"))


