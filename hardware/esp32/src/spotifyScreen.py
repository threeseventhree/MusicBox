from src.display import DisplayHandler
from src.spotifyService import SpotifyService
from src.qr import QRHandler
class SpotifyScreen:
    def __init__(self, displayHandler: DisplayHandler, spotifyService: SpotifyService):
        self.displayHandler = displayHandler
        self.spotifyService = spotifyService
        self.qrHandler = QRHandler(displayHandler)
        self.cursorPos = 0
        self.options = ["Now Playing", "Connect", "Disconnect"]
        self.connected = False
        self.nowPlayingActive = False

    def show(self):
        self.displayHandler.fill(0)
        self.displayHandler.centerText("Spotify", 0)
        self.displayHandler.displayParamsList(self.options, self.cursorPos)
        self.displayHandler.show()

    def scroll(self):
        self.cursorPos += 1
        if self.cursorPos >= len(self.options): self.cursorPos = 0
        self.show()

    def enter(self):
        if self.cursorPos == 0:
            self.nowPlaying()
        elif self.cursorPos == 1:
            self.connect()
        elif self.cursorPos == 2:
            self.disconnect()

    def nowPlaying(self):
        if not self.connected:
            self.displayHandler.fill(0)
            self.displayHandler.centerText("Spotify", 0)
            self.displayHandler.centerText("Not Connected", 24)
            self.displayHandler.show()
            return

        self.nowPlayingActive = True

        self.displayHandler.fill(0)
        self.displayHandler.centerText("Now Playing", 0)
        self.displayHandler.centerText("Waiting...", 24)
        self.displayHandler.show()

    def connect(self):
        print("Spotify connect started")
    
        self.displayHandler.fill(0)
        self.displayHandler.centerText("Connecting...", 24)
        self.displayHandler.show()
    
        print("Requesting auth URL...")
        response = self.spotifyService.connect()
    
        print("Response received:")
        print(response)
    
        authUrl = response["auth_url"]
    
        print("Displaying QR...")
        self.qrHandler.display(authUrl)
    
        print("QR displayed")

    def disconnect(self):
        self.connected = False
        self.nowPlayingActive = False

        self.displayHandler.fill(0)
        self.displayHandler.centerText("Spotify", 0)
        self.displayHandler.centerText("Disconnected", 24)
        self.displayHandler.show()

    def update(self):
        if not self.nowPlayingActive:
            return
        #spotify api 
