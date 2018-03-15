#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Dorian Wang 2018.03.16
# Test for Click in Android Simulator in Background.

import pyautogui
import time
import win32

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True
width, height = pyautogui.size()

# Main Program
print(time.strftime("%Y-%m-%d %H:%M:%S\n", time.localtime()))

# check the default value of FGO window
win_fgo = pyautogui.getWindow('FGO_US')
X = win_fgo.get_position()[0]
Y = win_fgo.get_position()[1]


pyautogui.click(1000,500)