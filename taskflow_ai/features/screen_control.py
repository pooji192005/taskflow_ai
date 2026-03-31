import pyautogui

def move(x, y):
    pyautogui.moveTo(x, y)

def click():
    pyautogui.click()

def type_text(text):
    pyautogui.write(text)

def press(key):
    pyautogui.press(key)