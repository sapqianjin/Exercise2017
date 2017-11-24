#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Dorian Wang 2017.11.21~2017.11.24
# Auto Click FGO
# add to GitHub

import pyautogui
import time

bufferSecond = 1
waitingSecond = 1
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True
width, height = pyautogui.size()


def repeatClick1(position, repeatTime=1):
    # 简单的单个位置重复点击
    try:
        posX = position[0]
        posY = position[1]
        for i in range(0, repeatTime):
            # 发现模拟器窗口无法点击，也无法按键切换回去
            # 只能使用Apower Mirror，测试OK
            pyautogui.click(posX, posY)
            print(i, time.strftime("%H:%M:%S", time.localtime()))
            pyautogui.time.sleep(waitingSecond)
        print('Done.')
        # Log end time
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    except KeyboardInterrupt:
        print('User Break.')
    return ()


def bufferConfirm(target=0):
    # confirm buffer
    pyautogui.click(1500, 800)
    # choose target servant
    if target == 1:
        pyautogui.click(850, 850)
    elif target == 2:
        pyautogui.click(1230, 850)
    elif target == 3:
        pyautogui.click(1700, 850)
    # waiting for result
    pyautogui.time.sleep(3)
    return ()


def chooseEnemy(target=3):
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
    return ()


def servantSkill(servant, skill, target=0):
    # 从者技能(buff)释放
    try:
        # choose buffer
        if servant == 1:
            if skill == 1:
                pyautogui.click(450, 1030)
            elif skill == 2:
                pyautogui.click(590, 1030)
            elif skill == 3:
                pyautogui.click(720, 1030)
        elif servant == 2:
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
        # confirm buffer and choose target
        bufferConfirm(target)
    except KeyboardInterrupt:
        print('User Break.')
    return ()


def masterSkill(skill, target=0):
    # 御主技能释放
    try:
        # open skill
        pyautogui.click(2050, 650)
        # choose skill
        if skill == 1:
            pyautogui.click(1650, 650)
        elif skill == 2:
            pyautogui.click(1775, 650)
        elif skill == 3:
            pyautogui.click(1900, 650)
        # confirm buffer and choose target
        bufferConfirm(target)
    except KeyboardInterrupt:
        print('User Break.')
    return ()


def attack(cards):
    # 战斗卡片选择
    try:
        # open attack
        pyautogui.click(2000, 1000)
        pyautogui.time.sleep(3)
        for card in cards:
            # click card
            if card == 1:
                pyautogui.click(550, 1000)
            elif card == 2:
                pyautogui.click(900, 1000)
            elif card == 3:
                pyautogui.click(1300, 1000)
            elif card == 4:
                pyautogui.click(1650, 1000)
            elif card == 5:
                pyautogui.click(2000, 1000)
            elif card == 6:
                pyautogui.click(950, 500)
            elif card == 7:
                pyautogui.click(1300, 500)
            elif card == 8:
                pyautogui.click(1600, 500)
    except KeyboardInterrupt:
        print('User Break.')
    return ()


def summonByFriendPoints(repeatTime=20):
    # 友情点召唤
    try:
        for i in range(0, repeatTime):
            # click summon button
            pyautogui.click(1500, 1175)
            # select summon 10 cards
            pyautogui.click(1475, 1050)
            # confirm summon
            pyautogui.click(1475, 1050)
            # waiting for result
            pyautogui.time.sleep(3)
            # click to finish summon
            pyautogui.click(1500, 1175)
            pyautogui.time.sleep(1)
            print(i, time.strftime("%H:%M:%S", time.localtime()))
        print('Done.')
        # Log end time
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    except KeyboardInterrupt:
        print('User Break.')
    return ()


def NeroFestAutumnExpertFirstRound():
    chooseEnemy(1)
    servantSkill(3, 1, 1)
    servantSkill(3, 2, 0)
    servantSkill(3, 3, 0)
    return ()


def NeroFestAutumnExpertLastRound(target=1):
    chooseEnemy(3)
    masterSkill(3, 3)
    servantSkill(1, 2)
    servantSkill(1, 3)
    servantSkill(2, 2)
    servantSkill(2, 3)
    servantSkill(3, 2)
    servantSkill(3, 3)
    # 孔明技能1需要依照实际情况调整目标，默认兰斯洛特
    servantSkill(3, 1, target)
    # 默认按照孔明、贞德Alter、兰斯洛特依次使用宝具卡
    attack((8, 7, 6))
    pyautogui.time.sleep(30)
    repeatClick1((1600, 1100), 5)
    return ()


# Main Program
# Switch to FGO window
pyautogui.hotkey('alt', 'tab')
pyautogui.time.sleep(bufferSecond)
# Log start time
print(time.strftime("%Y-%m-%d %H:%M:%S\n", time.localtime()))

# 友情点召唤
# summonByFriendPoints(25)

# 尼禄祭无限池抽奖，
# 至少需要点击600/20*4=120次
# 重复次数取决于网络信号，使用130-150，大约4-5分钟。
# repeatClick1((1000, 800), 80)

# 尼禄祭花瓣池第一回合
# NeroFestAutumnExpertFirstRound()

# 尼禄祭花瓣池最后一回合
# 孔明技能1需要依照实际情况调整目标
# NeroFestAutumnExpertLastRound(1)

# Switch back to Python window, so user could know the program is finished.
pyautogui.hotkey('alt', 'tab')
