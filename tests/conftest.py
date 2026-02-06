"""
Pytest fixtures for mobile automation tests.
"""
import pytest
import time
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
    Logs out if logged in, then navigates to login page.
    """
    page = LoginPage(driver)
    
    # If on login page already, just return
    if page.is_on_login_page():
        return page
    
    # If logged in (on products page), logout first
    if page.is_logged_in():
        page.full_logout()
        time.sleep(2)
    
    # Navigate to login screen
    page.navigate_to_login()
    time.sleep(1)
    
    return page
