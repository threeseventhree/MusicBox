from uQR import QRCode  # type: ignore
class QRHandler:
    def __init__(self, displayHandler):
        self.displayHandler = displayHandler

    def display(self, data):
        qr = QRCode()
        qr.add_data(data)
        matrix = qr.get_matrix()
        self.displayHandler.fill(0)
        size = len(matrix)
        scale = min(
            self.displayHandler.width // size,
            self.displayHandler.height // size
        )
        if scale < 1:
            print("QR code too large for display")
            return
        qrWidth = size * scale
        offsetX = (self.displayHandler.width - qrWidth) // 2
        offsetY = (self.displayHandler.height - qrWidth) // 2
        for y in range(size):
            for x in range(size):
                if matrix[y][x]:
                    self.displayHandler.fillRect(
                        offsetX + x * scale,
                        offsetY + y * scale,
                        scale,
                        scale,
                        1
                    )
        self.displayHandler.show()
