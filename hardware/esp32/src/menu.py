from src.display import DisplayHandler
menuScreenParams = ["Recognize", "Spotify", "Settings"]
def handleMenuScreen(displayHandler, cursorPos: int):
    displayHandler.display.fill(0)
    displayHandler.centerText("MUSICBOX", 0)
    displayHandler.displayParamsList(menuScreenParams, cursorPos)
    displayHandler.display.show()

def refreshMenu(cursorPos: int, displayHandler: DisplayHandler):
    displayHandler.display.fill(0)
    displayHandler.centerText("MUSICBOX", 0)
    displayHandler.displayParamsList(menuScreenParams, cursorPos)
    displayHandler.display.show()
