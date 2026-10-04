from src.display import DisplayHandler
spotifyScreenParams = ["Now Playing", "Connect", "Disconnect"]
def handleSpotifyScreen(displayHandler: DisplayHandler, cursorPos):
    displayHandler.display.fill(0)
    displayHandler.centerText("Spotify Listener", 0)
    displayHandler.displayParamsList(spotifyScreenParams, cursorPos)
    displayHandler.display.show()
