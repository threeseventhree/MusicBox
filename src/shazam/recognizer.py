from shazamio import Shazam
from src.models.track import Track

class ShazamRecognizer:
    def __init__(self):
        self.shazam = Shazam();
    async def getTrackData(self, audioPATH: str):
        data = await self.shazam.recognize(audioPATH)
        return data
    async def convertDataToTrack(self, data: dict) -> Track:
        trackData = data["track"]
        album = None
        for item in trackData["sections"][0]["metadata"]:
            if item["title"] == "Album":
                album = item["text"]
                break
        trackTitle = trackData["title"]
        trackArtist = trackData["subtitle"]
        trackAlbum = album
        trackArtworkURL = trackData["images"]["coverart"]
        trackShazamUrl = trackData["url"]
        return Track(trackTitle, trackArtist, trackAlbum, trackArtworkURL, trackShazamUrl)
