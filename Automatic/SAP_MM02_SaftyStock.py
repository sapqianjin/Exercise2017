#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Dorian Wang 2017.09.27
# Use MM02 to change the safety stock in SAP
# Create for Client_F, because they cannot get authorization for MM17/LSMW/SCAT
# Test OK. Add to GitHub

import pyautogui
import time, codecs

# Some SAP system need waiting feedback from server.
# So we can set small pause time for some local steps,
# but for these steps need return information from server,
# we need set buffer time, I prefer 1 second (at least 0.5 second).
# The buffer time must be adjusted based on the network!
pyautogui.PAUSE = 0.1
pyautogui.FAILSAFE = True
bufferSecond = 1.5

# Before start this program, the SAP GUI window must be open first,
# The t-code MM02 should be started, and set default in view/org
# SAP GUI use the Corbu theme, the color will be used in program logic
# If you run it in your computer, the position/color maybe need adjust.
# You can use pyautogui.position() get the position value.

# All position are based on Win 10, task bar in left side
# All color are based on Corbu theme
# SAP Program SAPLMGMM Screen 0060
posX_materialNumber = 430
posY_materialNumber = 330
# SAP Program SAPLMGMM Screen 0070
posX_viewWindow = 900
posY_viewWindow = 365
color_viewWindow = (81, 81, 81)
# SAP Program SAPLMGMM Screen 0080
posX_orgWindow = 900
posY_orgWindow = 325
color_orgWindow = (81, 81, 81)
# SAP Program SAPLMGD1 Screen2486
posX_safetyStock = 512
posY_safetyStock = 980
posX_saveActive = 565
posY_saveActive = 100
color_saveActive = (158, 189, 217)

# Switch to SAP MM02 window
pyautogui.hotkey('alt', 'tab')
pyautogui.time.sleep(bufferSecond)
# Log start time
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

try:
    with codecs.open("MM02_SS.txt", "r", encoding="utf-8") as f:
        for line in f.readlines():
            materialNumber, safetyStock = line.split()
            print("Material:", materialNumber, "Safety Stock:", safetyStock)
            # Click field of material, del exist data, then send material number
            pyautogui.click(posX_materialNumber, posY_materialNumber)
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.hotkey('del')
            pyautogui.typewrite(materialNumber)
            pyautogui.hotkey('enter')
            pyautogui.time.sleep(bufferSecond)

            # Check the view window is active or not
            # Recommend set "selection only on request" to skip it
            if pyautogui.pixelMatchesColor(posX_viewWindow, posY_viewWindow, color_viewWindow):
                # Click enter if the view selection window active
                pyautogui.hotkey('enter')
                pyautogui.time.sleep(bufferSecond)

            # Check the organize window is active or not
            # Recommend set "selection only on request" to skip it
            if pyautogui.pixelMatchesColor(posX_orgWindow, posY_orgWindow, color_orgWindow):
                # Click enter if organize window active
                pyautogui.hotkey('enter')
                pyautogui.time.sleep(bufferSecond)

            # Click field of Safety Stock, del exist data, then send the quantity from text file
            pyautogui.click(posX_safetyStock, posY_safetyStock)
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.hotkey('del')
            pyautogui.typewrite(safetyStock)
            pyautogui.hotkey('ctrl', 's')
            pyautogui.time.sleep(bufferSecond)

            # Check the save button is still active or not, sometime warning message will pause save action
            if pyautogui.pixelMatchesColor(posX_saveActive, posY_saveActive, color_saveActive):
                # Click enter to skip the warning message
                pyautogui.hotkey('enter')
                pyautogui.time.sleep(bufferSecond)
            else:
                continue

    print('Done.')
    # Log end time
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

except KeyboardInterrupt:
    print('User Break.')

# Switch back to Python window, so user could know the program is finished.
pyautogui.hotkey('alt', 'tab')

# 0.5 second is accept , for each material, avg time 5~7s
# So the efficiency is very low, but # 0.25 is not accept,
# because program will place safety stock in material description field.
# Actually, even I set 0.5 second, the program still change one
# material description wrong in 19:49:23. (only run no more than 50 material).
# So I prefer change the PAUSE time to 1 second at least.

# Some test result in Client_C test:
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

# Pause 0.1 second, buffer 1.5 Second
# test 50 material with view, org:
# 2017-09-28 15:00:41 ~ 2017-09-28 15:06:46
# average: each material 7.3 s
# not exist error.

# Pause 0.1 second, buffer 1.5 Second
# test 50 material without view, org:
# 2017-09-28 15:08:15 ~ 2017-09-28 15:11:40
# average: each material 3.5 s
# not exist error.

