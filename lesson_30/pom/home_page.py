from selenium.webdriver.common.by import By

class HomePage:

    SIGN_UP = (By.XPATH, '//button[text()=\'Sign up\']')

    def __init__(self, driver):
        self.driver = driver

    def sign_up_button(self):
        return self.driver.find_element(*HomePage.SIGN_UP)