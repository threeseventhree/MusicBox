from src.spotify.client import SpotifyClient
from hardware.esp32.src.spotifyService import SpotifyService
import time

spotifyClient = SpotifyClient()
spotifyService = SpotifyService(spotifyClient)

connection = spotifyService.connect()

print("Session:", connection["session_id"])
print("URL:", connection["url"])

while True:
    if spotifyService.isConnected():
        print("Spotify connected!")
        break

    print("Waiting for Spotify...")
    time.sleep(2)
