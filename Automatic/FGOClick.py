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
print(time.strftime("%Y-%m-%d %H:%M:%S\n", time.localtime()))

def repeatClick1(repeatTime, position):
    try:
        posX = position[0]
        posY = position[1]
        for i in range(0, repeatTime):
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

    return()

def servantSkill(servant, skill, target):
    try:
        # click buffer
        if servant ==1:
            if skill == 1:
                pyautogui.click(450, 1030)
            elif skill == 2:
                pyautogui.click(590, 1030)
            elif skill == 3:
                pyautogui.click(720, 1030)
        elif servant ==2:
            if skill == 1:
                pyautogui.click(900, 1030)
            elif skill == 2:
                pyautogui.click(1050, 1030)
            elif skill == 3:
                pyautogui.click(1150, 1030)
        elif servant == 3:
            if skill == 1:
                pyautogui.click(1350, 1030)
            elif skill == 2:
                pyautogui.click(1500, 1030)
            elif skill == 3:
                pyautogui.click(1650, 1030)
        # confirm buffer
        pyautogui.click(1500, 800)
        # click target servant
        if target == 1:
            pyautogui.click(1650, 1030)
        elif target == 2:
            pyautogui.click(1650, 1030)
        elif target == 3:
            pyautogui.click(1650, 1030)

    except KeyboardInterrupt:
        print('User Break.')

    return()

def chooseEnemy(target):
    try:
        # click enemy
        if target == 1:
            pyautogui.click(420, 250)
        elif target == 2:
            pyautogui.click(750, 250)
        elif target == 3:
            pyautogui.click(1100, 250)

    except KeyboardInterrupt:
        print('User Break.')

    return()

def masterSkill(skill):
    try:
        # open skill
        pyautogui.click(2050, 650)
        # click skill
        if skill == 1:
            pyautogui.click(1650, 650)
        elif skill == 2:
            pyautogui.click(1775, 650)
        elif skill == 3:
            pyautogui.click(1900, 650)
        # close skill
        pyautogui.click(2050, 650)
    except KeyboardInterrupt:
        print('User Break.')

    return()

def attack(card):
    try:
        # open attack
        pyautogui.click(2000, 1000)
        # click skill
        if card == 1:
            pyautogui.click(550,1000)
        elif card == 2:
            pyautogui.click(900,1000)
        elif card == 3:
            pyautogui.click(1300,1000)
        elif card == 4:
            pyautogui.click(1650, 1000)
        elif card == 5:
            pyautogui.click(2000, 1000)
        # close skill
        pyautogui.click(2050, 650)
    except KeyboardInterrupt:
        print('User Break.')

    return()

def summerByFriendPoint(repeatTime):
    try:
        for i in range(0, repeatTime):
            # click Summer button
            pyautogui.click(1500, 1175)
            # click summer 10 cards
            pyautogui.click(1475, 1050)
            # confirm summer
            pyautogui.click(1475, 1050)
            # waiting for result
            pyautogui.time.sleep(3)
            # click to finish summer
            pyautogui.click(1500, 1175)
            pyautogui.time.sleep(1)
            print(i, time.strftime("%H:%M:%S", time.localtime()))
        print('Done.')
        # Log end time
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

    except KeyboardInterrupt:
        print('User Break.')

    return()


# 尼禄祭无限池抽奖
repeatClick1(150, (1000, 800))

# 友情点召唤
# summerByFriendPoint(5)


# Switch back to Python window, so user could know the program is finished.
pyautogui.hotkey('alt', 'tab')
