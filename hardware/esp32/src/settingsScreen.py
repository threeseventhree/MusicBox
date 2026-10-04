from src.display import DisplayHandler
class SettingsScreen:
    def __init__(self, displayHandler: DisplayHandler):
        self.displayHandler = displayHandler
        self.cursorPos = 0
        self.options = ["Information"]

    def show(self):
        self.displayHandler.fill(0)
        self.displayHandler.centerText("Settings", 0)
        self.displayHandler.displayParamsList(self.options, self.cursorPos)
        self.displayHandler.show()

    def scroll(self):
        self.cursorPos += 1
        if self.cursorPos >= len(self.options): self.cursorPos = 0
        self.show()
