#-*- coding: utf-8 -*
# Dorian Wang 2017.08.31
# lesson 39: Guess Number Game, with SAVE function

from random import randint

key = randint(1, 100)
newName = True

name = input("Hi, what's your name?\n")

try:
    loadFile = open('L039_Save.txt')
    allLines = loadFile.readlines()
    loadFile.close()
    # print(allLines)

    for line in allLines[1:]:
        # print(line)
        oldRecord = line.split('\t')
        if name == oldRecord[0]:
            newName = False
            totalGame = int(oldRecord[1])
            totalRound = int(oldRecord[2])
            totalWin =  int(oldRecord[3])
            avageWinRound =  float(oldRecord[4])
            print("\nLoading...... Your saved score is: ")
            print(allLines[0], end='')
            print(line)
            break
except:
    print("Saved file is not exist.")

if newName:
    print("\nWelcome to the Guess Number Game, %s.\n" % name)
    totalGame = 0
    totalRound = 0
    totalWin = 0
    avageWinRound = 0

def isEqual(yourName, yourAnswer, keyNumber, ):
    global totalRound, totalWin, avageWinRound, thisRound
    totalRound = totalRound +1
    thisRound = thisRound + 1

    if yourAnswer < keyNumber:
        print("Your answer %d is too small, %s." % (yourAnswer, yourName))
        return False
    elif yourAnswer > keyNumber:
        print("Your answer %d is too big, %s." % (yourAnswer, yourName))
        return False
    else:
        print("Bingo! %s, you guess it, it's %d." % (yourName, keyNumber))
        totalWin = totalWin + 1
        avageWinRound = totalRound / totalWin
        thisRound = 0
        return True


try:
    answer = int(input("Please guess which number(1-99) I think?\n"))
    thisRound = 0

    while not(isEqual(name, answer, key)):
        try:
            answer = int(input("Guess it again?\n"))
            if (answer < 1) or (answer > 99):
                break
        except:
            print("Please input a number (1-99) to continue, or 0 to exit.\n")
            continue

    totalGame = totalGame + 1

    try:
        saveFile = open('L039_Save.txt', 'w')
        # print(allLines) # the allLines is already read in first read part.
        allLines[0] = 'name\ttotalGame\ttotalRound\ttotalWin\tavageWinRound\n'

        if newName:
            allLines.append('%s\t%d\t%d\t%d\t%f\n' %(name, totalGame, totalRound, totalWin, avageWinRound))
        else:
            for i in range(1,len(allLines)):
                oldRecord = allLines[i].split('\t')
                if name == oldRecord[0]:
                    print('\nOld record: %s' % str(allLines[i]), end='')
                    allLines[i] = '%s\t%d\t%d\t%d\t%f\n' %(name, totalGame, totalRound, totalWin, avageWinRound)
                    print('New record: %s' % str(allLines[i]))
                    break

        # print(allLines)
        saveFile.writelines(allLines)
        saveFile.close()
        print("The game result is saved sucessfully.")
    except:
        print("Sorry, the game result is NOT saved sucessfully.")

except:
    print("It's not a number, exit.\n")



