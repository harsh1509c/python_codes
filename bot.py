##### PIANO AUTO BOT #####

from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

# Title 1 Position : X:  428 Y:  780
# Title 2 Position : X:  534 Y:  780
# Title 3 Position : X:  661 Y:  780
# Title 4 Position : X:  782 Y:  780

# to perform a click
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)  # this pause the script for 0.01 second
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    
while keyboard.is_pressed('q') == False:

    if pyautogui.pixel(428,780)[0] == 0:
        click(428,780)
    if pyautogui.pixel(534,780)[0] == 0:
        click(534,780)
    if pyautogui.pixel(661,780)[0] == 0:
        click(661,780)
    if pyautogui.pixel(782,780)[0] == 0:
        click(782,780)