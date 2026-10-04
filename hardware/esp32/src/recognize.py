from src.display import DisplayHandler
def handleRecognizeScreen(displayHandler: DisplayHandler):
    displayHandler.display.fill(0)
    displayHandler.centerText("Recognize Song", 0)
    displayHandler.centerText("Listening...", 24)
    displayHandler.display.show()
