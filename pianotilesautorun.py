from pyautogui import*
import pyautogui as auto
import time
import keyboard
import random
import pyautogui
import win32api, win32con



def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep (0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)




#(x=779, y=556)
#(x=881, y=553)
#(x=1014, y=548)
#(x=1148, y=554)

while keyboard.is_pressed("q") == False:
        
    


    if pyautogui.pixel(779, 600) [0] == 0:
             click(779, 600)


    if pyautogui.pixel(881,600) [0] == 0:
             click(881, 600)

        
    if pyautogui.pixel(1014, 600) [0] == 0:
             click(1014, 600)


    if pyautogui.pixel(1148, 600) [0] == 0:
             click(1148, 600)



    
    
    
    
    
