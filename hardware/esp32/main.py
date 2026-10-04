from src.buttons import ButtonHandler
from src.display import DisplayHandler
from src.menu import handleMenuScreen
from src.recognize import handleRecognizeScreen
from src.spotify import handleSpotifyScreen # type: ignore
from src.settings import handleSettingsScreen
menuCursor = 0
spotifyCursor = 0
settingsCursor = 0

displayHandler = DisplayHandler()
buttonHandler = ButtonHandler()

handleMenuScreen(displayHandler, menuCursor)
while True:
    if not buttonHandler.enterButton.value():
        if menuCursor == 0:
            handleRecognizeScreen(displayHandler)
            displayHandler.screen = displayHandler.screens[0]
        elif menuCursor == 1:
            handleSpotifyScreen(displayHandler, spotifyCursor)
            displayHandler.screen = displayHandler.screens[1]
        elif menuCursor == 2:
            handleSettingsScreen(displayHandler, settingsCursor)
            displayHandler.screen = displayHandler.screens[2]
        buttonHandler.waitForRelease(buttonHandler.enterButton)

    if not buttonHandler.scrollButton.value():
        if displayHandler.screen == "menu":
            menuCursor += 1
            if menuCursor >= len(displayHandler.screens): menuCursor = 0
            handleMenuScreen(displayHandler, menuCursor)
        elif displayHandler.screen == "spotify":
            spotifyCursor += 1
            if spotifyCursor >= len(displayHandler.screens): spotifyCursor = 0
            handleSpotifyScreen(displayHandler, spotifyCursor)
            pass
        elif displayHandler.screen == "settings":
            pass
        buttonHandler.waitForRelease(buttonHandler.scrollButton)

    if not buttonHandler.backButton.value():
        if(displayHandler.screen != "menu"):
            handleMenuScreen(displayHandler, menuCursor)
            displayHandler.screen = "menu"
        buttonHandler.waitForRelease(buttonHandler.backButton)
