from http.server import BaseHTTPRequestHandler, HTTPServer
import json

from src.spotify.client import SpotifyClient
from src.core.artwork import artworkToBitmap


spotifyClient = SpotifyClient()

sessionID = None

currentArtworkURL = None
currentArtwork = None


class MusicboxHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        global sessionID
        global currentArtworkURL
        global currentArtwork

        if self.path == "/spotify/connect":
            sessionID = spotifyClient.createSession()

            response = {
                "session_id": sessionID,
                "url": spotifyClient.getConnectURL(sessionID)
            }

            body = json.dumps(response).encode()

            self.send_response(200)
            self.send_header(
                "Content-Type",
                "application/json"
            )
            self.send_header(
                "Content-Length",
                str(len(body))
            )
            self.end_headers()

            self.wfile.write(body)
            return

        if self.path == "/spotify/status":
            if not sessionID:
                connected = False
            else:
                status = spotifyClient.getStatus(
                    sessionID
                )

                connected = status["connected"]

            body = json.dumps({
                "connected": connected
            }).encode()

            self.send_response(200)
            self.send_header(
                "Content-Type",
                "application/json"
            )
            self.send_header(
                "Content-Length",
                str(len(body))
            )
            self.end_headers()

            self.wfile.write(body)
            return

        if self.path == "/spotify/currently-playing":
            if not sessionID:
                body = json.dumps(None).encode()

            else:
                track = spotifyClient.getCurrentlyPlaying(
                    sessionID
                )

                if track and track.get("artworkURL"):
                    artworkURL = track["artworkURL"]

                    if artworkURL != currentArtworkURL:
                        print("Downloading new artwork...")

                        currentArtwork = artworkToBitmap(
                            artworkURL,
                            32
                        )

                        currentArtworkURL = artworkURL

                    track["artwork"] = currentArtwork

                body = json.dumps(track).encode()

            self.send_response(200)
            self.send_header(
                "Content-Type",
                "application/json"
            )
            self.send_header(
                "Content-Length",
                str(len(body))
            )
            self.end_headers()

            self.wfile.write(body)
            return

        self.send_response(404)
        self.end_headers()

    def log_message(self, format, *args):
        pass


def startServer():
    server = HTTPServer(
        ("0.0.0.0", 8000),
        MusicboxHandler
    )

    print("Musicbox server running on port 8000")

    server.serve_forever()


if __name__ == "__main__":
    startServer()
