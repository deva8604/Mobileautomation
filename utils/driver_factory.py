"""
Driver Factory for creating Appium driver instances.
"""
from appium import webdriver
from appium.options.android import UiAutomator2Options
from config.config import APPIUM_URL, DEVICE_CAPABILITIES


class DriverFactory:
    """Factory class for creating Appium WebDriver instances."""
    
    _driver = None
    
    @classmethod
    def create_driver(cls, capabilities: dict = None) -> webdriver.Remote:
        """Create a new Appium driver instance."""
        caps = capabilities or DEVICE_CAPABILITIES.copy()
        
        options = UiAutomator2Options()
        for key, value in caps.items():
            options.set_capability(key, value)
        
        cls._driver = webdriver.Remote(
            command_executor=APPIUM_URL,
            options=options
        )
        cls._driver.implicitly_wait(10)
        return cls._driver
    
    @classmethod
    def quit_driver(cls):
        """Quit and clean up the driver instance."""
        if cls._driver:
            cls._driver.quit()
            cls._driver = None
