"""
Pytest fixtures for mobile automation tests.
"""
import pytest
from utils.driver_factory import DriverFactory
from pages.login_page import LoginPage


@pytest.fixture(scope="session")
def driver():
    """Create Appium driver for test session."""
    driver = DriverFactory.create_driver()
    yield driver
    DriverFactory.quit_driver()


@pytest.fixture(scope="function")
def login_page(driver):
    """
    Fixture for LoginPage object.
    Navigates to login screen before each test.
    """
    try:
        driver.terminate_app("com.saucelabs.mydemoapp.rn")
        driver.activate_app("com.saucelabs.mydemoapp.rn")
    except Exception:
        pass
    
    page = LoginPage(driver)
    page.navigate_to_login()
    return page
