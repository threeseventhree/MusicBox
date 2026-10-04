from machine import Pin, I2C # type: ignore
import ssd1306 # type: ignore
class DisplayHandler():
    def __init__(self):
        self.width = 128
        self.height = 64
        self.fontSize = 8
        self.yOffset = 8
        self.i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400000)
        self.display = ssd1306.SSD1306_I2C(self.width, self.height, self.i2c)
        self.screens = ["recognize", "spotify", "settings"]
        self.screen = "menu"

    def centerText(self, text: str, y: int):
        length = len(text)
        lengthPixels = self.fontSize * length
        centerXPos = int(self.width / 2)
        x = centerXPos - int(lengthPixels / 2)
        self.display.text(text, x, y)

    def displayParamsList(self, params: list, cursorPos: int):
        for i, item in enumerate(params):
            y = self.yOffset * 2 + i * self.fontSize
            if i == cursorPos:
                self.display.text("> " + item, 0, y)
            else:
                self.display.text("  " + item, 0, y)
