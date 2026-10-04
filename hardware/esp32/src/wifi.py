import network # type: ignore
from time import sleep

class WiFiHandler:
    def __init__(self):
        self.wlan = network.WLAN(network.STA_IF)
    
    def connect(self):
        self.wlan.active(True)
        self.wlan.connect("Wokwi-GUEST","")
        print("Connecting to Wi-Fi...")
        while not self.wlan.isconnected(): sleep(0.1)
        print("Wi-Fi connected")
        print(self.wlan.ifconfig())

    def isConnected(self):
        return self.wlan.isconnected()
