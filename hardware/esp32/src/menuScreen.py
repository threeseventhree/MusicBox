from src.display import DisplayHandler
class MenuScreen:
    def __init__(self, displayHandler: DisplayHandler):
        self.displayHandler = displayHandler
        self.cursorPos = 0
        self.options = ["Recognize", "Spotify", "Settings"]
    def show(self):
            self.displayHandler.fill(0)
            self.displayHandler.centerText("MusicBox", 0)
            self.displayHandler.displayParamsList(self.options, self.cursorPos)
            self.displayHandler.show()
    
    def scroll(self):
        self.cursorPos += 1
        if self.cursorPos >= len(self.options): self.cursorPos = 0
        self.show()

    def enter(self):
        if self.cursorPos == 0:
            self.displayHandler.screen = "recognize"
        elif self.cursorPos == 1:
            self.displayHandler.screen = "spotify"
        elif self.cursorPos == 2:
            self.displayHandler.screen = "settings"
