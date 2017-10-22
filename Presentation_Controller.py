from bluedot import BlueDot
from signal import pause
import keyboard
import subprocess

def controller(pos):
    if pos.top:
        print("Present From Current Slide")
        keyboard.press_and_release('shift+f5')
    elif pos.bottom:
        print("Exit Presentation")
        keyboard.press_and_release('esc')
    elif pos.left:
        print("Previous Slide")
        keyboard.press_and_release('left')
    elif pos.right:
        print("Next Slide")
        keyboard.press_and_release('right')
    elif pos.middle:
        print("Present From Start")
        keyboard.press_and_release('f5')

def audio_control(pos):
    percentage = round(pos.distance * 100, 2)
    print("{}%".format(percentage))
    #Change Master to PCM for Pi audio
    subprocess.call(["amixer", "set", "Master", str(percentage)])

bd = BlueDot()
bd.when_pressed = controller
bd.when_moved = audio_control
pause()
