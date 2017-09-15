#-*- coding: utf-8 -*
from random import randint

answer = randint(1,100)

number = int(input("Please guess which number I think?"))

while number!=answer:
    if number < answer:
        print("Your answer is too small.")
    else:
        print("Your answer is too big.")
    number = int(input("Guess it again?"))

print("Bingo! You guess it.")