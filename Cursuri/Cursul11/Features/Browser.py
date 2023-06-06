from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Browser:

    BASE_URL = 'http://jules.app/'
    email_selector = (By.CSS_SELECTOR, 'input[placeholder="Enter your email"]')
    password_selector = (By.CSS_SELECTOR, 'input[placeholder="Enter your password"]')
    button_selector = (By.CSS_SELECTOR, 'button[data-test-id="login-button"]')

    def __init__(self):
        service = Service(ChromeDriverManager().install())
        self.driver = Chrome(service=service)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def close(self):
        self.driver.quit()

    def go_to(self, page):
        self.driver.get(f'{self.BASE_URL}{page}')

    def input_email(self, email):
        self.driver.find_element(*self.email_selector).send_keys(email)

    def input_password(self, password):
        password_input = self.driver.find_element(*self.password_selector)
        password_input.send_keys(password)

    def click_login_button(self):
        login_button = self.driver.find_element(*self.button_selector)
        login_button.click()

