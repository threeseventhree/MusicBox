import io
import base64
import requests

from PIL import Image, ImageOps


def artworkToBitmap(url: str, size: int = 32) -> str:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    image = Image.open(
        io.BytesIO(response.content)
    ).convert("L")

    image = ImageOps.fit(
        image,
        (size, size)
    )

    image = image.point(
        lambda pixel: 255 if pixel > 128 else 0 # type: ignore
    )

    # Convert to framebuf.MONO_VLSB format
    bitmap = bytearray(size * size // 8)

    for y in range(size):
        for x in range(size):
            if image.getpixel((x, y)):
                index = (y // 8) * size + x
                bitmap[index] |= 1 << (y % 8)

    return base64.b64encode(bitmap).decode("ascii")
