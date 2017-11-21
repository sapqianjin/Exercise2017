#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Dorian Wang 2017.11.21~2017.11.21
# Auto Click FGO
# add to GitHub

import pyautogui
import time

bufferSecond = 1
waitingSecond = 1
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True
width, height = pyautogui.size()

# Switch to FGO window
pyautogui.hotkey('alt', 'tab')
pyautogui.time.sleep(bufferSecond)
# Log start time
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

try:
    #尼禄祭无限池抽奖
    iMax = 150
    posX = 1000
    posY = 950

    for i in range(0, iMax):
        # 发现模拟器窗口无法点击，也无法按键切换回去
        # 只能使用ApowerMirror，测试OK
        pyautogui.click(posX, posY)
        print(i, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        pyautogui.time.sleep(waitingSecond)
    print('Done.')
    # Log end time
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

except KeyboardInterrupt:
    print('User Break.')

# Switch back to Python window, so user could know the program is finished.
pyautogui.hotkey('alt', 'tab')
