import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils.config import Config

@pytest.fixture(scope="function")
def driver():
    # Setup Chrome WebDriver with correct capabilities
    options = webdriver.ChromeOptions()
    service = Service(ChromeDriverManager().install())  # Use Service for the driver path
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(Config.TIMEOUT)
    yield driver
    driver.quit()
