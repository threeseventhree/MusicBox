import qrcode
from rich.console import Console

console = Console()
def displayQRCode(url: str):
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,  # type: ignore
        box_size=1,
        border=1
    )
    qr.add_data(url)
    qr.make(fit=True)
    matrix = qr.get_matrix()
    for y in range(0, len(matrix), 2):
        line = ""
        for x in range(len(matrix[0])):
            top = matrix[y][x]
            bottom = (
                matrix[y + 1][x]
                if y + 1 < len(matrix)
                else False
            )
            if top and bottom:
                line += "█"
            elif top:
                line += "▀"
            elif bottom:
                line += "▄"
            else:
                line += " "
        console.print(line)
