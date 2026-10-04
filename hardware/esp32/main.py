from src.buttons import ButtonHandler
from src.display import DisplayHandler
from src.menuScreen import MenuScreen
from src.recognizeScreen import RecognizeScreen
from src.spotifyScreen import SpotifyScreen
from src.spotifyService import SpotifyService
from src.settingsScreen import SettingsScreen
from src.wifi import WiFiHandler
from src.api import APIHandler
from time import sleep

wifiHandler = WiFiHandler()
wifiHandler.connect()
sleep(1)
api = APIHandler("http://host.wokwi.internal:8000")
spotifyService = SpotifyService(api)
print(spotifyService.getStatus())

displayHandler = DisplayHandler()
buttonHandler = ButtonHandler()
menuScreen = MenuScreen(displayHandler)
recognizeScreen = RecognizeScreen(displayHandler)
spotifyScreen = SpotifyScreen(displayHandler, spotifyService)
settingsScreen = SettingsScreen(displayHandler)

menuScreen.show()
while True:
    if not buttonHandler.enterButton.value():
        if displayHandler.screen == "menu":
            menuScreen.enter()
            if displayHandler.screen == "recognize":
                recognizeScreen.show()
            elif displayHandler.screen == "spotify":
                spotifyScreen.show()
            elif displayHandler.screen == "settings":
                settingsScreen.show()
        elif displayHandler.screen == "spotify":
            spotifyScreen.enter()
        buttonHandler.waitForRelease(buttonHandler.enterButton)

    if not buttonHandler.scrollButton.value():
        if displayHandler.screen == "menu":
            menuScreen.scroll()
        elif displayHandler.screen == "spotify":
            spotifyScreen.scroll()
        elif displayHandler.screen == "settings":
            settingsScreen.scroll()
        buttonHandler.waitForRelease(buttonHandler.scrollButton)

    if not buttonHandler.backButton.value():
        if(displayHandler.screen != "menu"):
            menuScreen.show()
            displayHandler.screen = "menu"
        buttonHandler.waitForRelease(buttonHandler.backButton)

    if displayHandler.screen == "spotify":
        spotifyScreen.update()
