from src.shazam.recognizer import ShazamRecognizer
from src.spotify.auth import SpotifyAuth
import asyncio

async def main():
    shazam = ShazamRecognizer()
    spotify = SpotifyAuth()
    data = await shazam.getTrackData("audio/IN2THAT.mp3")
    track = await shazam.convertDataToTrack(data)
    # print(track)
    print(spotify.createAuthUrl())
    

if __name__ == "__main__":
    asyncio.run(main())