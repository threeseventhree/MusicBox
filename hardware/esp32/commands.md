# Start Wokwi MicroPython
```
cd hardware/esp32

mpremote connect port:rfc2217://localhost:4000 mip install ssd1306

mpremote connect port:rfc2217://localhost:4000 fs mkdir src
mpremote connect port:rfc2217://localhost:4000 fs cp src/display.py :src/display.py
mpremote connect port:rfc2217://localhost:4000 fs cp src/menu.py :src/menu.py
mpremote connect port:rfc2217://localhost:4000 fs cp src/buttons.py :src/buttons.py

mpremote connect port:rfc2217://localhost:4000 fs cp main.py :main.py
```
