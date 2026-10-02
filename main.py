from src.shazam.recognizer import ShazamRecognizer
from src.spotify.auth import SpotifyAuth
from src.spotify.callback import startCallbackServer
import asyncio

async def main():
    shazam = ShazamRecognizer()
    data = await shazam.getTrackData("audio/IN2THAT.mp3")
    track = await shazam.convertDataToTrack(data)
    # print(track)
    spotify = SpotifyAuth()
    authUrl = spotify.createAuthUrl()
    print(authUrl)

    code = startCallbackServer()
    print("Auth code received.")

    tokenData = spotify.exchangeCode(code)
    print("Authentication successful!")
    print(tokenData)
    

if __name__ == "__main__":
    asyncio.run(main())