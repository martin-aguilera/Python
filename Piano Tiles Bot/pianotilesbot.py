from pyautogui import *
import pyautogui, time, keyboard, random, win32api, win32con


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.04)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


while keyboard.is_pressed("q") == False:

    if pyautogui.pixel(770, 700)[0] == 0:
        click(770, 700)

    if pyautogui.pixel(895, 700)[0] == 0:
        click(895, 700)

    if pyautogui.pixel(1020, 700)[0] == 0:
        click(1020, 700)

    if pyautogui.pixel(1140, 700)[0] == 0:
        click(1140, 700)
