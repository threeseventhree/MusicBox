from src.shazam.recognizer import ShazamRecognizer
from src.spotify.auth import SpotifyAuth
from src.spotify.client import SpotifyClient
from src.spotify.callback import startCallbackServer
from src.core.display import displayTrack
import asyncio

async def main():
    # shazam = ShazamRecognizer()
    # data = await shazam.getTrackData("audio/IN2THAT.mp3")
    # track = await shazam.convertDataToTrack(data)
    # print(track)
    spotifyAuth = SpotifyAuth()
    authUrl = spotifyAuth.createAuthUrl()
    print(authUrl)

    code = startCallbackServer()
    # print("Auth code received.")

    tokenData = spotifyAuth.exchangeCode(code)
    # print("Authentication successful!")
    # print(tokenData)
    accessToken = tokenData["access_token"]

    spotifyClient = SpotifyClient(accessToken)
    currentlyPlaying = spotifyClient.getCurrentlyPlaying()
    if currentlyPlaying:
        track = spotifyClient.convertDataToTrack(currentlyPlaying)
        displayTrack(track)
    else:
        print("Nothing is currently playing.")

if __name__ == "__main__":
    asyncio.run(main())