from src.display import DisplayHandler
def handleSettingsScreen(displayHandler: DisplayHandler, cursorPos: int):
    displayHandler.display.fill(0)
    displayHandler.centerText("Settings", 0)
    displayHandler.display.show()
