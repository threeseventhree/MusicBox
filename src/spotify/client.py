import requests
class SpotifyClient:
    BASE_URL = "https://musicbox-kohl.vercel.app"
    def createSession(self):
        response = requests.post(f"{self.BASE_URL}/api/sessions")
        response.raise_for_status()
        return response.json()["sessionID"]

    def getStatus(self, sessionID: str):
        response = requests.get(f"{self.BASE_URL}/api/sessions/{sessionID}")
        response.raise_for_status()
        return response.json()

    def getCurrentlyPlaying(self, sessionID: str):
        response = requests.get(f"{self.BASE_URL}/api/sessions/{sessionID}/currently-playing")
        response.raise_for_status()
        return response.json()
