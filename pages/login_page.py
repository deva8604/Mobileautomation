"""
Login Page Object Model for SauceLabs MyDemoApp.
"""
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class LoginPage:
    """Page Object for the SauceLabs MyDemoApp Login screen."""
    
    # Element Locators for MyDemoApp RN
    MENU_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "open menu")
    LOGIN_MENU_ITEM = (AppiumBy.ACCESSIBILITY_ID, "menu item log in")
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
    
    def navigate_to_login(self):
        """Navigate to login screen from main screen."""
        try:
            menu = self.wait.until(EC.element_to_be_clickable(self.MENU_BUTTON))
            menu.click()
            login_item = self.wait.until(EC.element_to_be_clickable(self.LOGIN_MENU_ITEM))
            login_item.click()
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
            return element.text or element.get_attribute("text")
        except Exception:
            return None
            
    def is_login_successful(self) -> bool:
        """Check if login was successful (Catalog screen displayed)."""
        try:
            wait = WebDriverWait(self.driver, 10)
            element = wait.until(EC.visibility_of_element_located(self.CATALOG_HEADER))
            return element.is_displayed()
        except TimeoutException:
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
            # Check password attribute
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
