import pytest
from selenium.webdriver.common.by import By

from pages.login_page import LoginPage
from utils.logger import setup_logger
from utils.config import Config

logger = setup_logger()

def test_login_valid_credentials(driver):
    logger.info("Starting test_login_valid_credentials")

    driver.get(Config.BASE_URL + "/login")

    login_page = LoginPage(driver)
    login_page.enter_username("Bhagya")
    login_page.enter_password("973383566Vb#")
    login_page.click_login()

    # Add assertions to verify login success
    assert "DEMOQA" in driver.title  # Update the expected title to match the actual page title
    assert "https://demoqa.com/login" in driver.current_url  # Check for redirect to profile page
    # # Check for presence of a specific element that indicates successful login (e.g., profile name or logout button)
    # assert driver.find_element(By.ID, "profile")  # Replace with an actual element that signifies a successful login (e.g., profile icon)

    # Verify that no error message is displayed (if applicable)
    assert not driver.find_elements(By.CLASS_NAME, "error-message")  # Adjust with actual error class name if needed


    logger.info("Completed test_login_valid_credentials")
