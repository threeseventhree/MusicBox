
cd hardware/esp32

mpremote connect COM5 fs cp sh1106.py :sh1106.py
mpremote connect COM5 mip install urequests 
mpremote connect COM5 mip install https://raw.githubusercontent.com/JASchilz/uQR/master/uQR.py

mpremote connect COM5 fs mkdir src

mpremote connect COM5 fs cp src/display.py :src/display.py
mpremote connect COM5 fs cp src/buttons.py :src/buttons.py
mpremote connect COM5 fs cp src/menuScreen.py :src/menuScreen.py
mpremote connect COM5 fs cp src/recognizeScreen.py :src/recognizeScreen.py
mpremote connect COM5 fs cp src/spotifyScreen.py :src/spotifyScreen.py
mpremote connect COM5 fs cp src/spotifyService.py :src/spotifyService.py
mpremote connect COM5 fs cp src/settingsScreen.py :src/settingsScreen.py
mpremote connect COM5 fs cp src/wifi.py :src/wifi.py
mpremote connect COM5 fs cp src/api.py :src/api.py
mpremote connect COM5 fs cp src/qr.py :src/qr.py

mpremote connect COM5 fs cp main.py :main.py

mpremote connect COM5 reset
# debug

mpremote connect COM5 fs ls
mpremote connect COM5 fs ls :src

mpremote connect COM5 repl
