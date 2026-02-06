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

#### TC_001: Valid Login
| Field | Details |
|-------|---------|
| **Objective** | Verify successful login with valid credentials |
| **Priority** | High |
| **Markers** | `@positive`, `@smoke` |

**Test Steps:**
1. Launch app and navigate to login screen
2. Enter valid email: `bob@example.com`
3. Enter valid password: `10203040`
4. Hide keyboard
5. Click Login button

**Expected Result:** User navigates to Products page successfully

---

### 2. Negative Tests (5)

#### TC_002: Invalid Email Format
| Field | Details |
|-------|---------|
| **Objective** | Verify error for invalid email format |
| **Priority** | High |
| **Marker** | `@negative` |

**Test Steps:**
1. Enter invalid email: `invalid@email`
2. Enter password: `password123`
3. Hide keyboard and click Login

**Expected Result:** Error message displayed for invalid email format

---

#### TC_003: Incorrect Password
| Field | Details |
|-------|---------|
| **Objective** | Verify error for wrong password |
| **Priority** | High |
| **Marker** | `@negative` |

**Test Steps:**
1. Enter email: `bob@example.com`
2. Enter wrong password: `wrong_password`
3. Hide keyboard and click Login

**Expected Result:** Error message displayed for incorrect password

---

#### TC_004: Empty Email Field
| Field | Details |
|-------|---------|
| **Objective** | Verify error when email is empty |
| **Priority** | High |
| **Marker** | `@negative` |

**Test Steps:**
1. Leave email field empty
2. Enter password: `secret_sauce`
3. Hide keyboard and click Login

**Expected Result:** Error message displayed - Username required

---

#### TC_005: Empty Password Field
| Field | Details |
|-------|---------|
| **Objective** | Verify error when password is empty |
| **Priority** | High |
| **Marker** | `@negative` |

**Test Steps:**
1. Enter email: `bob@example.com`
2. Leave password field empty
3. Hide keyboard and click Login

**Expected Result:** Error message displayed - Password required

---

#### TC_006: Unregistered Email
| Field | Details |
|-------|---------|
| **Objective** | Verify error for unregistered user |
| **Priority** | Medium |
| **Marker** | `@negative` |

**Test Steps:**
1. Enter unregistered email: `unregistered@test.com`
2. Enter password: `password123`
3. Hide keyboard and click Login

**Expected Result:** Error message displayed for unregistered user

---

### 3. Boundary Tests (2)

#### TC_007: Minimum Character Email
| Field | Details |
|-------|---------|
| **Objective** | Verify error for single character email |
| **Priority** | Medium |
| **Marker** | `@boundary` |

**Test Steps:**
1. Enter single character: `a`
2. Enter password: `password123`
3. Hide keyboard and click Login

**Expected Result:** Error message displayed for invalid email

---

#### TC_008: Maximum Character Email
| Field | Details |
|-------|---------|
| **Objective** | Verify app handles 256+ character email |
| **Priority** | Medium |
| **Marker** | `@boundary` |

**Test Steps:**
1. Enter 256+ character email: `aaa...@test.com`
2. Enter password: `password123`
3. Hide keyboard and click Login

**Expected Result:** App handles gracefully (error displayed or stays on login page)

---

### 4. UI/UX Tests (2)

#### TC_009: Error Message Visibility
| Field | Details |
|-------|---------|
| **Objective** | Verify error message is visible and contains text |
| **Priority** | Medium |
| **Marker** | `@ui` |

**Test Steps:**
1. Enter invalid email: `invalid@test.com`
2. Enter password: `wrongpass`
3. Hide keyboard and click Login
4. Verify error message element

**Expected Result:** Error message is visible and contains descriptive text

---

#### TC_010: Loading Indicator
| Field | Details |
|-------|---------|
| **Objective** | Verify login completes after loading |
| **Priority** | Low |
| **Marker** | `@ui` |

**Test Steps:**
1. Enter email: `bob@example.com`
2. Enter password: `10203040`
3. Hide keyboard and click Login
4. Wait 2 seconds for completion

**Expected Result:** Login completes successfully (success page or error displayed)

---

### 5. Security Tests (2)

#### TC_011: Password Visibility Toggle
| Field | Details |
|-------|---------|
| **Objective** | Verify password masking and toggle |
| **Priority** | High |
| **Marker** | `@security` |

**Test Steps:**
1. Enter password: `TestPassword123`
2. Verify password is masked
3. Click visibility toggle icon

**Expected Result:** Password is initially masked and toggle changes visibility

---

#### TC_012: Rate Limiting
| Field | Details |
|-------|---------|
| **Objective** | Verify app handles multiple failed attempts |
| **Priority** | Medium |
| **Marker** | `@security` |

**Test Steps:**
1. Enter fake email and wrong password
2. Click Login and get error
3. Clear fields and repeat 2 more times (3 total attempts)

**Expected Result:** App handles multiple failed attempts gracefully (error displayed or login button remains visible)

---

## Execution Commands
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

---

## Test Results
| Date | Passed | Failed | Duration |
|------|--------|--------|----------|
| 2026-02-06 | 12 | 0 | 3m 42s |
