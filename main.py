from src.shazam.recognizer import ShazamRecognizer
from src.spotify.auth import SpotifyAuth
from src.spotify.client import SpotifyClient
from src.spotify.callback import startCallbackServer
from src.core.display import displayTrack
from src.spotify.qr import displayQRCode
import asyncio

async def main():
    # shazam = ShazamRecognizer()
    # data = await shazam.getTrackData("audio/IN2THAT.mp3")
    # track = await shazam.convertDataToTrack(data)
    # print(track)
    spotifyAuth = SpotifyAuth()
    authUrl = spotifyAuth.createAuthUrl()
    print("Scan QR code to connect Spotify:")
    displayQRCode(authUrl)
    print()
    print("Or open this URL:")
    print(authUrl)
    
    code = startCallbackServer()
    tokenData = spotifyAuth.exchangeCode(code)
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
