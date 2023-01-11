import random
import time
import mouse
import pyautogui

delay = 3

for i in range(99999999):
    time.sleep(random.uniform(0.1, 0.11))

    if random.random() < 0.8:
        mouse.click(button="left")
        pyautogui.keyDown("a")
        pyautogui.sleep(delay)
        pyautogui.keyUp("a")
    else:
        mouse.click(button="left")

        pyautogui.keyDown("d")
        pyautogui.sleep(delay)
        pyautogui.keyUp("d")