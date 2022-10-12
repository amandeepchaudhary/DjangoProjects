import pyautogui
import time

time.sleep(4)

count = 0

while count <= 1000:
    pyautogui.typewrite("bebe" + str(count))
    pyautogui.press("enter")
    count = count + 1
