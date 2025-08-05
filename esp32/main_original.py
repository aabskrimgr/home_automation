import network
import urequests as requests
import ujson
import time
from machine import Pin, reset

# Wi-Fi credentials
SSID = "Aabiskar_wifi_2.4"
PASSWORD = "a23@45#90Grr"

# Firebase URL
FIREBASE_URL = "https://homeautomation-dd177-default-rtdb.asia-southeast1.firebasedatabase.app/led_state.json"

# GPIO pins
pins = {
    "room1": Pin(15, Pin.OUT),
    "room2": Pin(2, Pin.OUT),
    "room3": Pin(4, Pin.OUT),
    "freeze": Pin(5, Pin.OUT),
    "ac": Pin(18, Pin.OUT),
    "main": Pin(19, Pin.OUT),
}

def wifi_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    
    if wlan.isconnected():
        return wlan
        
    wlan.connect(SSID, PASSWORD)
    
    for i in range(30):
        if wlan.isconnected():
            print(f"WiFi OK: {wlan.ifconfig()[0]}")
            return wlan
        time.sleep(1)
    
    print("WiFi failed")
    return None

def update_pins(data):
    for key, pin in pins.items():
        if key in data:
            pin.value(int(data[key]))

# Initialize pins OFF
for pin in pins.values():
    pin.value(0)

# Connect WiFi
wlan = wifi_connect()
if not wlan:
    reset()

# Main loop
errors = 0
while True:
    try:
        # Check WiFi
        if not wlan.isconnected():
            wlan = wifi_connect()
            if not wlan:
                errors += 1
                if errors > 5:
                    reset()
                continue
        
        # Get data
        response = requests.get(FIREBASE_URL, timeout=5)
        if response.status_code == 200:
            data = ujson.loads(response.text)
            update_pins(data)
            errors = 0  # Reset error count on success
        response.close()
        
    except Exception as e:
        print(f"Error: {e}")
        errors += 1
        if errors > 10:
            reset()
    
    time.sleep(1)
