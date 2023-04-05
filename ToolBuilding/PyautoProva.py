import pyautogui
from time import sleep


pyautogui.hotkey("win")
sleep(1)
pyautogui.typewrite("cmd")
sleep(1)
pyautogui.hotkey("enter")
sleep(1)
pyautogui.typewrite("netsh wlan show profile")
sleep(1)
pyautogui.hotkey("enter")
sleep(3)
screen = pyautogui.screenshot()
screen.save("C:/Users/Mattia Palmucci/Desktop/Prova2.png")
sleep(2)
pyautogui.hotkey("alt","f4")
