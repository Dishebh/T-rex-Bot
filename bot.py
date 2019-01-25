from typing import Tuple

from PIL import ImageGrab, ImageOps
import pyautogui
import time
from numpy import *

class Cordinates():
    replayBtn = (340,390)
    dinosaur = (171, 395)

def restartGame():
    pyautogui.click(Cordinates.replayBtn)

def pressSpace():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    print("Jump")
    pyautogui.keyUp('space')

def imageGrab():
    box = (Cordinates.dinosaur[0]+60, Cordinates.dinosaur[1], Cordinates.dinosaur[0]+150, Cordinates.dinosaur[1]+100)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    print(a.sum())

def main():
    restartGame()
    while True:
        if(imageGrab() != 9338):
            pressSpace()
            time.sleep(0.1)

main()

