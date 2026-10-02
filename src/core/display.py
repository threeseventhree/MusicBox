import io
import requests

from PIL import Image
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.style import Style


console = Console()
def imageToText(image, width=30):
    aspect_ratio = image.height / image.width

    # Two vertical pixels are represented by one terminal character.
    height = int(width * aspect_ratio)

    image = image.resize(
        (width, height),
        Image.Resampling.BOX
    ).convert("RGB")

    text = Text()

    for y in range(0, height - 1, 2):
        for x in range(width):

            top = image.getpixel((x, y))
            bottom = image.getpixel((x, y + 1))

            topColor = (
                f"rgb({top[0]},{top[1]},{top[2]})"
            )

            bottomColor = (
                f"rgb({bottom[0]},{bottom[1]},{bottom[2]})"
            )

            style = Style(
                color=topColor,
                bgcolor=bottomColor
            )

            text.append("▀", style=style)

        text.append("\n")

    return text

def displayTrack(track):

    # Download artwork
    response = requests.get(track.artworkURL)
    response.raise_for_status()

    image = Image.open(
        io.BytesIO(response.content)
    )

    artwork = imageToText(image, width=40)

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
