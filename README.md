# SauceLabs Mobile Automation Framework

Mobile automation framework for **SauceLabs MyDemoApp** using **Appium + Python + Pytest** with **Page Object Model**.

---

## 📁 Project Structure

```
Mobautomation/
├── app/
│   └── SauceLabs.apk           # Test APK
├── config/
│   ├── __init__.py
│   └── config.py               # Configuration
├── pages/
│   ├── __init__.py
│   └── login_page.py           # Page Object
├── tests/
│   ├── __init__.py
│   ├── conftest.py             # Fixtures
│   └── test_login.py           # 12 Test Cases
├── utils/
│   ├── __init__.py
│   └── driver_factory.py       # Appium Driver
├── docs/
│   └── TEST_PLAN.md
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## 🔧 Prerequisites

- Python 3.11+
- Android SDK / Emulator
- Appium 2.x

```powershell
npm install -g appium
appium driver install uiautomator2
pip install -r requirements.txt
```

---

## 🚀 Running Tests

```powershell
# 1. Start emulator
emulator -avd Medium_Phone_API_36.1

# 2. Start Appium (new terminal)
appium --address 127.0.0.1 --port 4723

# 3. Run tests
cd c:\Users\lenovo\Desktop\Mobautomation
python -m pytest tests/ -v
```

---

## 🧪 Test Cases (12 Total)

### Positive Tests (1)
| # | Test | Description |
|---|------|-------------|
| 1 | test_valid_login | Valid email and password |

### Negative Tests (5)
| # | Test | Description |
|---|------|-------------|
| 2 | test_invalid_email_format | Invalid email format |
| 3 | test_incorrect_password | Wrong password |
| 4 | test_empty_email | Empty email field |
| 5 | test_empty_password | Empty password field |
| 6 | test_unregistered_email | Unregistered user |

### Boundary Tests (2)
| # | Test | Description |
|---|------|-------------|
| 7 | test_min_character_email | 1 character email |
| 8 | test_max_character_email | 256+ character email |

### UI/UX Tests (2)
| # | Test | Description |
|---|------|-------------|
| 9 | test_error_message_visibility | Error text visible |
| 10 | test_loading_indicator | Loading completes |

### Security Tests (2)
| # | Test | Description |
|---|------|-------------|
| 11 | test_password_visibility_toggle | Password show/hide |
| 12 | test_rate_limiting | Multiple failed attempts |

---

## 🏃 Run by Category

```powershell
python -m pytest tests/ -m positive -v
python -m pytest tests/ -m negative -v
python -m pytest tests/ -m boundary -v
python -m pytest tests/ -m ui -v
python -m pytest tests/ -m security -v
```

---

## 📊 Test Results

Latest run: **9 passed, 3 failed** (4 min 15 sec)
