"""
This code is made so you can skip youtube ads 
automatically. All you need to do is inform 
where the code and the image are located in
your PC (the "C:/Users/...") run the code
and start watching your videos. Of course, it
will not skip unskippable ads an you cant't
close it after you start runing it, or the code
will just stop working. To turn it off, just
drag your mouse to the top-left border of your
screen. Hope you like it!

"""

import pyautogui as pgui
import time
import os

os.chdir(input("Type the directory/path the code and the image are located: "))

pgui.FAILSAFE = True

position = pgui.position()
n = 0

while position != (0,0):
    try:
        pgui.moveTo(pgui.locateOnScreen('skip_button.png', grayscale=True, confidence=0.8))
        pgui.click()
        n += 1
        print("Skipped another one!")
    except:
        time.sleep(0.5)

    position = pgui.position()

print("In total, ", n, " ads were skipped. See you next time!")