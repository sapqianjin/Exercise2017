#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Dorian Wang 2017.09.21
# Auto Click Web for Pre Order
# add to GitHub

import pyautogui
import time

bufferSecond = 10
pyautogui.PAUSE = 0.1
pyautogui.FAILSAFE = True
width, height = pyautogui.size()
print(time.strftime("%Y-%m-%d", time.localtime()))

posX, posY = (1369,1300)
color = (247,247,247)

try:
    while True:
        if pyautogui.pixelMatchesColor(120, 125, (36, 109, 182)):
            # Chrome is already active in waiting time
            activeChrome = False
        else:
            # active Chrome window
            pyautogui.hotkey('win', '2')
            activeChrome = True

        if pyautogui.pixelMatchesColor(posX, posY, color):
            # pyautogui.time.sleep(1)
            continue
        else:
            pyautogui.click(posX, posY)
except KeyboardInterrupt:
    print('Done.')
