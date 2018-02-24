#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Dorian Wang 2017.09.07~2017.09.11
# Auto Click QiDian
# add to GitHub

import pyautogui
import time

bufferSecond = 10
pyautogui.PAUSE = 0.1
pyautogui.FAILSAFE = True
width, height = pyautogui.size()
print(time.strftime("%Y-%m-%d", time.localtime()))

# for posX, waitingMinutes in ((925, 5), (1085, 10), (1245, 20), (1405, 30),
#                              (1565, 60), (1725, 60), (1885, 60), (2050, 0)):
for i, (posX, waitingMinutes) in enumerate(((925, 5), (1085, 10), (1245, 20), (1405, 30),
                                            (1565, 60), (1725, 60), (1885, 60), (2050, 0))):

    # check the Chrome is active or not
    # because currently pyautoGUI cannot get active window title,
    # so use color of the second window(Chrome) to determination
    if pyautogui.pixelMatchesColor(120, 125, (36, 109, 182)):
        # Chrome is already active in waiting time
        activeChrome = False
    else:
        # active Chrome window
        pyautogui.hotkey('win', '2')
        activeChrome = True

    # active QiDian website
    pyautogui.hotkey('ctrl', '4')

    # check the ad is show or not, to determinate position of Y
    if pyautogui.pixelMatchesColor(950, 525, (255, 255, 255)):
        posY = 1225
    else:
        posY = 1125

    # just test mouse position foreground
    # pyautogui.moveTo(posX, posY, duration=0.1)
    # pyautogui.moveRel(100, 0, duration=0.1)
    # pyautogui.moveRel(0, 50, duration=0.1)
    # pyautogui.moveRel(-100, 0, duration=0.1)
    # pyautogui.moveRel(0, -50, duration=0.1)

    # print button position, so we could understand the progress
    logString = "%d    X:%4d, Y:%4d    Waiting:%2d Min.    Time " + time.strftime("%H:%M:%S", time.localtime())
    print(logString % (i + 1, posX, posY, waitingMinutes))

    if pyautogui.pixelMatchesColor(posX, posY, (191, 44, 36)):
        oldX, oldY = pyautogui.position()
        pyautogui.click(posX, posY)
        pyautogui.moveTo(oldX, oldY)  # move mouse back

        # do we need check for button color change?
        # I don't think so, because the click is very fast, maybe it cannot waiting and check the changes.
        # if the color is not change, do we need come back to last button?
        # maybe I don't need it, because when we run the program, there should exist one ready button.

        # come back to previous window
        if activeChrome:
            pyautogui.hotkey('alt', 'tab')
            activeChrome = False

        # waiting until next round
        pyautogui.time.sleep(waitingMinutes * 60 + bufferSecond)
    else:
        continue

if activeChrome:
    pyautogui.hotkey('alt', 'tab')
    activeChrome = False
print('Done.')
