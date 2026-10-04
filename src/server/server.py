from http.server import BaseHTTPRequestHandler, HTTPServer
from src.spotify.auth import SpotifyAuth
import json
class MusicboxHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/spotify/status":
            response = {"connected": False}
            body = json.dumps(response).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        elif self.path == "/spotify/connect":
            auth = SpotifyAuth()
            authUrl = auth.createAuthUrl()
            response = {"auth_url": authUrl}
            body = json.dumps(response).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        pass

def startServer():
    server = HTTPServer(("0.0.0.0", 8000), MusicboxHandler)
    print("Musicbox server running on port 8000")
    server.serve_forever()

if __name__ == "__main__":
    startServer()
