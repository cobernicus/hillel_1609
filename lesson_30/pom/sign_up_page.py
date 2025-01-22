from selenium.webdriver.common.by import By




class Sigh_Up_Page:
    X_BUTTON =(By.XPATH, '//button[text()=\'Sign up\']')
    INPUT_NAME = (By.XPATH, '//input[@id=\'signupName\']')
    INPUT_LAST_NAME = (By.XPATH, '//input[@id=\'signupLastName\']')
    INPUT_EMAIL = (By.XPATH, '//input[@name=\"email\"]')
    INPUT_PASSWORD = (By.XPATH, '//input[@name="password" and @type="password"]')
    RE_ENTER_PASSWORD = (By.XPATH, '//input[@name="repeatPassword" and @type="password"]')
    REGISTER = (By.XPATH, '//button[@type=\'button\' and text()=\'Register\']')

    def __init__(self, driver):
        self.driver = driver



    def name_field(self):
        return self.driver.find_element(*Sigh_Up_Page.INPUT_NAME)

    def last_name_field(self):
        return self.driver.find_element(*Sigh_Up_Page.INPUT_LAST_NAME)

    def email_field(self):
        return self.driver.find_element(*Sigh_Up_Page.INPUT_EMAIL)

    def password_field(self):
        return self.driver.find_element(*Sigh_Up_Page.INPUT_PASSWORD)

    def reenter_password_field(self):
        return self.driver.find_element(*Sigh_Up_Page.RE_ENTER_PASSWORD)

    def register_button(self):
        return self.driver.find_element(*Sigh_Up_Page.REGISTER)

    def x_button(self):
        return self.driver.find_element(*Sigh_Up_Page.X_BUTTON)

    def name_text(self):
        return self.driver.find_element(*Sigh_Up_Page.INPUT_NAME).get_attribute('value')
