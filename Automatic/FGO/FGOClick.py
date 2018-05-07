#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Dorian Wang 2017.11.21~2017.11.24
# Auto Click FGO
# add to GitHub
# 2017.12.09: rename all var and function name.
# todo background click window?
# ApowerMirror 1.2.6 is OK, but the 1.2.7 is not available.

import pyautogui
import time
import random
import winsound

BUFFER_SECOND = 1
WAITING_SECOND = 1
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True
width, height = pyautogui.size()
# Default position and color of ApowerMirror FGO window
X_DEFAULT = 240
Y_DEFAULT = 154
X = -70
Y = 0
# Define Random Range for small div
POS_RANGE = 5
TIME_RANGE = 1
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
POS_ATTACK_CARDS = ((), (X + 440, Y + 900), (X + 815, Y + 900), (X + 1175, Y + 900), (X + 1545, Y + 900), (X + 1920, Y + 900), (X + 1020, Y + 620), (X + 1355, Y + 620), (X + 1525, Y + 620))
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
COLOR_BATTLE_BEGIN_BUTTON = (191, 197, 198)
COLOR_BATTLE_END_ASCEND = (0, 1, 0)
COLOR_BATTLE_END = (8, 5, 3)
COLOR_UNLIMITED_LINEUP_BUTTON = (21, 202, 243)
COLOR_UNLIMITED_LINEUP_RESET = (138, 175, 223)


def same_color(position, color):
    # 按钮颜色难以完全一致，所以定义RGB色差之和在10以内均为OK
    color_position = pyautogui.screenshot().getpixel(position)
    color_different = 0
    for i in range(0, 3):
        color_different = color_different + (color_position[i] - color[i])
    if abs(color_different) < 10:
        print(color_position, "active.")
        return True
    else:
        print(color_position, "inactive.")
        return False


def card_color(card):
    color_card = pyautogui.screenshot().getpixel(POS_ATTACK_CARDS[card])
    # print('The card', card, 'color is', color_card)
    if color_card[0] > 100:
        # print('RED')
        return ('RED')
    elif color_card[1] > 100:
        # print('GREEN')
        return ('GREEN')
    else:
        # print('BLUE')
        return ('BLUE')


def click_around(postion):
    # 避免每次精确点击同一像素
    pos_div = random.randint(-POS_RANGE, POS_RANGE)
    pyautogui.click(postion[0] + pos_div, postion[1] + pos_div)
    return ()


def sleep_around(time_sleep):
    # 避免每次精确等待相同时间
    time_div = random.randrange(0, TIME_RANGE)
    pyautogui.time.sleep(time_sleep + time_div)
    return ()


def repeat_click1(position, repeat=1, waiting_time=WAITING_SECOND):
    # 单个位置重复点击
    try:
        for i in range(repeat, 0, -1):
            # 发现模拟器窗口无法点击，也无法按键切换回去
            # 只能使用Apower Mirror，测试OK
            click_around(position)
            print(i, time.strftime("%H:%M:%S", time.localtime()))
            sleep_around(waiting_time)
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
    # 每次点击大约3秒钟左右 (WAITING_SECOND + time_div + pyautogui.PAUSE)
    print("Need around", int(round(click_round * (WAITING_SECOND + TIME_RANGE / 2 + pyautogui.PAUSE) / 60, 60)), "Minutes.")
    repeat_click1(POS_UNLIMITED_LINEUP_BUTTON, click_round)
    return ()


def auto_unlimited_lineup(gifts_qty=300):
    # 无限池抽奖，自动重置
    # 通过检查重置按钮颜色，判断是否需要重置。
    # 但无法考虑额外的10%点击次数
    gifts_round = int(gifts_qty / 10)
    # 每次点击大约2秒钟左右 (WAITING_SECOND + pyautogui.PAUSE)
    print("Need around", int(round(gifts_round * 4 * (WAITING_SECOND + TIME_RANGE / 2 + pyautogui.PAUSE) / 60, 60)), "Minutes.")
    for i in range(gifts_round, 0, -1):
        if not (same_color(POS_UNLIMITED_LINEUP_BUTTON, COLOR_UNLIMITED_LINEUP_BUTTON)):
            if same_color(POS_UNLIMITED_LINEUP_RESET, COLOR_UNLIMITED_LINEUP_RESET):
                click_around(POS_UNLIMITED_LINEUP_RESET)
                sleep_around(WAITING_SECOND)
                click_around(POS_UNLIMITED_LINEUP_RESET_CONFIRM)
                sleep_around(WAITING_SECOND)
                click_around(POS_UNLIMITED_LINEUP_RESET_CONFIRM)
                sleep_around(WAITING_SECOND)
        repeat_click1(POS_UNLIMITED_LINEUP_BUTTON, 4)
    return ()


def buffer_confirm(target=0):
    # confirm buffer
    # the confirm is already disable in game menu
    # click_around(POS_BUFFER_CONFIRM)
    # choose target servant
    if target != 0:
        click_around(POS_BUFFER_TARGETS[target])
    # waiting for result
    sleep_around(3)
    return ()


def choose_enemy(target=3):
    try:
        # click enemy
        if target != 0:
            click_around(POS_ENEMY[target])
    except KeyboardInterrupt:
        print('User Break.')
    return ()


def servant_skill(servant, skill, target=0):
    # 从者技能(buff)释放
    # 需要指定目标则输入target参数
    try:
        # choose buffer
        click_around(POS_SERVANT_SKILLS[servant][skill])
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
        click_around(POS_MASTER_SKILL_BUTTON)
        # choose skill
        click_around(POS_MASTER_SKILLS[skill])
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
            click_around(POS_ATTACK_CARDS[card])
    except KeyboardInterrupt:
        print('User Break.')
    return ()


def fix_attack_one_turn(cards):
    # 战斗界面选择
    try:
        # open attack screen
        click_around(POS_ATTACK_BUTTON)
        sleep_around(3)
        choose_attack_cards(cards)
    except KeyboardInterrupt:
        print('User Break.')
    return ()


def get_cards(max_card=5):
    red_cards = []
    blue_cards = []
    green_cards = []
    for card in range(1, max_card + 1):
        # pyautogui.moveTo(POS_ATTACK_CARDS[card])
        # sleep_around(1)
        #  这里可以考虑改进，因为如果是绿、蓝卡，card_color会被调用两次。
        if card_color(card) == 'RED':
            red_cards.append(card)
        elif card_color(card) == 'GREEN':
            green_cards.append(card)
        else:
            blue_cards.append(card)
    return (red_cards, blue_cards, green_cards)


def auto_attack_one_turn(max_card=5, max_red=3, max_blue=3, max_green=3):
    # 自动战斗，按照红-蓝-绿颜色优先次序
    # 普通攻击抽卡无非以下几种情况：红≥3；蓝≥3；绿≥3；红2蓝≥1绿≥1；红1蓝≥1绿≥1；
    try:
        # open attack screen
        click_around(POS_ATTACK_BUTTON)
        sleep_around(3)
        (red_cards, blue_cards, green_cards) = get_cards(max_card=5)
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


def battle_begin():
    # print("POS_BATTLE_BEGIN_BUTTON",POS_BATTLE_BEGIN_BUTTON)
    # print("COLOR_BATTLE_BEGIN_BUTTON",COLOR_BATTLE_BEGIN_BUTTON)
    print("now check battle begin or continue:")
    print("attack button ", end="")
    new_attack_active = same_color(POS_ATTACK_BUTTON, COLOR_ATTACK_BUTTON)
    print("battle begin ", end="")
    battle_begin_active = same_color(POS_BATTLE_BEGIN_BUTTON, COLOR_BATTLE_BEGIN_BUTTON)
    # 有时会出现既不在开始画面，又不在战斗画面的情况，加入等待3次*10秒的机制
    wait = 3
    while (not new_attack_active) and (not battle_begin_active) and (wait > 0):
        sleep_around(10)
        print("  wait:", wait)
        wait = wait - 1
        new_attack_active = same_color(POS_ATTACK_BUTTON, COLOR_ATTACK_BUTTON)
        battle_begin_active = same_color(POS_BATTLE_BEGIN_BUTTON, COLOR_BATTLE_BEGIN_BUTTON)
        print()
    if battle_begin_active:
        print("battle_begin.")
        click_around(POS_BATTLE_BEGIN_BUTTON)
        sleep_around(25)
    return ()


def battle_end():
    sleep_around(20)
    print("now check battle end or not:")
    # normal 15~20 second is ok, but if enemy NP, or servant died, need longer time
    print("attack ", end="")
    new_attack_active = same_color(POS_ATTACK_BUTTON, COLOR_ATTACK_BUTTON)
    print("battle end ", end="")
    battle_end_active = same_color(POS_BATTLE_END, COLOR_BATTLE_END)
    print("ascend level up ", end="")
    battle_end_ascend_active = same_color(POS_BATTLE_END, COLOR_BATTLE_END_ASCEND)
    # 只用颜色判断条件很容易死循环，加入循环次数判断，等待时间最多延长3次
    wait = 3
    while (not new_attack_active) and (not battle_end_ascend_active) and (not battle_end_active) and (wait > 0):
        sleep_around(10)
        print("  wait:", wait)
        wait = wait - 1
        print("attack ", end="")
        new_attack_active = same_color(POS_ATTACK_BUTTON, COLOR_ATTACK_BUTTON)
        print("battle end ", end="")
        battle_end_active = same_color(POS_BATTLE_END, COLOR_BATTLE_END)
        print("ascend level up ", end="")
        battle_end_ascend_active = same_color(POS_BATTLE_END, COLOR_BATTLE_END_ASCEND)
        print()
    # 判断是否完毕
    if battle_end_active or battle_end_ascend_active:
        print("battle_end_active")
        repeat_click1(POS_BATTLE_END_BUTTON, repeat=3, waiting_time=3)
        winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
        return True
    else:
        return False


def friend_point_summon(cards_qty=10):
    # 友情点召唤
    try:
        cards_round = int(cards_qty / 10)
        # 每次点击大约10秒钟左右 (4 +2 + 4 * pyautogui.PAUSE)
        # 每次sleep_around大约要增加1秒，+2
        print("Need around", int(round(cards_round * (4 + TIME_RANGE + 4 * pyautogui.PAUSE) / 60, 60)), "Minutes.")
        for i in range(cards_round, 0, -1):
            # click summon button
            click_around(POS_SUMMON_END_BUTTON)
            # select summon 10 cards
            click_around(POS_SUMMON_TEN_BUTTON)
            # confirm summon
            click_around(POS_SUMMON_TEN_BUTTON)
            # waiting for result
            sleep_around(3)
            # click to finish summon
            click_around(POS_SUMMON_END_BUTTON)
            sleep_around(1)
            print(i, time.strftime("%H:%M:%S", time.localtime()))
        print('Done.')
        # Log end time
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    except KeyboardInterrupt:
        print('User Break.')
    return ()


def auto_battle(max_turns=3, max_red=3, max_blue=3, max_green=3):
    for i in range(0, max_turns):
        print("turn:", i + 1)
        auto_attack_one_turn(max_card=5, max_red=max_red, max_blue=max_blue, max_green=max_green)
        if battle_end():
            print("battle_end, exit.")
            break
    return ()


def auto_battle_with_buffer(max_turns=9, max_red=3, max_blue=3, max_green=3):
    for i in range(1, max_turns + 1):
        print("turn:", i)
        if i == 1:
            servant_skill(1, 1)  # Jeanne Alter: +ATK
            # servant_skill(1, 2)  # Jeanne Alter: +ALL ATK
            servant_skill(1, 3)  # Jeanne Alter: +Critical ATK
            # servant_skill(2, 1)  # Artila +ALL NP ATK
            servant_skill(2, 2)  # Artila +ATK
            servant_skill(2, 3)  # Artila +Critical
            # 孔明技能1需要依照实际情况调整目标，默认Artila
            servant_skill(3, 1, 2)  # Kong Ming: +NP
            servant_skill(3, 2)  # Kong Ming: +ALL NP+Def
            servant_skill(3, 3)  # Kong Ming: +ALL NP+ATK
            auto_attack_one_turn(max_card=5, max_red=max_red, max_blue=max_blue, max_green=max_green)
        elif i == 8:
            servant_skill(1, 1)  # Jeanne Alter: +ATK
            servant_skill(1, 2, 1)  # Jeanne Alter: +ALL ATK
            servant_skill(1, 3)  # Jeanne Alter: +Critical ATK
            # servant_skill(2, 1)  # Artila +ALL NP ATK
            servant_skill(2, 2)  # Artila +ATK
            servant_skill(2, 3)  # Artila +Critical
            # 孔明技能1需要依照实际情况调整目标，默认Artila
            servant_skill(3, 1, 2)  # Kong Ming: +NP
            servant_skill(3, 2)  # Kong Ming: +ALL NP+Def
            servant_skill(3, 3)  # Kong Ming: +ALL NP+ATK
            master_skill(1, 0)  # +ALL ATK
            click_around(POS_ATTACK_BUTTON)
            sleep_around(3)
            if card_color(8) == 'BLUE':
                print([8, 7, 6])
                choose_attack_cards([8, 7, 6])
            else:
                (red_cards, blue_cards, green_cards) = get_cards(max_card=5)
                print((red_cards + blue_cards + green_cards)[0:1] + [7, 6])
                choose_attack_cards((red_cards + blue_cards + green_cards)[0:1] + [7, 6])
        else:
            auto_attack_one_turn(max_card=5, max_red=max_red, max_blue=max_blue, max_green=max_green)
        if battle_end():
            print("battle_end, exit.")
            break
    return ()


def daily_40ap():
    # Jeanne, Artila, Kong Ming
    battle_begin()
    auto_battle_with_buffer(max_turns=12, max_red=3, max_blue=3, max_green=3)
    return ()


def QP_40ap():
    # Jeanne, Artila, Rider
    battle_begin()
    auto_battle_with_buffer(max_turns=12, max_red=3, max_blue=3, max_green=3)


def GUDAGUDA_Honnoji_40ap(max_turns=12, max_red=3, max_blue=3, max_green=3):
    battle_begin()
    for i in range(1, max_turns + 1):
        print("turn:", i)
        if i == 1:
            servant_skill(1, 1)  #
            # 孔明技能1需要依照实际情况调整目标，默认2
            # servant_skill(3, 1, 2)  # Kong Ming: +NP
            # servant_skill(3, 2)  # Kong Ming: +ALL NP+Def
            # servant_skill(3, 3)  # Kong Ming: +ALL NP+ATK
            auto_attack_one_turn(max_card=5, max_red=max_red, max_blue=max_blue, max_green=max_green)
        elif i == 9:
            choose_enemy(2)
            servant_skill(1, 1)  #
            servant_skill(1, 2)  #
            servant_skill(1, 3)  #
            servant_skill(2, 1)  #
            servant_skill(2, 2)  #
            # servant_skill(2, 3)  #
            # servant_skill(3, 1)  #
            # servant_skill(3, 2)  #
            # servant_skill(3, 3)  #
            master_skill(1, 0)  # +ALL ATK
            click_around(POS_ATTACK_BUTTON)
            sleep_around(3)
            if card_color(7) == 'RED' and card_color(8) == "GREEN":
                # print([8, 6, 7])
                choose_attack_cards([8, 6, 7])
            elif card_color(8) == 'GREEN':
                (red_cards, blue_cards, green_cards) = get_cards(max_card=5)
                # print((red_cards + blue_cards + green_cards)[0:1] + [8, 6])
                choose_attack_cards((red_cards + blue_cards + green_cards)[0:1] + [8, 6])
            else:
                (red_cards, blue_cards, green_cards) = get_cards(max_card=5)
                # print((red_cards + blue_cards + green_cards)[0:2] + [6])
                choose_attack_cards((red_cards + blue_cards + green_cards)[0:2] + [6])
        else:
            auto_attack_one_turn(max_card=5, max_red=max_red, max_blue=max_blue, max_green=max_green)
        if battle_end():
            print("battle_end, exit.")
            break
    pass


# Main Program
# Switch to FGO window
pyautogui.hotkey('alt', 'tab')
sleep_around(BUFFER_SECOND)
# Log start time
print(time.strftime("%Y-%m-%d %H:%M:%S\n", time.localtime()))

# check the default value of FGO window
win_fgo = pyautogui.getWindow('ApowerMirror Main')
X = win_fgo.get_position()[0] - X_DEFAULT
print("X=", X)
X = -70
print("X=", X)
Y = win_fgo.get_position()[1] - Y_DEFAULT
print("Y=", Y)

# 友情点召唤
# friend_point_summon(cards_qty=100)

# 每日任务
# daily_40ap()
# QP_40ap()

GUDAGUDA_Honnoji_40ap()

# Already DONE.

# 圣诞节活动
# 圣诞节无限池抽奖，每池400礼物
# unlimited_lineup(gifts_qty=100)

# 尼禄祭活动
# 尼禄祭无限池抽奖，每池300礼物
# unlimited_lineup(gifts_qty=300)

# Switch back to Python window, so user could know the program is finished.
pyautogui.hotkey('alt', 'tab')
