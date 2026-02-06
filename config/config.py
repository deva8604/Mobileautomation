"""
Configuration settings for the mobile automation framework.
"""
import os
from pathlib import Path

# Project Paths
PROJECT_ROOT = Path(__file__).parent.parent
APP_PATH = PROJECT_ROOT / "app" / "SauceLabs.apk"

# Appium Server Configuration
APPIUM_HOST = os.getenv("APPIUM_HOST", "127.0.0.1")
APPIUM_PORT = os.getenv("APPIUM_PORT", "4723")
APPIUM_URL = f"http://{APPIUM_HOST}:{APPIUM_PORT}"

# Device Capabilities - Updated for SauceLabs MyDemoApp
DEVICE_CAPABILITIES = {
    "platformName": "Android",
    "deviceName": os.getenv("DEVICE_NAME", "Android Emulator"),
    "automationName": "UiAutomator2",
    "appPackage": "com.saucelabs.mydemoapp.rn",
    "appActivity": ".MainActivity",
    "noReset": False,
    "fullReset": False,
    "newCommandTimeout": 300,
    "autoGrantPermissions": True,
}

# Add APK path if exists
if APP_PATH.exists():
    DEVICE_CAPABILITIES["app"] = str(APP_PATH)

# Test Data - Valid Users
VALID_USERS = {
    "standard_user": {
        "username": "bob@example.com",
        "password": "10203040"
    }
}

# Test Data - Invalid Credentials  
INVALID_CREDENTIALS = {
    "invalid_email": {
        "username": "invalid@email",
        "password": "password123"
    },
    "wrong_password": {
        "username": "bob@example.com",
        "password": "wrong_password"
    }
}
