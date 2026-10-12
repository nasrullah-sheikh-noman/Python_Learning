import pyautogui
from time import *

n = int(input("Enter a input: "))


sleep(4)
pyautogui.write(str(n))

for i in range(0,n+1):
  pyautogui.write("#" * i, interval=0.25)
  pyautogui.press("enter")