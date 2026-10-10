import network #type: ignore
from time import sleep, time


class WiFiHandler:
    def __init__(self):
        self.wlan = network.WLAN(network.STA_IF)

    def connect(self):
        self.wlan.active(True)

        if self.wlan.isconnected():
            print("Wi-Fi already connected")
            print(self.wlan.ifconfig())
            return True

        # Replace these with your actual Wi-Fi credentials.
        self.wlan.connect("373", "threeseventhree")
        print("Connecting to Wi-Fi...")

        timeout = 20
        start = time()

        while not self.wlan.isconnected():
            if time() - start >= timeout:
                print("Wi-Fi connection timed out")
                return False
            sleep(0.25)

        print("Wi-Fi connected")
        print(self.wlan.ifconfig())
        return True

    def isConnected(self):
        return self.wlan.isconnected()
