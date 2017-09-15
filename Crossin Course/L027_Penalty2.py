#-*- coding: utf-8 -*
# Dorian Wang 2017.08.30
# lesson 27: List slice: Penalty2

from random import choice

direction = ['left','up','down','right']
name = input("Hi, what's your name?\n")
roundID = 1
leave = False
score_you = 0
score_computer = 0

while not(leave):
    print("==========Round %d==========" % roundID)
    goal = choice(direction)
    answer = str(input("Please guess direction to shoot?\n"))

    if answer == goal:
        print("Bingo! %s, you get the ball in %s side." % (name, answer))
        score_you = score_you + 1
    else:
        print("Your answer %s is not correct, %s. The ball is went to %s." % (answer, name, goal))
        score_computer = score_computer + 1

    leave = bool(input("Press Enter to continue, or press other key to leave.\n"))
    roundID = roundID + 1

print("%s's score: %s. \nComputer's score: %s." %(name, score_you,score_computer))

if score_you > score_computer:
    print("Winner: %s." % name)
elif score_you < score_computer:
    print("Winner: Computer.")
else:
    print("Draw.")