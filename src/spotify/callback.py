from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs


class SpotifyCallbackHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urlparse(self.path)
        params = parse_qs(parsed_url.query)

        code = params.get("code", [None])[0]
        error = params.get("error", [None])[0]

        if error:
            print(f"Spotify authorization failed: {error}")

        elif code:
            print("Spotify authorization successful!")
            print("Authorization code received.")

            self.server.authorization_code = code # type: ignore

        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()

        self.wfile.write(
            b"""
            <html>
                <body>
                    <h1>Musicbox</h1>
                    <p>Spotify authorization successful.</p>
                    <p>You can close this window.</p>
                </body>
            </html>
            """
        )

    def logMessage(self, format, *args):
        pass


def startCallbackServer():
    server = HTTPServer(
        ("127.0.0.1", 8888),
        SpotifyCallbackHandler
    )

    server.authorization_code = None # type: ignore

    print("Waiting for Spotify authorization...")

    while server.authorization_code is None: # type: ignore
        server.handle_request()

    return server.authorization_code # type: ignore
