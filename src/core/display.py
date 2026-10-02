import io
import requests

from PIL import Image
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.style import Style


console = Console()

def imageToText(image, width=60):
    # Braille uses 2x4 pixels per character
    aspect_ratio = image.height / image.width

    height = int(width * aspect_ratio * 4)

    image = image.resize(
        (width * 2, height),
        Image.Resampling.LANCZOS
    ).convert("RGB")

    text = Text()

    # Braille dot positions
    dots = {
        (0, 0): 0,
        (0, 1): 1,
        (0, 2): 2,
        (1, 0): 3,
        (1, 1): 4,
        (1, 2): 5,
        (0, 3): 6,
        (1, 3): 7,
    }

    for y in range(0, image.height - 3, 4):
        for x in range(0, image.width - 1, 2):

            braille = 0
            colors = []

            for dy in range(4):
                for dx in range(2):

                    pixel = image.getpixel((x + dx, y + dy))

                    # Brightness
                    brightness = (
                        0.299 * pixel[0]
                        + 0.587 * pixel[1]
                        + 0.114 * pixel[2]
                    )

                    # Decide whether this pixel should be visible
                    if brightness > 35:
                        braille |= 1 << dots[(dx, dy)]
                        colors.append(pixel)

            if colors:
                # Average the colors of active pixels
                r = sum(c[0] for c in colors) // len(colors)
                g = sum(c[1] for c in colors) // len(colors)
                b = sum(c[2] for c in colors) // len(colors)

                style = Style(
                    color=f"rgb({r},{g},{b})"
                )

                text.append(
                    chr(0x2800 + braille),
                    style=style
                )
            else:
                text.append(" ")

        text.append("\n")

    return text


def displayTrack(track):

    # Download artwork
    response = requests.get(track.artworkURL)
    response.raise_for_status()

    image = Image.open(
        io.BytesIO(response.content)
    )

    artwork = imageToText(image, width=30)

    # Track information
    info = Table.grid(padding=(0, 1))

    info.add_row("[bold]Title[/bold]", track.title)
    info.add_row("[bold]Artist[/bold]", track.artist)
    info.add_row("[bold]Album[/bold]", track.album or "Unknown")
    info.add_row("[bold]Song[/bold]", track.songUrl or "None")

    # Artwork + information
    layout = Table.grid(padding=(0, 3))

    layout.add_row(
        artwork,
        info
    )

    console.print(
        Panel(
            layout,
            title="[bold]♫ MUSICBOX[/bold]",
            subtitle="Now Playing",
            padding=(1, 2)
        )
    )