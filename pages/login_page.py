# login_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.login_button = (By.ID, "login")  # Update with the correct selector if needed


    def enter_username(self, username):
        username_field = self.driver.find_element(By.ID, "userName")  # Update with the correct selector
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = self.driver.find_element(By.ID, "password")  # Update with the correct selector
        password_field.send_keys(password)

    def click_login(self):
        # Wait until the login button is clickable
        login_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.login_button)
        )
        login_button.click()
