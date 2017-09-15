#-*- coding: utf-8 -*
# lesson 26: List example: Penalty
from random import choice

direction = ['left','up','down','right']
name = input("Hi, what's your name?\n")
leave = False

while not(leave):
    goal = choice(direction)
    answer = str(input("Please guess direction to shoot?\n"))

    if answer == goal:
        print("Bingo! %s, you get the ball in %s side." % (name, answer))
    else:
        print("Your answer %s is not correct, %s. The ball is went to %s." % (answer, name, goal))

    leave = bool(input("Press Enter to continue, or press other key to leave.\n"))