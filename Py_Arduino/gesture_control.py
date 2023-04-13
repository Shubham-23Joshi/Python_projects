import serial
import pyautogui
import time

Arduino_serial = serial.Serial('com7', 9600)
time.sleep(2)

while True:
    data = str(Arduino_serial.readline())
    print(data)

    if 'next' in data:
        pyautogui.hotkey('ctrl', 'pgdn')

    if 'previous' in data:
        pyautogui.hotkey('ctrl', 'pgup')

    if 'up' in data:
        pyautogui.scroll(100)
        #pyautogui.hotkey('up')
        pyautogui.hotkey('left')

    if 'down' in data:
        pyautogui.scroll(-100)
        pyautogui.hotkey('right')

    if 'change' in data:
        pyautogui.keyDown('alt')                   # performs "alt+tab" operation which switches the tab
        pyautogui.press('tab')
        pyautogui.keyUp('alt')

    