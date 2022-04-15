import keyboard
import pyautogui as pa

def foo():
    ##   pa.press(i,0.025)
    pa.write('2000004090012')
    pa.press('enter')

keyboard.add_hotkey('1', foo)

keyboard.wait('Ctrl + Q')