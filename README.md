# Home Automation System

A comprehensive home automation system built with **Flutter** for the mobile interface, **ESP32 with MicroPython** for hardware control, and **Firebase Realtime Database** as the backend.

## 🏠 Features

- **Real-time Control**: Control home appliances and lights in real-time
- **Multi-Room Support**: Manage different rooms independently
- **Cross-Platform**: Flutter app works on Android and iOS
- **Firebase Integration**: Real-time synchronization using Firebase Database
- **ESP32 Hardware**: Reliable microcontroller-based hardware control
- **Simple UI**: Clean and intuitive user interface

## 🛠️ Tech Stack

- **Frontend**: Flutter (Dart)
- **Backend**: Firebase Realtime Database
- **Hardware**: ESP32 with MicroPython
- **Database**: Firebase Realtime Database
- **IDE**: Android Studio

## 📱 Controlled Devices

- Room 1 Light
- Room 2 Light  
- Room 3 Light
- Freeze (Refrigerator)
- Air Conditioning (AC)
- Main Power

## 🚀 Getting Started

### Prerequisites

- Flutter SDK (3.8.1 or higher)
- Android Studio
- Firebase account
- ESP32 development board
- MicroPython firmware for ESP32

### Flutter App Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/home_automation.git
   cd home_automation
   ```

2. **Install dependencies**
   ```bash
   flutter pub get
   ```

3. **Firebase Configuration**
   - Create a new Firebase project at [Firebase Console](https://console.firebase.google.com/)
   - Enable Realtime Database
   - Download `google-services.json` and place it in `android/app/`
   - For iOS, download `GoogleService-Info.plist` and add to `ios/Runner/`

4. **Update Firebase URL**
   - Update the Firebase URL in your ESP32 code (see ESP32 setup below)

5. **Run the app**
   ```bash
   flutter run
   ```

### ESP32 Hardware Setup

1. **Install MicroPython**
   - Download MicroPython firmware for ESP32
   - Flash it to your ESP32 board

2. **Configure the ESP32 code**
   - Copy the code from `lib/main.py` (example template)
   - Create your own version with your credentials:
   
   ```python
   # Wi-Fi credentials  
   SSID = "your_wifi_name"
   PASSWORD = "your_wifi_password"
   
   # Firebase URL (replace with your Firebase URL)
   FIREBASE_URL = "https://your-project-id-default-rtdb.region.firebasedatabase.app/led_state.json"
   ```

3. **GPIO Pin Configuration**
   ```python
   pins = {
       "room1": Pin(15, Pin.OUT),
       "room2": Pin(2, Pin.OUT), 
       "room3": Pin(4, Pin.OUT),
       "freeze": Pin(5, Pin.OUT),
       "ac": Pin(18, Pin.OUT),
       "main": Pin(19, Pin.OUT),
   }
   ```

4. **Upload to ESP32**
   - Use tools like Thonny IDE or ampy to upload the code
   - Save as `main.py` on the ESP32

### Firebase Database Structure

The Firebase Realtime Database should have the following structure:

```json
{
  "led_state": {
    "room1": 0,
    "room2": 0,
    "room3": 0,
    "freeze": 0,
    "ac": 0,
    "main": 0
  }
}
```

Values: `0` = OFF, `1` = ON

## 🔧 Hardware Connections

Connect your devices to the ESP32 GPIO pins as configured:

| Device | GPIO Pin | Description |
|--------|----------|-------------|
| Room 1 Light | GPIO 15 | Controls room 1 lighting |
| Room 2 Light | GPIO 2 | Controls room 2 lighting |
| Room 3 Light | GPIO 4 | Controls room 3 lighting |
| Freeze | GPIO 5 | Controls refrigerator |
| AC | GPIO 18 | Controls air conditioning |
| Main Power | GPIO 19 | Main power control |

⚠️ **Safety Warning**: Always use appropriate relays and follow electrical safety guidelines when connecting high-voltage appliances.

## 📁 Project Structure

```
home_automation/
├── lib/
│   ├── main.dart          # Flutter app main file
│   └── main.py            # ESP32 MicroPython code template
├── android/               # Android-specific files
├── ios/                   # iOS-specific files  
├── web/                   # Web support files
├── test/                  # Test files
├── pubspec.yaml          # Flutter dependencies
└── README.md             # This file
```

## 🔒 Security Notes

- **Never commit sensitive files** like `google-services.json` to public repositories
- **Use environment variables** for API keys and credentials
- **Secure your WiFi credentials** in the ESP32 code
- **Set up Firebase security rules** for your database

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🐛 Troubleshooting

### Common Issues

1. **ESP32 not connecting to WiFi**
   - Check SSID and password
   - Ensure 2.4GHz network (ESP32 doesn't support 5GHz)

2. **Firebase connection issues**
   - Verify Firebase URL is correct
   - Check internet connectivity
   - Ensure Firebase Realtime Database is enabled

3. **Flutter build issues**
   - Run `flutter clean && flutter pub get`
   - Ensure all dependencies are properly installed

## 📞 Support

For support and questions, please open an issue on GitHub or contact [your-email@example.com]

---

**Happy Automating! 🏡✨**
