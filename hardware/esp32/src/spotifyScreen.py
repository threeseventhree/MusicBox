from src.display import DisplayHandler
from src.spotifyService import SpotifyService
from src.qr import QRHandler
from time import sleep, time
class SpotifyScreen:
    def __init__(self, displayHandler: DisplayHandler, spotifyService: SpotifyService):
        self.displayHandler = displayHandler
        self.spotifyService = spotifyService
        self.qrHandler = QRHandler(displayHandler)
        self.cursorPos = 0
        self.options = ["Now Playing", "Connect", "Disconnect"]
        self.connected = False
        self.nowPlayingActive = False
        self.lastUpdate = 0
        self.updateInterval = 5

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
        self.lastUpdate = 0
        self.updateNowPlaying()

    def connect(self):
        self.displayHandler.fill(0)
        self.displayHandler.centerText("Connecting...", 24)
        self.displayHandler.show()

        response = self.spotifyService.connect()
        connectURL = response["url"]
        self.qrHandler.display(connectURL)
        while True:
            if self.spotifyService.isConnected():
                self.connected = True
                self.displayHandler.fill(0)
                self.displayHandler.centerText("Spotify", 0)
                self.displayHandler.centerText("Connected", 24)
                self.displayHandler.show()
                break
            sleep(2)

    def disconnect(self):
        self.connected = False
        self.nowPlayingActive = False

        self.displayHandler.fill(0)
        self.displayHandler.centerText("Spotify", 0)
        self.displayHandler.centerText("Disconnected", 24)
        self.displayHandler.show()

    def update(self):
        if not self.nowPlayingActive: return
        currentTime = time()
        if currentTime - self.lastUpdate < self.updateInterval: return
        self.lastUpdate = currentTime
        self.updateNowPlaying()

    def updateNowPlaying(self):
        track = self.spotifyService.getCurrentlyPlaying()
        if not track:
            self.displayHandler.fill(0)
            self.displayHandler.centerText("Now Playing", 0)
            self.displayHandler.centerText("Nothing Playing", 24)
            self.displayHandler.show()
            return

        if not track["playing"]:
            self.displayHandler.fill(0)
            self.displayHandler.centerText("Now Playing", 0)
            self.displayHandler.centerText("Paused", 24)
            self.displayHandler.show()
            return
        title = track["title"]
        artist = track["artist"]
        self.displayHandler.fill(0)
        self.displayHandler.centerText("Now Playing", 0)
        self.displayHandler.text(title[:15], 0, 20)
        self.displayHandler.text(artist[:15], 0, 32)
        self.displayHandler.text(track["album"][:15], 0, 44)
        progress = track["progressMs"] // 1000
        duration = track["durationMs"] // 1000
        progressSeconds = progress % 60
        durationSeconds = duration % 60

        if progressSeconds < 10:
            progressSecondsText = "0" + str(progressSeconds)
        else:
            progressSecondsText = str(progressSeconds)
        if durationSeconds < 10:
            durationSecondsText = "0" + str(durationSeconds)
        else:
            durationSecondsText = str(durationSeconds)
        progressText = (
            str(progress // 60)
            + ":"
            + progressSecondsText
            + " / "
            + str(duration // 60)
            + ":"
            + durationSecondsText
        )
        self.displayHandler.text(
            progressText,
            0,
            56
        )
        self.displayHandler.show()
