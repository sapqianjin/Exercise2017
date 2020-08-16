#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Dorian Wang 2018.01.20
# test send keyboard and mouse to android emulators  window

import time
import pyautogui
import win32com, win32api, win32con, win32gui
import ctypes
import win32com.client

# # win32com SendKeys
# # unavailable, the window is active, but the key cannot be sent.
# # Switch to FGO window
# pyautogui.hotkey('alt', 'tab')
# pyautogui.time.sleep(3)
# pyautogui.click(800,400)
# pyautogui.click(1000,500)
# pyautogui.click(1200,600)



# win32com SendKeys

# # test for win32com, run new program
# shell = win32com.client.Dispatch('WScript.Shell')
# shell.Run("notepad")
# time.sleep(0.1)
# shell.SendKeys("Hello Word", 0)
# shell.SendKeys('{Enter}', 0)
# shell.SendKeys('{F5}', 0)
# # OK
#
# # test for win32com, active exist program
# shell = win32com.client.Dispatch('WScript.Shell')
# shell.AppActivate('Untitled - Notepad')
# shell.SendKeys("Hello Word", 0)
# shell.SendKeys('{Enter}', 0)
# shell.SendKeys('{F5}', 0)
# # OK


# test for win32api, active exist program, send mouse move and click
def clickLeft(x, y):
    # The win32api.SetCursorPos((x, y))  cannot be execute in Android, so change it to:
    # ctypes.windll.user32.SetCursorPos(x, y), it's could be execute without error, but still not work.
    # win32api.SetCursorPos((x, y))  # 将鼠标移动到x,y 的位置
    ctypes.windll.user32.SetCursorPos(x, y)
    # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)  # 驱动鼠标左击按下
    ctypes.windll.user32.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)  # 驱动鼠标左击按下
    time.sleep(1)  # in term of seconds
    # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)  # 驱动鼠标左击提起，点击完成
    ctypes.windll.user32.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)  # 驱动鼠标左击提起，点击完成
    time.sleep(1)


def clickRight(x, y):
    ctypes.windll.user32.SetCursorPos(x, y)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, x, y, 0, 0)
    time.sleep(1)  # in term of seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, x, y, 0, 0)
    time.sleep(1)


shell = win32com.client.Dispatch('WScript.Shell')
flags, hcursor, (x,y) = win32gui.GetCursorInfo() # x, y 就是当前鼠标的位置
print(x,y)

# shell.AppActivate('Untitled - Notepad')
# clickLeft(414,156)
# clickRight(414,156)
# # OK

shell.AppActivate('FGO_BiliBili')
clickLeft(414,156)
clickRight(414,156)
# Doesn't work in Android Simulator.



# import time
# import win32con
# import win32api
# import win32gui
# import win32process
#
# _, cmd = win32api.FindExecutable('notepad')
#
# _, _, pid, tid = win32process.CreateProcess(
#     None,    # name
#     cmd,     # command line
#     None,    # process attributes
#     None,    # thread attributes
#     0,       # inheritance flag
#     0,       # creation flag
#     None,    # new environment
#     None,    # current directory
#     win32process.STARTUPINFO ())
#
# # wcallb is callback for EnumThreadWindows and
# # EnumChildWindows. It populates the dict 'handle' with
# # references by class name for each window and child
# # window of the given thread ID.
#
# def wcallb(hwnd, handle):
#     handle[win32gui.GetClassName(hwnd)] = hwnd
#     win32gui.EnumChildWindows(hwnd, wcallb, handle)
#     return True
#
# handle = {}
# while not handle:   # loop until the window is loaded
#     time.sleep(0.1)
#     win32gui.EnumThreadWindows(tid, wcallb, handle)
#
# # Sending normal characters is a WM_CHAR message.
# # Function keys are sent as WM_KEYDOWN and WM_KEYUP
# # messages using the virtual keys defined in win32con,
# # such as VK_F5 for the f5 key.
# #
# # Notepad has a separate 'Edit' window to which you can
# # write, but function keys are processed by the main
# # window.
#
# for c in "Hello World\n":
#     win32api.PostMessage(
#         handle['Edit'],
#         win32con.WM_CHAR,
#         ord(c),
#         0)
#
# win32api.PostMessage(
#     handle['Notepad'],
#     win32con.WM_KEYDOWN,
#     win32con.VK_F5,
#     0)
# win32api.PostMessage(
#     handle['Notepad'],
#     win32con.WM_KEYUP,
#     win32con.VK_F5,
#     0)
#
# # SendMessage waits for a response, but PostMessage
# # queues the message and returns immediately