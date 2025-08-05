# ESP32 Hardware Setup Guide

This guide will help you set up the ESP32 hardware for the home automation system.

## 🛠️ Required Components

### Hardware:
- ESP32 Development Board (ESP32-WROOM-32 or similar)
- Relay modules (5V or 3.3V compatible) - 6 channels
- Jumper wires (Male to Male, Male to Female)
- Breadboard or PCB
- Power supply for ESP32 (USB or external 5V)
- Resistors (optional, for LED indicators)

### Safety Equipment:
- Proper electrical enclosure
- Circuit breakers/fuses
- Electrical tape
- Wire nuts/terminals

## 📋 Pin Configuration

| Device | ESP32 GPIO | Relay Module | Description |
|--------|------------|--------------|-------------|
| Room 1 Light | GPIO 15 | Relay 1 | Controls room 1 lighting |
| Room 2 Light | GPIO 2 | Relay 2 | Controls room 2 lighting |
| Room 3 Light | GPIO 4 | Relay 3 | Controls room 3 lighting |
| Freeze | GPIO 5 | Relay 4 | Controls refrigerator |
| AC | GPIO 18 | Relay 5 | Controls air conditioning |
| Main Power | GPIO 19 | Relay 6 | Main power control |

## 🔌 Wiring Diagram

### ESP32 to Relay Module Connections:

```
ESP32          Relay Module
─────          ────────────
3.3V     ──────  VCC
GND      ──────  GND
GPIO15   ──────  IN1 (Room1)
GPIO2    ──────  IN2 (Room2)
GPIO4    ──────  IN3 (Room3)
GPIO5    ──────  IN4 (Freeze)
GPIO18   ──────  IN5 (AC)
GPIO19   ──────  IN6 (Main)
```

### Relay to AC Appliances:

⚠️ **DANGER - HIGH VOLTAGE**: Only qualified electricians should work with AC mains voltage!

```
AC Main ──── Common Terminal (COM)
            │
            ├── Normally Open (NO) ──── Appliance Load
            │
            └── Normally Closed (NC) ──── (Not used)
```

## 🔧 Assembly Steps

### 1. ESP32 Setup
1. Connect ESP32 to computer via USB
2. Install MicroPython firmware
3. Test basic GPIO operations

### 2. Relay Module Connection
1. Connect VCC to ESP32 3.3V (or 5V if relay requires it)
2. Connect GND to ESP32 GND
3. Connect control pins as per table above
4. Test relay switching with simple code

### 3. Software Installation
1. Copy the MicroPython code to ESP32
2. Update WiFi credentials
3. Update Firebase URL
4. Test connectivity

### 4. Appliance Connection (⚠️ ELECTRICIAN REQUIRED)
1. Turn OFF main power
2. Connect relay outputs to appliance control circuits
3. Use proper electrical enclosures
4. Test with multimeter before powering on
5. Gradually test each circuit

## 🔒 Safety Considerations

### Electrical Safety:
- **NEVER** work on live circuits
- Use appropriate PPE (Personal Protective Equipment)
- Install proper circuit breakers
- Use GFCI protection where required
- Follow local electrical codes

### Fire Safety:
- Use appropriate wire gauges
- Secure all connections
- Monitor for overheating
- Install in fireproof enclosures

### Code Safety:
- Implement watchdog timers
- Add fail-safe mechanisms
- Test error handling thoroughly

## 🧪 Testing Procedure

### 1. Basic GPIO Test
```python
from machine import Pin
import time

# Test single pin
led = Pin(15, Pin.OUT)
led.on()
time.sleep(1)
led.off()
```

### 2. Relay Test
```python
# Test all relays sequentially
pins = [15, 2, 4, 5, 18, 19]
for pin_num in pins:
    pin = Pin(pin_num, Pin.OUT)
    pin.on()
    time.sleep(0.5)
    pin.off()
    time.sleep(0.5)
```

### 3. WiFi Connectivity Test
```python
import network
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('YOUR_SSID', 'YOUR_PASSWORD')
# Check wlan.isconnected()
```

### 4. Firebase Communication Test
```python
import urequests
response = urequests.get('YOUR_FIREBASE_URL')
print(response.text)
response.close()
```

## 🐛 Troubleshooting

### Common Issues:

1. **Relay not switching**
   - Check power supply voltage
   - Verify GPIO pin configuration
   - Test with multimeter

2. **WiFi connection fails**
   - Check SSID and password
   - Ensure 2.4GHz network
   - Check signal strength

3. **Firebase connection issues**
   - Verify internet connectivity
   - Check Firebase URL format
   - Test with browser first

4. **ESP32 keeps restarting**
   - Check power supply capacity
   - Review code for infinite loops
   - Monitor serial output for errors

## 📞 Support

For hardware-related questions:
- Check ESP32 documentation
- Visit MicroPython forums
- Consult local electrical professionals for AC wiring

---

**Remember: When in doubt about electrical work, consult a professional electrician! 🔌⚡**
