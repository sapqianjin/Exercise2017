#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Dorian Wang 2017.09.27
# Send Key and Click Mouse to Prevent PC Sleep
# Test OK. Add to GitHub

import pyautogui
import time, codecs

# Sometime you need mind don't let system sleep, or hard disk will
# sleep if nobody access it. So create this script.
pyautogui.PAUSE = 0.1
pyautogui.FAILSAFE = True
bufferSecond = 1.5

posX = 1400
posY = 270
endMinutes = 60
intervalMinutes = 1
now = 1


# Switch to SAP MM02 window
pyautogui.hotkey('alt', 'tab')
pyautogui.time.sleep(bufferSecond)
# Log start time
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

cycle = endMinutes / intervalMinutes

try:
    while now < cycle:
        pyautogui.hotkey('backspace')
        pyautogui.time.sleep(bufferSecond)
        pyautogui.doubleClick(posX, posY)
        logString = "%d    X:%4d, Y:%4d    Waiting:%2d Min.    Time " + time.strftime("%H:%M:%S", time.localtime())
        print(logString % (now, posX, posY, intervalMinutes))
        now = now + 1
        pyautogui.time.sleep(intervalMinutes * 60 - bufferSecond)

    print('Done.')
    # Log end time
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

except KeyboardInterrupt:
    print('User Break.')

# Switch back to Python window, so user could know the program is finished.
pyautogui.hotkey('alt', 'tab')
