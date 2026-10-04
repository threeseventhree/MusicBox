from machine import Pin, I2C # type: ignore
from time import sleep
import ssd1306 # type: ignore
from src.display import refreshMenu

button1 = Pin(19, Pin.IN, Pin.PULL_UP)
button2 = Pin(18, Pin.IN, Pin.PULL_UP)
button3 = Pin(17, Pin.IN, Pin.PULL_UP)
width = 128
height = 64
fontSize = 8
yOffset = 8
cursorPos = 0
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400000)
display = ssd1306.SSD1306_I2C(width, height, i2c)

menu = ["Recognize", "Spotify", "Settings"]

refreshMenu(menu, cursorPos, display)
# void loop
while True:
    if not button1.value():
        print("Button 1 - Enter")

    if not button2.value():
        cursorPos += 1
        if cursorPos >= len(menu):
            cursorPos = 0
        refreshMenu(menu, cursorPos, display)

    if not button3.value():
        print("Button 3 - Back")

    sleep(0.1)
