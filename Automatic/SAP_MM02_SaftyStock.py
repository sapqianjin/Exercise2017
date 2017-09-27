#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Dorian Wang 2017.09.27
# Use MM02 to change the safety stock in SAP
# Test OK. Add to GitHub

import pyautogui
import time, codecs

# Some SAP system need waiting feedback from server
# So we can set small pause time for some local steps, but we need
# buffer time for these steps need feedback from server.
pyautogui.PAUSE = 0.1
pyautogui.FAILSAFE = True
bufferSecond = 1

# Before start this program, the SAP GUI window must be open first,
# SAP GUI use the Corbu Theme, the color will be used in program logic
# The t-code MM02 should be started, and set default in view/org
# If you run it in your computer, the position should be adjust.
# You can use pyautogui.position() get the position value.
# SAP Screen SAPLMGMM 0060
posX_Material = 430
posY_Material = 330
# SAP Screen SAPLMGD1 2486
posX_SafetyStock = 512
posY_SafetyStock = 980

# Goto SAP MM02 window
pyautogui.hotkey('alt', 'tab')
pyautogui.time.sleep(bufferSecond)
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

try:
    with codecs.open("MM02_SS.txt", "r", encoding="utf-8") as f:
        for line in f.readlines():
            material,  safetyStock = line.split()
            print("Material:", material, "Safety Stock:", safetyStock)
            # Click field of material, then del exist data, and send material number
            pyautogui.click(posX_Material, posY_Material)
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.hotkey('del')
            pyautogui.typewrite(material)
            pyautogui.hotkey('enter')
            pyautogui.time.sleep(bufferSecond)

            # Check the view window is active or not
            # Recommend set "selection only on request" to skip it
            if pyautogui.pixelMatchesColor(900, 365, (81,81,81)):
                # Click enter if the view selection window active
                pyautogui.hotkey('enter')
                pyautogui.time.sleep(bufferSecond)

            # Check the organize window is active or not
            # Recommend set "selection only on request" to skip it
            if pyautogui.pixelMatchesColor(900, 325, (81,81,81)):
                # Click enter if organize window active
                pyautogui.hotkey('enter')
                pyautogui.time.sleep(bufferSecond)

            # Click field of Safety Stock, then send the quantity
            pyautogui.click(posX_SafetyStock, posY_SafetyStock)
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.hotkey('del')
            pyautogui.typewrite(safetyStock)
            pyautogui.hotkey('ctrl', 's')
            pyautogui.time.sleep(bufferSecond)

            # Check the save button is still active, sometime warning message
            if pyautogui.pixelMatchesColor(565,100, (158, 189, 217)):
                # Click enter to skip the warning message
                pyautogui.hotkey('enter')
                pyautogui.time.sleep(bufferSecond)
            else:
                continue


    print('Done.')
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

except KeyboardInterrupt:
    print('User Break.')

pyautogui.hotkey('alt', 'tab')

# 0.5 second is accept in CY test, for each material, avg time 5~7s
# test 100 material: 2017-09-27 19:44:55 ~ 2017-09-27 19:55:09
# So the efficiency is very low, but # 0.25 is not accept,
# because program will place safety stock in material description field.
# Actually, even I set 0.5 second, the program still change one
# material description wrong in 19:49:23. (only run no more than 50 material).
#
# So I prefer change the PAUSE time to 1 second.

# some test result:
# Pause 0.5 second
# test 100 material with view, org:
# 2017-09-27 19:44:55 ~ 2017-09-27 19:55:09
# average: each material 6.15 s
# exist error change for material description.

# Pause 1 second
# test 20 material without view, org:
# 2017-09-27 20:04:58 ~ 2017-09-27 20:08:21
# average: each material 10.15 s
# not exist error.
# test 50 material with view, org:
# 2017-09-27 20:16:25 ~ 2017-09-27 20:26:32
# average: each material 12.15 s
# not exist error.

# Pause 0.1 second, buffer 1 Second
# test 50 material with view, org:
# 2017-09-27 20:46:28 ~ 2017-09-27 20:50:56
# average: each material 5.36 s
# not exist error.

# Pause 0.1 second, buffer 1 Second
# test 50 material without view, org:
# 2017-09-27 20:53:07 ~ 2017-09-27 20:55:48
# average: each material 3.2 s
# not exist error.