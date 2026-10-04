from src.display import DisplayHandler
class RecognizeScreen:
    def __init__(self, displayHandler: DisplayHandler):
        self.displayHandler = displayHandler

    def show(self):
        self.displayHandler.display.fill(0)
        self.displayHandler.centerText("Recognize Song", 0)
        self.displayHandler.centerText("Listening...", 24)
        self.displayHandler.display.show()

    def listen(self):
        print("Testing nowPlaying")
