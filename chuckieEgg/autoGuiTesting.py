#automate opening of Fuse emulator and starting game
#messy code
#it'll find and walk to the egg on the same level
#Switching to openCV though to follow a normal approach
import pyautogui
import cv2 as cv
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
time.sleep(6) # allow time for Fuse to open
fuseWindow = pyautogui.locateOnScreen('fuseWindow.PNG', confidence=0.9)#quicker searching later if only searching window
pyautogui.press('f3')
time.sleep(3)
pyautogui.PAUSE = 5
#find and open the right file
mouseX, mouseY = pyautogui.locateCenterOnScreen('fileName.PNG', region=fuseWindow, confidence=0.8)
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
pyautogui.PAUSE = 1
pyautogui.keyDown('1')
pyautogui.PAUSE = 4
pyautogui.keyUp('1')
pyautogui.PAUSE = 0.5
#find all the eggs on screen
eggLocations = list(pyautogui.locateAllOnScreen('egg.PNG', region=fuseWindow, confidence=0.9))
playerLocationX, playerLocationY = pyautogui.locateCenterOnScreen('player.PNG', region=fuseWindow, confidence=0.9)
eggLocationsCenter = []
for egg in eggLocations:
    eggLocationsCenter.append(pyautogui.center(egg))
#point to the eggs
#for location in eggLocationsCenter:
#    x, y = location
#    pyautogui.moveTo(x, y, 0.25)
#point to the player
#pyautogui.moveTo(playerLocationX, playerLocationY, 0.25)
#
###### MAIN PART of finding eggs####
#Loop while there's eggs in the list
while len(eggLocationsCenter) > 0:
    for egg in eggLocationsCenter:
        x, y = egg
        if playerLocationY < y + 50 and playerLocationY > y - 50:
            if x - playerLocationX < 0:
                pyautogui.keyDown('9')
                playerLocationX -= 32
                print('Egg X : ', x)
                print('player X :', playerLocationX)
            #elif x - playerLocationX < 10 and x - playerLocationX > -10:
            elif x - playerLocationX > 0:
                pyautogui.keyUp('9')
                eggLocations.pop(egg)
            
