class SpotifyService:
    def __init__(self, apiClient):
        self.apiClient = apiClient
        self.sessionID = None
        self.currentArtworkURL = None
        self.currentArtwork = None

    def connect(self):
        response = self.apiClient.get("/spotify/connect")
        self.sessionID = response["session_id"]
        return response

    def isConnected(self):
        if not self.sessionID:
            return False
        status = self.apiClient.get("/spotify/status")
        return status["connected"]

    def getCurrentlyPlaying(self):
        if not self.sessionID:
            return None
        return self.apiClient.get(
            "/spotify/currently-playing"
        )
