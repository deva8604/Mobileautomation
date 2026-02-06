"""
Login Page Object Model for SauceLabs MyDemoApp.
"""
import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class LoginPage:
    """Page Object for the SauceLabs MyDemoApp Login screen."""
    
    # Element Locators for MyDemoApp RN
    MENU_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "open menu")
    LOGIN_MENU_ITEM = (AppiumBy.ACCESSIBILITY_ID, "menu item log in")
    LOGOUT_MENU_ITEM = (AppiumBy.ACCESSIBILITY_ID, "menu item log out")
    USERNAME_FIELD = (AppiumBy.ACCESSIBILITY_ID, "Username input field")
    PASSWORD_FIELD = (AppiumBy.ACCESSIBILITY_ID, "Password input field")
    LOGIN_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Login button")
    ERROR_MESSAGE = (AppiumBy.ACCESSIBILITY_ID, "generic-error-message")
    CATALOG_HEADER = (AppiumBy.ACCESSIBILITY_ID, "products screen")
    PASSWORD_TOGGLE = (AppiumBy.ACCESSIBILITY_ID, "show password button")
    
    def __init__(self, driver):
        """Initialize LoginPage with driver."""
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
    
    def is_logged_in(self) -> bool:
        """Check if user is logged in (on products or checkout screen)."""
        # Check for products screen
        try:
            wait = WebDriverWait(self.driver, 2)
            element = wait.until(EC.presence_of_element_located(self.CATALOG_HEADER))
            if element.is_displayed():
                return True
        except:
            pass
        
        # Also check for checkout screen
        try:
            CHECKOUT_HEADER = (AppiumBy.XPATH, "//*[contains(@text, 'Checkout')]")
            wait = WebDriverWait(self.driver, 2)
            element = wait.until(EC.presence_of_element_located(CHECKOUT_HEADER))
            if element.is_displayed():
                return True
        except:
            pass
        
        return False
    
    def is_on_login_page(self) -> bool:
        """Check if currently on login page."""
        try:
            wait = WebDriverWait(self.driver, 2)
            element = wait.until(EC.presence_of_element_located(self.USERNAME_FIELD))
            return element.is_displayed()
        except:
            return False
    
    def full_logout(self):
        """Perform complete logout from app."""
        try:
            # Step 1: Click menu button
            menu = self.wait.until(EC.element_to_be_clickable(self.MENU_BUTTON))
            menu.click()
            time.sleep(1)
            
            # Step 2: Click "Log Out" menu item
            logout_item = self.wait.until(EC.element_to_be_clickable(self.LOGOUT_MENU_ITEM))
            logout_item.click()
            time.sleep(1)
            
            # Step 3: Click confirmation "Log Out" button in dialog
            confirm_locators = [
                (AppiumBy.XPATH, "//android.widget.Button[@text='LOG OUT']"),
                (AppiumBy.XPATH, "//android.widget.Button[@text='Log Out']"),
                (AppiumBy.XPATH, "//*[@text='LOG OUT']"),
                (AppiumBy.XPATH, "//*[@text='Log Out']"),
                (AppiumBy.ACCESSIBILITY_ID, "Log Out"),
                (AppiumBy.ACCESSIBILITY_ID, "LOG OUT"),
            ]
            
            for locator in confirm_locators:
                try:
                    btn = WebDriverWait(self.driver, 2).until(
                        EC.element_to_be_clickable(locator)
                    )
                    btn.click()
                    time.sleep(1)
                    break
                except:
                    continue
            
            # Step 4: Click "OK" button if there's another popup
            ok_locators = [
                (AppiumBy.XPATH, "//android.widget.Button[@text='OK']"),
                (AppiumBy.XPATH, "//android.widget.Button[@text='Ok']"),
                (AppiumBy.XPATH, "//*[@text='OK']"),
                (AppiumBy.ACCESSIBILITY_ID, "OK"),
                (AppiumBy.ACCESSIBILITY_ID, "Ok"),
            ]
            
            for locator in ok_locators:
                try:
                    ok_btn = WebDriverWait(self.driver, 2).until(
                        EC.element_to_be_clickable(locator)
                    )
                    ok_btn.click()
                    time.sleep(1)
                    break
                except:
                    continue
            
            return True
                    
        except Exception as e:
            print(f"Logout failed: {e}")
        
        return False
    
    def navigate_to_login(self):
        """Navigate to login screen from main screen."""
        # Check if already on login page
        try:
            wait = WebDriverWait(self.driver, 2)
            wait.until(EC.presence_of_element_located(self.USERNAME_FIELD))
            return  # Already on login page
        except:
            pass
        
        # Navigate via menu
        try:
            menu = self.wait.until(EC.element_to_be_clickable(self.MENU_BUTTON))
            menu.click()
            time.sleep(0.5)
            login_item = self.wait.until(EC.element_to_be_clickable(self.LOGIN_MENU_ITEM))
            login_item.click()
            time.sleep(0.5)
        except Exception:
            pass
    
    def enter_username(self, username: str):
        """Enter username in the username field."""
        element = self.wait.until(EC.presence_of_element_located(self.USERNAME_FIELD))
        element.clear()
        element.send_keys(username)
        
    def enter_password(self, password: str):
        """Enter password in the password field."""
        element = self.wait.until(EC.presence_of_element_located(self.PASSWORD_FIELD))
        element.clear()
        element.send_keys(password)
        
    def click_login_button(self):
        """Click the login button."""
        element = self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON))
        element.click()
        
    def hide_keyboard(self):
        """Hide the keyboard if visible."""
        try:
            if self.driver.is_keyboard_shown():
                self.driver.hide_keyboard()
        except Exception:
            pass
            
    def is_error_displayed(self) -> bool:
        """Check if error message is displayed."""
        try:
            wait = WebDriverWait(self.driver, 5)
            element = wait.until(EC.visibility_of_element_located(self.ERROR_MESSAGE))
            return element.is_displayed()
        except TimeoutException:
            return False
            
    def get_error_message(self) -> str:
        """Get the error message text."""
        try:
            element = self.wait.until(EC.presence_of_element_located(self.ERROR_MESSAGE))
            
            # Try multiple ways to get text (React Native apps store text differently)
            text = element.text
            if text:
                return text
            
            # Try common attributes where text might be stored
            for attr in ["text", "content-desc", "name", "value", "label"]:
                try:
                    text = element.get_attribute(attr)
                    if text:
                        return text
                except:
                    continue
            
            # Try getting text from child elements
            try:
                children = element.find_elements(AppiumBy.XPATH, ".//*")
                for child in children:
                    child_text = child.text or child.get_attribute("text") or child.get_attribute("content-desc")
                    if child_text:
                        return child_text
            except:
                pass
            
            return ""
        except Exception:
            return None
            
    def is_login_successful(self) -> bool:
        """Check if login was successful (Products or Checkout screen displayed)."""
        # Check for products screen
        try:
            wait = WebDriverWait(self.driver, 5)
            element = wait.until(EC.visibility_of_element_located(self.CATALOG_HEADER))
            if element.is_displayed():
                return True
        except:
            pass
        
        # Also check for checkout screen (means logged in)
        try:
            CHECKOUT_HEADER = (AppiumBy.XPATH, "//*[contains(@text, 'Checkout')]")
            wait = WebDriverWait(self.driver, 3)
            element = wait.until(EC.visibility_of_element_located(CHECKOUT_HEADER))
            if element.is_displayed():
                return True
        except:
            pass
        
        return False
    
    def is_login_button_visible(self) -> bool:
        """Check if login button is visible."""
        try:
            wait = WebDriverWait(self.driver, 3)
            element = wait.until(EC.visibility_of_element_located(self.LOGIN_BUTTON))
            return element.is_displayed()
        except TimeoutException:
            return False
    
    def is_password_masked(self) -> bool:
        """Check if password field is masked."""
        try:
            element = self.wait.until(EC.presence_of_element_located(self.PASSWORD_FIELD))
            password_attr = element.get_attribute("password")
            return password_attr == "true"
        except Exception:
            return None
    
    def toggle_password_visibility(self):
        """Toggle password visibility."""
        try:
            toggle = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self.PASSWORD_TOGGLE)
            )
            toggle.click()
        except Exception:
            pass
    
    def clear_fields(self):
        """Clear username and password fields."""
        try:
            username = self.wait.until(EC.presence_of_element_located(self.USERNAME_FIELD))
            username.clear()
            password = self.wait.until(EC.presence_of_element_located(self.PASSWORD_FIELD))
            password.clear()
        except Exception:
            pass
