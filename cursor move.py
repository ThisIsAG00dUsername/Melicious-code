import pyautogui
import random
pyautogui.FALSESAFE=False
while True:
  n1=random.randint(0,1920)
  n2=random.randint(0,1080)
  pyautogui.moveTo(n1,n2)
  pyautogui.click()
