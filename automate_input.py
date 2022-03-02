from pickletools import pyunicode
import pyautogui
import time

# print(pyautogui.size()) #1920 x 1080
#! Move to 3 dots and click for dropdown menu.
pyautogui.moveTo(1875, 120, .5) #Moves mouse to absolute position on screen.
# pyautogui.moveTo(1875, 215, .3)
pyautogui.click()

#! Click to pull up print dialogue
pyautogui.moveRel(0,95,.1) #moves mouse relative to last position.
pyautogui.click()

#! Move to print dialogue
pyautogui.moveTo(1125, 576, .5)

time.sleep(.3)
pyautogui.click()
time.sleep(10)
pyautogui.moveTo(1651, 209, .5)
pyautogui.click()



