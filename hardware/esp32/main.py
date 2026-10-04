from machine import Pin # type: ignore
from time import sleep
from src.display import DisplayHandler
from src.menu import handleMenuScreen
from src.recognize import handleRecognizeScreen

button1 = Pin(19, Pin.IN, Pin.PULL_UP)
button2 = Pin(18, Pin.IN, Pin.PULL_UP)
button3 = Pin(17, Pin.IN, Pin.PULL_UP)
cursorPos = 0
displayHandler = DisplayHandler()
screens = ["recognize", "spotify", "settings"]
screen = "menu"
menu = ["Recognize", "Spotify", "Settings"]

def waitForRelease(button):
    while not button.value():
        sleep(0.01)

handleMenuScreen(menu, displayHandler, cursorPos)
# void loop
while True:
    if not button1.value():
        if(cursorPos == 0):
            handleRecognizeScreen(displayHandler)
            screen = screens[0]
        waitForRelease(button1)

    if not button2.value():
        cursorPos += 1
        if cursorPos >= len(menu): cursorPos = 0
        handleMenuScreen(menu, displayHandler, cursorPos)
        waitForRelease(button2)

    if not button3.value():
        if(screen != "menu"):
            handleMenuScreen(menu, displayHandler, cursorPos)
            screen = "menu"
        waitForRelease(button3)
