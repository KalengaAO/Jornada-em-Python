#!/usr/bin/env python3

import pyautogui
import time

time.sleep(2)
pyautogui.click(100, 200)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(2)
pyautogui.write("Automação com python")
pyautogui.press("enter")
time.sleep(2)

for i in range(5):
	screenshot = pyautogui.screenshot()
	screenshot.save(f"captura_{i}.png")
	time.sleep(5)
