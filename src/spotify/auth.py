import os
import secrets
import hashlib
import base64
import urllib.parse
import requests

from dotenv import load_dotenv
load_dotenv()

class SpotifyAuth:
    def __init__(self):
        self.client_id = os.getenv("SPOTIFY_CLIENT_ID")
        self.redirect_uri = os.getenv("SPOTIFY_REDIRECT_URI")
        self.code_verifier = None

    def createCodeVerifier(self):
        return secrets.token_urlsafe(64)

    def createCodeChallenge(self, verifier):
        digest = hashlib.sha256(verifier.encode()).digest()
        return base64.urlsafe_b64encode(digest).decode().rstrip("=")

    def createAuthUrl(self):
        self.code_verifier = self.createCodeVerifier()
        challenge = self.createCodeChallenge(self.code_verifier)

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
    def exchangeCode(self, code):
        data = {
            "client_id": self.client_id,
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": self.redirect_uri,
            "code_verifier": self.code_verifier
        }

        response = requests.post(
            "https://accounts.spotify.com/api/token",
            data=data
        )

        response.raise_for_status()

        return response.json()