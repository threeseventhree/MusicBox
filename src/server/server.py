from http.server import BaseHTTPRequestHandler, HTTPServer
import json

from src.spotify.client import SpotifyClient
from hardware.esp32.src.spotifyService import SpotifyService
spotifyClient = SpotifyClient()
spotifyService = SpotifyService(spotifyClient)
class MusicboxHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/spotify/connect":
            response = spotifyService.connect()
            body = json.dumps(response).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        if self.path == "/spotify/status":
            connected = spotifyService.isConnected()
            body = json.dumps({"connected": connected}).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        if self.path == "/spotify/currently-playing":
            track = spotifyService.getCurrentlyPlaying()
            body = json.dumps(track).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
    def log_message(self, format, *args):
        pass
def startServer():
    server = HTTPServer(("0.0.0.0", 8000),MusicboxHandler)
    print("Musicbox server running on port 8000")
    server.serve_forever()
if __name__ == "__main__":
    startServer()
