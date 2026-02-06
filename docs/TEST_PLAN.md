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

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Launch app and navigate to login screen | Login screen displayed |
| 2 | Enter valid email: `bob@example.com` | Email field populated |
| 3 | Enter valid password: `10203040` | Password field populated (masked) |
| 4 | Hide keyboard | Keyboard dismissed |
| 5 | Click Login button | Navigate to Products page |

---

### 2. Negative Tests (5)

#### TC_002: Invalid Email Format
| Field | Details |
|-------|---------|
| **Objective** | Verify error for invalid email format |
| **Priority** | High |
| **Marker** | `@negative` |

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Enter invalid email: `invalid@email` | Email field populated |
| 2 | Enter password: `password123` | Password field populated |
| 3 | Hide keyboard and click Login | Error message displayed |

---

#### TC_003: Incorrect Password
| Field | Details |
|-------|---------|
| **Objective** | Verify error for wrong password |
| **Priority** | High |
| **Marker** | `@negative` |

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Enter email: `bob@example.com` | Email field populated |
| 2 | Enter wrong password: `wrong_password` | Password field populated |
| 3 | Hide keyboard and click Login | Error message displayed |

---

#### TC_004: Empty Email Field
| Field | Details |
|-------|---------|
| **Objective** | Verify error when email is empty |
| **Priority** | High |
| **Marker** | `@negative` |

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Leave email field empty | Email field empty |
| 2 | Enter password: `secret_sauce` | Password field populated |
| 3 | Hide keyboard and click Login | Error: Username required |

---

#### TC_005: Empty Password Field
| Field | Details |
|-------|---------|
| **Objective** | Verify error when password is empty |
| **Priority** | High |
| **Marker** | `@negative` |

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Enter email: `bob@example.com` | Email field populated |
| 2 | Leave password field empty | Password field empty |
| 3 | Hide keyboard and click Login | Error: Password required |

---

#### TC_006: Unregistered Email
| Field | Details |
|-------|---------|
| **Objective** | Verify error for unregistered user |
| **Priority** | Medium |
| **Marker** | `@negative` |

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Enter unregistered email: `unregistered@test.com` | Email field populated |
| 2 | Enter password: `password123` | Password field populated |
| 3 | Hide keyboard and click Login | Error message displayed |

---

### 3. Boundary Tests (2)

#### TC_007: Minimum Character Email
| Field | Details |
|-------|---------|
| **Objective** | Verify error for single character email |
| **Priority** | Medium |
| **Marker** | `@boundary` |

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Enter single character: `a` | Email field shows "a" |
| 2 | Enter password: `password123` | Password field populated |
| 3 | Hide keyboard and click Login | Error message displayed |

---

#### TC_008: Maximum Character Email
| Field | Details |
|-------|---------|
| **Objective** | Verify app handles 256+ character email |
| **Priority** | Medium |
| **Marker** | `@boundary` |

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Enter 256+ char email: `aaa...@test.com` | Email field populated |
| 2 | Enter password: `password123` | Password field populated |
| 3 | Hide keyboard and click Login | App handles gracefully (error or stays on page) |

---

### 4. UI/UX Tests (2)

#### TC_009: Error Message Visibility
| Field | Details |
|-------|---------|
| **Objective** | Verify error message is visible and contains text |
| **Priority** | Medium |
| **Marker** | `@ui` |

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Enter invalid email: `invalid@test.com` | Email field populated |
| 2 | Enter password: `wrongpass` | Password field populated |
| 3 | Hide keyboard and click Login | Error message displayed |
| 4 | Verify error message element | Error visible with text content |

---

#### TC_010: Loading Indicator
| Field | Details |
|-------|---------|
| **Objective** | Verify login completes after loading |
| **Priority** | Low |
| **Marker** | `@ui` |

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Enter email: `bob@example.com` | Email field populated |
| 2 | Enter password: `10203040` | Password field populated |
| 3 | Hide keyboard and click Login | Loading indicator appears |
| 4 | Wait 2 seconds | Login completes (success or error) |

---

### 5. Security Tests (2)

#### TC_011: Password Visibility Toggle
| Field | Details |
|-------|---------|
| **Objective** | Verify password masking and toggle |
| **Priority** | High |
| **Marker** | `@security` |

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Enter password: `TestPassword123` | Password masked with dots |
| 2 | Verify password is masked | Password characters hidden |
| 3 | Click visibility toggle | Password becomes visible/hidden |

---

#### TC_012: Rate Limiting
| Field | Details |
|-------|---------|
| **Objective** | Verify app handles multiple failed attempts |
| **Priority** | Medium |
| **Marker** | `@security` |

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Enter fake email: `fake0@test.com` | Email field populated |
| 2 | Enter wrong password: `wrongpass` | Password field populated |
| 3 | Click Login, get error, clear fields | Error displayed, fields cleared |
| 4 | Repeat steps 1-3 two more times | App handles gracefully |
| 5 | Verify app state after 3 failures | Error displayed or login button visible |

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
