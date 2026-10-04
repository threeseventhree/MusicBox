from machine import Pin, I2C # type: ignore
from time import sleep
import ssd1306 # type: ignore

button1 = Pin(19, Pin.IN, Pin.PULL_UP)
button2 = Pin(18, Pin.IN, Pin.PULL_UP)
button3 = Pin(17, Pin.IN, Pin.PULL_UP)

i2c = I2C(
    0,
    scl=Pin(22),
    sda=Pin(21),
    freq=400000
)
# void setup
display = ssd1306.SSD1306_I2C(128, 64, i2c)

display.text("MUSICBOX", 0, 0)
display.show()
# void loop
while True:
    if not button1.value():
        print("Button 1 - Recognize")

    if not button2.value():
        print("Button 2 - Spotify")

    if not button3.value():
        print("Button 3 - Settings")

    sleep(0.1)
