# Start Wokwi MicroPython
```
cd hardware/esp32

mpremote connect port:rfc2217://localhost:4000 mip install ssd1306
mpremote connect port:rfc2217://localhost:4000 mip install urequests
mpremote connect port:rfc2217://localhost:4000 mip install https://raw.githubusercontent.com/JASchilz/uQR/master/uQR.py

mpremote connect port:rfc2217://localhost:4000 fs mkdir src
mpremote connect port:rfc2217://localhost:4000 fs cp src/display.py :src/display.py
mpremote connect port:rfc2217://localhost:4000 fs cp src/buttons.py :src/buttons.py
mpremote connect port:rfc2217://localhost:4000 fs cp src/menuScreen.py :src/menuScreen.py
mpremote connect port:rfc2217://localhost:4000 fs cp src/recognizeScreen.py :src/recognizeScreen.py
mpremote connect port:rfc2217://localhost:4000 fs cp src/spotifyScreen.py :src/spotifyScreen.py
mpremote connect port:rfc2217://localhost:4000 fs cp src/spotifyService.py :src/spotifyService.py
mpremote connect port:rfc2217://localhost:4000 fs cp src/settingsScreen.py :src/settingsScreen.py
mpremote connect port:rfc2217://localhost:4000 fs cp src/wifi.py :src/wifi.py
mpremote connect port:rfc2217://localhost:4000 fs cp src/api.py :src/api.py
mpremote connect port:rfc2217://localhost:4000 fs cp src/qr.py :src/qr.py

mpremote connect port:rfc2217://localhost:4000 fs cp main.py :main.py
```
