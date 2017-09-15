#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Dorian Wang 2017.09.07
# lesson: show mouse position now

import pyautogui

print("Press control+c to quit")

# get and print mouse position
try:
    while True:
        x, y = pyautogui.position()
        positionStr = "X:" + str(x).rjust(4) + "Y:" + str(y).rjust(4)
        print(positionStr, end="")
        print('\b' * len(positionStr), end="", flush=True)
except KeyboardInterrupt:
    print("\nDone.")
