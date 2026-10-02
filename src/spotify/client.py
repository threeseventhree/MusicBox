import requests
from src.models.track import Track

class SpotifyClient:
    BASE_URL = "https://api.spotify.com/v1"

    def __init__(self, access_token: str):
        self.access_token = access_token

    def getCurrentlyPlaying(self):
        headers = {"Authorization": f"Bearer {self.access_token}"}
        response = requests.get(
            f"{self.BASE_URL}/me/player/currently-playing",
            headers=headers
        )
        if response.status_code == 204:
            return None
        response.raise_for_status()
        return response.json()

    def convertDataToTrack(self, data: dict) -> Track:
        trackData = data["item"]
        trackTitle = trackData["name"]
        trackArtist = trackData["artists"][0]["name"]
        trackAlbum = trackData["album"]["name"]
        trackArtworkURL = trackData["album"]["images"][0]["url"]
        trackSpotifyUrl = trackData["external_urls"]["spotify"]
        return Track(
            trackTitle,
            trackArtist,
            trackAlbum,
            trackArtworkURL,
            trackSpotifyUrl
        )
