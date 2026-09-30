import os
import secrets
import hashlib
import base64
import urllib.parse

from dotenv import load_dotenv
load_dotenv()

class SpotifyAuth:
    def __init__(self):
        self.client_id = os.getenv("SPOTIFY_CLIENT_ID")
        self.redirect_uri = os.getenv("SPOTIFY_REDIRECT_URI")

    def create_code_verifier(self):
        return secrets.token_urlsafe(64)

    def create_code_challenge(self, verifier):
        digest = hashlib.sha256(verifier.encode()).digest()
        return base64.urlsafe_b64encode(digest).decode().rstrip("=")

    def createAuthUrl(self):
        verifier = self.create_code_verifier()
        challenge = self.create_code_challenge(verifier)

        params = {
            "client_id": self.client_id,
            "response_type": "code",
            "redirect_uri": self.redirect_uri,
            "code_challenge_method": "S256",
            "code_challenge": challenge,
            "scope": "user-read-currently-playing"
        }

        return (
            "https://accounts.spotify.com/authorize?"
            + urllib.parse.urlencode(params)
        )