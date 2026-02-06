# Test Plan - SauceLabs MyDemoApp Login Flow

## Overview
| Item | Details |
|------|---------|
| **App** | SauceLabs MyDemoApp (Android) |
| **Feature** | Login Flow |
| **Framework** | Appium + Python + Pytest |

---

## Test Scenarios (12 Total)

### 1. Positive Tests (1)
| ID | Scenario | Expected Result |
|----|----------|-----------------|
| TC_001 | Valid login with correct email/password | Navigate to Products page |

### 2. Negative Tests (5)
| ID | Scenario | Expected Result |
|----|----------|-----------------|
| TC_002 | Invalid email format | Error message displayed |
| TC_003 | Incorrect password | Error message displayed |
| TC_004 | Empty email field | Error: Username required |
| TC_005 | Empty password field | Error: Password required |
| TC_006 | Unregistered email | Error message displayed |

### 3. Boundary Tests (2)
| ID | Scenario | Input | Expected Result |
|----|----------|-------|-----------------|
| TC_007 | Min character email | "a" (1 char) | Error displayed |
| TC_008 | Max character email | 256+ chars | Handled gracefully |

### 4. UI/UX Tests (2)
| ID | Scenario | Verification |
|----|----------|--------------|
| TC_009 | Error message visibility | Error visible with text |
| TC_010 | Loading indicator | Loading completes successfully |

### 5. Security Tests (2)
| ID | Scenario | Expected Result |
|----|----------|-----------------|
| TC_011 | Password visibility toggle | Toggle works correctly |
| TC_012 | Rate limiting (3 failures) | App handles gracefully |

---

## Execution
```bash
# Run all tests
python -m pytest tests/ -v

# Run by category
python -m pytest tests/ -m positive -v
python -m pytest tests/ -m negative -v
python -m pytest tests/ -m boundary -v
python -m pytest tests/ -m ui -v
python -m pytest tests/ -m security -v
```
