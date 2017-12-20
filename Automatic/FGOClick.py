#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Dorian Wang 2017.11.21~2017.11.24
# Auto Click FGO
# add to GitHub
# 2017.12.09: rename all var and function name.

import pyautogui
import time
import win32api, win32gui, win32con

BUFFER_SECOND = 1
WAITING_SECOND = 1
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True
width, height = pyautogui.size()
# Default position of ApowerMirror FGO window
X = 140
Y = 150
# Position of Enemy
POS_ENEMY = ((), (X + 280, Y + 100), (X + 610, Y + 100), (X + 960, Y + 100))
# Position of Buffers button
POS_SERVANT_SKILLS = ((),
                      ((), (X + 310, Y + 880), (X + 450, Y + 880), (X + 580, Y + 880)),
                      ((), (X + 760, Y + 880), (X + 910, Y + 880), (X + 1010, Y + 880)),
                      ((), (X + 1210, Y + 880), (X + 1360, Y + 880), (X + 1510, Y + 880)))
POS_MASTER_SKILL_BUTTON = (X + 1910, Y + 500)
POS_MASTER_SKILLS = ((), (X + 1510, Y + 500), (X + 1635, Y + 500), (X + 1760, Y + 500))
POS_BUFFER_CONFIRM = (X + 1360, Y + 650)
POS_BUFFER_TARGETS = ((), (X + 710, Y + 700), (X + 1090, Y + 700), (X + 1560, Y + 700))
# Position of Attach Button and Cards
POS_ATTACK_BUTTON = (X + 1860, Y + 850)
# POS_ATTACK_CARDS = ((), (X + 410, Y + 850), (X + 760, Y + 850), (X + 1160, Y + 850), (X + 1510, Y + 850), (X + 1860, Y + 850), (X + 810, Y + 350), (X + 1160, Y + 350), (X + 1460, Y + 350))
POS_ATTACK_CARDS = ((), (440, 900), (815, 900), (1175, 900), (1545, 900), (1920, 900), (1020, 650), (1355, 650), (1635, 650))
POS_ATTACK_END_BUTTON = (X + 1460, Y + 950)
# Position of Other Button
POS_UNLIMITED_LINEUP_BUTTON = (X + 860, Y + 650)
POS_SUMMON_END_BUTTON = (X + 1360, Y + 1025)
POS_SUMMON_TEN_BUTTON = (X + 1335, Y + 900)
# Color of fix_attack_one_turn cards
COLOR_ATTACK_BUTTON = (0, 234, 247)
COLOR_ATTACK_RED = [(153, 25, 24), (152, 24, 22), (154, 24, 23)]
COLOR_ATTACK_BLUE = [(22, 64, 147), (21, 64, 148), (21, 65, 151), (22, 66, 150), (23, 65, 151), (22, 63, 153)]
COLOR_ATTACK_GREEN = ((30, 110, 12))
COLOR_UNLIMITED_LINEUP_BUTTON = ()
COLOR_UNLIMITED_LINEUP_RESET = ()


def repeat_click1(position, repeat_time=1):
    # 单个位置重复点击
    try:
        pos_x = position[0]
        pos_y = position[1]
        for i in range(0, repeat_time):
            # 发现模拟器窗口无法点击，也无法按键切换回去
            # 只能使用Apower Mirror，测试OK
            pyautogui.click(pos_x, pos_y)
            print(i, time.strftime("%H:%M:%S", time.localtime()))
            pyautogui.time.sleep(WAITING_SECOND)
        print('Done.')
        # Log end time
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    except KeyboardInterrupt:
        print('User Break.')
    return ()


def unlimited_lineup(gifts_qty=300):
    # 无限池抽奖
    # 至少需要点击gifts_qty/10*4次
    # 重复次数取决于网络信号，通常加10%。
    gifts_round = int(round(gifts_qty / 10 * 4.1, 0))
    # 每次点击大约2秒钟左右 (WAITING_SECOND + pyautogui.PAUSE)
    print("Need around", int(round(gifts_round * (WAITING_SECOND + pyautogui.PAUSE) / 60, 60)), "Minutes.")
    repeat_click1(POS_UNLIMITED_LINEUP_BUTTON, gifts_round)
    return ()


def buffer_confirm(target=0):
    # confirm buffer
    # the confirm is already disable in game menu
    # pyautogui.click(POS_BUFFER_CONFIRM)
    # choose target servant
    if target != 0:
        pyautogui.click(POS_BUFFER_TARGETS[target])
        # waiting for result
    pyautogui.time.sleep(3)
    return ()


def choose_enemy(target=3):
    try:
        # click enemy
        if target != 0:
            pyautogui.click(POS_ENEMY[target])
    except KeyboardInterrupt:
        print('User Break.')
    return ()


def servant_skill(servant, skill, target=0):
    # 从者技能(buff)释放
    # 需要指定目标则输入target参数
    try:
        # choose buffer
        pyautogui.click(POS_SERVANT_SKILLS[servant][skill])
        # confirm buffer and choose target
        buffer_confirm(target)
    except KeyboardInterrupt:
        print('User Break.')
    return ()


def master_skill(skill, target=0):
    # 御主技能释放
    # 需要指定目标则输入target参数
    try:
        # open skill
        pyautogui.click(POS_MASTER_SKILL_BUTTON)
        # choose skill
        pyautogui.click(POS_MASTER_SKILLS(skill))
        # confirm buffer and choose target
        buffer_confirm(target)
    except KeyboardInterrupt:
        print('User Break.')
    return ()


def choose_attack_cards(cards):
    # 战斗卡片选择
    try:
        for card in cards:
            # click card
            pyautogui.click(POS_ATTACK_CARDS[card])
    except KeyboardInterrupt:
        print('User Break.')
    return ()


def fix_attack_one_turn(cards):
    # 战斗界面选择
    try:
        # open attack screen
        pyautogui.click(POS_ATTACK_BUTTON)
        pyautogui.time.sleep(3)
        choose_attack_cards(cards)
    except KeyboardInterrupt:
        print('User Break.')
    return ()


def auto_attack_one_turn(max_card=5):
    # 自动战斗，按照红-蓝-绿颜色优先次序
    try:
        # open attack screen
        pyautogui.click(POS_ATTACK_BUTTON)
        pyautogui.time.sleep(3)
        red_cards = []
        blue_cards = []
        green_cards = []
        for card in range(1, max_card + 1):
            im = pyautogui.screenshot()
            # pyautogui.moveTo(POS_ATTACK_CARDS[card])
            # pyautogui.time.sleep(1)
            if im.getpixel(POS_ATTACK_CARDS[card])[1] > 85:
                green_cards.append(card)
            elif im.getpixel(POS_ATTACK_CARDS[card])[1] > 45:
                blue_cards.append(card)
            else:
                red_cards.append(card)
        if len(red_cards) > 2:
            choose_attack_cards(red_cards[0:3])
        elif len(blue_cards) > 3:
            choose_attack_cards(blue_cards[0:3])
        elif len(green_cards) > 3:
            choose_attack_cards(green_cards[0:3])
        else:
            # print(red_cards)
            # print(blue_cards)
            # print(green_cards)
            # print((red_cards + blue_cards + green_cards)[0:3])
            choose_attack_cards((red_cards + blue_cards + green_cards)[0:3])
    except KeyboardInterrupt:
        print('User Break.')
    return ()


def friend_point_summon(cards_qty=10):
    # 友情点召唤
    try:
        cards_round = int(cards_qty / 10)
        # 每次点击大约8秒钟左右 (4 + 4 * pyautogui.PAUSE)
        print("Need around", int(round(cards_round * (4 + 4 * pyautogui.PAUSE) / 60, 60)), "Minutes.")
        for i in range(0, cards_round):
            # click summon button
            pyautogui.click(POS_SUMMON_END_BUTTON)
            # select summon 10 cards
            pyautogui.click(POS_SUMMON_TEN_BUTTON)
            # confirm summon
            pyautogui.click(POS_SUMMON_TEN_BUTTON)
            # waiting for result
            pyautogui.time.sleep(3)
            # click to finish summon
            pyautogui.click(POS_SUMMON_END_BUTTON)
            pyautogui.time.sleep(1)
            print(i, time.strftime("%H:%M:%S", time.localtime()))
        print('Done.')
        # Log end time
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    except KeyboardInterrupt:
        print('User Break.')
    return ()


def nero_fest_autumn_expert_first_turn():
    choose_enemy(1)
    servant_skill(3, 1, 1)
    servant_skill(3, 2, 0)
    servant_skill(3, 3, 0)
    return ()


def nero_fest_autumn_expert_last_turn(target=1):
    choose_enemy(3)
    master_skill(3, 3)  # Kong Ming CD -2
    servant_skill(1, 2)  # Lancelot +Critical Star Drop
    servant_skill(1, 3)  # Lancelot +Critical
    servant_skill(2, 2)  # Jeanne Alter: +ATK
    servant_skill(2, 3)  # Jeanne Alter: +Critical ATK
    servant_skill(3, 2)  # Kong Ming: +NP+Def
    servant_skill(3, 3)  # Kong Ming: +NP+ATK
    # 孔明技能1需要依照实际情况调整目标，默认兰斯洛特
    servant_skill(3, 1, target)
    # 默认按照孔明、贞德Alter、兰斯洛特依次使用宝具卡
    fix_attack_one_turn((8, 7, 6))
    pyautogui.time.sleep(30)
    repeat_click1(POS_ATTACK_END_BUTTON, 5)
    return ()


def common_last_turn(target=1):
    servant_skill(1, 1)  # Artila +ALL NP ATK
    servant_skill(1, 3)  # Artila +Critical
    servant_skill(2, 1)  # Jeanne Alter: +ATK
    servant_skill(2, 2)  # Jeanne Alter: +ALL ATK
    servant_skill(2, 3)  # Jeanne Alter: +Critical ATK
    # 默认按照孔明、贞德Alter、阿蒂拉依次使用宝具卡
    fix_attack_one_turn((8, 7, 6))
    pyautogui.time.sleep(30)
    repeat_click1(POS_ATTACK_END_BUTTON, 5)
    return ()


def auto_battle(turns=3):
    for i in range(0, turns):
        auto_attack_one_turn(max_card=5)
        pyautogui.time.sleep(20)
        # normal 15~20 second is ok, but if enemy NP, or servant died, need longer time
        while not(pyautogui.pixelMatchesColor(POS_ATTACK_BUTTON[0],POS_ATTACK_BUTTON[1],COLOR_ATTACK_BUTTON)):
            pyautogui.time.sleep(10)
    return ()


# Main Program
# Switch to FGO window
pyautogui.hotkey('alt', 'tab')
pyautogui.time.sleep(BUFFER_SECOND)
# Log start time
print(time.strftime("%Y-%m-%d %H:%M:%S\n", time.localtime()))

# 友情点召唤
# friend_point_summon(cards_qty=20)

# 圣诞节活动
# 圣诞节无限池抽奖，每池500礼物
# unlimited_lineup(gifts_qty=500)


# 通用无脑进攻
auto_battle(turns=5)

# 通用最后一回合，
# common_last_turn()

# want to use win32, but failed.
# pyautogui.moveTo(1370,775)
# pyautogui.moveTo(2039,1074)
# print(1)
# windll.user32.SetCursorPos(2039,1074)
# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN|win32con.MOUSEEVENTF_LEFTUP, 0, 0)
# print(2)

# 尼禄祭活动
# 尼禄祭无限池抽奖，每池300礼物
# unlimited_lineup(gifts_qty=300)

# 尼禄祭花瓣池第一回合
# nero_fest_autumn_expert_first_turn()

# 尼禄祭花瓣池最后一回合
# 孔明技能1需要依照实际情况调整目标
# nero_fest_autumn_expert_last_turn(target=1)

# Switch back to Python window, so user could know the program is finished.
pyautogui.hotkey('alt', 'tab')
