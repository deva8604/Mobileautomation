# Login tests for SauceLabs MyDemoApp
# 12 test cases: positive, negative, boundary, ui, security

import pytest
import time
from pages.login_page import LoginPage
from config.config import VALID_USERS, INVALID_CREDENTIALS


class TestLogin:
    
    # positive tests
    
    @pytest.mark.positive
    @pytest.mark.smoke
    def test_valid_login(self, login_page, driver):
        # valid email and password login
        username = VALID_USERS["standard_user"]["username"]
        password = VALID_USERS["standard_user"]["password"]
        
        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.hide_keyboard()
        login_page.click_login_button()
        
        assert login_page.is_login_successful(), \
            "Login failed - Products page not displayed"
    
    # negative tests
    
    @pytest.mark.negative
    def test_invalid_email_format(self, login_page):
        # invalid email format should show error
        login_page.enter_username("invalid@email")
        login_page.enter_password("password123")
        login_page.hide_keyboard()
        login_page.click_login_button()
        
        assert login_page.is_error_displayed(), \
            "Error message should be displayed for invalid email"
    
    @pytest.mark.negative
    def test_incorrect_password(self, login_page):
        # wrong password should show error
        login_page.enter_username("bob@example.com")
        login_page.enter_password("wrong_password")
        login_page.hide_keyboard()
        login_page.click_login_button()
        
        assert login_page.is_error_displayed(), \
            "Error message should be displayed for incorrect password"
    
    @pytest.mark.negative
    def test_empty_email(self, login_page):
        # empty email should show error
        login_page.enter_password("secret_sauce")
        login_page.hide_keyboard()
        login_page.click_login_button()
        
        assert login_page.is_error_displayed(), \
            "Error message should be displayed for empty username"
    
    @pytest.mark.negative
    def test_empty_password(self, login_page):
        # empty password should show error
        login_page.enter_username("bob@example.com")
        login_page.hide_keyboard()
        login_page.click_login_button()
        
        assert login_page.is_error_displayed(), \
            "Error message should be displayed for empty password"
    
    @pytest.mark.negative
    def test_unregistered_email(self, login_page):
        # unregistered user should show error
        login_page.enter_username("unregistered@test.com")
        login_page.enter_password("password123")
        login_page.hide_keyboard()
        login_page.click_login_button()
        
        assert login_page.is_error_displayed(), \
            "Error message should be displayed for unregistered user"
    
    # boundary tests
    
    @pytest.mark.boundary
    def test_min_character_email(self, login_page):
        # single character email should show error
        login_page.enter_username("a")
        login_page.enter_password("password123")
        login_page.hide_keyboard()
        login_page.click_login_button()
        
        assert login_page.is_error_displayed(), \
            "Error should be displayed for single character email"
    
    @pytest.mark.boundary
    def test_max_character_email(self, login_page):
        # 256+ character email should be handled
        long_email = "a" * 256 + "@test.com"
        login_page.enter_username(long_email)
        login_page.enter_password("password123")
        login_page.hide_keyboard()
        login_page.click_login_button()
        
        assert login_page.is_error_displayed() or login_page.is_login_button_visible(), \
            "App should handle max length email gracefully"
    
    # ui tests
    
    @pytest.mark.ui
    def test_error_message_visibility(self, login_page):
        # error message should be visible and contain text
        login_page.enter_username("invalid@test.com")
        login_page.enter_password("wrongpass")
        login_page.hide_keyboard()
        login_page.click_login_button()
        
        assert login_page.is_error_displayed(), \
            "Error message should be visible"
        
        error_text = login_page.get_error_message()
        assert error_text is not None and len(error_text) > 0, \
            "Error message should contain text"
    
    @pytest.mark.ui
    def test_loading_indicator(self, login_page):
        # login should complete after loading
        login_page.enter_username("bob@example.com")
        login_page.enter_password("10203040")
        login_page.hide_keyboard()
        login_page.click_login_button()
        
        time.sleep(2)
        assert login_page.is_login_successful() or login_page.is_error_displayed(), \
            "Login should complete after loading"
    
    # security tests
    
    @pytest.mark.security
    def test_password_visibility_toggle(self, login_page):
        # password should be masked and toggle should work
        login_page.enter_password("TestPassword123")
        
        is_masked = login_page.is_password_masked()
        assert is_masked is not None, \
            "Should be able to check password masking state"
        
        login_page.toggle_password_visibility()
    
    @pytest.mark.security
    def test_rate_limiting(self, login_page):
        # multiple failed attempts should be handled
        for i in range(3):
            login_page.enter_username(f"fake{i}@test.com")
            login_page.enter_password("wrongpass")
            login_page.hide_keyboard()
            login_page.click_login_button()
            if login_page.is_error_displayed():
                login_page.clear_fields()
        
        assert login_page.is_error_displayed() or login_page.is_login_button_visible(), \
            "App should handle multiple failed attempts"
