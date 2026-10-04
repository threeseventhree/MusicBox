width = 128
height = 64
fontSize = 8
yOffset = 8

def displayCentered(text: str, y: int, display):
    length = len(text)
    lengthPixels = fontSize * length
    centerXPos = int(width / 2)
    x = centerXPos - int(lengthPixels / 2)
    display.text(text, x, y)

def refreshMenu(menu: list, cursorPos: int, display):
    display.fill(0)
    displayCentered("MUSICBOX", 0, display)
    for i, item in enumerate(menu):
        y = yOffset + i * fontSize
        if i == cursorPos:
            display.text("> " + item, 0, y)
        else:
            display.text("  " + item, 0, y)
    display.show()
