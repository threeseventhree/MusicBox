def handleMenuScreen(menu: list, displayHandler, cursorPos: int):
    displayHandler.display.fill(0)
    displayHandler.centerText("MUSICBOX", 0)
    for i, item in enumerate(menu):
        y = displayHandler.yOffset + i * displayHandler.fontSize
        if i == cursorPos:
            displayHandler.display.text("> " + item, 0, y)
        else:
            displayHandler.display.text("  " + item, 0, y)
    displayHandler.display.show()

def refreshMenu(menu: list, cursorPos: int, display):
    display.fill(0)
    display.displayCentered("MUSICBOX", 0, display)
    for i, item in enumerate(menu):
        y = display.yOffset + i * display.fontSize
        if i == cursorPos:
            display.text("> " + item, 0, y)
        else:
            display.text("  " + item, 0, y)
    display.show()
