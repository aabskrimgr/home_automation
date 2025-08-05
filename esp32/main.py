import network
import urequests as requests
import ujson
import time
from machine import Pin, reset

# Wi-Fi credentials - REPLACE WITH YOUR OWN
SSID = "YOUR_WIFI_SSID"
PASSWORD = "YOUR_WIFI_PASSWORD"

# Firebase URL - REPLACE WITH YOUR FIREBASE PROJECT URL
FIREBASE_URL = "https://your-project-id-default-rtdb.region.firebasedatabase.app/led_state.json"

# GPIO pins configuration - Modify according to your hardware setup
pins = {
    "room1": Pin(15, Pin.OUT),
    "room2": Pin(2, Pin.OUT),
    "room3": Pin(4, Pin.OUT),
    "freeze": Pin(5, Pin.OUT),
    "ac": Pin(18, Pin.OUT),
    "main": Pin(19, Pin.OUT),
}

def wifi_connect():
    """Connect to WiFi network"""
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    
    if wlan.isconnected():
        return wlan
        
    print(f"Connecting to WiFi: {SSID}")
    wlan.connect(SSID, PASSWORD)
    
    # Wait for connection with timeout
    for i in range(30):
        if wlan.isconnected():
            print(f"WiFi Connected! IP: {wlan.ifconfig()[0]}")
            return wlan
        print(".", end="")
        time.sleep(1)
    
    print("\nWiFi connection failed")
    return None

def update_pins(data):
    """Update GPIO pins based on Firebase data"""
    if not data:
        return
        
    for key, pin in pins.items():
        if key in data:
            state = int(data[key])
            pin.value(state)
            print(f"{key}: {'ON' if state else 'OFF'}")

def initialize_pins():
    """Initialize all pins to OFF state"""
    print("Initializing pins...")
    for name, pin in pins.items():
        pin.value(0)
        print(f"{name}: OFF")

# Main execution starts here
print("Home Automation ESP32 Controller Starting...")

# Initialize pins to OFF state
initialize_pins()

# Connect to WiFi
wlan = wifi_connect()
if not wlan:
    print("Failed to connect to WiFi. Restarting...")
    reset()

print("Starting main control loop...")

# Main control loop
errors = 0
max_errors = 10

while True:
    try:
        # Check WiFi connection
        if not wlan.isconnected():
            print("WiFi disconnected. Reconnecting...")
            wlan = wifi_connect()
            if not wlan:
                errors += 1
                if errors > 5:
                    print("Too many WiFi errors. Restarting...")
                    reset()
                continue
        
        # Fetch data from Firebase
        response = requests.get(FIREBASE_URL, timeout=10)
        
        if response.status_code == 200:
            data = ujson.loads(response.text)
            update_pins(data)
            errors = 0  # Reset error count on success
        else:
            print(f"HTTP Error: {response.status_code}")
            errors += 1
            
        response.close()
        
    except Exception as e:
        print(f"Error: {e}")
        errors += 1
        
        # Reset if too many consecutive errors
        if errors > max_errors:
            print("Too many errors. Restarting ESP32...")
            reset()
    
    # Wait before next iteration
    time.sleep(2)
