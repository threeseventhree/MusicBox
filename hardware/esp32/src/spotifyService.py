from src.api import APIHandler
class SpotifyService:
    def __init__(self, apiHandler: APIHandler):
        self.apiHandler = apiHandler

    def getStatus(self):
        return self.apiHandler.get("/spotify/status")

    def connect(self):
        return self.apiHandler.get("/spotify/connect")

    def disconnect(self):
        return self.apiHandler.post("/spotify/disconnect")

    def getCurrentlyPlaying(self):
        return self.apiHandler.get("/spotify/currently-playing")
