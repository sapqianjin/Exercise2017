#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Dorian Wang 2017.09.07
# lesson: auto control GUI

import pyautogui

pyautogui.PAUSE = 0
pyautogui.FAILSAFE = True

width, height = pyautogui.size()

waitingTime = 0.25

for i in range(10):
    pyautogui.moveTo(1000, 500, duration=waitingTime)
    pyautogui.moveTo(2000, 500, duration=waitingTime)
    pyautogui.moveTo(2000, 1000, duration=waitingTime)
    pyautogui.moveTo(1000, 1000, duration=waitingTime)