#automate opening of Fuse emulator
import pyautogui
import time
#pause 2.5 seconds between commands
pyautogui.PAUSE = 0.5
#turn failsafe on so we can abort program by moving mouse to corner of screen
pyautogui.FAILSAFE = True
#get main monitor size
screenWidth, screenHeight = pyautogui.size()
#minimize all windows
pyautogui.hotkey('win', 'd')
#move mouse to Fuse icon and double click
pyautogui.moveTo(200, 150, 0.5)
pyautogui.doubleClick()
time.sleep(10) # allow time for Fuse to open
pyautogui.press('f3')
time.sleep(10)
pyautogui.PAUSE = 5
#find and open the right file
mouseX, mouseY = pyautogui.locateCenterOnScreen('fileName.PNG', confidence=0.8)
pyautogui.PAUSE = 0.5
pyautogui.moveTo(mouseX, mouseY, 0.5)
pyautogui.PAUSE = 15
pyautogui.doubleClick()
#below is an crude way of choosing the game options
#the Zx spectrum wasn't quick to register keys so we need to hold them for a second
pyautogui.PAUSE = 1
pyautogui.keyDown('s')
pyautogui.PAUSE = 5
pyautogui.keyUp('s')
print('S key pressed')
pyautogui.PAUSE = 1
pyautogui.keyDown('1')
pyautogui.PAUSE = 4
pyautogui.keyUp('1')
print('1 key pressed')
pyautogui.PAUSE = 1
pyautogui.keyDown('m')
pyautogui.keyUp('m')


