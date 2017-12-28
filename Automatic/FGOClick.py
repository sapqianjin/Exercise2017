#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Dorian Wang 2017.11.21~2017.11.24
# Auto Click FGO
# add to GitHub
# 2017.12.09: rename all var and function name.
# todo background click window?

import pyautogui
import time

BUFFER_SECOND = 1
WAITING_SECOND = 1
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True
width, height = pyautogui.size()
# Default position and color of ApowerMirror FGO window
X = 0
Y = 0
X_DEFAULT = 240
Y_DEFAULT = 154
# Position of Enemy
POS_ENEMY = ((), (X + 420, Y + 250), (X + 750, Y + 250), (X + 1100, Y + 250))
# Position of Buffers button
POS_SERVANT_SKILLS = ((),
                      ((), (X + 450, Y + 1030), (X + 590, Y + 1030), (X + 720, Y + 1030)),
                      ((), (X + 900, Y + 1030), (X + 1050, Y + 1030), (X + 1150, Y + 1030)),
                      ((), (X + 1350, Y + 1030), (X + 1500, Y + 1030), (X + 1650, Y + 1030)))
POS_MASTER_SKILL_BUTTON = (X + 2050, Y + 650)
POS_MASTER_SKILLS = ((), (X + 1650, Y + 650), (X + 1775, Y + 650), (X + 1900, Y + 650))
POS_BUFFER_CONFIRM = (X + 1500, Y + 800)
POS_BUFFER_TARGETS = ((), (X + 850, Y + 850), (X + 1230, Y + 850), (X + 1700, Y + 850))
# Position of Attach Button and Cards
POS_ATTACK_BUTTON = (X + 2000, Y + 1000)
POS_ATTACK_CARDS = ((), (X + 440, Y + 900), (X + 815, Y + 900), (X + 1175, Y + 900), (X + 1545, Y + 900), (X + 1920, Y + 900), (X + 1020, Y + 650), (X + 1355, Y + 650), (X + 1635, Y + 650))
POS_BATTLE_BEGIN_BUTTON = (X + 2000, Y + 1200)
POS_BATTLE_END = (X + 2000, Y + 950)
POS_BATTLE_END_BUTTON = (X + 2000, Y + 1200)
# Position of Other Button
POS_UNLIMITED_LINEUP_BUTTON = (X + 1100, Y + 800)
POS_UNLIMITED_LINEUP_RESET = (X + 1900, Y + 475)
POS_UNLIMITED_LINEUP_RESET_CONFIRM = (X + 1400, Y + 1000)
POS_SUMMON_TEN_BUTTON = (X + 1475, Y + 1050)
POS_SUMMON_END_BUTTON = (X + 1500, Y + 1175)
# Color of fix_attack_one_turn cards
COLOR_ATTACK_BUTTON = (0, 234, 247)
# Red Attack  Cards: (153, 25, 24), (152, 24, 22), (154, 24, 23)
# Blue Attack  Cards: (22, 64, 147), (21, 64, 148), (21, 65, 151), (22, 66, 150), (23, 65, 151), (22, 63, 153)
# Green Attack Cards: (30, 110, 12)
COLOR_BATTLE_BEGIN_BUTTON = (182, 187, 191)
COLOR_BATTLE_END = (3, 10, 15)
COLOR_UNLIMITED_LINEUP_BUTTON = (21, 202, 243)
COLOR_UNLIMITED_LINEUP_RESET = (138, 175, 223)


def same_color(position, color):
    # 按钮颜色难以完全一致，所以定义RGB色差之和在10以内均为OK
    color_position = pyautogui.screenshot().getpixel(position)
    color_different = 0
    for i in range(0, 3):
        color_different = color_different + (color_position[i] - color[i])
    if abs(color_different) < 10:
        return True
    else:
        return False


def repeat_click1(position, repeat=1, waiting_time=WAITING_SECOND):
    # 单个位置重复点击
    try:
        pos_x = position[0]
        pos_y = position[1]
        for i in range(repeat, 0, -1):
            # 发现模拟器窗口无法点击，也无法按键切换回去
            # 只能使用Apower Mirror，测试OK
            pyautogui.click(pos_x, pos_y)
            print(i, time.strftime("%H:%M:%S", time.localtime()))
            pyautogui.time.sleep(waiting_time)
        print('Done.')
        # Log end time
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    except KeyboardInterrupt:
        print('User Break.')
    return ()


def unlimited_lineup(gifts_qty=300):
    # 无限池抽奖，单纯点击
    # 至少需要点击gifts_qty/10*4次
    # 重复次数取决于网络信号，通常加10%。
    click_round = int(round(gifts_qty / 10 * 4.1, 0))
    # 每次点击大约2秒钟左右 (WAITING_SECOND + pyautogui.PAUSE)
    print("Need around", int(round(click_round * (WAITING_SECOND + pyautogui.PAUSE) / 60, 60)), "Minutes.")
    repeat_click1(POS_UNLIMITED_LINEUP_BUTTON, click_round)
    return ()


def auto_unlimited_lineup(gifts_qty=300):
    # 无限池抽奖，自动重置
    # 通过检查重置按钮颜色，判断是否需要重置。
    # 但无法考虑额外的10%点击次数
    gifts_round = int(gifts_qty / 10)
    # 每次点击大约2秒钟左右 (WAITING_SECOND + pyautogui.PAUSE)
    print("Need around", int(round(gifts_round * 4 * (WAITING_SECOND + pyautogui.PAUSE) / 60, 60)), "Minutes.")
    for i in range(gifts_round, 0, -1):
        if not (same_color(POS_UNLIMITED_LINEUP_BUTTON, COLOR_UNLIMITED_LINEUP_BUTTON)):
            if same_color(POS_UNLIMITED_LINEUP_RESET, COLOR_UNLIMITED_LINEUP_RESET):
                pyautogui.click(POS_UNLIMITED_LINEUP_RESET)
                pyautogui.time.sleep(WAITING_SECOND)
                pyautogui.click(POS_UNLIMITED_LINEUP_RESET_CONFIRM)
                pyautogui.time.sleep(WAITING_SECOND)
                pyautogui.click(POS_UNLIMITED_LINEUP_RESET_CONFIRM)
                pyautogui.time.sleep(WAITING_SECOND)
        repeat_click1(POS_UNLIMITED_LINEUP_BUTTON, 4)
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
        pyautogui.click(POS_MASTER_SKILLS[skill])
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


def auto_attack_one_turn(max_card=5, max_red=3, max_blue=3, max_green=3):
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
        if len(red_cards) >= max_red:
            choose_attack_cards(red_cards[0:3])
        elif len(blue_cards) >= max_blue:
            choose_attack_cards(blue_cards[0:3])
        elif len(green_cards) >= max_green:
            choose_attack_cards(green_cards[0:3])
        elif len(red_cards) == 2:
            choose_attack_cards((red_cards[0:1] + blue_cards + green_cards)[0:2] + red_cards[1:2])
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
        for i in range(cards_round, 0, -1):
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
    repeat_click1(POS_BATTLE_END_BUTTON, 5)
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
    repeat_click1(POS_BATTLE_END_BUTTON, 5)
    return ()


def auto_battle(max_turns=3, max_red=3, max_blue=3, max_green=3):
    for i in range(0, max_turns):
        print("turn:", i + 1)
        auto_attack_one_turn(max_card=5, max_red=max_red, max_blue=max_blue, max_green=max_green)
        pyautogui.time.sleep(20)
        # normal 15~20 second is ok, but if enemy NP, or servant died, need longer time
        new_attack_active = same_color(POS_ATTACK_BUTTON, COLOR_ATTACK_BUTTON)
        battle_end_active = same_color(POS_BATTLE_END, COLOR_BATTLE_END)
        # 只用颜色判断条件很容易死循环，加入循环次数判断，等待时间最多延长3次
        wait = 3
        while (not new_attack_active) and (not battle_end_active) and (wait > 0):
            pyautogui.time.sleep(10)
            print("  wait:", wait)
            wait = wait - 1
            new_attack_active = same_color(POS_ATTACK_BUTTON, COLOR_ATTACK_BUTTON)
            battle_end_active = same_color(POS_BATTLE_END, COLOR_BATTLE_END)
            print()
        # 判断是否完毕
        if battle_end_active:
            break
    return ()


def christmas_2016_10ap():
    if same_color(POS_BATTLE_BEGIN_BUTTON, COLOR_BATTLE_BEGIN_BUTTON):
        pyautogui.click(POS_BATTLE_BEGIN_BUTTON)
        pyautogui.time.sleep(25)
    auto_battle(max_turns=12, max_red=3, max_blue=4, max_green=4)
    repeat_click1(POS_BATTLE_END_BUTTON, 3, 3)
    return ()


def christmas_2016_20ap():
    if same_color(POS_BATTLE_BEGIN_BUTTON, COLOR_BATTLE_BEGIN_BUTTON):
        pyautogui.click(POS_BATTLE_BEGIN_BUTTON)
        pyautogui.time.sleep(25)
    auto_battle(max_turns=5, max_red=3, max_blue=3, max_green=4)
    return ()


# Main Program
# Switch to FGO window
pyautogui.hotkey('alt', 'tab')
pyautogui.time.sleep(BUFFER_SECOND)
# Log start time
print(time.strftime("%Y-%m-%d %H:%M:%S\n", time.localtime()))

# check the default value of FGO window
win_fgo = pyautogui.getWindow('ApowerMirror Main')
X = win_fgo.get_position()[0] - X_DEFAULT
Y = win_fgo.get_position()[1] - Y_DEFAULT

# 友情点召唤
# friend_point_summon(cards_qty=140)

# 圣诞节活动
# 圣诞节无限池抽奖，每池500礼物
# unlimited_lineup(gifts_qty=400)

# 圣诞2016复刻
# christmas_2016_10ap()
christmas_2016_20ap()


# 通用无脑进攻
# auto_battle(max_turns=6, max_red=3, max_blue=3, max_green=3)

# 通用最后一回合，
# common_last_turn()

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
