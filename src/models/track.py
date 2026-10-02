from dataclasses import dataclass

@dataclass
class Track:
    title: str
    artist: str
    album: str | None = None
    artworkURL: str | None = None
    songUrl: str | None = None