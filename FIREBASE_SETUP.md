# Firebase Configuration Template

This file contains instructions for setting up Firebase for your home automation project.

## Step 1: Create Firebase Project

1. Go to [Firebase Console](https://console.firebase.google.com/)
2. Click "Create a project"
3. Enter project name (e.g., "home-automation-yourname")
4. Enable Google Analytics (optional)
5. Click "Create project"

## Step 2: Enable Realtime Database

1. In the Firebase console, navigate to "Realtime Database"
2. Click "Create Database"
3. Choose your location (preferably closest to your region)
4. Start in "Test mode" (you can modify rules later)

## Step 3: Get Configuration Files

### For Android:
1. Click "Project Settings" (gear icon)
2. Go to "General" tab
3. Under "Your apps", click "Add app" → Android
4. Enter package name: `com.example.home_automation`
5. Download `google-services.json`
6. Place it in `android/app/` directory

### For iOS:
1. Click "Add app" → iOS
2. Enter iOS bundle ID: `com.example.homeAutomation`
3. Download `GoogleService-Info.plist`
4. Place it in `ios/Runner/` directory

## Step 4: Database Structure

Set up your Realtime Database with this structure:

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

## Step 5: Security Rules (Optional)

For production, consider updating database rules:

```json
{
  "rules": {
    "led_state": {
      ".read": true,
      ".write": true
    }
  }
}
```

## Step 6: Get Firebase URLs

Your Firebase Realtime Database URL will be in format:
`https://YOUR_PROJECT_ID-default-rtdb.REGION.firebasedatabase.app/`

Use this URL in your ESP32 code.
